# -*- coding: utf-8 -*-

import names
import openpyxl
import re


EXCEL_PATH = "/home/ntc/Test_Automation_Gemini/Localisation/Suite_GFL_English/tst_LoginScreen-Logoff/testdata/Gemini strings.xlsx"

verified_strings = set()


def normalize(text):

    if text is None:
        return ""

    text = re.sub(r"<[^>]+>", " ", str(text))
    text = " ".join(text.split())
    text = re.sub(r"\s*<\s*", " < ", text)
    text = re.sub(r"\s*>\s*", " > ", text)

    return text.casefold()


def get_all_texts(obj):

    texts = []

    try:
        if not obj.visible:
            return texts
    except:
        pass

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


def load_english_strings():

    workbook = openpyxl.load_workbook(EXCEL_PATH, data_only=True)
    sheet = workbook.active

    strings = {}

    for row in sheet.iter_rows(min_row=2, values_only=True):

        if len(row) < 2:
            continue

        english = row[0]

        if english is None:
            continue

        english = str(english).strip()

        if not english:
            continue

        key = normalize(english)

        if key not in strings:
            strings[key] = english

    return list(strings.values())


def verify_screen(root_object, screen_name):

    excel_strings = load_english_strings()
    screen_texts = get_all_texts(root_object)

    unique_texts = set()

    for text in screen_texts:

        normalized = normalize(text)

        if normalized:
            unique_texts.add(normalized)

    for screen_text in unique_texts:

        matches = []

        for english in excel_strings:

            excel_text = normalize(english)

            if screen_text == excel_text:
                matches.append(english)

            elif len(excel_text) >= 4 and excel_text in screen_text:
                matches.append(english)

        matches.sort(
            key=lambda x: len(normalize(x)),
            reverse=True
        )

        for english in matches:

            key = normalize(english)

            if key in verified_strings:
                continue

            verified_strings.add(key)

            test.passes(english)


def main():

    # LOGIN
    sendEvent("QMoveEvent", waitForObject(names.o_ScreenSwitcher), 34, 208, 625, 226)
    verify_screen(waitForObject(names.o_ScreenSwitcher), "Login Screen")

    # ENTER PASSWORD
    clickButton(waitForObject(names.numpad_pushButton_4_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_5_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_4_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_5_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    snooze(3)
    

    # OK / WARNING DIALOG
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton))

    # VERIFY HOME SCREEN
    verify_screen(waitForObject(names.o_ScreenSwitcher), "Home Screen")

    # LOGOFF
    clickButton(waitForObject(names.homeScreen_logoffButton_QPushButton))
    

    # LOGOFF DIALOG
    verify_screen(waitForObject(names.logOffSystem_centralWidget_QFrame), "Logoff Dialog")

    # LOGOFF QUESTION
    mouseClick(waitForObject(names.logOffSystem_centralWidget_QFrame), 849, 266, Qt.NoModifier, Qt.LeftButton)
    verify_screen(waitForObject(names.logOffSystem_centralWidget_QFrame), "Logoff Question")

    # QUESTION LABEL
    mouseClick(waitForObject(names.centralWidget_questionLabel_QLabel), 602, 192, Qt.NoModifier, Qt.LeftButton)
    verify_screen(waitForObject(names.logOffSystem_centralWidget_QFrame), "Logoff Question Text")

    # ACCEPT LOGOFF
    clickButton(waitForObject(names.buttonsFrame_acceptButton_QPushButton))

    