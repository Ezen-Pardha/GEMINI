
# -*- coding: utf-8 -*-

import names
import croatian_localization as loc
import openpyxl
import re
import os


TESTCASE_DIR = os.path.dirname(os.path.abspath(__file__))

EXCEL_PATH = loc.EXCEL_PATH

SHEET_NAME = "Treatment Modes"


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
        35, 207, 674, 225
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

    # OPEN SOFT TISSUE ASSISTANT
    clickButton(
        waitForObject(names.homeScreen_pbSoftTissueAssistant_QToolButton)
    )

    clickButton(
        waitForObject(names.gbSoftTissueProcedures_pbIncision_QPushButton)
    )

    clickButton(
        waitForObject(
            names.softTissueAssistantModeScreen_pbContinue_QPushButton
        )
    )

    # VERIFY INITIAL SOFT TISSUE SCREEN
    verify_screen(
        waitForObject(names.o_ScreenSwitcher),
        "Soft Tissue Assistant"
    )

    test.vp("Verify Soft Tissue Guided Treatment")

    # CLICK LEFT PEDAL PRESET TAB
    mouseClick(
        waitForObject(names.leftPedalWidget_wdPresetTabs_TabWidget),
        615, 42,
        Qt.NoModifier,
        Qt.LeftButton
    )

    # VERIFY STRINGS AFTER CLICK
    verify_screen(
        waitForObject(names.o_ScreenSwitcher),
        "Left Pedal Presets"
    )
