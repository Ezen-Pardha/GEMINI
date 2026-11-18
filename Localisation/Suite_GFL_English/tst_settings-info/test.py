# -*- coding: utf-8 -*-

import names
import openpyxl
import re


EXCEL_PATH = "/home/ntc/Test_Automation_Gemini/Localisation/Suite_GFL_English/tst_LoginScreen-Logoff/testdata/Gemini strings.xlsx"

verified_strings = set()


def normalize(text):

    if text is None:
        return ""

    text = str(text)

    text = re.sub(r"<[^>]+>", " ", text)

    text = " ".join(text.split())

    text = re.sub(r"\s*<\s*", " < ", text)
    text = re.sub(r"\s*>\s*", " > ", text)

    text = re.sub(r"\s*:\s*", ": ", text)

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

        # ENGLISH = COLUMN A
        english = row[0]

        if english is None:
            continue

        english = str(english).strip()

        if not english:
            continue

        normalized = normalize(english)

        if not normalized:
            continue

        if normalized not in strings:

            strings[normalized] = english

    return strings


def verify_screen(root_object, screen_name):

    global verified_strings

    excel_strings = load_english_strings()

    screen_texts = get_all_texts(root_object)

    unique_screen_texts = {}

    for text in screen_texts:

        normalized = normalize(text)

        if not normalized:
            continue

        if len(normalized) < 2:
            continue

        if normalized not in unique_screen_texts:

            unique_screen_texts[normalized] = text


    for screen_normalized, actual_text in unique_screen_texts.items():

        if screen_normalized in verified_strings:
            continue

        matches = []


        # EXACT MATCH

        if screen_normalized in excel_strings:

            matches.append(
                excel_strings[screen_normalized]
            )


        else:

            # EXCEL STRING INSIDE UI STRING

            for excel_normalized, excel_original in excel_strings.items():

                if len(excel_normalized) < 4:
                    continue

                if excel_normalized in screen_normalized:

                    matches.append(
                        excel_original
                    )


            # UI STRING INSIDE EXCEL STRING

            if not matches:

                for excel_normalized, excel_original in excel_strings.items():

                    if len(screen_normalized) < 4:
                        continue

                    if screen_normalized in excel_normalized:

                        matches.append(
                            excel_original
                        )


        if matches:

            matched = matches[0]

            matched_key = normalize(matched)

            if matched_key not in verified_strings:

                verified_strings.add(matched_key)

                test.passes(matched)

        else:

            verified_strings.add(screen_normalized)

            test.fail(
                actual_text +
                " -> String not found in Excel"
            )


def main():

    # LOGIN

    sendEvent(
        "QMoveEvent",
        waitForObject(names.o_ScreenSwitcher),
        46,
        184,
        709,
        195
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


    # OPEN INFO TAB

    clickTab(
        waitForObject(
            names.settingsScreen_tbSystemInfo_TabWidget
        ),
        "INFO"
    )

    verify_screen(
        waitForObject(names.o_ScreenSwitcher),
        "System Information"
    )


    # SYSTEM INFORMATION

    mouseClick(
        waitForObject(
            names.wdSystemInfoLayout_gbSystemInformation_QGroupBox
        ),
        401,
        0,
        Qt.NoModifier,
        Qt.LeftButton
    )

    verify_screen(
        waitForObject(names.o_ScreenSwitcher),
        "System Information after click"
    )


    # FIBER INFORMATION

    mouseClick(
        waitForObject(
            names.wdSystemInfoLayout_gbFiberInformation_QGroupBox
        ),
        448,
        62,
        Qt.NoModifier,
        Qt.LeftButton
    )

    verify_screen(
        waitForObject(names.o_ScreenSwitcher),
        "Fiber Information"
    )