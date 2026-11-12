# -*- coding: utf-8 -*-

import names
import croatian_localization as loc
import openpyxl
import re


EXCEL_PATH = loc.EXCEL_PATH


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

    sendEvent("QMoveEvent", waitForObject(names.o_ScreenSwitcher), 39, 200, 787, 218)
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    doubleClick(waitForObject(names.numpad_pushButton_8_NumpadButton), 39, 47, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton))


    # CHANGE LANGUAGE TO CROATIAN

    clickButton(waitForObject(names.homeScreen_settingsButton_QPushButton))
    clickTab(waitForObject(names.settingsScreen_tbSystemInfo_TabWidget), "INFO")
    clickButton(waitForObject(names.gbSystemInformation_pbLanguageSettingsUpdate_QPushButton))
    clickButton(waitForObject(names.languagesFrame_pbCroatia_QPushButton))
    clickButton(waitForObject(names.buttonsFrame_acceptButton_QPushButton))
    


    # SYSTEM TAB

    clickTab(waitForObject(names.settingsScreen_tbSystemInfo_TabWidget), "SUSTAV")

    test.vp("Verify stystem Screen")

    


    # VERIFY COMPLETE SYSTEM SETTINGS SCREEN

    verify_screen(
        waitForObject(names.o_ScreenSwitcher),
        "System Settings"
    )


    # BRIGHTNESS CLICK

    mouseClick(waitForObject(names.systemsettingframe_lbBrightnessName_QLabel), 66, 35, Qt.NoModifier, Qt.LeftButton)


    # VERIFY COMPLETE SCREEN AGAIN

    verify_screen(
        waitForObject(names.o_ScreenSwitcher),
        "System Settings after Brightness click"
    )


    # AIMING BEAM CLICK

    mouseClick(waitForObject(names.aimingbeamsettingframe_lbAimingBeamDefaultModeName_QLabel), 58, 16, Qt.NoModifier, Qt.LeftButton)


    # VERIFY COMPLETE SCREEN AGAIN

    verify_screen(
        waitForObject(names.o_ScreenSwitcher),
        "System Settings after Aiming Beam click"
    )
