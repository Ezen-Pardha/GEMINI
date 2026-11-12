
# -*- coding: utf-8 -*-

import names
import croatian_localization as loc
import openpyxl
import re
import os

TESTCASE_DIR = os.path.dirname(os.path.abspath(__file__))

EXCEL_PATH = loc.EXCEL_PATH

SHEET_NAME = "Stone"

ENGLISH_COLUMN = 2       # Column B
CROATIAN_COLUMN = 4      # Column I


def normalize(text):
    return loc.normalize(text)


def load_croatian_strings():
    return loc.translated_rows()


def get_object_text(obj):
    texts = []

    for attribute in ("text", "windowTitle", "placeholderText"):
        try:
            value = getattr(obj, attribute)

            if callable(value):
                value = value()

            if value is not None:
                value = str(value).strip()

                if value and normalize(value):
                    texts.append(value)

        except Exception:
            pass

    try:
        value = str(obj).strip()

        if value and normalize(value):
            texts.append(value)

    except Exception:
        pass

    return texts


def collect_screen_text(obj, collected=None, visited=None, depth=0):
    return loc.collect_texts(obj, object.children)


def build_screen_candidates(screen_texts):
    candidates = {}

    for text_value in screen_texts:
        cleaned = normalize(text_value)

        if cleaned:
            candidates[cleaned] = text_value

        # Split multiline or HTML-derived text into individual lines.
        for line in re.split(r"[\r\n]+", str(text_value)):
            line = normalize(line)

            if line:
                candidates[line] = line

    return candidates


def validate_croatian_strings(translations, screen_candidates):
    return loc.verify_texts(list(screen_candidates.values()), "Stone Guided", test)


def main():
    # Load translations from Excel.
    croatian_translations = load_croatian_strings()

    if not croatian_translations:
        test.fail("No Croatian translations were loaded.")
        return

    # Log in to the application.
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton))

    # Set the application language to Croatian using the
    # language-selection steps already defined in your suite.
    # If the application is already set to Croatian, continue.

    loc.select_croatian(globals())

    # Open Stone Assistant.
    clickButton(
        waitForObject(names.homeScreen_pbStoneAssistant_QToolButton)
    )

    # Select Stone Guided options.
    clickButton(
        waitForObject(
            names.locationFrame_kidneyPcnlLocationButton_QPushButton
        )
    )

    clickButton(
        waitForObject(
            names.flowRateFrame_mediumFlowRateButton_QPushButton
        )
    )

    clickButton(
        waitForObject(
            names.hardnessFrame_largeHardnessButton_QPushButton
        )
    )

    # Wait for the Stone Guided screen.
    stone_screen = waitForObject(
        names.stoneAssistantModeScreen_StoneAssistantModeScreen
    )

    test.log("Screen: Stone Guided")

    # Compare the screen screenshot if the screenshot checkpoint
    # is configured in this test case.
    test.vp("Verify Stone Guided Screen")

    # Collect visible text from the current screen.
    screen_texts = collect_screen_text(stone_screen)

    test.log(
        "Screen text items collected: {}".format(len(screen_texts))
    )

    screen_candidates = build_screen_candidates(screen_texts)

    test.log(
        "Screen text candidates collected: {}".format(
            len(screen_candidates)
        )
    )

    # Validate every Croatian translation loaded from Excel.
    validate_croatian_strings(
        croatian_translations,
        screen_candidates
    )


def cleanup():
    pass
