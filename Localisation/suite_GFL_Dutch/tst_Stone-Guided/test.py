
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

SHEET_NAME = "Stone-Guided"

ENGLISH_COLUMN = 2
DUTCH_COLUMN = 7


def normalize(text):
    if text is None:
        return ""

    text = str(text)

    text = re.sub(
        r"<br\s*/?>",
        " ",
        text,
        flags=re.IGNORECASE
    )

    text = re.sub(r"<[^>]+>", " ", text)
    text = text.replace("\xa0", " ")
    text = " ".join(text.split())

    text = text.replace("–", "-")
    text = text.replace("—", "-")
    text = text.replace("−", "-")

    text = re.sub(r"\s*<\s*", "<", text)
    text = re.sub(r"\s*>\s*", ">", text)

    return text.strip().casefold()


def ignore_text(text):
    key = normalize(text)

    if not key:
        return True

    if re.search(r"\d", key):
        return True

    if re.fullmatch(r"[-_=.<>/%µμ:+]+", key):
        return True

    return False


def get_text_lines(obj, visited=None):
    if visited is None:
        visited = set()

    lines = []

    try:
        object_id = id(obj)

        if object_id in visited:
            return lines

        visited.add(object_id)
    except Exception:
        pass

    try:
        visible = obj.visible

        if visible is False:
            return lines
    except Exception:
        pass

    try:
        value = obj.text

        if value is not None:
            text = str(value).strip()

            if text:
                text = re.sub(
                    r"<br\s*/?>",
                    "\n",
                    text,
                    flags=re.IGNORECASE
                )

                text = re.sub(r"<[^>]+>", " ", text)

                for line in text.splitlines():
                    line = " ".join(line.split()).strip()

                    if line:
                        lines.append(line)

    except Exception:
        pass

    try:
        children = object.children(obj)
    except Exception:
        children = []

    for child in children:
        lines.extend(get_text_lines(child, visited))

    return lines


def load_dutch_excel(excel_path):
    if not os.path.isfile(excel_path):
        test.fail(
            "FAIL: Excel file not found: " + excel_path
        )
        return None, {}

    try:
        workbook = openpyxl.load_workbook(
            excel_path,
            data_only=True,
            read_only=True
        )
    except Exception as error:
        test.fail(
            "FAIL: Unable to load Dutch Excel: " + str(error)
        )
        return None, {}

    try:
        if SHEET_NAME not in workbook.sheetnames:
            available_sheets = ", ".join(workbook.sheetnames)

            test.fail(
                "FAIL: Worksheet not found: "
                + SHEET_NAME
                + " | Available worksheets: "
                + available_sheets
            )

            workbook.close()
            return None, {}

        sheet = workbook[SHEET_NAME]
        dutch_data = {}

        # English = Column B
        # Dutch = Column H

        for row in sheet.iter_rows(
            min_row=2,
            min_col=ENGLISH_COLUMN,
            max_col=DUTCH_COLUMN,
            values_only=True
        ):
            if len(row) < DUTCH_COLUMN - ENGLISH_COLUMN + 1:
                continue

            english = row[0]
            dutch = row[DUTCH_COLUMN - ENGLISH_COLUMN]

            if english is None or dutch is None:
                continue

            english = str(english).strip()
            dutch = str(dutch).strip()

            if not english or not dutch:
                continue

            if ignore_text(dutch):
                continue

            key = normalize(dutch)

            if key:
                dutch_data.setdefault(
                    key,
                    {
                        "english": english,
                        "dutch": dutch
                    }
                )

        return workbook, dutch_data

    except Exception as error:
        workbook.close()

        test.fail(
            "FAIL: Error reading Dutch Excel: " + str(error)
        )

        return None, {}


def verify_screen_strings(screen_object, dutch_data):
    screen_lines = get_text_lines(screen_object)
    screen_strings = {}

    for text in screen_lines:
        key = normalize(text)

        if ignore_text(text):
            continue

        if key not in screen_strings:
            screen_strings[key] = text.strip()

    pass_count = 0
    fail_count = 0

    for key in sorted(screen_strings):
        screen_text = screen_strings[key]

        if key in dutch_data:
            data = dutch_data[key]

            test.passes(
                "PASS: "
                + data["english"]
                + " -> "
                + data["dutch"]
            )

            pass_count += 1

        else:
            test.fail(
                "FAIL: Visible screen string is missing "
                "from Dutch Excel: "
                + screen_text
            )

            fail_count += 1

    total = len(screen_strings)

    if total == 0:
        test.fail(
            "FAIL: No eligible visible strings found on screen"
        )

    elif fail_count > 0:
        test.fail(
            "Dutch LOCALIZATION VALIDATION FAILED: "
            + str(fail_count)
            + " unmatched string(s) out of "
            + str(total)
        )

    else:
        test.passes(
            "Dutch LOCALIZATION VALIDATION PASSED: "
            + str(pass_count)
            + " unique visible string(s) verified"
        )

    return pass_count, fail_count


def main():
    workbook = None

    try:
        # LOGIN

        sendEvent(
            "QMoveEvent",
            waitForObject(names.o_ScreenSwitcher),
            57, 167, 718, 194
        )

        for _ in range(4):
            clickButton(
                waitForObject(
                    names.numpad_pushButton_8_NumpadButton
                )
            )

        snooze(2)

        clickButton(
            waitForObject(
                names.mainFrame_okButton_QPushButton
            )
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

        # OPEN STONE ASSISTANT

        clickButton(
            waitForObject(
                names.homeScreen_pbStoneAssistant_QToolButton
            )
        )

        # LOAD EXCEL

        workbook, dutch_data = load_dutch_excel(EXCEL_PATH)

        if workbook is None:
            return

        if not dutch_data:
            test.fail(
                "FAIL: No eligible Dutch translations found "
                "in worksheet: " + SHEET_NAME
            )
            return

        # STONE-GUIDED SELECTION

        clickButton(
            waitForObject(
                names.locationFrame_kidneyPcnlLocationButton_QPushButton
            )
        )

        mouseClick(
            waitForObject(
                names.locationFrame_label_3_QLabel
            ),
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
            waitForObject(
                names.flowRateFrame_label_4_QLabel
            ),
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
            waitForObject(
                names.hardnessFrame_label_6_QLabel
            ),
            196, 24,
            Qt.NoModifier,
            Qt.LeftButton
        )

        snooze(1)

        # GET STONE-GUIDED SCREEN

        stone = waitForObject(
            names.stoneAssistantModeScreen_StoneAssistantModeScreen
        )

        # VERIFY SCREEN STRINGS

        verify_screen_strings(
            stone,
            dutch_data
        )

    except Exception as error:
        test.fail(
            "Dutch LOCALIZATION TEST EXECUTION ERROR: "
            + str(error)
        )

    finally:
        if workbook is not None:
            workbook.close()
