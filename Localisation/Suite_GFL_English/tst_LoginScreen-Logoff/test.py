
# -*- coding: utf-8 -*-

import names
import openpyxl
import re
import os

# ==========================================================
# EXCEL CONFIGURATION
# ==========================================================

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

SHEET_NAME = "Trea"
ENGLISH_COLUMN = 2  # Column B

# ==========================================================
# GLOBAL VARIABLES
# ==========================================================

verified_strings = set()
failed_strings = set()
screen_results = {}

total_checks = 0
total_passed = 0
total_failed = 0


# ==========================================================
# NORMALIZE TEXT
# ==========================================================

def normalize(text):

    if text is None:
        return ""

    text = str(text)
    text = re.sub(r"\s+", " ", text)

    return text.strip().casefold()


# ==========================================================
# LOAD ENGLISH STRINGS FROM EXCEL
# ==========================================================

def load_english_strings():

    if not os.path.exists(EXCEL_PATH):
        test.fail("Excel file not found: " + EXCEL_PATH)
        return []

    workbook = None

    try:

        workbook = openpyxl.load_workbook(
            EXCEL_PATH,
            data_only=True,
            read_only=True
        )

        if SHEET_NAME not in workbook.sheetnames:

            test.fail("Worksheet not found: " + SHEET_NAME)
            return []

        worksheet = workbook[SHEET_NAME]

        english_strings = []
        unique_strings = set()

        for row in worksheet.iter_rows(
            min_row=2,
            values_only=True
        ):

            if len(row) < ENGLISH_COLUMN:
                continue

            value = row[ENGLISH_COLUMN - 1]

            if value is None:
                continue

            value = str(value).strip()

            normalized = normalize(value)

            if normalized and normalized not in unique_strings:

                unique_strings.add(normalized)
                english_strings.append(value)

        test.log(
            "Total unique English strings loaded: " +
            str(len(english_strings))
        )

        return english_strings

    except Exception as error:

        test.fail("Excel reading error: " + str(error))
        return []

    finally:

        if workbook:
            workbook.close()


# ==========================================================
# GET ALL VISIBLE TEXTS FROM SCREEN OBJECT
# ==========================================================

def get_all_texts(obj, visited=None):

    texts = []

    if visited is None:
        visited = set()

    try:

        object_id = id(obj)

        if object_id in visited:
            return texts

        visited.add(object_id)

    except Exception:
        pass

    # Read text property

    for property_name in [
        "text",
        "title",
        "windowTitle",
        "accessibleName",
        "accessibleDescription"
    ]:

        try:

            value = getattr(obj, property_name)

            if callable(value):
                value = value()

            if value is not None and str(value).strip():

                texts.append(str(value))

        except Exception:
            pass

    # Read child objects recursively

    try:

        children = object.children(obj)

        for child in children:

            texts.extend(
                get_all_texts(child, visited)
            )

    except Exception:
        pass

    return texts


# ==========================================================
# VERIFY STRINGS ON EACH SCREEN
# ==========================================================

def verify_screen(screen_name, screen_object, english_strings):

    global total_checks
    global total_passed
    global total_failed

    test.log("")
    test.log("========================================")
    test.log("VERIFYING: " + screen_name)
    test.log("========================================")

    visible_texts = get_all_texts(screen_object)

    normalized_visible = set()

    for text_value in visible_texts:

        normalized = normalize(text_value)

        if normalized:
            normalized_visible.add(normalized)

    screen_pass = 0
    screen_fail = 0

    screen_verified = []
    screen_missing = []

    for expected in english_strings:

        expected_normalized = normalize(expected)

        total_checks += 1

        if expected_normalized in normalized_visible:

            test.passes(
                "PASS: " + expected
            )

            verified_strings.add(expected_normalized)

            screen_verified.append(expected)

            screen_pass += 1
            total_passed += 1

        else:

            test.fail(
                "FAIL: English string not found: " + expected
            )

            failed_strings.add(expected_normalized)

            screen_missing.append(expected)

            screen_fail += 1
            total_failed += 1

    screen_results[screen_name] = {
        "total": len(english_strings),
        "passed": screen_pass,
        "failed": screen_fail,
        "missing": screen_missing,
        "verified": screen_verified
    }

    test.log("")
    test.log("Screen: " + screen_name)
    test.log("Total checked: " + str(len(english_strings)))
    test.log("Passed: " + str(screen_pass))
    test.log("Failed: " + str(screen_fail))


# ==========================================================
# FINAL SUMMARY
# ==========================================================

