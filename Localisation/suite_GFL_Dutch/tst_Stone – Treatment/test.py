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


def is_ignored(text):
    text = normalize(text)

    if not text or text == "aut":
        return True

    if re.match(r"^[\d\s.,:+\-/]+$", text):
        return True

    if re.match(r"^[\d\s.,:+\-/]+(w|j|hz|µm|mm|cm|s|min|%)$", text):
        return True

    return False


def get_object_text(obj):

    try:
        text = str(obj.text).strip()

        if text:
            text = re.sub(
                r"<br\s*/?>",
                " ",
                text,
                flags=re.IGNORECASE
            )
            text = re.sub(r"<[^>]+>", " ", text)
            text = " ".join(text.split())
            return text.strip()

    except:
        pass

    return ""


def get_screen_candidates(obj):

    candidates = []

    own_text = get_object_text(obj)

    if own_text and not is_ignored(own_text):
        candidates.append(own_text)

    try:
        children = object.children(obj)
    except:
        children = []

    child_texts = []

    for child in children:

        child_text = get_object_text(child)

        if child_text and not is_ignored(child_text):
            child_texts.append(child_text)
            candidates.append(child_text)

    for start in range(len(child_texts)):

        combined = ""

        for end in range(start, len(child_texts)):

            combined = (
                combined + " " + child_texts[end]
                if combined
                else child_texts[end]
            )

            if not is_ignored(combined):
                candidates.append(combined)

    for child in children:
        candidates.extend(get_screen_candidates(child))

    return candidates


