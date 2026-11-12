# -*- coding: utf-8 -*-

import names
import croatian_localization as loc
import openpyxl
import re


EXCEL_PATH = loc.EXCEL_PATH


def normalize(text):
    return loc.normalize(text)


def get_object_text(obj):
    try:
        text = str(obj.text).strip()
        if text:
            text = re.sub(r"<br\s*/?>", " ", text, flags=re.IGNORECASE)
            text = re.sub(r"<[^>]+>", " ", text)
            return " ".join(text.split()).strip()
    except:
        pass
    return ""


def get_screen_candidates(obj):
    candidates = []

    own_text = get_object_text(obj)
    if own_text:
        candidates.append(own_text)

    try:
        children = object.children(obj)
    except:
        children = []

    child_texts = []

    for child in children:
        child_text = get_object_text(child)
        if child_text:
            child_texts.append(child_text)
            candidates.append(child_text)

    for start in range(len(child_texts)):
        combined = ""
        for end in range(start, len(child_texts)):
            combined = combined + " " + child_texts[end] if combined else child_texts[end]
            candidates.append(combined)

    for child in children:
        candidates.extend(get_screen_candidates(child))

    return candidates


def main():

    # LOGIN
    sendEvent("QMoveEvent", waitForObject(names.o_ScreenSwitcher), 28, 208, 534, 218)
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton))

    # CHANGE LANGUAGE TO Croatia
    clickButton(waitForObject(names.homeScreen_settingsButton_QPushButton))
    clickTab(waitForObject(names.settingsScreen_tbSystemInfo_TabWidget), "INFO")
    clickButton(waitForObject(names.gbSystemInformation_pbLanguageSettingsUpdate_QPushButton))

    clickButton(waitForObject(names.languagesFrame_pbCroatia_QPushButton))
    clickButton(waitForObject(names.buttonsFrame_acceptButton_QPushButton))
    clickButton(waitForObject(names.settingsScreen_pbBack_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbSoftTissueQuickStart_QToolButton))
    mouseClick(waitForObjectItem(names.tabLeftMainPresets_leftPresetsView_PresetListView, "_1"), 163, 46, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.tabRightMainPresets_rightPresetsView_PresetListView, "_1"), 109, 31, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.quickStartScreen_pbContinue_QPushButton))
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton_2))
    mouseClick(waitForObject(names.croatiaTreatment_averagePowerName_QLabel), 7, 42, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.croatiaTreatment_averagePowerUnits_QLabel), 109, 40, Qt.NoModifier, Qt.LeftButton)




    loc.verify_screen(waitForObject(names.treatmentScreen_TreatmentScreen),
                      "Soft Tissue Quick Start Treatment", globals())
