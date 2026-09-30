# -*- coding: utf-8 -*-

import names
import openpyxl
import re


def normalize(text):
    text = re.sub(r"<br\s*/?>", " ", str(text), flags=re.IGNORECASE)
    text = re.sub(r"<[^>]+>", "", text)
    text = text.replace("\xa0", " ")
    return " ".join(text.split()).strip().lower()


def get_all_texts(obj):
    texts = []

    try:
        value = getattr(obj, "text")
        value = str(value)

        if len(value.strip()) > 0:
            value = re.sub(r"<br\s*/?>", " ", value, flags=re.IGNORECASE)
            value = re.sub(r"<[^>]+>", "", value)
            value = " ".join(value.split())

            if len(value) > 0:
                texts.append(value)

    except:
        pass

    try:
        children = object.children(obj)
    except:
        children = []

    try:
        for child in children:
            texts.extend(get_all_texts(child))
    except:
        pass

    return texts


def ignore_text(text):
    text = normalize(text)

    if len(text) == 0:
        return True

    if re.fullmatch(r"[-_=.]+", text):
        return True

    return False


def main():

    excelpath = "/home/ntc/Test_Automation_Gemini/Localisation/suite_GFL_Czech/tst_Home Screen/testdata/Gemini Split strings.xlsx"

    workbook = openpyxl.load_workbook(
        excelpath,
        data_only=True
    )

    sheet = workbook["Soft Tissue-Guided"]

    # LOGIN
    doubleClick(waitForObject(names.numpad_pushButton_8_NumpadButton), 68, 52, Qt.NoModifier, Qt.LeftButton)
    doubleClick(waitForObject(names.numpad_pushButton_8_NumpadButton), 116, 46, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton))

    # CHANGE LANGUAGE TO DUTCH
    clickButton(waitForObject(names.homeScreen_settingsButton_QPushButton))
    clickTab(waitForObject(names.settingsScreen_tbSystemInfo_TabWidget), "INFO")
    clickButton(waitForObject(names.gbSystemInformation_pbLanguageSettingsUpdate_QPushButton))
    clickButton(waitForObject(names.languagesFrame_pbDutch_QPushButton))
    clickButton(waitForObject(names.buttonsFrame_acceptButton_QPushButton))
    clickButton(waitForObject(names.settingsScreen_pbBack_QPushButton))
    snooze(1)

    # OPEN SOFT TISSUE ASSISTANT
    clickButton(waitForObject(names.homeScreen_pbSoftTissueAssistant_QToolButton))
    mouseClick(waitForObject(names.softTissueAssistantModeScreen_gbSoftTissueProcedures_QFrame), 165, 137, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.softTissueAssistantModeScreen_gbBphProcedures_QFrame), 24, 50, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.softTissueAssistantModeScreen_lbTooltipName_QLabel), 245, 4, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.topBar_buttonsBar_ButtonsBar_2), 428, 20, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.softTissueAssistantModeScreen_wdBottom_QWidget), 867, 59, Qt.NoModifier, Qt.LeftButton)
    snooze(1)

    # GET SOFT TISSUE SCREEN
    soft_tissue = waitForObject(
        names.softTissueAssistantModeScreen_SoftTissueAssistantModeScreen
    )

    # CAPTURE SCREEN TEXT
    screen_texts = get_all_texts(soft_tissue)

    actual_texts = set()

    for text in screen_texts:
        if not ignore_text(text):
            actual_texts.add(normalize(text))

    # VERIFY EXCEL DUTCH STRINGS
    verified = set()
    pass_count = 0
    fail_count = 0

    for row in sheet.iter_rows(
        min_row=2,
        values_only=True
    ):

        if len(row) < 7:
            continue

        if row[1] is None:
            continue

        if row[6] is None:
            continue

        english = str(row[1]).strip()
        dutch = str(row[6]).strip()

        if len(english) == 0:
            continue

        if len(dutch) == 0:
            continue

        dutch_key = normalize(dutch)

        if len(dutch_key) == 0:
            continue

        if dutch_key in verified:
            continue

        verified.add(dutch_key)

        if dutch_key in actual_texts:

            test.passes(
                "PASS: " +
                english +
                " -> " +
                dutch
            )

            pass_count += 1

        else:

            test.fail(
                "FAIL: " +
                english +
                " -> " +
                dutch +
                " | Dutch string is missing on Soft Tissue-Guided screen"
            )

            fail_count += 1

    workbook.close()

    # FINAL RESULT
    if fail_count > 0:

        test.fail(
            "DUTCH SOFT TISSUE-GUIDED LOCALIZATION VALIDATION FAILED"
        )

    elif pass_count > 0:

        test.passes(
            "DUTCH SOFT TISSUE-GUIDED LOCALIZATION VALIDATION PASSED"
        )

    else:

        test.fail(
            "NO DUTCH EXCEL STRINGS FOUND FOR VALIDATION"
        )