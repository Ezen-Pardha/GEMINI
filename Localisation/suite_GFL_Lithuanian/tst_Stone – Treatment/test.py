
# -*- coding: utf-8 -*-

import names
import openpyxl
import re
import os

TESTCASE_DIR = os.path.dirname(os.path.abspath(__file__))

EXCEL_PATH = os.path.abspath(
    os.path.join(
        TESTCASE_DIR,
        "..",
        "shared",
        "testdata",
        "Gemini Split strings.xlsx"
    )
)

SHEET_NAME = "Treatment Modes"
ENGLISH_COLUMN = 1
Lithuania_COLUMN = 16


def normalize(text):
    if text is None:
        return ""

    text = str(text)
    text = re.sub(r"<br\s*/?>", " ", text, flags=re.IGNORECASE)
    text = re.sub(r"<[^>]+>", " ", text)
    text = text.replace("\xa0", " ")
    text = " ".join(text.split())
    text = re.sub(r"\s*<\s*", "<", text)
    text = re.sub(r"\s*>\s*", ">", text)

    return text.strip().casefold()


def get_object_text(obj):
    try:
        visibility = obj.visible
        if visibility is not None and visibility == False:
            return ""
    except Exception:
        pass

    for property_name in ("text", "title"):
        try:
            value = getattr(obj, property_name)

            if callable(value):
                value = value()

            if value is None:
                continue

            text = str(value).strip()

            if text:
                text = re.sub(
                    r"<br\s*/?>",
                    " ",
                    text,
                    flags=re.IGNORECASE
                )
                text = re.sub(r"<[^>]+>", " ", text)
                text = text.replace("\xa0", " ")
                text = " ".join(text.split())

                return text.strip()

        except Exception:
            pass

    return ""


def get_screen_candidates(obj, visited=None):
    if visited is None:
        visited = set()

    candidates = []

    try:
        object_id = id(obj)

        if object_id in visited:
            return candidates

        visited.add(object_id)
    except Exception:
        pass

    own_text = get_object_text(obj)

    if own_text:
        candidates.append(own_text)

    try:
        children = object.children(obj)
    except Exception:
        children = []

    child_texts = []

    for child in children:
        child_text = get_object_text(child)

        if child_text:
            child_texts.append(child_text)
            candidates.append(child_text)

    # Combined candidates help identify labels split across widgets.
    for start in range(len(child_texts)):
        combined = ""

        for end in range(start, len(child_texts)):
            if combined:
                combined += " " + child_texts[end]
            else:
                combined = child_texts[end]

            candidates.append(combined)

    for child in children:
        candidates.extend(
            get_screen_candidates(child, visited)
        )

    return candidates


def load_Lithuania_strings():
    workbook = openpyxl.load_workbook(
        EXCEL_PATH,
        data_only=True,
        read_only=True
    )

    try:
        if SHEET_NAME not in workbook.sheetnames:
            test.fail(
                "Excel worksheet not found: " + SHEET_NAME
            )
            return {}

        sheet = workbook[SHEET_NAME]
        catalog = {}

        for row in sheet.iter_rows(
            min_row=2,
            values_only=True
        ):
            if len(row) <= Lithuania_COLUMN:
                continue

            trace_id = row[0]
            english = row[ENGLISH_COLUMN]
            Lithuania = row[Lithuania_COLUMN]

            if english is None or Lithuania is None:
                continue

            english = str(english).strip()
            Lithuania = str(Lithuania).strip()

            if not english or not Lithuania:
                continue

            key = normalize(Lithuania)

            if key:
                catalog[key] = {
                    "english": english,
                    "Lithuania": Lithuania,
                    "trace_id": (
                        ""
                        if trace_id is None
                        else str(trace_id).strip()
                    )
                }

        return catalog

    finally:
        workbook.close()


