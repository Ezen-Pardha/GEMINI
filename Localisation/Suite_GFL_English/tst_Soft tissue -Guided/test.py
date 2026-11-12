
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

SHEET_NAME = "Soft Tissue-Guided"
ENGLISH_COLUMN = 2



def normalize(text):

    text = str(text or "")

    text = re.sub(
        r"<br\s*/?>",
        " ",
        text,
        flags=re.IGNORECASE
    )

    text = re.sub(r"<[^>]+>", "", text)

    text = text.replace("\u00a0", " ")

    text = " ".join(text.split())

    return text.strip().casefold()




def ignore_text(text):

    text = normalize(text)

    if not text:
        return True

    if re.fullmatch(r"[-_=.<>/%µμ:+]+", text):
        return True

    if re.fullmatch(r"[\d\s.,:+\-/<>=%µμ]+", text):
        return True

    return False



def get_all_texts(obj):

    texts = []

    try:
        if not obj.visible:
            return texts
    except:
        pass

    for attr in ("text", "title"):

        try:
            value = getattr(obj, attr)

            if value is not None:

                value = str(value).strip()

                if value and value.lower() not in (
                    "none",
                    "null"
                ):
                    texts.append(value)

        except:
            pass

    try:

        for child in object.children(obj):

            texts.extend(
                get_all_texts(child)
            )

    except:
        pass

    return texts



def load_english_strings():

    workbook = openpyxl.load_workbook(
        EXCEL_PATH,
        data_only=True,
        read_only=True
    )

    try:

        if SHEET_NAME not in workbook.sheetnames:

            test.fail(
                "Worksheet not found: " + SHEET_NAME
            )

            return {}

        sheet = workbook[SHEET_NAME]

        excel_strings = {}

        for row in sheet.iter_rows(
            min_row=2,
            values_only=True
        ):

            if len(row) < ENGLISH_COLUMN:
                continue

            english_value = row[ENGLISH_COLUMN - 1]

            if english_value is None:
                continue

            english = str(english_value).strip()

            if ignore_text(english):
                continue

            key = normalize(english)

            if key and key not in excel_strings:

                excel_strings[key] = english

        test.log(
            "Total English strings loaded: {}".format(
                len(excel_strings)
            )
        )

        return excel_strings

    finally:

        workbook.close()




def is_string_present(expected, actual_texts):

    expected = normalize(expected)

    if not expected:
        return False


    for actual in actual_texts:

        actual = normalize(actual)

        if not actual:
            continue

        # Exact match
        if expected == actual:
            return True

        pattern = (
            r"(?<!\w)"
            + re.escape(expected)
            + r"(?!\w)"
        )

        if re.search(pattern, actual):
            return True

    return False




def main():

    if not os.path.exists(EXCEL_PATH):

        test.fail(
            "Excel file not found: " + EXCEL_PATH
        )

        return

    excel_strings = load_english_strings()

    if not excel_strings:

        test.fail("No English strings found in Excel")

        return

    # LOGIN
 

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

   
  

    clickButton(
        waitForObject(
            names.homeScreen_pbSoftTissueAssistant_QToolButton
        )
    )

    snooze(1)

    mouseClick(
        waitForObject(
            names.gbSoftTissueProcedures_lbSoftTissueProcedures_QLabel
        ),
        516, 9,
        Qt.NoModifier,
        Qt.LeftButton
    )

    mouseClick(
        waitForObject(
            names.softTissueAssistantModeScreen_gbSoftTissueProcedures_QFrame
        ),
        166, 197,
        Qt.NoModifier,
        Qt.LeftButton
    )

    mouseClick(
        waitForObject(
            names.softTissueAssistantModeScreen_gbBphProcedures_QFrame
        ),
        439, 14,
        Qt.NoModifier,
        Qt.LeftButton
    )

    mouseClick(
        waitForObject(
            names.softTissueAssistantModeScreen_gbBphProcedures_QFrame
        ),
        633, 11,
        Qt.NoModifier,
        Qt.LeftButton
    )

    snooze(1)

   

    soft_tissue = waitForObject(
        names.softTissueAssistantModeScreen_SoftTissueAssistantModeScreen
    )

    actual_texts = get_all_texts(soft_tissue)



    test.log("")
    test.log("========== ACTUAL SCREEN TEXTS ==========")

    for text in sorted(set(actual_texts)):

        test.log(
            "SCREEN TEXT: {}".format(text)
        )

    test.log("=========================================")

  

    total_pass = 0
    total_fail = 0

    test.log("")
    test.log("======================================")
    test.log("ENGLISH SOFT TISSUE STRING VERIFICATION")
    test.log("======================================")

    for key, english in sorted(excel_strings.items()):

        if is_string_present(english, actual_texts):

            test.passes(
                "PASS: English string verified: {}".format(
                    english
                )
            )

            total_pass += 1

        else:

            test.fail(
                "FAIL: English string not found on screen: {}".format(
                    english
                )
            )

            total_fail += 1

    # --------------------------------------------------
    # SUMMARY
    # --------------------------------------------------

    test.log("")
    test.log("======================================")
    test.log("ENGLISH LOCALIZATION SUMMARY")
    test.log("======================================")

    test.log(
        "Total Excel strings: {}".format(
            len(excel_strings)
        )
    )

    test.log(
        "Total PASS: {}".format(total_pass)
    )

    test.log(
        "Total FAIL: {}".format(total_fail)
    )

    if total_fail > 0:

        test.fail(
            "ENGLISH SOFT TISSUE VALIDATION FAILED: "
            "{} strings not found".format(total_fail)
        )

    else:

        test.passes(
            "ENGLISH SOFT TISSUE VALIDATION PASSED: "
            "{} strings verified".format(total_pass)
        )


main()
