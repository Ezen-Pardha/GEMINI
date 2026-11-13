
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

SHEET_NAME = "settings"
TRACE_IDS = ["TL", "SY"]
TRACE_COLUMN = 0
ENGLISH_COLUMN = 1

verified_strings = set()
pass_count = 0
fail_count = 0


def normalize(text):
    if text is None:
        return ""

    text = str(text)
    text = re.sub(r"<[^>]+>", "", text)
    text = text.replace("&nbsp;", " ")
    text = text.replace("\n", " ")
    text = text.replace("\r", " ")
    text = re.sub(r"\s+", " ", text)

    return text.strip().upper()


def ignore(text):
    text = normalize(text)

    if not text:
        return True

    patterns = [
        r"\d{1,2}[-/]\d{1,2}[-/]\d{2,4}\s+\d{1,2}:\d{2}(:\d{2})?\s*(AM|PM)?",
        r"\d{1,2}[-/]\d{1,2}[-/]\d{2,4}",
        r"\d{4}[-/]\d{1,2}[-/]\d{1,2}",
        r"\d{1,2}:\d{2}(:\d{2})?\s*(AM|PM)?",
        r"^\d+(\.\d+)?$",
        r"^PAGE\s+\d+\s*/\s*\d+$"
    ]

    for pattern in patterns:
        if re.fullmatch(pattern, text, re.IGNORECASE):
            return True

    return False


def load_english_strings():
    workbook = openpyxl.load_workbook(
        EXCEL_PATH,
        data_only=True
    )

    if SHEET_NAME not in workbook.sheetnames:
        workbook.close()
        test.fail("Worksheet not found: {}".format(SHEET_NAME))
        return {}

    sheet = workbook[SHEET_NAME]
    english_strings = {}

    for row in sheet.iter_rows(min_row=2, values_only=True):

        if len(row) <= ENGLISH_COLUMN:
            continue

        trace_value = normalize(row[TRACE_COLUMN])
        english_value = normalize(row[ENGLISH_COLUMN])

        if not trace_value or not english_value:
            continue

        row_trace_ids = [
            item.strip()
            for item in trace_value.split(",")
        ]

        if any(trace_id in row_trace_ids for trace_id in TRACE_IDS):
            english_strings[english_value] = english_value

    workbook.close()

    test.log("Excel strings loaded: {}".format(len(english_strings)))

    return english_strings


def get_object_texts(obj):
    texts = []

    try:
        value = normalize(obj.property("text"))

        if value:
            texts.append(value)
    except:
        pass

    try:
        value = normalize(obj.property("title"))

        if value:
            texts.append(value)
    except:
        pass

    try:
        children = object.children(obj)

        for child in children:
            texts.extend(get_object_texts(child))

    except:
        pass

    return texts


def get_table_model_texts(table):
    texts = []

    try:
        model = table.model()

        row_count = model.rowCount()
        column_count = model.columnCount()

        for column in range(column_count):

            try:
                header = model.headerData(
                    column,
                    Qt.Horizontal,
                    Qt.DisplayRole
                )

                header = normalize(header)

                if header:
                    texts.append(header)

            except:
                pass

        for row in range(row_count):

            for column in range(column_count):

                try:
                    index = model.index(row, column)

                    value = model.data(
                        index,
                        Qt.DisplayRole
                    )

                    value = normalize(value)

                    if value:
                        texts.append(value)

                except:
                    pass

    except:
        pass

    return texts


def match_excel(ui_text, excel_strings):

    if ui_text in excel_strings:
        return True

    if ui_text.endswith(":"):
        if ui_text[:-1].strip() in excel_strings:
            return True

    if ui_text == "DATE/TIME":
        return (
            "DATE" in excel_strings and
            "TIME" in excel_strings
        )

    return False


def verify_logs_screen(excel_strings):
    global pass_count
    global fail_count

    ui_strings = []

    try:
        table = waitForObject(
            names.systemEventErrorLogWidget_tableView_QTableView
        )

        ui_strings.extend(
            get_table_model_texts(table)
        )

    except Exception:
        test.fail("Unable to capture Logs table.")
        return

    try:
        screen = waitForObject(names.o_ScreenSwitcher)

        screen_texts = get_object_texts(screen)

        allowed_footer_strings = [
            "BACK",
            "DOWNLOAD LOGS TO USB"
        ]

        for value in screen_texts:

            if value in allowed_footer_strings:
                ui_strings.append(value)

    except:
        pass

    unique_ui_strings = set(
        value for value in ui_strings if value
    )

    if not unique_ui_strings:
        test.fail("No Logs screen strings were captured.")
        return

    for ui_text in sorted(unique_ui_strings):

        ui_text = normalize(ui_text)

        if ignore(ui_text):
            continue

        if ui_text in verified_strings:
            continue

        verified_strings.add(ui_text)

        if match_excel(ui_text, excel_strings):

            test.passes(
                "PASS: {}".format(ui_text)
            )

            pass_count += 1

        else:

            test.fail(
                "FAIL: {} -> String not found in Excel worksheet".format(
                    ui_text
                )
            )

            fail_count += 1


def main():
    global pass_count
    global fail_count

    excel_strings = load_english_strings()

    if not excel_strings:
        test.fail("No English strings loaded from Excel.")
        return

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

    clickButton(
        waitForObject(names.mainFrame_okButton_QPushButton)
    )

    clickButton(
        waitForObject(names.homeScreen_settingsButton_QPushButton)
    )

    clickTab(
        waitForObject(names.settingsScreen_tbSystemInfo_TabWidget),
        "LOGS"
    )

    verify_logs_screen(excel_strings)

    test.log("========== FINAL LOGS SCREEN RESULT ==========")
    test.log("Total unique strings checked: {}".format(len(verified_strings)))
    test.log("PASS: {}".format(pass_count))
    test.log("FAIL: {}".format(fail_count))
    test.log("===============================================")

    test.log("Logs screen English verification completed.")
