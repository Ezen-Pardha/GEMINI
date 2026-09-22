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

    unique_texts = set()

    for text in screen_texts:

        text = normalize(text)

        if text:
            unique_texts.add(text)

    for screen_normalized in unique_texts:

        matches = []

        for item in excel_strings:

            excel_normalized = item["normalized"]

            if screen_normalized == excel_normalized:

                matches.append(item)

            elif len(excel_normalized) >= 4 and excel_normalized in screen_normalized:

                matches.append(item)

        matches.sort(
            key=lambda x: len(x["normalized"]),
            reverse=True
        )

        for item in matches:

            result_key = (
                normalize(item["english"]),
                normalize(item["croatian"])
            )

            if result_key in VERIFIED_RESULTS:
                continue

            VERIFIED_RESULTS.add(result_key)

            test.passes(
                item["english"] + " -> " + item["croatian"]
            )


def main():

    sendEvent("QMoveEvent", waitForObject(names.o_ScreenSwitcher), 45, 176, 662, 188)

    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton))

    clickButton(waitForObject(names.homeScreen_settingsButton_QPushButton))

    clickTab(waitForObject(names.settingsScreen_tbSystemInfo_TabWidget), "INFO")

    clickButton(waitForObject(names.gbSystemInformation_pbLanguageSettingsUpdate_QPushButton))
    clickButton(waitForObject(names.languagesFrame_pbCroatia_QPushButton))
    clickButton(waitForObject(names.buttonsFrame_acceptButton_QPushButton))


    verify_screen(waitForObject(names.o_ScreenSwitcher), "System Information")


    mouseClick(waitForObject(names.gbSystemInformation_lbSystemInformation_QLabel), 439, 11, Qt.NoModifier, Qt.LeftButton)

    verify_screen(waitForObject(names.o_ScreenSwitcher), "System Information after click")


    mouseClick(waitForObject(names.wdSystemInfoLayout_gbFiberInformation_QGroupBox), 394, 54, Qt.NoModifier, Qt.LeftButton)

    verify_screen(waitForObject(names.o_ScreenSwitcher), "Fiber Information")