def main():

    # LOGIN

    sendEvent(
        "QMoveEvent",
        waitForObject(names.o_ScreenSwitcher),
        59, 182, 556, 197
    )

    clickButton(
        waitForObject(
            names.numpad_pushButton_8_NumpadButton,
            51432
        )
    )

    for _ in range(3):
        clickButton(
            waitForObject(
                names.numpad_pushButton_8_NumpadButton
            )
        )

    clickButton(
        waitForObject(names.mainFrame_okButton_QPushButton)
    )

    # CHANGE LANGUAGE TO Lithuania

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
        waitForObject(names.languagesFrame_pbLithuania_QPushButton)
    )

    clickButton(
        waitForObject(names.buttonsFrame_acceptButton_QPushButton)
    )

    clickButton(
        waitForObject(names.settingsScreen_pbBack_QPushButton)
    )

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

    # TREATMENT SCREEN ACTIONS

    mouseClick(
        waitForObject(names.topBar_buttonsBar_ButtonsBar),
        75, 43,
        Qt.NoModifier,
        Qt.LeftButton
    )

    mouseClick(
        waitForObject(
            names.averagePowerWidget_progressFrame_QFrame
        ),
        30, 17,
        Qt.NoModifier,
        Qt.LeftButton
    )

    mouseClick(
        waitForObject(
            names.averagePowerWidget_unitsOfMeasureLabel_QLabel_2
        ),
        174, 69,
        Qt.NoModifier,
        Qt.LeftButton
    )

    mouseClick(
        waitForObject(
            names.averagePowerWidget_progressFrame_QFrame_2
        ),
        18, 11,
        Qt.NoModifier,
        Qt.LeftButton
    )

    mouseClick(
        waitForObject(
            names.pulseModeWidget_frequencyWidget_ParameterSettingsWidget
        ),
        21, 19,
        Qt.NoModifier,
        Qt.LeftButton
    )

    mouseClick(
        waitForObject(
            names.pulseModeWidget_buttonsWidget_QWidget_2
        ),
        162, 32,
        Qt.NoModifier,
        Qt.LeftButton
    )

    mouseClick(
        waitForObject(names.bottomBar_lbPedalStatusIcon_QLabel),
        12, 65,
        Qt.NoModifier,
        Qt.LeftButton
    )

    mouseClick(
        waitForObject(names.treatmentScreen_bottomBar_QFrame),
        891, 74,
        Qt.NoModifier,
        Qt.LeftButton
    )

    snooze(1)

    # LOAD Lithuania EXCEL CATALOG

    excel_strings = load_Lithuania_strings()

    if not excel_strings:
        test.fail("No Lithuania strings loaded from Excel.")
        return

    # COLLECT TREATMENT SCREEN TEXT

    screen = waitForObject(
        names.treatmentScreen_bottomBar_QFrame
    )

    screen_candidates = get_screen_candidates(screen)

    # CHECK SCREEN PARENT

    try:
        parent = object.parent(screen)

        screen_candidates.extend(
            get_screen_candidates(parent)
        )
    except Exception:
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
        except Exception:
            pass

    # LOAD UNIQUE INDIVIDUAL TEXT CANDIDATES

    individual_candidates = []
    combined_candidates = []
    seen_individual = set()
    seen_combined = set()

    for candidate in screen_candidates:
        text = str(candidate).strip()
        key = normalize(text)

        if not key:
            continue

        # Keep combined strings available for matching,
        # but do not automatically report them as missing.
        if " " in text:
            if key not in seen_combined:
                seen_combined.add(key)
                combined_candidates.append(text)
        else:
            if key not in seen_individual:
                seen_individual.add(key)
                individual_candidates.append(text)

    # MATCH INDIVIDUAL STRINGS FIRST

    matches = {}
    missing_strings = {}

    for candidate in individual_candidates:
        key = normalize(candidate)

        if key in excel_strings:
            matches[key] = excel_strings[key]
        else:
            missing_strings[key] = candidate

    # MATCH COMBINED CANDIDATES THAT REPRESENT EXCEL STRINGS.
    # This supports phrases split over multiple UI elements.

    for candidate in combined_candidates:
        key = normalize(candidate)

        if key in excel_strings:
            matches[key] = excel_strings[key]

            # Remove a matching string from the missing set.
            if key in missing_strings:
                del missing_strings[key]

    # REPORT PASS RESULTS

    pass_count = 0

    for key in sorted(matches):
        data = matches[key]

        test.passes(
            data["english"] + " -> " + data["Lithuania"]
        )

        pass_count += 1

    # REPORT FAIL RESULTS FOR UNMATCHED INDIVIDUAL TEXT

    fail_count = 0

    for key in sorted(missing_strings):
        test.fail(
            "Visible screen string missing from Lithuania Excel: "
            + missing_strings[key]
        )

        fail_count += 1

    # FINAL RESULT

    if fail_count == 0 and pass_count > 0:
        test.passes(
            "Lithuania STONE TREATMENT LOCALIZATION VALIDATION PASSED"
        )
    else:
        test.fail(
            "Lithuania STONE TREATMENT LOCALIZATION VALIDATION FAILED: "
            "{} PASS, {} FAIL".format(
                pass_count,
                fail_count
            )
        )
