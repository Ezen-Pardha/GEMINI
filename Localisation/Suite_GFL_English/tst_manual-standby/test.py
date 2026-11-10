
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

SHEET_NAME = "Treatment Modes"

verified_strings = set()
excel_strings = {}



def normalize(text):

    if text is None:
        return ""

    text = str(text)

    text = re.sub(r"<[^>]+>", " ", text)
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

    # Get object text
    try:

        value = obj.text

        if value is not None:

            value = str(value).strip()

            if value:

                value = re.sub(r"<[^>]+>", " ", value)
                value = " ".join(value.split())

                if value:
                    texts.append(value)

    except:
        pass

    # Get object title
    try:

        value = obj.title

        if value is not None:

            value = str(value).strip()

            if value:

                value = re.sub(r"<[^>]+>", " ", value)
                value = " ".join(value.split())

                if value:
                    texts.append(value)

    except:
        pass

    # Get child objects recursively
    try:

        for child in object.children(obj):

            texts.extend(get_all_texts(child))

    except:
        pass

    return texts



def load_english_strings():

    try:

        if not os.path.exists(EXCEL_PATH):

            test.fail(
                "Excel file not found: " + EXCEL_PATH
            )

            return {}

        workbook = openpyxl.load_workbook(
            EXCEL_PATH,
            data_only=True,
            read_only=True
        )

        if SHEET_NAME not in workbook.sheetnames:

            test.fail(
                "Worksheet not found: " + SHEET_NAME
            )

            workbook.close()
            return {}

        sheet = workbook[SHEET_NAME]

        strings = {}

        # Read English strings from Column A
        for row in sheet.iter_rows(
            min_row=2,
            min_col=1,
            max_col=30,
            values_only=True
        ):

            english = row[1]

            if english is None:
                continue

            english = str(english).strip()

            if not english:
                continue

            key = normalize(english)

            if key not in strings:

                strings[key] = english

        workbook.close()

        test.log(
            "Total English strings loaded: "
            + str(len(strings))
        )

        return strings

    except Exception as e:

        test.fail(
            "Excel reading error: " + str(e)
        )

        return {}



def verify_screen(root_object, screen_name):

    screen_texts = get_all_texts(root_object)

    unique_texts = set()

    for text in screen_texts:

        normalized = normalize(text)

        if normalized:
            unique_texts.add(normalized)

    screen_verified = 0

    for screen_text in unique_texts:

        matches = []

        for excel_normalized, english in excel_strings.items():

            # Exact match
            if screen_text == excel_normalized:

                matches.append(english)

            # Combined UI text
            elif (
                len(excel_normalized) >= 4
                and excel_normalized in screen_text
            ):

                matches.append(english)

        # Longest matching string first
        matches.sort(
            key=lambda x: len(normalize(x)),
            reverse=True
        )

        for english in matches:

            key = normalize(english)

            # Prevent duplicate results
            if key in verified_strings:
                continue

            verified_strings.add(key)

            screen_verified += 1

            # Individual PASS result in Squish
            test.passes(
                "VERIFIED | "
                + screen_name
                + " | "
                + english
            )

    test.log(
        "Total verified on "
        + screen_name
        + ": "
        + str(screen_verified)
    )



def final_verification():

    test.log("----------------------------------------")
    test.log("VISIBLE ENGLISH STRING VERIFICATION")
    test.log("----------------------------------------")

    test.log(
        "Total Excel strings: "
        + str(len(excel_strings))
    )

    test.log(
        "Total unique verified strings: "
        + str(len(verified_strings))
    )

    test.log("----------------------------------------")

    test.log("VERIFIED STRINGS LIST:")

    for english in sorted(verified_strings):

        test.log(english)

    test.log("----------------------------------------")



def main():

    global excel_strings

    # LOAD EXCEL STRINGS ONCE

    excel_strings = load_english_strings()

    if not excel_strings:

        test.fail(
            "No English strings available for verification."
        )

        return



    sendEvent(
        "QMoveEvent",
        waitForObject(names.o_ScreenSwitcher),
        61,
        186,
        672,
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

    verify_screen(
        waitForObject(names.o_ScreenSwitcher),
        "After Login"
    )



    clickButton(
        waitForObject(
            names.gbExpert_expertButton_QPushButton
        )
    )

    verify_screen(
        waitForObject(names.o_ScreenSwitcher),
        "Expert"
    )



    mouseClick(
        waitForObject(
            names.rightPedalWidget_wdPresetTabs_TabWidget
        ),
        5,
        30,
        Qt.NoModifier,
        Qt.LeftButton
    )

    verify_screen(
        waitForObject(names.o_ScreenSwitcher),
        "Expert - Right Pedal Preset"
    )



    mouseClick(
        waitForObject(
            names.leftPedalWidget_wdPresetTabs_TabWidget
        ),
        457,
        30,
        Qt.NoModifier,
        Qt.LeftButton
    )

    verify_screen(
        waitForObject(names.o_ScreenSwitcher),
        "Expert - Left Pedal Preset"
    )



    final_verification()
