# -*- coding: utf-8 -*-

import names
import openpyxl
import re


def get_all_texts(obj):
    texts = []

    try:
        text = str(obj.text).strip()

        if text:
            if "<html>" in text:
                text = re.sub("<[^>]+>", "", text)
                text = text.strip()

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

    workbook = openpyxl.load_workbook(excelpath)
    sheet = workbook["Soft Tissue-Guided"]

    # Login

    doubleClick(waitForObject(names.numpad_pushButton_8_NumpadButton), 68, 52, Qt.NoModifier, Qt.LeftButton)
    doubleClick(waitForObject(names.numpad_pushButton_8_NumpadButton), 116, 46, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton))

    # Settings

    clickButton(waitForObject(names.homeScreen_settingsButton_QPushButton))
    clickTab(waitForObject(names.settingsScreen_tbSystemInfo_TabWidget), "INFO")
    clickButton(waitForObject(names.gbSystemInformation_pbLanguageSettingsUpdate_QPushButton))
    clickButton(waitForObject(names.languagesFrame_pbDenmark_QPushButton))
    clickButton(waitForObject(names.buttonsFrame_acceptButton_QPushButton))
    clickButton(waitForObject(names.settingsScreen_pbBack_QPushButton))

    # Soft Tissue-Guided

    clickButton(waitForObject(names.homeScreen_pbSoftTissueAssistant_QToolButton))
    mouseClick(waitForObject(names.softTissueAssistantModeScreen_gbSoftTissueProcedures_QFrame), 314, 19, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.softTissueAssistantModeScreen_lbTooltipName_QLabel), 304, 6, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.softTissueAssistantModeScreen_wdTabWidgets_QWidget), 97, 336, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.softTissueAssistantModeScreen_gbBphProcedures_QFrame), 24, 46, Qt.NoModifier, Qt.LeftButton)

    soft_tissue = waitForObject(names.softTissueAssistantModeScreen_SoftTissueAssistantModeScreen)

    actual_texts = get_all_texts(soft_tissue)
    actual_texts = list(set(actual_texts))

    # Verify Danish strings

    verified = set()

    for text in actual_texts:

        if ignore_text(text):
            continue

        for row in sheet.iter_rows(min_row=2, values_only=True):

            if len(row) < 5:
                continue

            if row[1] is None or row[5] is None:
                continue

            english = str(row[1]).strip()
            danish = str(row[5]).strip()

            if danish == text and danish not in verified:

                test.passes(english + " -> " + danish)
                verified.add(danish)
                break

    workbook.close()

    if verified:
        test.passes("DANISH SOFT TISSUE-GUIDED LOCALIZATION VALIDATION PASSED")
    else:
        test.fail("NO DANISH STRINGS FOUND ON SOFT TISSUE-GUIDED SCREEN")