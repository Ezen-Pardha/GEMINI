# -*- coding: utf-8 -*-

import names
import croatian_localization as loc
import openpyxl
import re
import os

TESTCASE_DIR = os.path.dirname(os.path.abspath(__file__))

EXCEL_PATH = loc.EXCEL_PATH

verified_strings = set()


def normalize(text):
    return loc.normalize(text)


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
    return loc.translated_rows()


def verify_screen(root_object, screen_name):
    return loc.verify_screen(root_object, screen_name, globals())


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