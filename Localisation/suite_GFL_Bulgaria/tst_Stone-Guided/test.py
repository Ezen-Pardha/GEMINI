# -*- coding: utf-8 -*-

import names
import openpyxl
import re


def normalize(text):
    text = str(text)
    text = re.sub(r"<[^>]+>", "", text)
    text = " ".join(text.split())
    text = re.sub(r"\s*<\s*", "<", text)
    text = re.sub(r"\s*>\s*", ">", text)
    return text.strip().lower()


def get_text_lines(obj):
    lines = []

    try:
        if not obj.visible:
            return lines
    except:
        pass

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
        children = object.children(obj)

        for child in children:
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

            if combined:
                combined += " " + lines[end]
            else:
                combined = lines[end]

            result.append(combined)

    try:
        children = object.children(obj)

        for child in children:
            result.extend(
                get_all_text_combinations(child)
            )

    except:
        pass

    return result


def main():

    # LOGIN

    sendEvent(
        "QMoveEvent",
        waitForObject(names.o_ScreenSwitcher),
        57, 167, 718, 194
    )

    clickButton(
        waitForObject(names.numpad_pushButton_8_NumpadButton)
    )

    clickButton(
        waitForObject(names.numpad_pushButton_8_NumpadButton)
    )

    clickButton(
        waitForObject(names.numpad_pushButton_8_NumpadButton)
    )

    clickButton(
        waitForObject(names.numpad_pushButton_8_NumpadButton)
    )

    snooze(2)

    clickButton(
        waitForObject(names.mainFrame_okButton_QPushButton)
    )


    # CHANGE LANGUAGE TO BULGARIAN

    clickButton(
        waitForObject(names.homeScreen_settingsButton_QPushButton)
    )

    clickTab(
        waitForObject(names.settingsScreen_tbSystemInfo_TabWidget),
        "INFO"
    )

    clickButton(
        waitForObject(
            names.gbSystemInformation_pbLanguageSettingsUpdate_QPushButton
        )
    )

    clickButton(
        waitForObject(names.languagesFrame_pbBulgaria_QPushButton)
    )

    clickButton(
        waitForObject(names.buttonsFrame_acceptButton_QPushButton)
    )

    clickButton(
        waitForObject(names.settingsScreen_pbBack_QPushButton)
    )


    # OPEN STONE ASSISTANT

    clickButton(
        waitForObject(names.homeScreen_pbStoneAssistant_QToolButton)
    )


    # STONE GUIDED SELECTION

    clickButton(
        waitForObject(
            names.locationFrame_kidneyPcnlLocationButton_QPushButton
        )
    )

    mouseClick(
        waitForObject(names.locationFrame_label_3_QLabel),
        189, 20,
        Qt.NoModifier,
        Qt.LeftButton
    )

    clickButton(
        waitForObject(
            names.flowRateFrame_lowFlowRateButton_QPushButton
        )
    )

    mouseClick(
        waitForObject(names.flowRateFrame_label_4_QLabel),
        202, 28,
        Qt.NoModifier,
        Qt.LeftButton
    )

    clickButton(
        waitForObject(
            names.hardnessFrame_largeHardnessButton_QPushButton
        )
    )

    clickButton(
        waitForObject(
            names.hardnessFrame_mediumHardnessButton_QPushButton
        )
    )

    mouseClick(
        waitForObject(names.hardnessFrame_label_6_QLabel),
        196, 24,
        Qt.NoModifier,
        Qt.LeftButton
    )

    snooze(1)


    # READ EXCEL

    excelpath = "/home/ntc/Test_Automation_Gemini/Localisation/suite_GFL_Czech/tst_Home Screen/testdata/Gemini Split strings.xlsx"

    workbook = openpyxl.load_workbook(
        excelpath,
        data_only=True
    )

    sheet = workbook["Stone-Guided"]


    # GET STONE GUIDED SCREEN

    stone = waitForObject(
        names.stoneAssistantModeScreen_StoneAssistantModeScreen
    )

    screen_candidates = get_all_text_combinations(stone)

    screen_candidates = list(
        set(screen_candidates)
    )


    # READ BULGARIAN FROM EXCEL

    excel_strings = {}

    for row in sheet.iter_rows(
        min_row=2,
        values_only=True
    ):

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
            "trace_id":
                "" if trace_id is None
                else str(trace_id).strip()
        }


    # MATCH SCREEN STRINGS WITH EXCEL

    matches = []

    for candidate in screen_candidates:

        normalized_candidate = normalize(
            candidate
        )

        if not normalized_candidate:
            continue

        if normalized_candidate in excel_strings:

            data = excel_strings[
                normalized_candidate
            ]

            matches.append(
                (
                    len(normalized_candidate),
                    data["english"],
                    data["bulgarian"]
                )
            )


    # REMOVE DUPLICATES

    unique_matches = {}

    for length, english, bulgarian in matches:

        key = normalize(bulgarian)

        if key not in unique_matches:

            unique_matches[key] = (
                length,
                english,
                bulgarian
            )


    # VALIDATION

    pass_count = 0

    for key in sorted(
        unique_matches,
        key=lambda x: unique_matches[x][0],
        reverse=True
    ):

        data = unique_matches[key]

        english = data[1]
        bulgarian = data[2]

        test.passes(
            english +
            " -> " +
            bulgarian
        )

        pass_count += 1


    # FINAL RESULT

    if pass_count > 0:

        test.passes(
            "BULGARIAN STONE-GUIDED LOCALIZATION VALIDATION PASSED"
        )

    else:

        test.fail(
            "NO BULGARIAN STRINGS FOUND ON STONE-GUIDED SCREEN"
        )

    workbook.close()