# -*- coding: utf-8 -*-

import names
import openpyxl
import re

EXCEL_PATH = "/home/ntc/suite_gemini_Localization_croatian/tst_GEM-LOC-CROATIA-STONE-GUIDED/testdata/Gemini strings.xlsx"


def normalize(text):
    if text is None:
        return ""
    text = str(text)
    text = re.sub(r"<[^>]+>", " ", text)
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


def load_croatian_strings():

    workbook = openpyxl.load_workbook(EXCEL_PATH, data_only=True)
    sheet = workbook.active

    strings = []

    for row in sheet.iter_rows(min_row=2, values_only=True):

        if len(row) < 9:
            continue

        trace_id = row[0]
        english = row[1]
        croatian = row[8]

        if english is None or croatian is None:
            continue

        english = str(english).strip()
        croatian = str(croatian).strip()

        if not english or not croatian:
            continue

        strings.append({
            "trace_id": str(trace_id).strip() if trace_id is not None else "",
            "english": english,
            "croatian": croatian,
            "normalized": normalize(croatian)
        })

    return strings


def verify_screen(root_object, screen_name):

    excel_strings = load_croatian_strings()
    screen_texts = get_all_texts(root_object)

    unique_texts = []

    for text in screen_texts:
        text = text.strip()
        if text and text not in unique_texts:
            unique_texts.append(text)

    verified = []

    for screen_text in unique_texts:

        screen_normalized = normalize(screen_text)
        matches = []

        for item in excel_strings:

            excel_normalized = item["normalized"]

            if screen_normalized == excel_normalized:
                matches.append(item)

            elif excel_normalized in screen_normalized:
                matches.append(item)

        matches.sort(key=lambda x: len(x["normalized"]), reverse=True)

        for item in matches:

            croatian = item["croatian"]

            if croatian in verified:
                continue

            verified.append(croatian)
            test.passes(item["english"] + " -> " + item["croatian"])


def main():

    # Login
    sendEvent("QMoveEvent", waitForObject(names.o_ScreenSwitcher), 22, 157, 607, 168)
    sendEvent("QMoveEvent", waitForObject(names.o_ScreenSwitcher), 22, 155, 607, 166)
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    doubleClick(waitForObject(names.numpad_pushButton_8_NumpadButton), 64, 52, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton))

    # Change language to Croatian
    clickButton(waitForObject(names.homeScreen_settingsButton_QPushButton, 38323))
    clickTab(waitForObject(names.settingsScreen_tbSystemInfo_TabWidget), "INFO")
    clickButton(waitForObject(names.gbSystemInformation_pbLanguageSettingsUpdate_QPushButton))
    clickButton(waitForObject(names.languagesFrame_pbCroatia_QPushButton))
    clickButton(waitForObject(names.buttonsFrame_acceptButton_QPushButton))
    clickButton(waitForObject(names.settingsScreen_pbBack_QPushButton))

    # Open Stone Assistant
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    clickButton(waitForObject(names.locationFrame_kidneyPcnlLocationButton_QPushButton))
    clickButton(waitForObject(names.flowRateFrame_mediumFlowRateButton_QPushButton))
    clickButton(waitForObject(names.hardnessFrame_mediumHardnessButton_QPushButton))
    clickButton(waitForObject(names.stoneAssistantModeScreen_continueButton_QPushButton))

    # Stone Sense
    clickButton(waitForObject(names.stoneSenseFrame_pbStoneSense_QPushButton))
    verify_screen(waitForObject(names.stoneSenseFrame_pbStoneSense_QPushButton), "Stone Sense")

    # Initiate Calibration
    mouseClick(waitForObject(names.pInitiateCalibrationFrame_pCalibrationMessageLabel_QLabel), 400, 280, Qt.NoModifier, Qt.LeftButton)

    # Calibration Popup
    calibration_popup = waitForObject(names.calibrationPopupDialog_CalibrationPopupDialog)
    verify_screen(calibration_popup, "Calibration Popup")
    clickButton(waitForObject(names.calibrationPopupDialog_pbMiddleButton_QPushButton))

    # Calibration screen
    mouseClick(waitForObject(names.pInitiateCalibrationFrame_pCalibrationMessageLabel_QLabel), 289, 442, Qt.NoModifier, Qt.LeftButton)
    calibration_screen = waitForObject(names.pInitiateCalibrationFrame_pCalibrationMessageLabel_QLabel)

    try:
        calibration_root = object.parent(calibration_screen)
    except:
        calibration_root = calibration_screen

    verify_screen(calibration_root, "Calibration screen")

    # Stone Sense text
    mouseClick(waitForObject(names.frame_pStoneSenseTextLabel_QLabel), 496, 462, Qt.NoModifier, Qt.LeftButton)

    # Calibration Success
    success_button = waitForObject(names.pCalibrationSuccessFrame_pOKButton_QPushButton)

    try:
        success_root = object.parent(success_button)
    except:
        success_root = success_button

    verify_screen(success_root, "Calibration Success")
    clickButton(waitForObject(names.pCalibrationSuccessFrame_pOKButton_QPushButton))

    # Stone Sense after Calibration
    clickButton(waitForObject(names.stoneSenseFrame_pbStoneSense_QPushButton))
    verify_screen(waitForObject(names.stoneSenseFrame_pbStoneSense_QPushButton), "Stone Sense after Calibration")

    # Disable
    mouseClick(waitForObject(names.centralWidget_QFrame_2), 739, 485, Qt.NoModifier, Qt.LeftButton)
    disable_screen = waitForObject(names.centralWidget_QFrame_2)
    verify_screen(disable_screen, "Disable screen")
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))