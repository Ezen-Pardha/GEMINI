
# -*- coding: utf-8 -*-

import names
import openpyxl
import os
import re
import html



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
RESULT_SHEET = "Verification Results"

verified_results = []



STRING_OBJECTS = {
    "SYSTEM": [
        "wdSystemSettingsLayout_0_QLabel"
    ],

    "SYSTEM SETTINGS": [
        "systemsettingframe_label_QLabel"
    ],

    "SCREEN BRIGHTNESS": [
        "systemsettingframe_lbBrightnessName_QLabel"
    ],

    "VOLUME": [
        "systemsettingframe_lbVolumeName_QLabel"
    ],

    "AIMING BEAM SETTINGS": [
        "aimingbeamsettingframe_label_2_QLabel"
    ],

    "MODE": [
        "aimingbeamsettingframe_lbAimingBeamDefaultModeName_QLabel"
    ],

    "ENABLED": [
        "aimingbeamsettingframe_gbAimingBeamDefaultLevel_QWidget"
    ],

    "DISABLED": [
        "aimingbeamsettingframe_gbAimingBeamDefaultLevel_QWidget"
    ],

    "INTENSITY LEVEL": [
        "aimingbeamsettingframe_gbAimingBeamDefaultLevel_QWidget"
    ],

    "BACK": [
        "settingsScreen_pbBack_QPushButton"
    ]
}



def normalize(value):

    if value is None:
        return ""

    value = html.unescape(str(value))
    value = re.sub(r"<[^>]+>", "", value)
    value = re.sub(r"\s+", " ", value)

    return value.strip().casefold()




def load_english_strings():

    if not os.path.exists(EXCEL_PATH):
        test.fail("Excel file not found: " + EXCEL_PATH)
        return set()

    try:
        workbook = openpyxl.load_workbook(
            EXCEL_PATH,
            data_only=True
        )

        if SHEET_NAME not in workbook.sheetnames:
            workbook.close()
            test.fail("Settings worksheet not found in Excel")
            return set()

        worksheet = workbook[SHEET_NAME]

        reference_strings = set()

        for row in range(1, worksheet.max_row + 1):

            value = worksheet.cell(
                row=row,
                column=ENGLISH_COLUMN
            ).value

            value = normalize(value)

            if value:
                reference_strings.add(value)

        workbook.close()

        return reference_strings

    except Exception as error:
        test.fail("Excel reading error: {}".format(error))
        return set()




def read_text(obj):

    values = []

    properties = [
        "text",
        "title",
        "windowTitle",
        "accessibleName",
        "accessibleDescription",
        "toolTip",
        "currentText"
    ]

    for prop in properties:

        try:
            value = obj.property(prop)

            if value is not None and str(value).strip():
                values.append(str(value))

        except:
            pass

        try:
            value = getattr(obj, prop)

            if callable(value):
                value = value()

            if value is not None and str(value).strip():
                values.append(str(value))

        except:
            pass

    return values




def collect_text(obj, result, depth=0):

    if depth > 15:
        return

    for value in read_text(obj):

        normalized = normalize(value)

        if normalized:
            result.add(normalized)

    try:
        children = obj.children()

        for child in children:
            collect_text(child, result, depth + 1)

    except:
        pass



def verify_string(expected, object_names, reference_strings):

    actual_text = set()

    for object_name in object_names:

        try:
            obj = waitForObjectExists(
                getattr(names, object_name)
            )

            collect_text(obj, actual_text)

        except Exception:
            pass

    expected_normalized = normalize(expected)

    if expected_normalized in actual_text:

        test.passes(
            "English string verified: {}".format(expected)
        )

        result = "PASS"

    else:

        test.fail(
            "English string not verified: {}".format(expected)
        )

        result = "FAIL"

    if expected_normalized not in reference_strings:
        test.log(
            "Reference missing in Excel: {}".format(expected)
        )

    verified_results.append([
        "SYSTEM",
        expected,
        result
    ])


# --------------------------------------------------
# VERIFY SYSTEM SETTINGS SCREEN
# --------------------------------------------------

def verify_system_screen(reference_strings):

    global verified_results

    verified_results = []

    for expected, object_names in STRING_OBJECTS.items():

        verify_string(
            expected,
            object_names,
            reference_strings
        )


# --------------------------------------------------
# SAVE RESULTS TO EXCEL
# --------------------------------------------------

def save_results_to_excel():

    try:

        workbook = openpyxl.load_workbook(EXCEL_PATH)

        if RESULT_SHEET in workbook.sheetnames:
            del workbook[RESULT_SHEET]

        worksheet = workbook.create_sheet(RESULT_SHEET)

        worksheet.append([
            "Screen",
            "English String",
            "Result"
        ])

        for result in verified_results:
            worksheet.append(result)

        total = len(verified_results)

        passed = sum(
            1 for row in verified_results
            if row[2] == "PASS"
        )

        failed = total - passed

        worksheet.append([])
        worksheet.append(["VERIFICATION SUMMARY"])
        worksheet.append(["Total Checked", total])
        worksheet.append(["PASS", passed])
        worksheet.append(["FAIL", failed])

        worksheet.column_dimensions["A"].width = 20
        worksheet.column_dimensions["B"].width = 35
        worksheet.column_dimensions["C"].width = 15

        workbook.save(EXCEL_PATH)
        workbook.close()

        test.log("Excel verification results saved successfully")

    except Exception as error:

        test.fail(
            "Unable to save Excel results: {}".format(error)
        )


# --------------------------------------------------
# MAIN
# --------------------------------------------------

def main():

    reference_strings = load_english_strings()

    # Login
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

    snooze(2)

    # Open Settings
    clickButton(
        waitForObject(names.homeScreen_settingsButton_QPushButton)
    )

    snooze(2)

    # Select SYSTEM tab
    clickTab(
        waitForObject(names.settingsScreen_tbSystemInfo_TabWidget),
        "SYSTEM"
    )

    snooze(2)

    # Verify screen strings
    verify_system_screen(reference_strings)

    # Click Back after verification
    clickButton(
        waitForObject(names.settingsScreen_pbBack_QPushButton)
    )

    # Save Excel results
    save_results_to_excel()
