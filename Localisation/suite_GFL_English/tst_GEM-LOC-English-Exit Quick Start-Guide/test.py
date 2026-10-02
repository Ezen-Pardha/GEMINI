
# -*- coding: utf-8 -*-

import names
import openpyxl
import re
from openpyxl import load_workbook


# =========================================================
# Excel Configuration
# =========================================================

EXCEL_PATH = (
    "/home/ezen/Test_Automation_Gemini/Localisation/"
    "suite_GFL_English/"
    "tst_GEM-LOC-English-PeakPower-SoftTissueCharacters/"
    "testdata/Gemini Split strings.xlsx"
)

# Excel:
# Column B = English

ENGLISH_COLUMN = 2

SHEET_NAME = "Soft tissue"


# =========================================================
# Normalize Text
# =========================================================

def normalize(text):

    if text is None:
        return ""

    text = str(text)

    # -----------------------------------------------------
    # Remove HTML tags
    # -----------------------------------------------------

    text = re.sub(
        r"<[^>]+>",
        " ",
        text
    )

    # -----------------------------------------------------
    # Normalize spaces and new lines
    # -----------------------------------------------------

    text = " ".join(
        text.split()
    )

    # -----------------------------------------------------
    # Normalize angle brackets
    # -----------------------------------------------------

    text = re.sub(
        r"\s*<\s*",
        " < ",
        text
    )

    text = re.sub(
        r"\s*>\s*",
        " > ",
        text
    )

    return text.strip().casefold()


# =========================================================
# Load Excel
# =========================================================

def load_excel():

    try:

        
        workbook = openpyxl.load_workbook(
            EXCEL_PATH,
            data_only=True,
            read_only=True
        )

        if SHEET_NAME not in workbook.sheetnames:

            test.fail(
                "Excel sheet not found: "
                + SHEET_NAME
                + " | Available sheets: "
                + str(workbook.sheetnames)
            )

            workbook.close()

            return None, None

        sheet = workbook[SHEET_NAME]

       

        return workbook, sheet

    except Exception as e:

        test.fail(
            "Unable to load English localization Excel: "
            + str(e)
        )

        return None, None


# =========================================================
# Find English Value in Column B
#
# The lookup text is used to locate the English value
# in Excel.
#
# No Excel row numbers are hard-coded.
# =========================================================

def get_english_value(
    sheet,
    english_text
):

    expected_english = normalize(
        english_text
    )

    if not expected_english:
        return None

    # -----------------------------------------------------
    # Search complete English Column B
    # -----------------------------------------------------

    for row in sheet.iter_rows(
        min_row=2,
        min_col=ENGLISH_COLUMN,
        max_col=ENGLISH_COLUMN
    ):

        english_value = row[0].value

        if english_value is None:
            continue

        english_value = str(
            english_value
        ).strip()

        if not english_value:
            continue

        # -------------------------------------------------
        # Exact normalized match
        # -------------------------------------------------

        if normalize(
            english_value
        ) == expected_english:

            return english_value

    return None


# =========================================================
# Verify Object Text Against English Excel
# =========================================================

def verify_text(
    sheet,
    object_name,
    english_text,
    description
):

    # -----------------------------------------------------
    # Wait before every verification
    # -----------------------------------------------------

    snooze(6)

    # -----------------------------------------------------
    # Get object
    # -----------------------------------------------------

    try:

        obj = waitForObjectExists(
            object_name
        )

    except Exception as e:

        test.fail(
            description
            + " | Unable to find object: "
            + str(e)
        )

        return False

    # -----------------------------------------------------
    # Get actual UI text
    # -----------------------------------------------------

    try:

        actual_value = obj.text

        actual = ""

        if actual_value is not None:

            actual = str(
                actual_value
            ).strip()

    except Exception as e:

        test.fail(
            description
            + " | Unable to read object text: "
            + str(e)
        )

        return False

    # -----------------------------------------------------
    # UI text empty
    # -----------------------------------------------------

    if not actual:

        test.fail(
            description
            + " | UI text is empty"
        )

        return False

    # -----------------------------------------------------
    # Find English value in Excel Column B
    # -----------------------------------------------------

    expected_value = get_english_value(
        sheet,
        english_text
    )

    # -----------------------------------------------------
    # English string not found
    # -----------------------------------------------------

    if expected_value is None:

        test.fail(
            description
            + " | English string not found in Column B: "
            + english_text
        )

        return False

    # -----------------------------------------------------
    # Normalize actual and expected
    # -----------------------------------------------------

    actual_normalized = normalize(
        actual
    )

    expected_normalized = normalize(
        expected_value
    )

    # -----------------------------------------------------
    # Compare
    # -----------------------------------------------------

    test.compare(
        actual_normalized,
        expected_normalized,
        description
    )

    # -----------------------------------------------------
    # Log result
    # -----------------------------------------------------

    if actual_normalized == expected_normalized:

        test.log(
            description
            + " | PASS"
            + " | English: "
            + expected_value
        )

        return True

    else:

        test.fail(
            description
            + " | Expected English value: "
            + expected_value
            + " | Actual: "
            + actual
        )

        return False


