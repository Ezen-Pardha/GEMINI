# -*- coding: utf-8 -*-

import names
import openpyxl
import re


EXCEL_PATH = "/home/ntc/Test_Automation_Gemini/Localisation/suite_GFL_Croatia/tst_GEM-LOC-CROATIA-STONE-GUIDED/testdata/Gemini strings.xlsx"


# Stores strings already reported during the complete test
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

    strings = {}

    for row in sheet.iter_rows(min_row=2, values_only=True):

        if len(row) < 9:
            continue

        english = row[1]
        croatian = row[8]

        if english is None or croatian is None:
            continue

        english = str(english).strip()
        croatian = str(croatian).strip()

        if not english or not croatian:
            continue

        key = normalize(croatian)

        if key not in strings:
            strings[key] = {
                "english": english,
                "croatian": croatian
            }

    return list(strings.values())


def verify_screen(root_object, screen_name):

    excel_strings = load_croatian_strings()
    screen_texts = get_all_texts(root_object)

    unique_texts = set()

    for text in screen_texts:

        normalized = normalize(text)

        if normalized:
            unique_texts.add(normalized)

    for screen_text in unique_texts:

        matches = []

        for item in excel_strings:

            excel_text = normalize(item["croatian"])

            if screen_text == excel_text:
                matches.append(item)

            elif len(excel_text) >= 4 and excel_text in screen_text:
                matches.append(item)

        matches.sort(
            key=lambda x: len(normalize(x["croatian"])),
            reverse=True
        )

        for item in matches:

            key = normalize(item["croatian"])

            # Do not report the same Croatian string again
            if key in verified_strings:
                continue

            verified_strings.add(key)

            test.passes(
                item["english"] + " -> " + item["croatian"]
            )


def main():

    # LOGIN
    sendEvent("QMoveEvent", waitForObject(names.o_ScreenSwitcher), 33, 192, 737, 203)
    doubleClick(waitForObject(names.numpad_pushButton_8_NumpadButton), 76, 50, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton))

    # LANGUAGE
    clickButton(waitForObject(names.homeScreen_settingsButton_QPushButton))
    clickTab(waitForObject(names.settingsScreen_tbSystemInfo_TabWidget), "INFO")
    clickButton(waitForObject(names.gbSystemInformation_pbLanguageSettingsUpdate_QPushButton))
    clickButton(waitForObject(names.languagesFrame_pbCroatia_QPushButton))
    clickButton(waitForObject(names.buttonsFrame_acceptButton_QPushButton))
    clickButton(waitForObject(names.settingsScreen_pbBack_QPushButton))
    
    

    # OPEN QUICK START
    clickButton(waitForObject(names.homeScreen_pbStoneQuickStart_QToolButton))
    verify_screen(waitForObject(names.o_ScreenSwitcher), "Quick Start")

    # SELECT LEFT PRESET
    mouseClick(waitForObjectItem(names.tabLeftMainPresets_leftPresetsView_PresetListView, "_1"), 404, 36, Qt.NoModifier, Qt.LeftButton)
    verify_screen(waitForObject(names.o_ScreenSwitcher), "Quick Start - Left Preset")

    # SELECT RIGHT PRESET
    mouseClick(waitForObjectItem(names.tabRightMainPresets_rightPresetsView_PresetListView, "_1"), 92, 47, Qt.NoModifier, Qt.LeftButton)
    verify_screen(waitForObject(names.o_ScreenSwitcher), "Quick Start - Right Preset")

    # CONTINUE TO TREATMENT
    clickButton(waitForObject(names.quickStartScreen_pbContinue_QPushButton))
    verify_screen(waitForObject(names.o_ScreenSwitcher), "Treatment Screen")

    test.vp("Verify sonte treatment screen")

    

    # CLICK LEFT PEDAL
    mouseClick(waitForObject(names.treatmentScreen_leftPedalWidgetBorder_QWidget), 629, 48, Qt.NoModifier, Qt.LeftButton)
    verify_screen(waitForObject(names.o_ScreenSwitcher), "Treatment Screen - Left Pedal")
