# -*- coding: utf-8 -*-

import names
import croatian_localization as loc
import openpyxl
import re
import os

TESTCASE_DIR = os.path.dirname(os.path.abspath(__file__))
 
EXCEL_PATH = loc.EXCEL_PATH
# EXCEL_PATH = "/home/Ezen/Test_Automation_Gemini/Localisation/suite_GFL_Croatia/tst_GEM-LOC-CROATIA-STONE-GUIDED/testdata/Gemini strings.xlsx"

def normalize(text):
    return loc.normalize(text)


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


def load_croatian_strings():
    return loc.translated_rows()


def verify_screen(root_object, screen_name):
    return loc.verify_screen(root_object, screen_name, globals())


def main():

    # LOGIN

    sendEvent("QMoveEvent", waitForObject(names.o_ScreenSwitcher), 62, 205, 692, 220)
    doubleClick(waitForObject(names.numpad_pushButton_8_NumpadButton), 64, 50, Qt.NoModifier, Qt.LeftButton)
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


    # OPEN EXPERT SCREEN

    clickButton(waitForObject(names.gbExpert_expertButton_QPushButton))

    # test.vp("Verify Manual Screen")

   


    # VERIFY COMPLETE EXPERT SCREEN

    verify_screen(waitForObject(names.o_ScreenSwitcher), "Expert")


    # CLICK AVERAGE POWER UNITS

    mouseClick(waitForObject(names.croatiaTreatment_averagePowerUnits_QLabel), 153, 75, Qt.NoModifier, Qt.LeftButton)

    verify_screen(waitForObject(names.o_ScreenSwitcher), "Expert after Average Power unit click")


    # CLICK AVERAGE POWER NAME

    mouseClick(waitForObject(names.croatiaTreatment_averagePowerName_QLabel), 13, 64, Qt.NoModifier, Qt.LeftButton)

    verify_screen(waitForObject(names.o_ScreenSwitcher), "Expert after Average Power click")


    # CLICK LEFT PEDAL PRESET TAB

    mouseClick(waitForObject(names.leftPedalWidget_wdPresetTabs_TabWidget), 587, 18, Qt.NoModifier, Qt.LeftButton)

    verify_screen(waitForObject(names.o_ScreenSwitcher), "Expert after Left Pedal preset click")
