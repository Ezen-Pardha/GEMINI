# -*- coding: utf-8 -*-

import names
import openpyxl
import re
import os

TESTCASE_DIR = os.path.dirname(os.path.abspath(__file__))

EXCEL_PATH = os.path.abspath(
    os.path.join(
        TESTCASE_DIR,
        "..",
        "shared",
        "testdata",
        "Gemini Split strings.xlsx"
    )
)
verified_strings = set()
missing_strings = set()

def normalize(text):
    if text is None:
        return ""
    text = re.sub(r"<[^>]+>", " ", str(text))
    text = " ".join(text.split())
    text = re.sub(r"\s*<\s*", " < ", text)
    text = re.sub(r"\s*>\s*", " > ", text)
    return text.casefold()

def get_all_texts(obj, is_root=False):
    texts = []
    if not is_root:
        try:
            if not obj.visible:
                return texts
        except:
            return texts
    try:
        value = str(obj.text).strip()
        if value:
            value = re.sub(r"<[^>]+>", " ", value)
            value = " ".join(value.split())
            if value:
                texts.append(value)
    except:
        pass
    try:
        value = str(obj.title).strip()
        if value:
            value = re.sub(r"<[^>]+>", " ", value)
            value = " ".join(value.split())
            if value:
                texts.append(value)
    except:
        pass
    try:
        for child in object.children(obj):
            texts.extend(get_all_texts(child))
    except:
        pass
    return texts

def load_luthanian_strings():
    workbook = openpyxl.load_workbook(EXCEL_PATH, data_only=True, read_only=True)
    strings = {}
    for sheet in workbook.worksheets:
        for row in sheet.iter_rows(min_row=2, values_only=True):
            if len(row) < 17:
                continue
            english = row[1]
            luthanian = row[16]
            if english is None or luthanian is None:
                continue
            english = str(english).strip()
            luthanian = str(luthanian).strip()
            if not english or not luthanian:
                continue
            key = normalize(luthanian)
            if key and key not in strings:
                strings[key] = {
                    "english": english,
                    "luthanian": luthanian
                }
    workbook.close()
    return strings

def verify_screen(root_object, luthanian_strings):
    screen_texts = get_all_texts(root_object, is_root=True)
    screen_strings = set()
    for text in screen_texts:
        normalized = normalize(text)
        if normalized:
            screen_strings.add(normalized)
    for screen_text in screen_strings:
        if screen_text in luthanian_strings:
            if screen_text in verified_strings:
                continue
            verified_strings.add(screen_text)
            test.passes(
                luthanian_strings[screen_text]["english"] +
                " -> " +
                luthanian_strings[screen_text]["luthanian"]
            )
        else:
            if screen_text in missing_strings:
                continue
            missing_strings.add(screen_text)
            test.fail(
                "Missing in Excel luthanian column: " +
                screen_text
            )

def main():
    luthanian_strings = load_luthanian_strings()
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_settingsButton_QPushButton))
    clickTab(waitForObject(names.settingsScreen_tbSystemInfo_TabWidget), "INFO")
    clickButton(waitForObject(names.gbSystemInformation_pbLanguageSettingsUpdate_QPushButton))
    clickButton(waitForObject(names.languagesFrame_pbLithuania_QPushButton))
    clickButton(waitForObject(names.buttonsFrame_acceptButton_QPushButton))
    clickButton(waitForObject(names.settingsScreen_pbBack_QPushButton))
    clickButton(waitForObject(names.homeScreen_logButton_QPushButton))
    mouseClick(waitForObject(names.topBar_buttonsBar_ButtonsBar), 1007, 26, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.treatmentLogScreen_TreatmentLogScreen), 955, 73, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.treatmentLogScreen_tvLogsTable_QTreeView), 775, 136, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.treatmentLogScreen_wdBottom_QWidget), 427, 53, Qt.NoModifier, Qt.LeftButton)
    verify_screen(waitForObject(names.o_ScreenSwitcher), luthanian_strings)
