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


    sendEvent(
        "QMoveEvent",
        waitForObject(names.o_ScreenSwitcher),
        73,
        169,
        688,
        186
    )

    doubleClick(
        waitForObject(names.numpad_pushButton_8_NumpadButton),
        79,
        62,
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



    clickButton(
        waitForObject(names.homeScreen_pbStoneAssistant_QToolButton)
    )

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
            names.hardnessFrame_mediumHardnessButton_QPushButton
        )
    )

    clickButton(
        waitForObject(
            names.stoneAssistantModeScreen_continueButton_QPushButton
        )
    )



    clickButton(
        waitForObject(names.stoneSenseFrame_pbStoneSense_QPushButton)
    )



    clickButton(
        waitForObject(
            names.calibrationPopupDialog_pbFailedCalibrationButton_QPushButton
        )
    )



    error_label = waitForObject(
        names.pCalibrationErrorFrame_pErrorAnimation_QLabel
    )

    try:
        error_frame = object.parent(error_label)
    except:
        error_frame = error_label



    verify_screen(
        error_frame,
        "Calibration Failed"
    )

    test.vp("Verify Calibration Failed Screen")

    



    mouseClick(
        waitForObject(
            names.pCalibrationErrorFrame_pErrorAnimation_QLabel
        ),
        117,
        180,
        Qt.NoModifier,
        Qt.LeftButton
    )

    clickButton(
        waitForObject(
            names.pCalibrationErrorFrame_pRetryButton_QPushButton
        )
    )
