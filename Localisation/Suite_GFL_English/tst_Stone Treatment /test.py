
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

TREATMENT_SHEET = "Treatment Modes"
HOME_SHEET = "Home Screen"
GLOBAL_SHEET = "GUI Strings"

TRACE_ID = "TM"


UI_ALIASES = {
    "uses remaining": "fiber uses remaining"
}



def normalize(text):

    if text is None:
        return ""

    text = str(text)

    text = re.sub(r"<[^>]+>", " ", text)

    text = text.replace("™", "")
    text = text.replace("®", "")

    text = text.replace("μ", "µ")

    text = " ".join(text.split())

    return text.casefold().strip()



def get_all_texts(obj):

    texts = []

    try:
        if not obj.visible:
            return texts
    except:
        pass

    try:

        value = obj.text

        if value is not None and str(value).strip():
            texts.append(str(value).strip())

    except:
        pass

    try:

        value = obj.title

        if value is not None and str(value).strip():
            texts.append(str(value).strip())

    except:
        pass

    # Get child objects
    try:

        for child in object.children(obj):

            texts.extend(
                get_all_texts(child)
            )

    except:
        pass

    return texts



def read_sheet_strings(workbook, sheet_name, trace_filter=None,
                       only_empty_trace=False):

    strings = {}

    if sheet_name not in workbook.sheetnames:

        test.fail(
            "Worksheet not found: " + sheet_name
        )

        return strings

    sheet = workbook[sheet_name]

    headers = next(
        sheet.iter_rows(
            min_row=1,
            max_row=1,
            values_only=True
        )
    )

    trace_column = None
    english_column = None

    for index, header in enumerate(headers):

        if header is None:
            continue

        header = str(header).strip().casefold()

        if header == "gui spec trace ids":
            trace_column = index

        elif header == "english":
            english_column = index

    if english_column is None:

        test.fail(
            "English column not found in " + sheet_name
        )

        return strings

    for row in sheet.iter_rows(
        min_row=2,
        values_only=True
    ):

        if len(row) <= english_column:
            continue

        english = row[english_column]

        if english is None:
            continue

        english = str(english).strip()

        if not english:
            continue

        # Read trace ID
        trace_value = ""

        if trace_column is not None and len(row) > trace_column:
            trace_value = row[trace_column]

        trace_ids = []

        if trace_value:

            trace_ids = [
                item.strip().upper()
                for item in str(trace_value).split(",")
            ]

        # Filter selected trace IDs
        if trace_filter is not None:

            if not any(
                trace in trace_ids
                for trace in trace_filter
            ):
                continue

        # Read only globally untagged strings
        if only_empty_trace:

            if trace_ids:
                continue

        key = normalize(english)

        if key and key not in strings:

            strings[key] = english

    return strings



def load_english_strings():

    if not os.path.exists(EXCEL_PATH):

        test.fail(
            "Excel file not found: " + EXCEL_PATH
        )

        return {}

    try:

        workbook = openpyxl.load_workbook(
            EXCEL_PATH,
            data_only=True,
            read_only=True
        )

        strings = {}

        # 1. Treatment Modes strings
        treatment_strings = read_sheet_strings(
            workbook,
            TREATMENT_SHEET,
            trace_filter=[TRACE_ID]
        )

        strings.update(treatment_strings)

        # 2. Shared header strings from Home Screen
        home_strings = read_sheet_strings(
            workbook,
            HOME_SHEET
        )

        strings.update(home_strings)

        # 3. Untagged global strings
        global_strings = read_sheet_strings(
            workbook,
            GLOBAL_SHEET,
            only_empty_trace=True
        )

        strings.update(global_strings)

        workbook.close()

        test.log(
            "Treatment Modes strings: " +
            str(len(treatment_strings))
        )

        test.log(
            "Home Screen strings: " +
            str(len(home_strings))
        )

        test.log(
            "Global strings: " +
            str(len(global_strings))
        )

        return strings

    except Exception as error:

        test.fail(
            "Excel reading error: " + str(error)
        )

        return {}



