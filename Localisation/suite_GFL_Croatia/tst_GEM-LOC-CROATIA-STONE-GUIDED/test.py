
# -*- coding: utf-8 -*-

import names
import openpyxl
import os
import re
import html


# --------------------------------------------------
# CONFIGURATION
# --------------------------------------------------

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

SHEET_NAME = "Stone-Guided"

ENGLISH_COLUMN = 2
CROATIAN_COLUMN = 4


# --------------------------------------------------
# NORMALIZE TEXT
# --------------------------------------------------

def normalize(text):

    if text is None:
        return ""

    text = html.unescape(str(text))

    # Remove HTML tags
    text = re.sub(r"<[^>]+>", "", text)

    # Normalize spaces
    text = re.sub(r"\s+", " ", text)

    # Normalize spaces around comparison symbols
    text = re.sub(r"\s*([<>])\s*", r"\1", text)

    return text.strip()


# --------------------------------------------------
# GET ALL TEXTS FROM SCREEN
# --------------------------------------------------

def get_all_texts(obj):

    texts = []

    try:
        text = normalize(obj.text)

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


# --------------------------------------------------
# MAIN
# --------------------------------------------------

def main():

    # --------------------------------------------------
    # LOGIN
    # --------------------------------------------------

    clickButton(
        waitForObject(names.numpad_pushButton_8_NumpadButton)
    )

    clickButton(
        waitForObject(names.numpad_pushButton_8_NumpadButton)
    )

    clickButton(
        waitForObject(names.numpad_pushButton_8_NumpadButton)
    )

    clickButton(
        waitForObject(names.numpad_pushButton_8_NumpadButton)
    )

    clickButton(
        waitForObject(names.mainFrame_okButton_QPushButton)
    )


    # --------------------------------------------------
    # CHANGE LANGUAGE TO CROATIAN
    # --------------------------------------------------

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

    clickButton(
        waitForObject(names.languagesFrame_pbCroatia_QPushButton)
    )

    clickButton(
        waitForObject(names.buttonsFrame_acceptButton_QPushButton)
    )

    clickButton(
        waitForObject(names.settingsScreen_pbBack_QPushButton)
    )


    # --------------------------------------------------
    # OPEN STONE ASSISTANT
    # --------------------------------------------------

    clickButton(
        waitForObject(names.homeScreen_pbStoneAssistant_QToolButton)
    )


    # --------------------------------------------------
    # SELECT STONE CHARACTERISTICS
    # --------------------------------------------------

    clickButton(
        waitForObject(
            names.locationFrame_kidneyPcnlLocationButton_QPushButton
        )
    )

    clickButton(
        waitForObject(
            names.flowRateFrame_lowFlowRateButton_QPushButton
        )
    )

    clickButton(
        waitForObject(
            names.hardnessFrame_smallHardnessButton_QPushButton
        )
    )

    mouseClick(
        waitForObject(names.fiberFrame_label_QLabel),
        296, 22,
        Qt.NoModifier,
        Qt.LeftButton
    )

    mouseClick(
        waitForObject(
            names.stoneAssistantModeScreen_StoneAssistantModeScreen
        ),
        862, 689,
        Qt.NoModifier,
        Qt.LeftButton
    )


    # --------------------------------------------------
    # READ EXCEL
    # --------------------------------------------------

    if not os.path.exists(EXCEL_PATH):

        test.fail("Excel file not found: " + EXCEL_PATH)
        return

    workbook = openpyxl.load_workbook(EXCEL_PATH)

    if SHEET_NAME not in workbook.sheetnames:

        test.fail("Worksheet not found: " + SHEET_NAME)
        workbook.close()
        return

    sheet = workbook[SHEET_NAME]


    # --------------------------------------------------
    # LOAD CROATIAN TRANSLATIONS
    # --------------------------------------------------

    expected_strings = {}

    for row in sheet.iter_rows(min_row=2, values_only=True):

        english_value = row[ENGLISH_COLUMN - 1]
        croatian_value = row[CROATIAN_COLUMN - 1]

        if english_value is None or croatian_value is None:
            continue

        english = normalize(english_value)
        croatian = normalize(croatian_value)

        if english and croatian:
            expected_strings[croatian] = english


    # --------------------------------------------------
    # GET CURRENT SCREEN TEXT
    # --------------------------------------------------

    stone_screen = waitForObject(
        names.stoneAssistantModeScreen_StoneAssistantModeScreen
    )

    actual_texts = get_all_texts(stone_screen)

    actual_texts = list(set(actual_texts))


    # --------------------------------------------------
    # VERIFY ONLY SCREEN STRINGS
    # --------------------------------------------------

    verified_strings = set()

    for text in actual_texts:

        text = normalize(text)

        if text in expected_strings:

            if text not in verified_strings:

                english = expected_strings[text]

                test.passes(
                    "Verified: " + english + " -> " + text
                )

                verified_strings.add(text)


    # --------------------------------------------------
    # FINAL RESULT
    # --------------------------------------------------

    if verified_strings:

        test.passes(
            "Total Croatian strings verified: " +
            str(len(verified_strings))
        )

    else:

        test.fail(
            "No matching Croatian strings found on Stone Guided screen"
        )

    workbook.close()
