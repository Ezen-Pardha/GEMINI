
# -*- coding: utf-8 -*-

import names
import openpyxl
import re


# =========================================================
# Excel Path
# =========================================================

EXCEL_PATH = (
    "/home/ezen/Test_Automation_Gemini/Localisation/"
    "suite_GFL_Czech/"
    "tst_GEM-LOC-CZECH-Exit Quick Start-Guide/"
    "testdata/Gemini strings.xlsx"
)

# Column B = English
# Column M = Czech
ENGLISH_COLUMN = 2
CZECH_COLUMN = 13


# =========================================================
# Normalize Text
# =========================================================

def normalize(text):

    if text is None:
        return ""

    text = str(text)

    # Remove HTML tags
    text = re.sub(r"<[^>]+>", " ", text)

    # Normalize spaces
    text = " ".join(text.split())

    # Normalize angle brackets
    text = re.sub(r"\s*<\s*", " < ", text)
    text = re.sub(r"\s*>\s*", " > ", text)

    return text.strip().casefold()


# =========================================================
# Load Excel
# =========================================================

def load_excel():

    try:

        workbook = openpyxl.load_workbook(
            EXCEL_PATH,
            data_only=True
        )

        sheet = workbook.active

        return workbook, sheet

    except Exception as e:

        test.fail(
            "Unable to load Gemini Strings Excel: "
            + str(e)
        )

        return None, None


# =========================================================
# Get Czech Values
#
# Match English string in Column B.
# Return ALL corresponding Czech values from Column M.
#
# No Excel row numbers are hard-coded.
# =========================================================

def get_czech_values(sheet, english_text):

    expected_english = normalize(english_text)

    czech_values = []

    for row in range(2, sheet.max_row + 1):

        english_value = sheet.cell(
            row=row,
            column=ENGLISH_COLUMN
        ).value

        if english_value is None:
            continue

        if normalize(english_value) == expected_english:

            czech_value = sheet.cell(
                row=row,
                column=CZECH_COLUMN
            ).value

            if czech_value is not None:

                czech_value = str(
                    czech_value
                ).strip()

                if czech_value:
                    czech_values.append(
                        czech_value
                    )

    return czech_values


# =========================================================
# Verify Object Text Against Excel
# =========================================================

def verify_text(
    sheet,
    object_name,
    english_text,
    description
):

    snooze(6)

    try:

        obj = waitForObjectExists(
            object_name
        )

        actual_value = obj.text

        actual = ""

        if actual_value is not None:
            actual = str(
                actual_value
            ).strip()

    except Exception as e:

        test.fail(
            description
            + " | Unable to read object: "
            + str(e)
        )

        return


    expected_values = get_czech_values(
        sheet,
        english_text
    )


    if not expected_values:

        test.fail(
            description
            + " | English string not found in Column B: "
            + english_text
        )

        return


    actual_normalized = normalize(
        actual
    )


    # -----------------------------------------------------
    # Compare against all matching Czech values
    # -----------------------------------------------------

    for expected in expected_values:

        expected_normalized = normalize(
            expected
        )

        if actual_normalized == expected_normalized:

            test.compare(
                actual_normalized,
                expected_normalized,
                description
            )

            return


    # -----------------------------------------------------
    # Verification failed
    # -----------------------------------------------------

    test.fail(
        description
        + " | Expected Czech value from Column M: "
        + " / ".join(expected_values)
        + " | Actual: "
        + actual
    )


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

                    return central_widget

            except:
                pass

            snooze(0.5)

        return None

    except:

        return None


# =========================================================
# Main
# =========================================================

