# -*- coding: utf-8 -*-

import names
import openpyxl
import re

EXCEL_PATH = "/home/ntc/suite_gemini_Localization_croatian/tst_GEM-LOC-CROATIA-STONE-GUIDED/testdata/Gemini strings.xlsx"
VERIFIED_RESULTS = set()


def normalize(text):
    if text is None:
        return ""
    text = str(text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = " ".join(text.split())
    text = re.sub(r"\s*<\s*", " < ", text)
    text = re.sub(r"\s*>\s*", " > ", text)
    return text.casefold()


def clean_text(text):
    if text is None:
        return ""
    text = re.sub(r"<[^>]+>", " ", str(text))
    return " ".join(text.split()).strip()


def get_all_texts(obj):

    texts = []

    try:
        if not obj.visible:
            return texts
    except:
        pass

    for attribute in ("text", "title", "windowTitle", "caption", "displayText", "toolTip"):
        try:
            value = getattr(obj, attribute)
            if callable(value):
                value = value()
            value = clean_text(value)
            if value:
                texts.append(value)
        except:
            pass

    # Get model data for QListView/QTreeView
    try:
        model = obj.model
        if callable(model):
            model = model()

        if model:
            for row in range(model.rowCount()):
                for column in range(model.columnCount()):
                    try:
                        value = clean_text(model.data(model.index(row, column)))
                        if value:
                            texts.append(value)
                    except:
                        pass
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

        english = row[1]
        croatian = row[8]

        if english is None or croatian is None:
            continue

        english = str(english).strip()
        croatian = str(croatian).strip()

        if not english or not croatian:
            continue

        strings.append({
            "english": english,
            "croatian": croatian,
            "normalized": normalize(croatian)
        })

    return strings


def verify_screen(root_object, screen_name):

    excel_strings = load_croatian_strings()
    screen_texts = get_all_texts(root_object)

    unique_texts = []
    seen_texts = set()

    for text in screen_texts:

        normalized_text = normalize(text)

        if not normalized_text or normalized_text in seen_texts:
            continue

        seen_texts.add(normalized_text)
        unique_texts.append(text)

    for screen_text in unique_texts:

        screen_normalized = normalize(screen_text)
        matches = []

        for item in excel_strings:

            excel_normalized = item["normalized"]

            if screen_normalized == excel_normalized:
                matches.append(item)

            elif len(excel_normalized) >= 4 and excel_normalized in screen_normalized:
                matches.append(item)

        matches.sort(key=lambda x: len(x["normalized"]), reverse=True)

        for item in matches:

            result_key = (normalize(item["english"]), normalize(item["croatian"]))

            if result_key in VERIFIED_RESULTS:
                continue

            VERIFIED_RESULTS.add(result_key)
            test.passes(item["english"] + " -> " + item["croatian"])


def main():

    sendEvent("QMoveEvent", waitForObject(names.o_ScreenSwitcher), 38, 211, 667, 224)
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    doubleClick(waitForObject(names.numpad_pushButton_8_NumpadButton), 81, 86, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton))

    clickButton(waitForObject(names.homeScreen_settingsButton_QPushButton))
    clickTab(waitForObject(names.settingsScreen_tbSystemInfo_TabWidget), "INFO")
    clickButton(waitForObject(names.gbSystemInformation_pbLanguageSettingsUpdate_QPushButton))
    clickButton(waitForObject(names.languagesFrame_pbCroatia_QPushButton))
    clickButton(waitForObject(names.buttonsFrame_acceptButton_QPushButton))
    clickButton(waitForObject(names.settingsScreen_pbBack_QPushButton))

    clickButton(waitForObject(names.homeScreen_pbStoneQuickStart_QToolButton))

    verify_screen(waitForObject(names.o_ScreenSwitcher), "Quick Start Initial")

    left_preset = waitForObjectItem(names.tabLeftMainPresets_leftPresetsView_PresetListView, "_1")
    mouseClick(left_preset, 413, 45, Qt.NoModifier, Qt.LeftButton)
    verify_screen(waitForObject(names.o_ScreenSwitcher), "Left Preset Selected")

    right_preset = waitForObjectItem(names.tabRightMainPresets_rightPresetsView_PresetListView, "_1")
    mouseClick(right_preset, 161, 42, Qt.NoModifier, Qt.LeftButton)
    verify_screen(waitForObject(names.o_ScreenSwitcher), "Right Preset Selected")

    clickButton(waitForObject(names.tabLeftMainPresets_nextPageButton_QPushButton))
    verify_screen(waitForObject(names.o_ScreenSwitcher), "Left Page 2")

    clickButton(waitForObject(names.tabRightMainPresets_nextPageButton_QPushButton))
    verify_screen(waitForObject(names.o_ScreenSwitcher), "Right Page 2")

    mouseClick(waitForObject(names.tabLeftMainPresets_tabLeftPresetsScroll_PageScroll), 544, 30, Qt.NoModifier, Qt.LeftButton)
    verify_screen(waitForObject(names.o_ScreenSwitcher), "Left Scroll")

    mouseClick(waitForObject(names.tabRightMainPresets_tabRightPresetsScroll_PageScroll), 56, 16, Qt.NoModifier, Qt.LeftButton)
    verify_screen(waitForObject(names.o_ScreenSwitcher), "Right Scroll")

    clickButton(waitForObject(names.tabLeftMainPresets_nextPageButton_QPushButton))
    verify_screen(waitForObject(names.o_ScreenSwitcher), "Left Page 3")

    mouseClick(waitForObject(names.tabLeftMainPresets_tabLeftPresetsScroll_PageScroll), 563, 53, Qt.NoModifier, Qt.LeftButton)
    verify_screen(waitForObject(names.o_ScreenSwitcher), "Left Scroll 2")

    clickButton(waitForObject(names.tabRightMainPresets_nextPageButton_QPushButton))
    verify_screen(waitForObject(names.o_ScreenSwitcher), "Right Page 3")

    mouseClick(waitForObject(names.tabRightMainPresets_tabRightPresetsScroll_PageScroll), 528, 36, Qt.NoModifier, Qt.LeftButton)
    verify_screen(waitForObject(names.o_ScreenSwitcher), "Right Scroll 2")