# -*- coding: utf-8 -*-

import names
import openpyxl
import re

EXCEL_PATH = "/home/ntc/Test_Automation_Gemini/Localisation/suite_GFL_Czech/tst_Home Screen/testdata/Gemini Split strings.xlsx"


def normalize(text):
    text = re.sub(r"<br\s*/?>", " ", str(text), flags=re.IGNORECASE)
    text = re.sub(r"<[^>]+>", "", text).replace("\xa0", " ")
    return " ".join(text.split()).strip().lower()


def get_all_texts(obj):
    texts = []
    try:
        if not obj.visible: return texts
    except: pass
    for attr in ("text", "title"):
        try:
            value = str(getattr(obj, attr)).strip()
            if value:
                value = re.sub(r"<br\s*/?>", " ", value, flags=re.IGNORECASE)
                value = re.sub(r"<[^>]+>", "", value)
                value = " ".join(value.split())
                if value: texts.append(value)
        except: pass
    try:
        for child in object.children(obj): texts.extend(get_all_texts(child))
    except: pass
    return texts


def main():

    sendEvent("QMoveEvent", waitForObject(names.o_ScreenSwitcher), 82, 182, 715, 202)
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton))

    clickButton(waitForObject(names.homeScreen_settingsButton_QPushButton))
    clickTab(waitForObject(names.settingsScreen_tbSystemInfo_TabWidget), "INFO")
    clickButton(waitForObject(names.gbSystemInformation_pbLanguageSettingsUpdate_QPushButton))
    clickButton(waitForObject(names.languagesFrame_pbDutch_QPushButton))
    clickButton(waitForObject(names.buttonsFrame_acceptButton_QPushButton))
    clickButton(waitForObject(names.settingsScreen_pbBack_QPushButton))
    snooze(1)

    home = waitForObject(names.homeScreen_HomeScreen)
    mouseClick(home, 643, 86, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.homeScreen_gbExpert_QFrame), 86, 108, Qt.NoModifier, Qt.LeftButton)
    snooze(1)

    workbook = openpyxl.load_workbook(EXCEL_PATH, data_only=True)
    sheet = workbook["Home Screen"]

    actual_texts = set(normalize(text) for text in get_all_texts(home) if text and text.strip())

    verified = set()
    pass_count = 0
    fail_count = 0

    for row in sheet.iter_rows(min_row=2, values_only=True):

        if len(row) < 5: continue

        english, dutch = row[1], row[6]

        if english is None or dutch is None: continue

        english, dutch = str(english).strip(), str(dutch).strip()

        if not english or not dutch: continue

        dutch_key = normalize(dutch)

        if not dutch_key or dutch_key in verified: continue

        verified.add(dutch_key)

        if dutch_key in actual_texts:
            test.passes("PASS: " + english + " -> " + dutch)
            pass_count += 1
        else:
            test.fail("FAIL: " + english + " -> " + dutch + " | Dutch string is missing on Home Screen")
            fail_count += 1

    workbook.close()

    if fail_count > 0:
        test.fail("DUTCH HOME SCREEN LOCALIZATION VALIDATION FAILED")
    elif pass_count > 0:
        test.passes("DUTCH HOME SCREEN LOCALIZATION VALIDATION PASSED")
    else:
        test.fail("NO DUTCH EXCEL STRINGS FOUND FOR VALIDATION")