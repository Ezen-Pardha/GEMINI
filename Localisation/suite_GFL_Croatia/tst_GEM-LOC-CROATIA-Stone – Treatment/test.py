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
    except Exception:
        pass

    try:
        value = str(obj.text).strip()

        if value:
            value = re.sub(r"<[^>]+>", " ", value)
            value = " ".join(value.split())

            if value:
                texts.append(value)
    except Exception:
        pass

    try:
        value = str(obj.title).strip()

        if value:
            value = re.sub(r"<[^>]+>", " ", value)
            value = " ".join(value.split())

            if value:
                texts.append(value)
    except Exception:
        pass

    try:
        for child in object.children(obj):
            texts.extend(get_all_texts(child))
    except Exception:
        pass

    return texts


def load_croatian_strings():
    workbook = openpyxl.load_workbook(
        EXCEL_PATH,
        data_only=True,
        read_only=True
    )

    try:
        sheet = workbook.active
        strings = {}

        for row in sheet.iter_rows(min_row=2, values_only=True):

            if len(row) < 4:
                continue

            english = row[1]
            croatian = row[3]

            if english is None or croatian is None:
                continue

            english = str(english).strip()
            croatian = str(croatian).strip()

            if not english or not croatian:
                continue

            key = normalize(croatian)

            if key and key not in strings:
                strings[key] = {
                    "english": english,
                    "croatian": croatian
                }

        return list(strings.values())

    finally:
        workbook.close()


def verify_screen(root_object, screen_name):
    excel_strings = load_croatian_strings()
    screen_texts = get_all_texts(root_object)

    unique_texts = {}

    for text in screen_texts:
        normalized = normalize(text)

        if normalized:
            unique_texts.setdefault(normalized, text.strip())

    matched_count = 0
    missing_count = 0

    for normalized, screen_text in unique_texts.items():

        matches = []

        for item in excel_strings:
            excel_text = normalize(item["croatian"])

            if normalized == excel_text:
                matches.append(item)

            elif len(excel_text) >= 4 and excel_text in normalized:
                matches.append(item)

        matches.sort(
            key=lambda item: len(normalize(item["croatian"])),
            reverse=True
        )

        if matches:
            for item in matches:
                key = normalize(item["croatian"])

                if key in verified_strings:
                    continue

                verified_strings.add(key)

                test.passes(
                    "{} | PASS: {} -> {}".format(
                        screen_name,
                        item["english"],
                        item["croatian"]
                    )
                )

                matched_count += 1

        else:
            test.fail(
                "{} | FAIL: Visible string missing from Croatian Excel: {}".format(
                    screen_name,
                    screen_text
                )
            )

            missing_count += 1

    test.log(
        "{} | Total screen strings: {} | Matched: {} | Missing: {}".format(
            screen_name,
            len(unique_texts),
            matched_count,
            missing_count
        )
    )


def main():

    # LOGIN

    sendEvent(
        "QMoveEvent",
        waitForObject(names.o_ScreenSwitcher),
        33, 192, 737, 203
    )

    doubleClick(
        waitForObject(names.numpad_pushButton_8_NumpadButton),
        76, 50,
        Qt.NoModifier,
        Qt.LeftButton
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

    # CHANGE LANGUAGE TO CROATIAN

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

    # OPEN QUICK START

    clickButton(
        waitForObject(names.homeScreen_pbStoneQuickStart_QToolButton)
    )

    verify_screen(
        waitForObject(names.o_ScreenSwitcher),
        "Quick Start"
    )

    # SELECT LEFT PRESET

    mouseClick(
        waitForObjectItem(
            names.tabLeftMainPresets_leftPresetsView_PresetListView,
            "_1"
        ),
        404, 36,
        Qt.NoModifier,
        Qt.LeftButton
    )

    verify_screen(
        waitForObject(names.o_ScreenSwitcher),
        "Quick Start - Left Preset"
    )

    # SELECT RIGHT PRESET

    mouseClick(
        waitForObjectItem(
            names.tabRightMainPresets_rightPresetsView_PresetListView,
            "_1"
        ),
        92, 47,
        Qt.NoModifier,
        Qt.LeftButton
    )

    verify_screen(
        waitForObject(names.o_ScreenSwitcher),
        "Quick Start - Right Preset"
    )

    # CONTINUE TO TREATMENT

    clickButton(
        waitForObject(names.quickStartScreen_pbContinue_QPushButton)
    )

    verify_screen(
        waitForObject(names.o_ScreenSwitcher),
        "Treatment Screen"
    )

    test.vp("Verify stone treatment screen")

    # CLICK LEFT PEDAL

    mouseClick(
        waitForObject(names.treatmentScreen_leftPedalWidgetBorder_QWidget),
        629, 48,
        Qt.NoModifier,
        Qt.LeftButton
    )

    verify_screen(
        waitForObject(names.o_ScreenSwitcher),
        "Treatment Screen - Left Pedal"
    )