# =========================================================
# Get Visible centralWidget
# =========================================================

def get_central_widget():

    try:

        central_widget = findObject(
            {
                "name": "centralWidget",
                "type": "QFrame",
                "window": ":o_ScreenSwitcher"
            }
        )

        for i in range(20):

            try:

                if central_widget.visible:

                    test.log(
                        "centralWidget is visible"
                    )

                    return central_widget

            except:

                pass

            snooze(0.5)

        test.log(
            "centralWidget was found but is not visible"
        )

        return None

    except Exception as e:

        test.log(
            "centralWidget not found: "
            + str(e)
        )

        return None


# =========================================================
# Main
# =========================================================

def main():

    # =====================================================
    # LOAD EXCEL
    # =====================================================

    workbook, sheet = load_excel()

    if workbook is None or sheet is None:

        return


    # =====================================================
    # LOGIN
    # =====================================================

    

    clickButton(
        waitForObject(
            names.numpad_pushButton_8_NumpadButton
        )
    )

    snooze(2)

    doubleClick(
        waitForObject(
            names.numpad_pushButton_8_NumpadButton
        ),
        94,
        77,
        Qt.NoModifier,
        Qt.LeftButton
    )

    snooze(2)

    doubleClick(
        waitForObject(
            names.numpad_pushButton_8_NumpadButton
        ),
        94,
        77,
        Qt.NoModifier,
        Qt.LeftButton
    )

    snooze(2)

    clickButton(
        waitForObject(
            names.mainFrame_okButton_QPushButton
        )
    )


    # =====================================================
    # ENGLISH LANGUAGE
    # =====================================================
    #
    # The application is already in English.
    #
    # No language settings are opened.
    # No Denmark/Czech language button is clicked.
    #
    # =====================================================


    # =====================================================
    # SOFT TISSUE QUICK START
    # =====================================================

    snooze(6)

    clickButton(
        waitForObject(
            names.homeScreen_pbSoftTissueQuickStart_QToolButton
        )
    )


    # =====================================================
    # SELECT LEFT PRESET
    # =====================================================

    snooze(6)

    mouseClick(
        waitForObjectItem(
            names.tabLeftMainPresets_leftPresetsView_PresetListView,
            "_1"
        ),
        377,
        65,
        Qt.NoModifier,
        Qt.LeftButton
    )


    # =====================================================
    # SELECT RIGHT PRESET
    # =====================================================

    snooze(6)

    mouseClick(
        waitForObjectItem(
            names.tabRightMainPresets_rightPresetsView_PresetListView,
            "_1"
        ),
        150,
        37,
        Qt.NoModifier,
        Qt.LeftButton
    )


    # =====================================================
    # MOVE SCREEN
    # =====================================================

    snooze(6)

    sendEvent(
        "QMoveEvent",
        waitForObject(
            names.o_ScreenSwitcher
        ),
        0,
        -50,
        1288,
        292
    )


    # =====================================================
    # QUICK START CONTINUE
    # =====================================================

    snooze(6)

    clickButton(
        waitForObject(
            names.quickStartScreen_pbContinue_QPushButton
        )
    )

    snooze(6)

    clickButton(
        waitForObject(
            names.mainFrame_okButton_QPushButton_2
        )
    )


    # =====================================================
    # QUICK START EXIT POPUP
    # =====================================================

    snooze(6)

    mouseClick(
        waitForObject(
            names.modeButton_nameLabel_QLabel
        ),
        115,
        15,
        Qt.NoModifier,
        Qt.LeftButton
    )


    # =====================================================
    # QUICK START EXIT TITLE
    # =====================================================

    verify_text(
        sheet,
        names.centralWidget_TitleLabel_QLabel_2,
        "EXIT QUICK START MODE?",
        "Quick Start Exit Title"
    )


    # =====================================================
    # QUICK START EXIT MESSAGE
    # =====================================================

    verify_text(
        sheet,
        names.centralWidget_MessageLabel_QLabel_2,
        "Please confirm that you want to exit quick start mode.",
        "Quick Start Exit Message"
    )


    # =====================================================
    # QUICK START CANCEL
    # =====================================================

    verify_text(
        sheet,
        names.centralWidget_CancelButton_QPushButton_3,
        "CANCEL",
        "Quick Start Cancel Button"
    )


    # =====================================================
    # QUICK START CONFIRM
    # =====================================================

    verify_text(
        sheet,
        names.centralWidget_DisableButton_QPushButton_2,
        "CONFIRM",
        "Quick Start Confirm Button"
    )


    # =====================================================
    # CONFIRM EXIT
    # =====================================================

    snooze(6)

    clickButton(
        waitForObject(
            names.centralWidget_DisableButton_QPushButton_2
        )
    )


    # =====================================================
    # RETURN HOME
    # =====================================================

    snooze(6)

    clickButton(
        waitForObject(
            names.buttonsBar_homeButton_QPushButton_2
        )
    )


    # =====================================================
    # SOFT TISSUE ASSISTANT
    # =====================================================

    snooze(6)

    clickButton(
        waitForObject(
            names.homeScreen_pbSoftTissueAssistant_QToolButton
        )
    )


    # =====================================================
    # INCISION
    # =====================================================

    snooze(6)

    clickButton(
        waitForObject(
            names.gbSoftTissueProcedures_pbIncision_QPushButton
        )
    )


    # =====================================================
    # CONTINUE
    # =====================================================

    snooze(6)

    clickButton(
        waitForObject(
            names.softTissueAssistantModeScreen_pbContinue_QPushButton
        )
    )


    # =====================================================
    # GUIDED MODE EXIT
    # =====================================================

    snooze(6)

    mouseDrag(
        waitForObject(
            names.indexPicker_valuePicker_IntervalSlider
        ),
        195,
        15,
        211,
        29,
        1,
        Qt.LeftButton
    )


    # =====================================================
    # GUIDED MODE EXIT TITLE
    # =====================================================

    verify_text(
        sheet,
        names.centralWidget_TitleLabel_QLabel_2,
        "EXIT GUIDED MODE?",
        "Guided Mode Exit Title"
    )


    # =====================================================
    # GUIDED MODE EXIT MESSAGE
    # =====================================================

    verify_text(
        sheet,
        names.centralWidget_MessageLabel_QLabel_2,
        "Please confirm that you want to exit guided mode.",
        "Guided Mode Exit Message"
    )


    # =====================================================
    # GUIDED MODE CANCEL
    # =====================================================

    verify_text(
        sheet,
        names.centralWidget_CancelButton_QPushButton_3,
        "CANCEL",
        "Guided Mode Cancel Button"
    )


    # =====================================================
    # GUIDED MODE CONFIRM
    # =====================================================

    verify_text(
        sheet,
        names.centralWidget_DisableButton_QPushButton_2,
        "CONFIRM",
        "Guided Mode Confirm Button"
    )


    # =====================================================
    # CLOSE GUIDED MODE POPUP
    # =====================================================

    snooze(6)

    clickButton(
        waitForObject(
            names.centralWidget_DisableButton_QPushButton_2
        )
    )


    # =====================================================
    # CLOSE EXCEL
    # =====================================================

    try:

        workbook.close()

    except:

        pass


    test.log(
        "English Soft Tissue localization verification completed"
    )
