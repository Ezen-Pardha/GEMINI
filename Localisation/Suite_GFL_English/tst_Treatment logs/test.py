# -*- coding: utf-8 -*-

import names
import openpyxl
import re

EXCEL_PATH = "/home/ntc/Test_Automation_Gemini/Localisation/Suite_GFL_English/tst_LoginScreen-Logoff/testdata/Gemini strings.xlsx"
verified = set()


def normalize(text):
    if text is None:
        return ""
    text = re.sub(r"<[^>]+>", " ", str(text))
    return " ".join(text.split()).casefold().strip()


def ignore(text):
    text = str(text).strip()
    return (
        not text
        or len(text) < 2
        or re.fullmatch(r"\d+(\.\d+)?%?", text)
        or re.fullmatch(r"\d+(\.\d+)?\s*[a-zA-Z]+", text)
        or re.fullmatch(r"\d+[/-]\d+[/-]\d+", text)
        or re.fullmatch(r"\d+[a-zA-Z]+\s*/\s*\d+[a-zA-Z]+", text)
    )


def get_texts(obj):
    result = []

    try:
        if not obj.visible:
            return result
    except:
        pass

    for attr in ("text", "title"):
        try:
            value = str(getattr(obj, attr)).strip()
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
    wb = openpyxl.load_workbook(EXCEL_PATH, data_only=True)
    data = {}

    for row in wb.active.iter_rows(min_row=2, values_only=True):
        if row and row[0]:
            value = str(row[0]).strip()
            data[normalize(value)] = value

    wb.close()
    return data


def verify(obj):
    excel = load_excel()

    for actual in set(get_texts(obj)):
        key = normalize(actual)

        if ignore(actual) or key in verified:
            continue

        match = excel.get(key)

        if not match:
            for excel_key, value in excel.items():
                if len(excel_key) >= 4 and (
                    excel_key in key or key in excel_key
                ):
                    match = value
                    break

        verified.add(key)

        if match:
            test.passes(match)
        else:
            test.fail(actual + " -> String not found in Excel")


def click(obj):
    clickButton(waitForObject(obj))


def main():

    # LOGIN - NO VERIFICATION
    sendEvent(
        "QMoveEvent",
        waitForObject(names.o_ScreenSwitcher),
        71, 180, 836, 196
    )

    for _ in range(4):
        click(names.numpad_pushButton_8_NumpadButton)

    click(names.mainFrame_okButton_QPushButton)

    # OPEN LOGS - VERIFICATION STARTS HERE
    click(names.homeScreen_logButton_QPushButton)

    verify(
        waitForObject(names.tvLogsTable_QHeaderView)
    )

    # LOG TABLE HEADER
    mouseClick(
        waitForObject(names.tvLogsTable_QHeaderView),
        1, 0,
        Qt.NoModifier,
        Qt.LeftButton
    )

    verify(
        waitForObject(names.tvLogsTable_QHeaderView)
    )

    # BOTTOM AREA
    mouseClick(
        waitForObject(names.treatmentLogScreen_wdBottom_QWidget),
        525, 46,
        Qt.NoModifier,
        Qt.LeftButton
    )

    verify(
        waitForObject(names.treatmentLogScreen_wdBottom_QWidget)
    )