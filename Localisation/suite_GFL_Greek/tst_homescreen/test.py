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

def load_greek_strings():
    workbook = openpyxl.load_workbook(EXCEL_PATH, data_only=True, read_only=True)
    sheet = workbook["Home Screen"]
    strings = {}
    for row in sheet.iter_rows(min_row=2, values_only=True):
        if len(row) < 12:
            continue
        english = row[1]
        greek = row[11]
        if english is None or greek is None:
            continue
        english = str(english).strip()
        greek = str(greek).strip()
        if not english or not greek:
            continue
        key = normalize(greek)
        if key and key not in strings:
            strings[key] = {
                "english": english,
                "greek": greek
            }
    workbook.close()
    return strings

def verify_screen(root_object, greek_strings):
    screen_texts = get_all_texts(root_object, is_root=True)
    screen_strings = set()
    for text in screen_texts:
        normalized = normalize(text)
        if normalized:
            screen_strings.add(normalized)
    for screen_text in screen_strings:
        if screen_text in greek_strings:
            if screen_text in verified_strings:
                continue
            verified_strings.add(screen_text)
            test.passes(
                greek_strings[screen_text]["english"] +
                " -> " +
                greek_strings[screen_text]["greek"]
            )
        else:
            if screen_text in missing_strings:
                continue
            missing_strings.add(screen_text)
            test.fail(
                "Missing in Excel greek column: " +
                screen_text
            )

def main():
    greek_strings = load_greek_strings()
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    mouseClick(waitForObject(names.fiberVerificationWarningDialog_mainFrame_QFrame), 571, 633, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_settingsButton_QPushButton))
    clickTab(waitForObject(names.settingsScreen_tbSystemInfo_TabWidget), "INFO")
    clickButton(waitForObject(names.gbSystemInformation_pbLanguageSettingsUpdate_QPushButton))
    clickButton(waitForObject(names.languagesFrame_pbGreece_QPushButton))
    clickButton(waitForObject(names.buttonsFrame_acceptButton_QPushButton))
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    verify_screen(waitForObject(names.o_ScreenSwitcher), greek_strings)
    test.vp("Verifying homescreen")