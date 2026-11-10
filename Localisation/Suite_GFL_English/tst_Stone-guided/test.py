
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

    if not os.path.exists(EXCEL_PATH):
        test.fail("Excel file not found: " + EXCEL_PATH)
        return []

    try:

        workbook = openpyxl.load_workbook(
            EXCEL_PATH,
            read_only=True,
            data_only=True
        )

        strings = {}

        for sheet in workbook.worksheets:

            test.log("Reading worksheet: " + sheet.title)

            # Column B contains English strings
            for row in sheet.iter_rows(
                min_row=2,
                min_col=2,
                max_col=2,
                values_only=True
            ):

                english = row[0]

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
            "Total unique English strings loaded: "
            + str(len(strings))
        )

        return list(strings.values())

    except Exception as e:

        test.fail("Excel reading error: " + str(e))
        return []




def verify_screen(root_object):

    excel_strings = load_english_strings()

    if not excel_strings:
        test.fail("No English strings loaded from Excel.")
        return

    screen_texts = get_all_texts(root_object)

    unique_texts = set()

    for text in screen_texts:

        normalized = normalize(text)

        if normalized:
            unique_texts.add(normalized)

    screen_verified = set()

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
            screen_verified.add(key)

            test.passes(
                "English string verified: " + english
            )

    if not screen_verified:

        test.log(
            "No new English strings matched on this screen."
        )




def main():

    

    sendEvent(
        "QMoveEvent",
        waitForObject(names.o_ScreenSwitcher),
        31,
        178,
        662,
        192
    )

    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))

    clickButton(waitForObject(names.mainFrame_okButton_QPushButton))

    verify_screen(waitForObject(names.o_ScreenSwitcher))

    

    clickButton(
        waitForObject(
            names.homeScreen_pbStoneAssistant_QToolButton
        )
    )

    verify_screen(waitForObject(names.o_ScreenSwitcher))

    

    clickButton(
        waitForObject(
            names.locationFrame_kidneyPcnlLocationButton_QPushButton
        )
    )

    verify_screen(waitForObject(names.o_ScreenSwitcher))

    

    clickButton(
        waitForObject(
            names.flowRateFrame_lowFlowRateButton_QPushButton
        )
    )

    verify_screen(waitForObject(names.o_ScreenSwitcher))

    

    clickButton(
        waitForObject(
            names.hardnessFrame_smallHardnessButton_QPushButton
        )
    )

    verify_screen(waitForObject(names.o_ScreenSwitcher))

    

    mouseClick(
        waitForObject(
            names.stoneAssistantModeScreen_centralWidget_QWidget
        ),
        851,
        260,
        Qt.NoModifier,
        Qt.LeftButton
    )

    verify_screen(waitForObject(names.o_ScreenSwitcher))

    

    mouseClick(
        waitForObject(
            names.stoneAssistantModeScreen_centralWidget_QWidget
        ),
        428,
        328,
        Qt.NoModifier,
        Qt.LeftButton
    )

    verify_screen(waitForObject(names.o_ScreenSwitcher))