def show_summary():

    test.log("")
    test.log("================================================")
    test.log("       ENGLISH STRING VERIFICATION SUMMARY")
    test.log("================================================")

    for screen_name, result in screen_results.items():

        test.log("")
        test.log("Screen: " + screen_name)

        test.log(
            "Total: " + str(result["total"])
        )

        test.log(
            "PASS: " + str(result["passed"])
        )

        test.log(
            "FAIL: " + str(result["failed"])
        )

    test.log("")
    test.log("================================================")
    test.log("                 OVERALL RESULT")
    test.log("================================================")

    test.log(
        "Total checks: " + str(total_checks)
    )

    test.log(
        "Total PASS: " + str(total_passed)
    )

    test.log(
        "Total FAIL: " + str(total_failed)
    )

    test.log(
        "Unique strings verified at least once: " +
        str(len(verified_strings))
    )

    test.log(
        "Unique strings failed at least once: " +
        str(len(failed_strings))
    )

    test.log("")
    test.log("================================================")
    test.log("             VERIFIED ENGLISH STRINGS")
    test.log("================================================")

    for value in sorted(verified_strings):

        test.log("PASS: " + value)

    test.log("")
    test.log("================================================")
    test.log("              MISSING ENGLISH STRINGS")
    test.log("================================================")

    for screen_name, result in screen_results.items():

        if result["missing"]:

            test.log("")
            test.log("Screen: " + screen_name)

            for value in result["missing"]:

                test.log("FAIL: " + value)

    test.log("")
    test.log("================================================")

    if total_failed == 0:

        test.passes(
            "All English strings passed verification."
        )

    else:

        test.fail(
            "English string verification completed with failures."
        )


# ==========================================================
# MAIN TEST EXECUTION
# ==========================================================

def main():

    english_strings = load_english_strings()

    if not english_strings:

        test.fail(
            "No English strings available for verification."
        )

        return

    # ------------------------------------------------------
    # LOGIN SCREEN
    # ------------------------------------------------------

    test.log("Opening Login Screen")

    login_screen = waitForObject(
        names.o_ScreenSwitcher
    )

    verify_screen(
        "Login Screen",
        login_screen,
        english_strings
    )

    # ------------------------------------------------------
    # LOGIN NAVIGATION
    # ------------------------------------------------------

    test.log("Entering Login Credentials")

    sendEvent(
        "QMoveEvent",
        waitForObject(names.o_ScreenSwitcher),
        34, 208, 625, 226
    )

    clickButton(
        waitForObject(names.numpad_pushButton_4_QPushButton)
    )

    clickButton(
        waitForObject(names.numpad_pushButton_5_QPushButton)
    )

    clickButton(
        waitForObject(names.numpad_pushButton_4_QPushButton)
    )

    clickButton(
        waitForObject(names.numpad_pushButton_5_QPushButton)
    )

    clickButton(
        waitForObject(names.numpad_pushButton_8_QPushButton)
    )

    clickButton(
        waitForObject(names.numpad_pushButton_8_QPushButton)
    )

    clickButton(
        waitForObject(names.numpad_pushButton_8_QPushButton)
    )

    clickButton(
        waitForObject(names.numpad_pushButton_8_QPushButton)
    )

    clickButton(
        waitForObject(names.mainFrame_okButton_QPushButton)
    )

    snooze(2)

    # ------------------------------------------------------
    # HOME SCREEN
    # ------------------------------------------------------

    test.log("Opening Home Screen")

    home_screen = waitForObject(
        names.o_ScreenSwitcher
    )

    verify_screen(
        "Home Screen",
        home_screen,
        english_strings
    )

    # ------------------------------------------------------
    # LOGOFF NAVIGATION
    # ------------------------------------------------------

    test.log("Opening Logoff Dialog")

    clickButton(
        waitForObject(
            names.homeScreen_logoffButton_QPushButton
        )
    )

    snooze(2)

    # ------------------------------------------------------
    # LOGOFF DIALOG
    # ------------------------------------------------------

    logoff_screen = waitForObject(
        names.logOffSystem_centralWidget_QFrame
    )

    verify_screen(
        "Logoff Dialog",
        logoff_screen,
        english_strings
    )

    # ------------------------------------------------------
    # LOGOFF CONFIRMATION
    # ------------------------------------------------------

    test.log("Opening Logoff Confirmation")

    mouseClick(
        waitForObject(
            names.logOffSystem_centralWidget_QFrame
        ),
        849, 266,
        Qt.NoModifier,
        Qt.LeftButton
    )

    snooze(1)

    # ------------------------------------------------------
    # CONFIRMATION QUESTION
    # ------------------------------------------------------

    question_screen = waitForObject(
        names.centralWidget_questionLabel_QLabel
    )

    verify_screen(
        "Logoff Confirmation Question",
        question_screen,
        english_strings
    )

    mouseClick(
        waitForObject(
            names.centralWidget_questionLabel_QLabel
        ),
        602, 192,
        Qt.NoModifier,
        Qt.LeftButton
    )

    snooze(1)

    clickButton(
        waitForObject(
            names.buttonsFrame_acceptButton_QPushButton
        )
    )

    snooze(2)

    # ------------------------------------------------------
    # FINAL SUMMARY
    # ------------------------------------------------------

    show_summary()


# ==========================================================
# EXECUTE TEST
# ==========================================================

main()
