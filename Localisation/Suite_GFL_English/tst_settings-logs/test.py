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

    return text.casefold().strip()


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

    workbook = openpyxl.load_workbook(
        EXCEL_PATH,
        data_only=True
    )

    sheet = workbook.active

    strings = {}

    for row in sheet.iter_rows(
        min_row=2,
        values_only=True
    ):

        if len(row) < 1:
            continue

        # English is Column A
        english = row[0]

        if english is None:
            continue

        english = str(english).strip()

        if not english:
            continue

        key = normalize(english)

        if key not in strings:
            strings[key] = english

    return strings


def verify_screen(root_object, screen_name):

    global verified_strings

    excel_strings = load_english_strings()
    screen_texts = get_all_texts(root_object)

    unique_texts = set()

    for text in screen_texts:

        normalized = normalize(text)

        if normalized:
            unique_texts.add(normalized)

    for screen_text in unique_texts:

        if screen_text in verified_strings:
            continue

        matches = []

        # Exact match
        if screen_text in excel_strings:

            matches.append(
                excel_strings[screen_text]
            )

        else:

            # Excel string contained in UI text
            for excel_normalized, excel_original in excel_strings.items():

                if len(excel_normalized) >= 4 and excel_normalized in screen_text:

                    matches.append(excel_original)

            # UI text contained in Excel string
            if not matches:

                for excel_normalized, excel_original in excel_strings.items():

                    if len(screen_text) >= 4 and screen_text in excel_normalized:

                        matches.append(excel_original)

        if matches:

            matched = matches[0]
            key = normalize(matched)

            if key not in verified_strings:

                verified_strings.add(key)
                test.passes(matched)

        else:

            verified_strings.add(screen_text)

            test.fail(
                str(screen_text) +
                " -> String not found in Excel"
            )


def main():

    # LOGIN

    sendEvent(
        "QMoveEvent",
        waitForObject(names.o_ScreenSwitcher),
        55,
        179,
        687,
        187
    )

    clickButton(
        waitForObject(
            names.numpad_pushButton_8_NumpadButton
        )
    )

    clickButton(
        waitForObject(
            names.numpad_pushButton_8_NumpadButton
        )
    )

    clickButton(
        waitForObject(
            names.numpad_pushButton_8_NumpadButton
        )
    )

    clickButton(
        waitForObject(
            names.numpad_pushButton_8_NumpadButton
        )
    )

    clickButton(
        waitForObject(
            names.mainFrame_okButton_QPushButton
        )
    )

    # OPEN SETTINGS

    clickButton(
        waitForObject(
            names.homeScreen_settingsButton_QPushButton
        )
    )

    verify_screen(
        waitForObject(names.o_ScreenSwitcher),
        "Settings"
    )

    # OPEN LOGS TAB

    clickTab(
        waitForObject(
            names.settingsScreen_tbSystemInfo_TabWidget
        ),
        "LOGS"
    )

    verify_screen(
        waitForObject(names.o_ScreenSwitcher),
        "Logs"
    )

    # CLICK LOG ENTRY

    mouseClick(
        waitForObjectItem(
            names.systemEventErrorLogWidget_tableView_QTableView,
            "3/0"
        ),
        217,
        17,
        Qt.NoModifier,
        Qt.LeftButton
    )

    verify_screen(
        waitForObject(names.o_ScreenSwitcher),
        "Logs after selecting entry"
    )