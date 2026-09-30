# -*- coding: utf-8 -*-

import names
import openpyxl
import re


def normalize(text):
    text = re.sub(r"<br\s*/?>", " ", str(text), flags=re.IGNORECASE)
    text = re.sub(r"<[^>]+>", "", text)
    text = " ".join(text.split())
    text = re.sub(r"\s*<\s*", "<", text)
    text = re.sub(r"\s*>\s*", ">", text)
    return text.strip().lower()


def get_text_lines(obj):
    lines = []

    try:
        text = str(obj.text).strip()
        if text:
            text = re.sub(r"<br\s*/?>", "\n", text, flags=re.IGNORECASE)
            text = re.sub(r"<[^>]+>", "", text)
            for line in text.splitlines():
                line = " ".join(line.split()).strip()
                if line:
                    lines.append(line)
    except:
        pass

    try:
        for child in object.children(obj):
            lines.extend(get_text_lines(child))
    except:
        pass

    return lines


def get_all_text_combinations(obj):
    result = []
    lines = get_text_lines(obj)

    for start in range(len(lines)):
        combined = ""
        for end in range(start, len(lines)):
            combined = combined + " " + lines[end] if combined else lines[end]
            result.append(combined)

    return list(set(result))


def main():

    # LOGIN

    sendEvent("QMoveEvent", waitForObject(names.o_ScreenSwitcher), 57, 167, 718, 194)

    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    snooze(2)
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton))

    # CHANGE LANGUAGE TO DUTCH

    clickButton(waitForObject(names.homeScreen_settingsButton_QPushButton))
    clickTab(waitForObject(names.settingsScreen_tbSystemInfo_TabWidget), "INFO")
    clickButton(waitForObject(names.gbSystemInformation_pbLanguageSettingsUpdate_QPushButton))
    clickButton(waitForObject(names.languagesFrame_pbDutch_QPushButton))
    clickButton(waitForObject(names.buttonsFrame_acceptButton_QPushButton))
    clickButton(waitForObject(names.settingsScreen_pbBack_QPushButton))
    snooze(1)

    # OPEN STONE ASSISTANT

    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))

    # READ EXCEL

    excelpath = "/home/ntc/Test_Automation_Gemini/Localisation/suite_GFL_Czech/tst_Home Screen/testdata/Gemini Split strings.xlsx"
    workbook = openpyxl.load_workbook(excelpath, data_only=True)
    sheet = workbook["Stone-Guided"]

    # STONE GUIDED SELECTION

    clickButton(waitForObject(names.locationFrame_kidneyPcnlLocationButton_QPushButton))
    mouseClick(waitForObject(names.locationFrame_label_3_QLabel), 189, 20, Qt.NoModifier, Qt.LeftButton)

    clickButton(waitForObject(names.flowRateFrame_lowFlowRateButton_QPushButton))
    mouseClick(waitForObject(names.flowRateFrame_label_4_QLabel), 202, 28, Qt.NoModifier, Qt.LeftButton)

    clickButton(waitForObject(names.hardnessFrame_largeHardnessButton_QPushButton))
    clickButton(waitForObject(names.hardnessFrame_mediumHardnessButton_QPushButton))
    mouseClick(waitForObject(names.hardnessFrame_label_6_QLabel), 196, 24, Qt.NoModifier, Qt.LeftButton)

    snooze(1)

    # GET STONE GUIDED SCREEN

    stone = waitForObject(names.stoneAssistantModeScreen_StoneAssistantModeScreen)

    screen_candidates = set(
        normalize(text)
        for text in get_all_text_combinations(stone)
        if normalize(text)
    )

    # READ ENGLISH -> DUTCH FROM EXCEL

    excel_strings = {}

    for row in sheet.iter_rows(min_row=2, values_only=True):

        if len(row) < 7:
            continue

        english = row[1]
        dutch = row[6]

        if english is None or dutch is None:
            continue

        english = str(english).strip()
        dutch = str(dutch).strip()

        if not english or not dutch:
            continue

        dutch_key = normalize(dutch)

        if dutch_key:
            excel_strings[dutch_key] = {
                "english": english,
                "dutch": dutch
            }

    # VALIDATE EXCEL DUTCH STRINGS AGAINST SCREEN

    pass_count = 0
    fail_count = 0
    verified = set()

    for dutch_key, data in excel_strings.items():

        if dutch_key in verified:
            continue

        verified.add(dutch_key)

        if dutch_key in screen_candidates:

            test.passes(
                "PASS: " +
                data["english"] +
                " -> " +
                data["dutch"]
            )

            pass_count += 1

        else:

            test.fail(
                "FAIL: " +
                data["english"] +
                " -> " +
                data["dutch"] +
                " | Dutch string is missing on Stone-Guided screen"
            )

            fail_count += 1

    workbook.close()

    # FINAL RESULT

    if fail_count > 0:
        test.fail("DUTCH STONE-GUIDED LOCALIZATION VALIDATION FAILED")
    elif pass_count > 0:
        test.passes("DUTCH STONE-GUIDED LOCALIZATION VALIDATION PASSED")
    else:
        test.fail("NO DUTCH EXCEL STRINGS FOUND FOR VALIDATION")