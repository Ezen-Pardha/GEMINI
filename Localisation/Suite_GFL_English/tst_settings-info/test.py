
# -*- coding: utf-8 -*-

import names
import subprocess
import xml.etree.ElementTree as ET
import builtins
import re
import html
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
ENGLISH_COLUMN = 2

verified_strings = set()


def norm(x):
    x = html.unescape(str(x or ""))
    x = re.sub(r"<[^>]+>", " ", x)
    return re.sub(r"\s+", " ", x).strip().casefold()


def remove_duplicates(strings):
    unique_strings = []
    seen = set()

    for value in strings:
        normalized = norm(value)

        if normalized and normalized not in seen:
            seen.add(normalized)
            unique_strings.append(value)

    return unique_strings


def texts(obj, is_root=True):
    result = []

    if not is_root:
        try:
            if not obj.visible:
                return result
        except:
            pass

    for attr in ("text", "title"):
        try:
            value = str(getattr(obj, attr))

            if value and value not in ("None", "<PyQt5...>"):
                result.append(value)

        except:
            pass

    try:
        for child in object.children(obj):
            result.extend(texts(child, False))
    except:
        pass

    return result


def unzip(member):
    process = subprocess.Popen(
        ["unzip", "-p", EXCEL_PATH, member],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    data, error = process.communicate()

    if process.returncode:
        raise Exception("Cannot read Excel file: " + member)

    return data


def col(reference):
    number = 0

    for char in reference:
        if not char.isalpha():
            break

        number = number * 26 + ord(char.upper()) - 64

    return number


def excel():
    ns = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
    rs = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"

    workbook = ET.fromstring(unzip("xl/workbook.xml"))
    relationships = ET.fromstring(
        unzip("xl/_rels/workbook.xml.rels")
    )

    links = {
        item.attrib["Id"]: item.attrib["Target"]
        for item in relationships
    }

    sheet = next(
        (
            item for item in workbook.find("{%s}sheets" % ns)
            if item.attrib["name"] == SHEET_NAME
        ),
        None
    )

    if sheet is None:
        raise Exception("Excel sheet not found: " + SHEET_NAME)

    target = links[sheet.attrib["{%s}id" % rs]]
    target = target.replace("\\", "/").lstrip("/")

    if not target.startswith("xl/"):
        target = "xl/" + target

    root = ET.fromstring(unzip(target))

    shared_strings = []

    try:
        shared_root = ET.fromstring(
            unzip("xl/sharedStrings.xml")
        )

        shared_strings = [
            "".join(
                item.text or ""
                for item in string.iter("{%s}t" % ns)
            )
            for string in shared_root.findall("{%s}si" % ns)
        ]

    except:
        pass

    strings = {}

    for row in root.findall(
        ".//{%s}sheetData/{%s}row" % (ns, ns)
    ):
        for cell in row.findall("{%s}c" % ns):

            if col(cell.attrib["r"]) != ENGLISH_COLUMN:
                continue

            cell_type = cell.attrib.get("t")
            node = cell.find("{%s}v" % ns)

            value = (
                "".join(
                    item.text or ""
                    for item in cell.iter("{%s}t" % ns)
                )
                if cell_type == "inlineStr"
                else (
                    node.text
                    if node is not None
                    else ""
                )
            )

            if cell_type == "s" and value:
                value = shared_strings[builtins.int(value)]

            value = str(value).strip()
            normalized = norm(value)

            if normalized:
                strings[normalized] = value

    if not strings:
        raise Exception(
            "No English strings found in settings worksheet column {}".format(
                ENGLISH_COLUMN
            )
        )

    return strings


def verify(actual_texts, screen_name):
    excel_strings = excel()
    actual_texts = remove_duplicates(actual_texts)

    for actual_text in actual_texts:
        actual_normalized = norm(actual_text)

        if len(actual_normalized) < 2:
            continue

        if re.fullmatch(r"[\d\s.,:/-]+", actual_normalized):
            continue

        matched = []

        if actual_normalized in excel_strings:
            matched.append(excel_strings[actual_normalized])

        else:
            for excel_normalized, english in excel_strings.items():

                if len(excel_normalized) < 4:
                    continue

                if (
                    excel_normalized in actual_normalized
                    or (
                        len(actual_normalized) >= 4
                        and actual_normalized in excel_normalized
                    )
                ):
                    matched.append(english)

        if matched:
            for english in matched:
                key = norm(english)

                if key in verified_strings:
                    continue

                verified_strings.add(key)

                test.verify(
                    True,
                    "PASS: {} | English: {}".format(
                        screen_name,
                        english
                    )
                )

        else:
            key = actual_normalized

            if key in verified_strings:
                continue

            verified_strings.add(key)

            test.verify(
                False,
                "FAIL: {} | Actual UI text: {}".format(
                    screen_name,
                    actual_text
                )
            )


def verify_current_screen(screen_name):
    root = waitForObject(names.o_ScreenSwitcher)
    actual_texts = texts(root)
    verify(actual_texts, screen_name)


def main():

    sendEvent(
        "QMoveEvent",
        waitForObject(names.o_ScreenSwitcher),
        46, 184, 709, 195
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
            names.homeScreen_settingsButton_QPushButton
        )
    )

    clickTab(
        waitForObject(
            names.settingsScreen_tbSystemInfo_TabWidget
        ),
        "INFO"
    )

    snooze(1)

    verify_current_screen("System Information")

    mouseClick(
        waitForObject(
            names.wdSystemInfoLayout_gbSystemInformation_QGroupBox
        ),
        401,
        0,
        Qt.NoModifier,
        Qt.LeftButton
    )

    snooze(1)

    verify_current_screen("System Information Details")

    mouseClick(
        waitForObject(
            names.wdSystemInfoLayout_gbFiberInformation_QGroupBox
        ),
        448,
        62,
        Qt.NoModifier,
        Qt.LeftButton
    )

    snooze(1)

    verify_current_screen("Fiber Information")

    test.log("English string verification completed.")
