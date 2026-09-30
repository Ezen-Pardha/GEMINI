# -*- coding: utf-8 -*-

import names
import openpyxl
import re


EXCEL_PATH = "/home/ntc/Test_Automation_Gemini/Localisation/Suite_GFL_English/tst_LoginScreen-Logoff/testdata/Gemini strings.xlsx"


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
        value = obj.text

        if value is not None:
            value = str(value).strip()

            if value:
                texts.append(value)
    except:
        pass

    try:
        value = obj.title

        if value is not None:
            value = str(value).strip()

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


def load_english_strings():

    workbook = openpyxl.load_workbook(
        EXCEL_PATH,
        data_only=True
    )

    sheet = workbook.active

    strings = {}

    for row in sheet.iter_rows(
        min_row=2,
        values_only=True
    ):

        if not row:
            continue

        english = row[0]

        if english is None:
            continue

        english = str(english).strip()

        if not english:
            continue

        key = normalize(english)

        if key not in strings:
            strings[key] = english

    workbook.close()

    return strings


def verify_treatment_screen():

    test.log("========== TREATMENT SCREEN ENGLISH VERIFICATION ==========")

    excel_strings = load_english_strings()

    test.log(
        "English strings loaded from Excel: " +
        str(len(excel_strings))
    )

    root = waitForObject(names.o_ScreenSwitcher)

    screen_texts = get_all_texts(root)

    test.log(
        "UI text objects found: " +
        str(len(screen_texts))
    )

    found_matches = set()

    for text in screen_texts:

        normalized_ui = normalize(text)

        if not normalized_ui:
            continue

        for excel_key, excel_text in excel_strings.items():

            if normalized_ui == excel_key:

                if excel_key not in found_matches:

                    found_matches.add(excel_key)

                    test.passes(
                        "English string verified: " +
                        excel_text
                    )

                break

            elif len(excel_key) >= 4 and excel_key in normalized_ui:

                if excel_key not in found_matches:

                    found_matches.add(excel_key)

                    test.passes(
                        "English string verified: " +
                        excel_text
                    )

                break

    test.log(
        "Total English strings verified: " +
        str(len(found_matches))
    )

    if len(found_matches) == 0:

        test.fail(
            "No English strings from Excel were found on the Treatment Screen."
        )

    test.log("===========================================================")


def main():

    sendEvent(
        "QMoveEvent",
        waitForObject(names.o_ScreenSwitcher),
        45,
        205,
        727,
        218
    )

    clickButton(
        waitForObject(
            names.numpad_pushButton_8_NumpadButton
        )
    )

    clickButton(
        waitForObject(
            names.numpad_pushButton_8_NumpadButton
        )
    )

    clickButton(
        waitForObject(
            names.numpad_pushButton_8_NumpadButton
        )
    )

    clickButton(
        waitForObject(
            names.numpad_pushButton_8_NumpadButton
        )
    )

    clickButton(
        waitForObject(
            names.mainFrame_okButton_QPushButton
        )
    )

    clickButton(
        waitForObject(
            names.homeScreen_pbStoneQuickStart_QToolButton
        )
    )

    mouseClick(
        waitForObjectItem(
            names.tabLeftMainPresets_leftPresetsView_PresetListView,
            "_1"
        ),
        306,
        29,
        Qt.NoModifier,
        Qt.LeftButton
    )

    mouseClick(
        waitForObjectItem(
            names.tabRightMainPresets_rightPresetsView_PresetListView,
            "_1"
        ),
        229,
        57,
        Qt.NoModifier,
        Qt.LeftButton
    )

    clickButton(
        waitForObject(
            names.quickStartScreen_pbContinue_QPushButton
        )
    )

    clickTab(
        waitForObject(
            names.leftPedalWidget_wdPresetTabs_TabWidget
        ),
        "KIDNEY DUSTING-(MEDIUM FLOW)"
    )

    mouseClick(
        waitForObject(
            names.pulseModeWidget_averagePowerWidget_ParameterWithEnumerableValueWidget_3
        ),
        556,
        5,
        Qt.NoModifier,
        Qt.LeftButton
    )

    mouseClick(
        waitForObject(
            names.totalTimeFrame_nameLabel_QLabel
        ),
        159,
        23,
        Qt.NoModifier,
        Qt.LeftButton
    )

    mouseClick(
        waitForObject(
            names.treatmentScreen_bottomBar_QFrame
        ),
        910,
        65,
        Qt.NoModifier,
        Qt.LeftButton
    )

    mouseClick(
        waitForObject(
            names.pulseModeWidget_buttonsWidget_QWidget
        ),
        172,
        60,
        Qt.NoModifier,
        Qt.LeftButton
    )

    mouseClick(
        waitForObject(
            names.pulseModeWidget_buttonsWidget_QWidget_2
        ),
        11,
        45,
        Qt.NoModifier,
        Qt.LeftButton
    )

    mouseClick(
        waitForObject(
            names.topBar_buttonsBar_ButtonsBar_2
        ),
        465,
        24,
        Qt.NoModifier,
        Qt.LeftButton
    )

    # ONLY HERE we verify the Treatment Screen
    # verify_treatment_screen()
    #
    # test.vp(
    #     "Verify Treatment Screen English Strings"
    # )