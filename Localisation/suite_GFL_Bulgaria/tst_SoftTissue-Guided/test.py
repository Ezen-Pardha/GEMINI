# -*- coding: utf-8 -*-

import names
import openpyxl
import re


def normalize(text):
    text = str(text).strip()
    text = re.sub(r"<[^>]+>", "", text)
    text = " ".join(text.split())
    return text.casefold()


def get_all_texts(obj):

    texts = []

    try:
        if not obj.visible:
            return texts
    except:
        pass

    try:
        text = str(obj.text).strip()

        if text:
            text = re.sub(r"<[^>]+>", "", text)
            text = " ".join(text.split())

            if text:
                texts.append(text)

    except:
        pass

    try:
        children = object.children(obj)

        for child in children:
            texts.extend(get_all_texts(child))

    except:
        pass

    return texts


def ignore_text(text):

    text = str(text).strip()

    if not text:
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

    doubleClick(
        waitForObject(names.numpad_pushButton_8_NumpadButton),
        68, 52,
        Qt.NoModifier,
        Qt.LeftButton
    )

    doubleClick(
        waitForObject(names.numpad_pushButton_8_NumpadButton),
        116, 46,
        Qt.NoModifier,
        Qt.LeftButton
    )

    clickButton(
        waitForObject(names.mainFrame_okButton_QPushButton)
    )

    # SETTINGS

    clickButton(
        waitForObject(names.homeScreen_settingsButton_QPushButton)
    )

    clickTab(
        waitForObject(names.settingsScreen_tbSystemInfo_TabWidget),
        "INFO"
    )

    clickButton(
        waitForObject(
            names.gbSystemInformation_pbLanguageSettingsUpdate_QPushButton
        )
    )

    # BULGARIAN

    clickButton(
        waitForObject(names.languagesFrame_pbBulgaria_QPushButton)
    )

    clickButton(
        waitForObject(names.buttonsFrame_acceptButton_QPushButton)
    )

    clickButton(
        waitForObject(names.settingsScreen_pbBack_QPushButton)
    )

    # OPEN SOFT TISSUE ASSISTANT

    clickButton(
        waitForObject(
            names.homeScreen_pbSoftTissueAssistant_QToolButton
        )
    )

    mouseClick(
        waitForObject(
            names.softTissueAssistantModeScreen_gbSoftTissueProcedures_QFrame
        ),
        179, 107,
        Qt.NoModifier,
        Qt.LeftButton
    )

    mouseClick(
        waitForObject(
            names.softTissueAssistantModeScreen_gbBphProcedures_QFrame
        ),
        232, 18,
        Qt.NoModifier,
        Qt.LeftButton
    )

    mouseClick(
        waitForObject(
            names.topBar_buttonsBar_ButtonsBar_2
        ),
        162, 37,
        Qt.NoModifier,
        Qt.LeftButton
    )

    snooze(1)

    # GET SOFT TISSUE SCREEN

    soft_tissue = waitForObject(
        names.softTissueAssistantModeScreen_SoftTissueAssistantModeScreen
    )

    actual_texts = get_all_texts(soft_tissue)

    actual_texts = list(set(actual_texts))

    # BUILD BULGARIAN EXCEL DATA
    # English = Column B
    # Bulgarian = Column C

    excel_strings = {}

    for row in sheet.iter_rows(
        min_row=2,
        values_only=True
    ):

        if len(row) < 3:
            continue

        english = row[1]
        bulgarian = row[2]

        if english is None or bulgarian is None:
            continue

        english = str(english).strip()
        bulgarian = str(bulgarian).strip()

        if not english or not bulgarian:
            continue

        excel_strings[normalize(bulgarian)] = (
            english,
            bulgarian
        )

    # VALIDATION

    verified = set()
    pass_count = 0

    for text in actual_texts:

        if ignore_text(text):
            continue

        key = normalize(text)

        if key in excel_strings:

            english, bulgarian = excel_strings[key]

            if key not in verified:

                verified.add(key)

                test.passes(
                    english + " -> " + bulgarian
                )

                pass_count += 1

    # FINAL RESULT

    if pass_count > 0:

        test.passes(
            "BULGARIAN SOFT TISSUE LOCALIZATION VALIDATION PASSED"
        )

    else:

        test.fail(
            "NO BULGARIAN STRINGS FOUND ON SOFT TISSUE SCREEN"
        )

    workbook.close()