def main():

    # LOGIN

    sendEvent(
        "QMoveEvent",
        waitForObject(names.o_ScreenSwitcher),
        59,
        182,
        556,
        197
    )

    clickButton(
        waitForObject(
            names.numpad_pushButton_8_NumpadButton,
            51432
        )
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
        waitForObject(names.mainFrame_okButton_QPushButton)
    )

    # CHANGE LANGUAGE TO DUTCH

    clickButton(
        waitForObject(
            names.homeScreen_settingsButton_QPushButton
        )
    )

    clickTab(
        waitForObject(
            names.settingsScreen_tbSystemInfo_TabWidget
        ),
        "INFO"
    )

    clickButton(
        waitForObject(
            names.gbSystemInformation_pbLanguageSettingsUpdate_QPushButton
        )
    )

    clickButton(
        waitForObject(
            names.languagesFrame_pbDutch_QPushButton
        )
    )

    clickButton(
        waitForObject(
            names.buttonsFrame_acceptButton_QPushButton
        )
    )

    clickButton(
        waitForObject(
            names.settingsScreen_pbBack_QPushButton
        )
    )

    snooze(1)

    # OPEN STONE ASSISTANT

    clickButton(
        waitForObject(
            names.homeScreen_pbStoneAssistant_QToolButton
        )
    )

    clickButton(
        waitForObject(
            names.locationFrame_kidneyPcnlLocationButton_QPushButton
        )
    )

    clickButton(
        waitForObject(
            names.flowRateFrame_lowFlowRateButton_QPushButton
        )
    )

    clickButton(
        waitForObject(
            names.hardnessFrame_smallHardnessButton_QPushButton
        )
    )

    clickButton(
        waitForObject(
            names.stoneAssistantModeScreen_continueButton_QPushButton
        )
    )

    # TREATMENT SCREEN

    mouseClick(
        waitForObject(
            names.topBar_buttonsBar_ButtonsBar
        ),
        75,
        43,
        Qt.NoModifier,
        Qt.LeftButton
    )

    mouseClick(
        waitForObject(
            names.averagePowerWidget_progressFrame_QFrame
        ),
        30,
        17,
        Qt.NoModifier,
        Qt.LeftButton
    )

    mouseClick(
        waitForObject(
            names.averagePowerWidget_unitsOfMeasureLabel_QLabel_2
        ),
        174,
        69,
        Qt.NoModifier,
        Qt.LeftButton
    )

    mouseClick(
        waitForObject(
            names.averagePowerWidget_progressFrame_QFrame_2
        ),
        18,
        11,
        Qt.NoModifier,
        Qt.LeftButton
    )

    mouseClick(
        waitForObject(
            names.pulseModeWidget_frequencyWidget_ParameterSettingsWidget
        ),
        21,
        19,
        Qt.NoModifier,
        Qt.LeftButton
    )

    mouseClick(
        waitForObject(
            names.pulseModeWidget_buttonsWidget_QWidget_2
        ),
        162,
        32,
        Qt.NoModifier,
        Qt.LeftButton
    )

    mouseClick(
        waitForObject(
            names.bottomBar_lbPedalStatusIcon_QLabel
        ),
        12,
        65,
        Qt.NoModifier,
        Qt.LeftButton
    )

    mouseClick(
        waitForObject(
            names.treatmentScreen_bottomBar_QFrame
        ),
        891,
        74,
        Qt.NoModifier,
        Qt.LeftButton
    )

    snooze(1)

    # READ EXCEL

    excelpath = (
        "/home/ntc/Test_Automation_Gemini/Localisation/"
        "suite_GFL_Czech/tst_Home Screen/testdata/"
        "Gemini Split strings.xlsx"
    )

    workbook = openpyxl.load_workbook(
        excelpath,
        data_only=True
    )

    sheet = workbook["Treatment Modes"]

    # GET CURRENT TREATMENT SCREEN

    screen = waitForObject(
        names.treatmentScreen_bottomBar_QFrame
    )

    screen_candidates = get_screen_candidates(screen)

    # CHECK PARENT

    try:
        parent = object.parent(screen)

        screen_candidates.extend(
            get_screen_candidates(parent)
        )

    except:
        pass

    # CHECK RECORDED OBJECTS

    recorded_objects = [
        names.topBar_buttonsBar_ButtonsBar,
        names.averagePowerWidget_progressFrame_QFrame,
        names.averagePowerWidget_unitsOfMeasureLabel_QLabel_2,
        names.averagePowerWidget_progressFrame_QFrame_2,
        names.pulseModeWidget_frequencyWidget_ParameterSettingsWidget,
        names.pulseModeWidget_buttonsWidget_QWidget_2,
        names.bottomBar_lbPedalStatusIcon_QLabel,
        names.treatmentScreen_bottomBar_QFrame
    ]

    for object_name in recorded_objects:

        try:
            obj = waitForObject(object_name)
            screen_candidates.extend(
                get_screen_candidates(obj)
            )
        except:
            pass

    screen_candidates = list(set(screen_candidates))

    # READ DUTCH FROM EXCEL
    # DUTCH = COLUMN G

    excel_strings = {}

    for row in sheet.iter_rows(
        min_row=2,
        values_only=True
    ):

        if len(row) < 7:
            continue

        trace_id = row[0]
        english = row[1]
        dutch = row[6]

        if english is None or dutch is None:
            continue

        english = str(english).strip()
        dutch = str(dutch).strip()

        if not english or not dutch:
            continue

        excel_strings[normalize(dutch)] = {
            "english": english,
            "dutch": dutch,
            "trace_id": (
                ""
                if trace_id is None
                else str(trace_id).strip()
            )
        }

    # MATCH SCREEN STRINGS WITH DUTCH EXCEL

    matches = {}

    for candidate in screen_candidates:

        normalized_candidate = normalize(candidate)

        if not normalized_candidate:
            continue

        if normalized_candidate in excel_strings:

            data = excel_strings[normalized_candidate]

            key = normalize(data["dutch"])

            matches[key] = (
                len(normalized_candidate),
                data["english"],
                data["dutch"]
            )

    # REMOVE DUPLICATES

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

        test.passes(
            "DUTCH STONE TREATMENT "
            "LOCALIZATION VALIDATION PASSED"
        )

    else:

        test.fail(
            "NO DUTCH STRINGS FOUND ON "
            "STONE TREATMENT SCREEN"
        )

    workbook.close()