# -*- coding: utf-8 -*-

import names
import openpyxl
import re


EXCEL_PATH = "/home/ntc/Test_Automation_Gemini/Localisation/suite_GFL_Croatia/tst_GEM-LOC-CROATIA-STONE-GUIDED/testdata/Gemini strings.xlsx"

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

        normalized = normalize(croatian)

        
        if normalized not in strings:
            strings[normalized] = {
                "english": english,
                "croatian": croatian
            }

    return list(strings.values())


def verify_screen(root_object, screen_name):

    excel_strings = load_croatian_strings()

    screen_texts = get_all_texts(root_object)

    
    unique_texts = {}
    
    for text in screen_texts:

        text = text.strip()

        if not text:
            continue

        normalized = normalize(text)

        if normalized not in unique_texts:
            unique_texts[normalized] = text

    # Keep only one result for each Croatian translation
    verified = set()

    for screen_normalized, screen_text in unique_texts.items():

        matches = []

        for item in excel_strings:

            excel_normalized = normalize(item["croatian"])

            # Exact match
            if screen_normalized == excel_normalized:
                matches.append(item)

            # Match strings contained inside combined UI text
            elif len(excel_normalized) >= 4 and excel_normalized in screen_normalized:
                matches.append(item)

        # Longest strings first
        matches.sort(
            key=lambda x: len(normalize(x["croatian"])),
            reverse=True
        )

        for item in matches:

            key = normalize(item["croatian"])

            if key in verified:
                continue

            verified.add(key)

            test.passes(
                item["english"] + " -> " + item["croatian"]
            )


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
