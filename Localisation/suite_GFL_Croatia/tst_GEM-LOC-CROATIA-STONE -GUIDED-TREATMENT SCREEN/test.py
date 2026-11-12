# -*- coding: utf-8 -*-

import names
import croatian_localization as loc
import openpyxl
import re
import os


<<<<<<< HEAD
EXCEL_PATH = loc.EXCEL_PATH
=======
TESTCASE_DIR = os.path.dirname(os.path.abspath(__file__))
>>>>>>> afaf95eb9524d0398baf7cef49b0e422af595ff6

EXCEL_PATH = os.path.abspath(
    os.path.join(
        TESTCASE_DIR,
        "..",
        "shared",
        "testdata",
        "Gemini Split strings.xlsx"
    )
)
def normalize(text):
    return loc.normalize(text)


def get_all_texts(obj):

    texts = []

    try:
        if not obj.visible:
            return texts
    except:
        pass

    # TEXT
    try:
        value = str(obj.text).strip()

        if value:
            value = re.sub(r"<[^>]+>", " ", value)
            value = " ".join(value.split())

            if value:
                texts.append(value)
    except:
        pass

    # TITLE
    try:
        value = str(obj.title).strip()

        if value:
            value = re.sub(r"<[^>]+>", " ", value)
            value = " ".join(value.split())

            if value:
                texts.append(value)
    except:
        pass

    # CHILDREN
    try:
        for child in object.children(obj):
            texts.extend(get_all_texts(child))
    except:
        pass

    return texts


def load_croatian_strings():
    return loc.translated_rows()


def verify_screen(root_object, screen_name):
    return loc.verify_screen(root_object, screen_name, globals())


def main():

    # LOGIN
    sendEvent("QMoveEvent", waitForObject(names.o_ScreenSwitcher), 28, 208, 711, 224)
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton))

    # CHANGE LANGUAGE TO CROATIAN
    clickButton(waitForObject(names.homeScreen_settingsButton_QPushButton))
    clickTab(waitForObject(names.settingsScreen_tbSystemInfo_TabWidget), "INFO")
    clickButton(waitForObject(names.gbSystemInformation_pbLanguageSettingsUpdate_QPushButton))
    clickButton(waitForObject(names.languagesFrame_pbCroatia_QPushButton))
    clickButton(waitForObject(names.buttonsFrame_acceptButton_QPushButton))
    clickButton(waitForObject(names.settingsScreen_pbBack_QPushButton))

    # OPEN STONE ASSISTANT
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    clickButton(waitForObject(names.locationFrame_kidneyPcnlLocationButton_QPushButton))
    clickButton(waitForObject(names.flowRateFrame_lowFlowRateButton_QPushButton))
    clickButton(waitForObject(names.hardnessFrame_smallHardnessButton_QPushButton))
    clickButton(waitForObject(names.stoneAssistantModeScreen_continueButton_QPushButton))

    # VERIFY STONE ASSISTANT SCREEN
    verify_screen(waitForObject(names.o_ScreenSwitcher), "Stone Assistant")

    # CLICK LEFT PEDAL PRESET TAB
    mouseClick(waitForObject(names.leftPedalWidget_wdPresetTabs_TabWidget), 623, 63, Qt.NoModifier, Qt.LeftButton)

    # VERIFY STRINGS AFTER LEFT PEDAL CLICK
    verify_screen(waitForObject(names.o_ScreenSwitcher), "Left Pedal Presets")

    # CLICK PEDAL STATUS ICON
    mouseClick(waitForObject(names.bottomBar_lbPedalStatusIcon_QLabel), 47, 47, Qt.NoModifier, Qt.LeftButton)

    test.vp("Verify Stone guided Treatment screen")

    # VERIFY STRINGS AFTER STATUS ICON CLICK
    verify_screen(waitForObject(names.o_ScreenSwitcher), "Pedal Status")
