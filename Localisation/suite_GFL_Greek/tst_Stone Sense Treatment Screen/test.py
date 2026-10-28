
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

# EXCEL_PATH = "/home/ntc/Test_Automation_Gemini/Localisation/suite_GFL_Czech/tst_Home Screen/testdata/Gemini Split strings.xlsx"
SHEET_NAME = "Treatment Modes"
GREEK_COLUMN = 11


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
        if not obj.visible:
            return ""
    except Exception:
        pass

    try:
        text = str(obj.text).strip()

        if text:
            text = re.sub(
                r"<br\s*/?>", " ", text, flags=re.IGNORECASE
            )
            text = re.sub(r"<[^>]+>", " ", text)
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

    for child in children:
        candidates.extend(
            get_screen_candidates(child, visited)
        )

    return candidates


def is_dynamic_numeric_value(text):
    text = str(text).strip()

    # Ignore values such as 0 J, 10 W, 5.5 J and 20 Hz.
    # Do not ignore standalone units such as W.
    # return bool(
    #     re.fullmatch(
    #         r"\d+(?:[.,]\d+)?\s*(?:J|W|Hz|ms|s|µm|um|%)",
    #         text,
    #         flags=re.IGNORECASE
    #     )
    # )


def main():

    # LOGIN

    sendEvent(
        "QMoveEvent",
        waitForObject(names.o_ScreenSwitcher),
        105, 204, 657, 223
    )

    for _ in range(4):
        clickButton(
            waitForObject(
                names.numpad_pushButton_8_NumpadButton
            )
        )

    clickButton(
        waitForObject(names.mainFrame_okButton_QPushButton)
    )

    # CHANGE LANGUAGE TO GREEK

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
            names.languagesFrame_pbGreece_QPushButton
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

    # OPEN STONE QUICK START

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
        291, 67, Qt.NoModifier, Qt.LeftButton
    )

    mouseClick(
        waitForObjectItem(
            names.tabRightMainPresets_rightPresetsView_PresetListView,
            "_1"
        ),
        103, 45, Qt.NoModifier, Qt.LeftButton
    )

    clickButton(
        waitForObject(
            names.quickStartScreen_pbContinue_QPushButton
        )
    )

    # TREATMENT SCREEN

    mouseClick(
        waitForObject(
            names.pulseModeWidget_averagePowerWidget_ParameterWithEnumerableValueWidget
        ),
        526, 3, Qt.NoModifier, Qt.LeftButton
    )

    mouseClick(
        waitForObject(
            names.rightPedalWidget_wdPresetTabs_TabWidget
        ),
        73, 35, Qt.NoModifier, Qt.LeftButton
    )

    mouseClick(
        waitForObject(
            names.topBar_buttonsBar_ButtonsBar
        ),
        381, 15, Qt.NoModifier, Qt.LeftButton
    )

    mouseClick(
        waitForObject(
            names.totalTimeFrame_nameLabel_QLabel
        ),
        161, 40, Qt.NoModifier, Qt.LeftButton
    )

    mouseClick(
        waitForObject(
            names.treatmentScreen_bottomBar_QFrame
        ),
        896, 24, Qt.NoModifier, Qt.LeftButton
    )

    snooze(1)

    # READ EXCEL

    try:
        workbook = openpyxl.load_workbook(
            EXCEL_PATH,
            data_only=True,
            read_only=True
        )

        if SHEET_NAME not in workbook.sheetnames:
            workbook.close()
            test.fail(
                "FAIL: Excel worksheet not found: "
                + SHEET_NAME
            )
            return

        sheet = workbook[SHEET_NAME]

    except Exception as error:
        test.fail(
            "FAIL: Unable to read Greek localization Excel: "
            + str(error)
        )
        return

    # LOAD GREEK TRANSLATIONS
    # Column A = Trace ID
    # Column B = English
    # Column L = Greek

    excel_strings = {}

    try:
        for row in sheet.iter_rows(
            min_row=2,
            values_only=True
        ):

            if len(row) <= GREEK_COLUMN:
                continue

            trace_id = row[0]
            english = row[1]
            greek = row[GREEK_COLUMN]

            if english is None or greek is None:
                continue

            english = str(english).strip()
            greek = str(greek).strip()

            normalized_greek = normalize(greek)

            if not normalized_greek:
                continue

            excel_strings.setdefault(
                normalized_greek,
                {
                    "english": english,
                    "Greek": greek,
                    "trace_id": (
                        ""
                        if trace_id is None
                        else str(trace_id).strip()
                    )
                }
            )

    except Exception as error:
        test.fail(
            "FAIL: Unable to load Greek translations: "
            + str(error)
        )
        workbook.close()
        return

    workbook.close()

    # COLLECT VISIBLE SCREEN STRINGS

    screen_candidates = []

    try:
        screen = waitForObject(
            names.treatmentScreen_bottomBar_QFrame
        )

        screen_candidates.extend(
            get_screen_candidates(screen)
        )

        try:
            parent = object.parent(screen)

            screen_candidates.extend(
                get_screen_candidates(parent)
            )
        except Exception:
            pass

    except Exception as error:
        test.fail(
            "FAIL: Unable to read Treatment screen: "
            + str(error)
        )
        return

    # CHECK RECORDED SCREEN OBJECTS

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

            screen_candidates.extend(
                get_screen_candidates(obj)
            )
        except Exception:
            pass

    # REMOVE EMPTY STRINGS AND DUPLICATES

    unique_candidates = {}

    for candidate in screen_candidates:

        candidate = str(candidate).strip()
        normalized_candidate = normalize(candidate)

        if not normalized_candidate:
            continue

        unique_candidates.setdefault(
            normalized_candidate,
            candidate
        )

    # MATCH SCREEN STRINGS AGAINST EXCEL

    matched_strings = {}
    missing_strings = set()

    for normalized_candidate, original_candidate in (
        unique_candidates.items()
    ):

        original_candidate = original_candidate.strip()

        # Ignore dynamic numeric values such as 0 J.
        if is_dynamic_numeric_value(original_candidate):
            continue

        # Check for letters from any language, including Greek.
        if not re.search(
            r"[^\W\d_]",
            original_candidate,
            flags=re.UNICODE
        ):
            continue

        if normalized_candidate in excel_strings:

            matched_strings[normalized_candidate] = (
                excel_strings[normalized_candidate]
            )

        else:
            missing_strings.add(original_candidate)

    # REPORT MATCHED STRINGS

    pass_count = 0
    fail_count = 0

    for key in sorted(matched_strings):

        data = matched_strings[key]

        test.passes(
            "PASS: "
            + data["english"]
            + " -> "
            + data["Greek"]
        )

        pass_count += 1

    # REPORT STRINGS MISSING FROM EXCEL

    for missing in sorted(
        missing_strings,
        key=str.casefold
    ):

        test.fail(
            "FAIL: Visible screen string missing from Greek Excel: "
            + missing
        )

        fail_count += 1

    # FINAL RESULT

    if pass_count > 0 and fail_count == 0:

        test.passes(
            "Greek STONE QUICK START LOCALIZATION VALIDATION PASSED"
            + " | Matched: " + str(pass_count)
            + " | Missing: 0"
        )

    else:

        test.fail(
            "Greek STONE QUICK START LOCALIZATION VALIDATION FAILED"
            + " | Matched: " + str(pass_count)
            + " | Missing from Excel: " + str(fail_count)
        )
