
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

SHEET_NAME = "Treatment Logs"
ENGLISH_COLUMN = 1
TRACE_COLUMN = 0
TRACE_ID = "TL"

verified = set()
excel_strings = {}

passed_count = 0
failed_count = 0
skipped_count = 0


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


def ignore(text):

    text = str(text).strip()

    if not text:
        return True

    if re.fullmatch(r"\d+(\.\d+)?%?", text):
        return True

    if re.fullmatch(r"\d+(\.\d+)?\s*[a-zA-Zµμ]+", text):
        return True

    if re.fullmatch(r"\d+[/-]\d+[/-]\d+", text):
        return True

    if re.fullmatch(r"\d+[a-zA-Z]+\s*/\s*\d+[a-zA-Z]+", text):
        return True

    return False


def remove_duplicates(strings):

    result = []
    seen = set()

    for value in strings:

        key = normalize(value)

        if key and key not in seen:
            seen.add(key)
            result.append(value)

    return result


def get_texts(obj):

    result = []

    try:
        if not obj.visible:
            return result
    except:
        pass

    for attr in ("text", "title"):

        try:
            value = getattr(obj, attr)

            if value is not None:

                value = str(value).strip()

                if value:
                    result.append(value)

        except:
            pass

    try:
        for child in object.children(obj):
            result.extend(get_texts(child))
    except:
        pass

    return result


def load_excel():

    if not os.path.exists(EXCEL_PATH):
        raise Exception("Excel file not found: " + EXCEL_PATH)

    wb = openpyxl.load_workbook(
        EXCEL_PATH,
        data_only=True,
        read_only=True
    )

    if SHEET_NAME not in wb.sheetnames:
        wb.close()
        raise Exception("Excel sheet not found: " + SHEET_NAME)

    sheet = wb[SHEET_NAME]

    data = {}

    for row in sheet.iter_rows(min_row=2, values_only=True):

        if len(row) <= max(ENGLISH_COLUMN, TRACE_COLUMN):
            continue

        trace_value = row[TRACE_COLUMN]
        english = row[ENGLISH_COLUMN]

        if english is None or trace_value is None:
            continue

        trace_ids = [
            item.strip().upper()
            for item in str(trace_value).split(",")
        ]

        if TRACE_ID not in trace_ids:
            continue

        english = str(english).strip()

        if not english:
            continue

        key = normalize(english)

        if key and key not in data:
            data[key] = english

    wb.close()

    if not data:
        raise Exception("No English strings found for TL trace ID.")

    return data


def find_match(actual, excel):

    key = normalize(actual)

    if key in excel:
        return excel[key]

    return None


def verify(obj, area_name):

    global passed_count
    global failed_count
    global skipped_count

    test.log("========== VERIFYING " + area_name + " ==========")

    actual_texts = remove_duplicates(get_texts(obj))

    test.log(
        "Visible UI strings captured: " + str(len(actual_texts))
    )

    for actual in actual_texts:

        key = normalize(actual)

        if ignore(actual):

            skipped_count += 1
            test.log("SKIP: " + actual)
            continue

        if key in verified:
            continue

        verified.add(key)

        match = find_match(actual, excel_strings)

        if match:

            passed_count += 1
            test.passes("PASS: " + actual + " | Excel: " + match)

        else:

            failed_count += 1
            test.fail(
                "FAIL: " + actual +
                " -> String not found in Excel"
            )


def verification_summary():

    total = passed_count + failed_count

    test.log("========== TREATMENT LOGS VERIFICATION SUMMARY ==========")
    test.log("Worksheet: " + SHEET_NAME)
    test.log("Trace ID: " + TRACE_ID)
    test.log("Total unique strings checked: " + str(total))
    test.log("PASS: " + str(passed_count))
    test.log("FAIL: " + str(failed_count))
    test.log("SKIP: " + str(skipped_count))
    test.log("==========================================================")

    if failed_count == 0:
        test.log("RESULT: All verified strings matched Excel.")
    else:
        test.log("RESULT: Some visible strings were not found in Excel.")


def main():

    global excel_strings

    try:
        excel_strings = load_excel()

        test.log(
            "English strings loaded: " + str(len(excel_strings))
        )

    except Exception as error:

        test.fail("Excel loading failed: " + str(error))
        return

    sendEvent(
        "QMoveEvent",
        waitForObject(names.o_ScreenSwitcher),
        71, 180, 836, 196
    )

    for _ in range(4):

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
            names.homeScreen_logButton_QPushButton
        )
    )

    verify(
        waitForObject(names.tvLogsTable_QHeaderView),
        "LOG TABLE HEADER"
    )

    mouseClick(
        waitForObject(names.tvLogsTable_QHeaderView),
        1, 0,
        Qt.NoModifier,
        Qt.LeftButton
    )

    verify(
        waitForObject(names.tvLogsTable_QHeaderView),
        "LOG TABLE AFTER HEADER INTERACTION"
    )

    mouseClick(
        waitForObject(names.treatmentLogScreen_wdBottom_QWidget),
        525, 46,
        Qt.NoModifier,
        Qt.LeftButton
    )

    verify(
        waitForObject(names.treatmentLogScreen_wdBottom_QWidget),
        "BOTTOM AREA"
    )

    verification_summary()

    test.log("Treatment Logs English verification completed.")
