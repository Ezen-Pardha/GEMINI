# -*- coding: utf-8 -*-

import names
import openpyxl
import re


EXCEL_PATH = "/home/ntc/Test_Automation_Gemini/Localisation/suite_GFL_Czech/tst_Home Screen/testdata/Gemini Split strings.xlsx"


def normalize(text):
    text = str(text)
    text = re.sub(r"<br\s*/?>", " ", text, flags=re.IGNORECASE)
    text = re.sub(r"<[^>]+>", "", text)
    text = text.replace("\xa0", " ")
    text = " ".join(text.split())
    text = re.sub(r"\s*<\s*", "<", text)
    text = re.sub(r"\s*>\s*", ">", text)
    return text.strip().lower()


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

    # CHANGE LANGUAGE TO English
    clickButton(waitForObject(names.homeScreen_settingsButton_QPushButton))
    clickTab(waitForObject(names.settingsScreen_tbSystemInfo_TabWidget), "INFO")

    clickButton(waitForObject(names.gbSystemInformation_pbLanguageSettingsUpdate_QPushButton))
    clickButton(waitForObject(names.languagesFrame_pbEnglish_QPushButton))
    clickButton(waitForObject(names.buttonsFrame_acceptButton_QPushButton_2))
    clickButton(waitForObject(names.settingsScreen_pbBack_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbSoftTissueQuickStart_QToolButton))
    mouseClick(waitForObjectItem(names.tabLeftMainPresets_leftPresetsView_PresetListView, "_1"), 209, 53, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.tabRightMainPresets_rightPresetsView_PresetListView, "_1"), 160, 25, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.quickStartScreen_pbContinue_QPushButton))
    mouseClick(waitForObject(names.mainFrame_messageLabelMargin_QWidget), 491, 26, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton_2))
    mouseClick(waitForObject(names.averagePowerWidget_unitsOfMeasureLabel_QLabel), 161, 61, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.averagePowerWidget_nameLabel_QLabel), 20, 63, Qt.NoModifier, Qt.LeftButton)


    # LOAD EXCEL
    workbook = openpyxl.load_workbook(EXCEL_PATH, data_only=True)
    sheet = workbook["Treatment Modes"]

    # GET CURRENT TREATMENT SCREEN
    screen = waitForObject(names.treatmentScreen_bottomBar_QFrame)
    candidates = get_screen_candidates(screen)

    try:
        candidates.extend(get_screen_candidates(object.parent(screen)))
    except:
        pass

    candidates = set(normalize(text) for text in candidates if text)

    # LOAD English STRINGS FROM EXCEL
    excel_strings = {}

    for row in sheet.iter_rows(min_row=2, values_only=True):
        if len(row) < 3 or row[1] is None or row[2] is None:
            continue

        english = str(row[1]).strip()
        English = str(row[1]).strip()

        if english and English:
            excel_strings[normalize(English)] = {
                "english": english,
                "English": English
            }

    # MATCH SCREEN STRINGS AGAINST EXCEL
    matches = {}

    for candidate in candidates:
        if candidate in excel_strings:
            data = excel_strings[candidate]
            key = normalize(data["English"])
            matches[key] = (data["english"], data["English"])

    # REPORT UNIQUE MATCHES
    pass_count = 0

    for key in sorted(matches):
        english, English = matches[key]
        test.passes(english + " -> " + English)
        pass_count += 1

    # FINAL RESULT
    if pass_count:
        test.passes("English SOFT TISSUE QUICK START LOCALIZATION VALIDATION PASSED")
    else:
        test.fail("NO English STRINGS FOUND ON SCREEN")

    workbook.close()