def find_excel_match(ui_text, excel_strings):

    ui_key = normalize(ui_text)

    if not ui_key:
        return []

    # Ignore numeric-only values
    if not any(char.isalpha() for char in ui_key):
        return []

    # 1. Exact matching
    if ui_key in excel_strings:

        return [
            excel_strings[ui_key]
        ]

    # 2. Explicit aliases for split UI labels
    if ui_key in UI_ALIASES:

        alias_key = normalize(
            UI_ALIASES[ui_key]
        )

        if alias_key in excel_strings:

            return [
                excel_strings[alias_key]
            ]


    if re.search(r"\d", ui_key):

        cleaned = re.sub(
            r"\d+(?:[.,]\d+)?",
            " ",
            ui_key
        )

        cleaned = " ".join(cleaned.split())

        if not cleaned:
            return []

        # Check the remaining complete phrase
        if cleaned in excel_strings:

            return [
                excel_strings[cleaned]
            ]

        # Check individual remaining words
        words = cleaned.split()

        matches = []

        for word in words:

            if word in excel_strings:

                matches.append(
                    excel_strings[word]
                )

            else:
                return []

        return matches

    words = ui_key.split()

    if len(words) > 1:

        matches = []

        for word in words:

            if word in excel_strings:

                matches.append(
                    excel_strings[word]
                )

            else:

                matches = []
                break

        if matches:
            return matches

    # No exact match
    return []



def verify_treatment_screen():

    test.log(
        "========== TREATMENT SCREEN ENGLISH VERIFICATION =========="
    )

    test.log(
        "Excel worksheet: " + TREATMENT_SHEET
    )

    test.log(
        "Trace ID: " + TRACE_ID
    )

    # Load Excel strings
    excel_strings = load_english_strings()

    if not excel_strings:

        test.fail(
            "No English strings loaded from Excel."
        )

        return

    test.log(
        "Total English reference strings: " +
        str(len(excel_strings))
    )

    # Get current screen
    try:

        root = waitForObject(
            names.o_ScreenSwitcher
        )

    except Exception as error:

        test.fail(
            "Treatment Screen object not found: " +
            str(error)
        )

        return

    # Capture visible UI strings
    screen_texts = get_all_texts(root)

    # Normalize and remove duplicates
    ui_strings = {}

    for text in screen_texts:

        key = normalize(text)

        if not key:
            continue

        # Ignore numeric-only values
        if not any(char.isalpha() for char in key):
            continue

        if key not in ui_strings:

            ui_strings[key] = text

    test.log(
        "Unique visible UI strings captured: " +
        str(len(ui_strings))
    )

    passed = 0
    failed = 0
    skipped = 0

    # Verify visible UI strings only
    for ui_key, ui_text in sorted(ui_strings.items()):

        matches = find_excel_match(
            ui_text,
            excel_strings
        )

        if matches:

            passed += 1

            test.passes(
                "PASS: " + ui_text +
                " | Excel: " + ", ".join(matches)
            )

        else:

            if re.search(r"\d", ui_key):

                skipped += 1

                test.log(
                    "SKIP: Dynamic UI value: " + ui_text
                )

            else:

                failed += 1

                test.fail(
                    "FAIL: Visible UI string not found in Excel: " +
                    ui_text
                )

    # Final summary
    total = passed + failed

    test.log(
        "========== FINAL VERIFICATION SUMMARY =========="
    )

    test.log(
        "Worksheet: " + TREATMENT_SHEET
    )

    test.log(
        "Total visible strings checked: " + str(total)
    )

    test.log(
        "PASS: " + str(passed)
    )

    test.log(
        "FAIL: " + str(failed)
    )

    test.log(
        "SKIP: " + str(skipped)
    )

    test.log(
        "=================================================="
    )

    if failed == 0:

        test.log(
            "RESULT: All checked visible English strings matched Excel."
        )

    else:

        test.log(
            "RESULT: Some visible English strings were not found in Excel."
        )



def main():

    # Login
    sendEvent(
        "QMoveEvent",
        waitForObject(names.o_ScreenSwitcher),
        45,
        205,
        727,
        218
    )

    for i in range(4):

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

    # Verify visible Treatment Screen strings
    verify_treatment_screen()
