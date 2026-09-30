# -*- coding: utf-8 -*-

import names
import openpyxl
import re


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
        if not obj.visible:
            return ""
    except:
        pass

    try:
        text = str(obj.text).strip()
        if text:
            text = re.sub(r"<br\s*/?>", " ", text, flags=re.IGNORECASE)
            text = re.sub(r"<[^>]+>", " ", text)
            text = " ".join(text.split())
            return text.strip()
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

    sendEvent("QMoveEvent", waitForObject(names.o_ScreenSwitcher), 105, 204, 657, 223)
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton))

    # CHANGE LANGUAGE TO BULGARIAN

    clickButton(waitForObject(names.homeScreen_settingsButton_QPushButton))
    clickTab(waitForObject(names.settingsScreen_tbSystemInfo_TabWidget), "INFO")
    clickButton(waitForObject(names.gbSystemInformation_pbLanguageSettingsUpdate_QPushButton))
    clickButton(waitForObject(names.languagesFrame_pbBulgaria_QPushButton))
    clickButton(waitForObject(names.buttonsFrame_acceptButton_QPushButton))
    clickButton(waitForObject(names.settingsScreen_pbBack_QPushButton))

    # STONE QUICK START

    clickButton(waitForObject(names.homeScreen_pbStoneQuickStart_QToolButton))
    mouseClick(waitForObjectItem(names.tabLeftMainPresets_leftPresetsView_PresetListView, "_1"), 433, 57, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.tabRightMainPresets_rightPresetsView_PresetListView, "_1"), 223, 61, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.quickStartScreen_pbContinue_QPushButton))

    mouseClick(waitForObject(names.averagePowerWidget_unitsOfMeasureLabel_QLabel_2), 144, 58, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.rightPedalWidget_wdPresetTabs_TabWidget), 21, 28, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.topBar_buttonsBar_ButtonsBar), 824, 27, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.treatmentScreen_leftPedalWidgetBorder_QWidget), 625, 444, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.bottomBar_lbPedalStatusIcon_QLabel), 33, 37, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.treatmentScreen_bottomBar_QFrame), 898, 52, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.bottomBar_fiberFrame_FiberInfoWidget), 31, 6, Qt.NoModifier, Qt.LeftButton)

    snooze(1)

    # READ EXCEL

    excelpath = "/home/ntc/Test_Automation_Gemini/Localisation/suite_GFL_Czech/tst_Home Screen/testdata/Gemini Split strings.xlsx"

    workbook = openpyxl.load_workbook(excelpath, data_only=True)
    sheet = workbook["Treatment Modes"]

    # GET CURRENT TREATMENT SCREEN

    screen = waitForObject(names.treatmentScreen_bottomBar_QFrame)
    screen_candidates = get_screen_candidates(screen)

    # CHECK PARENT

    try:
        parent = object.parent(screen)
        screen_candidates.extend(get_screen_candidates(parent))
    except:
        pass

    # CHECK RECORDED OBJECTS

    recorded_objects = [
        names.pulseModeWidget_averagePowerWidget_ParameterWithEnumerableValueWidget,
        names.rightPedalWidget_wdPresetTabs_TabWidget,
        names.topBar_buttonsBar_ButtonsBar,
        names.totalTimeFrame_nameLabel_QLabel,
        names.treatmentScreen_bottomBar_QFrame
    ]

    for object_name in recorded_objects:
        try:
            obj = waitForObject(object_name)
            screen_candidates.extend(get_screen_candidates(obj))
        except:
            pass

    screen_candidates = list(set(screen_candidates))

    # READ BULGARIAN STRINGS FROM EXCEL

    excel_strings = {}

    for row in sheet.iter_rows(min_row=2, values_only=True):

        if len(row) < 3:
            continue

        trace_id = row[0]
        english = row[1]
        bulgarian = row[2]

        if english is None or bulgarian is None:
            continue

        english = str(english).strip()
        bulgarian = str(bulgarian).strip()

        if not english or not bulgarian:
            continue

        excel_strings[normalize(bulgarian)] = {
            "english": english,
            "bulgarian": bulgarian,
            "trace_id": "" if trace_id is None else str(trace_id).strip()
        }

    # MATCH SCREEN STRINGS WITH EXCEL

    matches = {}

    for candidate in screen_candidates:

        normalized_candidate = normalize(candidate)

        if not normalized_candidate:
            continue

        if normalized_candidate in excel_strings:

            data = excel_strings[normalized_candidate]
            key = normalize(data["bulgarian"])

            matches[key] = (
                len(normalized_candidate),
                data["english"],
                data["bulgarian"]
            )

    # REMOVE DUPLICATES AND VALIDATE

    pass_count = 0

    for key in sorted(
        matches,
        key=lambda x: matches[x][0],
        reverse=True
    ):

        data = matches[key]

        test.passes(
            data[1] + " -> " + data[2]
        )

        pass_count += 1

    # FINAL RESULT

    if pass_count > 0:
        test.passes("BULGARIAN STONE QUICK START LOCALIZATION VALIDATION PASSED")
    else:
        test.fail("NO BULGARIAN STRINGS FOUND ON STONE QUICK START TREATMENT SCREEN")