def main():

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

    doubleClick(
        waitForObject(
            names.numpad_pushButton_8_NumpadButton
        ),
        94,
        77,
        Qt.NoModifier,
        Qt.LeftButton
    )

    doubleClick(
        waitForObject(
            names.numpad_pushButton_8_NumpadButton
        ),
        94,
        77,
        Qt.NoModifier,
        Qt.LeftButton
    )

    clickButton(
        waitForObject(
            names.mainFrame_okButton_QPushButton
        )
    )


    # =====================================================
    # CHANGE LANGUAGE TO CZECH
    # =====================================================

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
            names.languagesFrame_pbCzech_QPushButton
        )
    )

    clickButton(
        waitForObject(
            names.buttonsFrame_acceptButton_QPushButton
        )
    )

    clickButton(
        waitForObject(
            names.buttonsBar_homeButton_QPushButton
        )
    )


    # =====================================================
    # SOFT TISSUE QUICK START
    # =====================================================

    clickButton(
        waitForObject(
            names.homeScreen_pbSoftTissueQuickStart_QToolButton
        )
    )

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

    clickButton(
        waitForObject(
            names.quickStartScreen_pbContinue_QPushButton
        )
    )

    clickButton(
        waitForObject(
            names.mainFrame_okButton_QPushButton_2
        )
    )


    # =====================================================
    # QUICK START EXIT POPUP
    # =====================================================

    mouseClick(
        waitForObject(
            names.modeButton_nameLabel_QLabel
        ),
        115,
        15,
        Qt.NoModifier,
        Qt.LeftButton
    )


    # Title
    verify_text(
        sheet,
        names.centralWidget_TitleLabel_QLabel_2,
        "EXIT QUICK START MODE?",
        "Quick Start Exit Title"
    )


    # Message
    verify_text(
        sheet,
        names.centralWidget_MessageLabel_QLabel_2,
        "Please confirm that you want to exit quick start mode.",
        "Quick Start Exit Message"
    )


    # Cancel
    verify_text(
        sheet,
        names.centralWidget_CancelButton_QPushButton_3,
        "CANCEL",
        "Quick Start Cancel Button"
    )


    # Confirm
    verify_text(
        sheet,
        names.centralWidget_DisableButton_QPushButton_2,
        "CONFIRM",
        "Quick Start Confirm Button"
    )


    # Confirm exit
    clickButton(
        waitForObject(
            names.centralWidget_DisableButton_QPushButton_2
        )
    )


    # =====================================================
    # RETURN HOME
    # =====================================================

    clickButton(
        waitForObject(
            names.buttonsBar_homeButton_QPushButton_2
        )
    )


    # =====================================================
    # SOFT TISSUE ASSISTANT
    # =====================================================

    clickButton(
        waitForObject(
            names.homeScreen_pbSoftTissueAssistant_QToolButton
        )
    )

    clickButton(
        waitForObject(
            names.gbSoftTissueProcedures_pbIncision_QPushButton
        )
    )

    clickButton(
        waitForObject(
            names.softTissueAssistantModeScreen_pbContinue_QPushButton
        )
    )


    # =====================================================
    # GUIDED MODE EXIT POPUP
    # =====================================================

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
    # GUIDED MODE POPUP VERIFICATION
    # =====================================================

    verify_text(
        sheet,
        names.centralWidget_TitleLabel_QLabel_2,
        "EXIT GUIDED MODE?",
        "Guided Mode Exit Title"
    )


    verify_text(
        sheet,
        names.centralWidget_MessageLabel_QLabel_2,
        "Please confirm that you want to exit guided mode.",
        "Guided Mode Exit Message"
    )


    verify_text(
        sheet,
        names.centralWidget_CancelButton_QPushButton_3,
        "CANCEL",
        "Guided Mode Cancel Button"
    )


    verify_text(
        sheet,
        names.centralWidget_DisableButton_QPushButton_2,
        "CONFIRM",
        "Guided Mode Confirm Button"
    )


    # =====================================================
    # CLOSE GUIDED MODE POPUP
    # =====================================================

    clickButton(
        waitForObject(
            names.centralWidget_DisableButton_QPushButton_2
        )
    )


    # =====================================================
    # CLOSE EXCEL
    # =====================================================

    workbook.close()
