
# -*- coding: utf-8 -*-

import names
import openpyxl
import re
from openpyxl import load_workbook


# ============================================================
# EXCEL CONFIGURATION
# ============================================================

EXCEL_PATH = (
    "/home/ezen/Test_Automation_Gemini/Localisation/"
    "suite_GFL_English/tst_GEM-LOC-English-PeakPower-SoftTissueCharacters/"
    "testdata/Gemini Split strings.xlsx"
)

# Gemini Split strings.xlsx
# Column B = English
ENGLISH_COLUMN = 2

SHEET_NAME = "Treatment Modes"


# ============================================================
# GLOBALS
# ============================================================

workbook = None
sheet = None


# ============================================================
# GET OBJECT TEXT
# ============================================================

def get_object_text(obj):

    # --------------------------------------------------------
    # text
    # --------------------------------------------------------

    try:
        value = obj.text

        if value is not None:
            value = str(value)

            if value.strip():
                return value

    except:
        pass


    # --------------------------------------------------------
    # title
    # --------------------------------------------------------

    try:
        value = obj.title

        if value is not None:
            value = str(value)

            if value.strip():
                return value

    except:
        pass


    # --------------------------------------------------------
    # windowTitle
    # --------------------------------------------------------

    try:
        value = obj.windowTitle

        if value is not None:
            value = str(value)

            if value.strip():
                return value

    except:
        pass


    # --------------------------------------------------------
    # accessibleName
    # --------------------------------------------------------

    try:
        value = obj.accessibleName

        if value is not None:
            value = str(value)

            if value.strip():
                return value

    except:
        pass


    return ""


# ============================================================
# NORMALIZE TEXT
# ============================================================

def normalize_text(text):

    if text is None:
        return ""

    text = str(text)


    # --------------------------------------------------------
    # Remove HTML/XML tags
    # --------------------------------------------------------

    text = re.sub(
        r"<[^>]*>",
        " ",
        text
    )


    # --------------------------------------------------------
    # Normalize special spaces
    # --------------------------------------------------------

    text = text.replace(
        "\u00A0",
        " "
    )

    text = text.replace(
        "\u2007",
        " "
    )

    text = text.replace(
        "\u202F",
        " "
    )


    # --------------------------------------------------------
    # Normalize line breaks and tabs
    # --------------------------------------------------------

    text = re.sub(
        r"[\r\n\t]+",
        " ",
        text
    )


    # --------------------------------------------------------
    # Remove trademark/copyright symbols
    # --------------------------------------------------------

    text = text.replace(
        "™",
        ""
    )

    text = text.replace(
        "®",
        ""
    )

    text = text.replace(
        "©",
        ""
    )


    # --------------------------------------------------------
    # Normalize Unicode
    # --------------------------------------------------------

    try:

        import unicodedata

        text = unicodedata.normalize(
            "NFKC",
            text
        )

    except:
        pass


    # --------------------------------------------------------
    # Normalize multiple spaces
    # --------------------------------------------------------

    text = re.sub(
        r"\s+",
        " ",
        text
    )


    # --------------------------------------------------------
    # Remove spaces before punctuation
    # --------------------------------------------------------

    text = re.sub(
        r"\s+([.,;:!?])",
        r"\1",
        text
    )


    # --------------------------------------------------------
    # Final normalization
    # --------------------------------------------------------

    return text.strip().casefold()


# ============================================================
# FIND ENGLISH TEXT IN COLUMN B
# ============================================================

def find_english_text(actual_text):

    if sheet is None:
        return None

    actual_normalized = normalize_text(
        actual_text
    )

    if not actual_normalized:
        return None


    # --------------------------------------------------------
    # Search complete English Column B
    # --------------------------------------------------------

    for row in sheet.iter_rows(
        min_row=2,
        min_col=ENGLISH_COLUMN,
        max_col=ENGLISH_COLUMN
    ):

        english_value = row[0].value

        if english_value is None:
            continue

        english_normalized = normalize_text(
            english_value
        )

        if not english_normalized:
            continue


        # ----------------------------------------------------
        # Exact normalized match
        # ----------------------------------------------------

        if actual_normalized == english_normalized:
            return english_value


    return None


# ============================================================
# VERIFY TEXT AGAINST ENGLISH COLUMN B
# ============================================================

def verify_text(object_name, description):

    # --------------------------------------------------------
    # Wait before every verification
    # --------------------------------------------------------

    snooze(6)


    # --------------------------------------------------------
    # Get object
    # --------------------------------------------------------

    try:

        obj = waitForObject(
            object_name
        )

    except Exception as e:

        test.fail(
            description
            + " | Object not found: "
            + str(e)
        )

        return False


    # --------------------------------------------------------
    # Get actual UI text
    # --------------------------------------------------------

    actual_text = get_object_text(
        obj
    )


    if not actual_text:

        test.fail(
            description
            + " | UI text is empty"
        )

        return False


    # --------------------------------------------------------
    # Search actual English text in Column B
    # --------------------------------------------------------

    matched_english = find_english_text(
        actual_text
    )


    # --------------------------------------------------------
    # Match found
    # --------------------------------------------------------

    if matched_english is not None:

        actual_normalized = normalize_text(
            actual_text
        )

        expected_normalized = normalize_text(
            matched_english
        )

        test.compare(
            actual_normalized,
            expected_normalized,
            description
        )

        return True


    # --------------------------------------------------------
    # Match not found
    # --------------------------------------------------------

    test.fail(
        description
        + " | English text not found in Column B: "
        + str(actual_text)
    )

    return False


# ============================================================
# VERIFY GROUP
# ============================================================

def verify_group(group_name):

    for object_name, description in verification_objects[group_name]:

        verify_text(
            object_name,
            description
        )


# ============================================================
# VERIFY POPUP
# ============================================================

def verify_popup(group_name):

    verify_group(
        group_name
    )

    snooze(6)

    clickButton(
        waitForObject(
            names.centralWidget_OKButton_QPushButton
        )
    )


# ============================================================
# VERIFICATION OBJECTS
# ============================================================

verification_objects = {


    # ========================================================
    # MAIN MODE SCREEN
    # ========================================================

    "main": [

        (
            names.centralWidget_lbTitle_QLabel,
            "Mode Selection Title"
        ),

        (
            names.centralWidget_label_2_QLabel,
            "Standard Mode Label"
        ),

        (
            names.centralWidget_Square_QPushButton,
            "Standard Pulse Button"
        ),

        (
            names.centralWidget_CW_QPushButton,
            "Continuous Wave Button"
        ),

        (
            names.centralWidget_MRP_QPushButton,
            "MRP Button"
        ),

        (
            names.centralWidget_label_QLabel,
            "Expert Mode Label"
        ),

        (
            names.centralWidget_Fragmentation_QPushButton,
            "Fragmentation Pulse Button"
        ),

        (
            names.centralWidget_Cleaning_QPushButton,
            "Cleaning Pulse Button"
        ),

        (
            names.centralWidget_Enucleation_QPushButton,
            "Enucleation Pulse Button"
        ),

        (
            names.buttonsFrame_rejectButton_QPushButton,
            "Cancel Button"
        )
    ],


    # ========================================================
    # STANDARD PULSE POPUP
    # ========================================================

    "standard_pulse": [

        (
            names.centralWidget_TitleLabel_QLabel_3,
            "Standard Pulse Popup Title"
        ),

        (
            names.centralWidget_MessageLabel_QLabel_3,
            "Standard Pulse Popup Message"
        ),

        (
            names.centralWidget_OKButton_QPushButton,
            "Standard Pulse Popup OK Button"
        )
    ],


    # ========================================================
    # CONTINUOUS WAVE POPUP
    # ========================================================

    "cw": [

        (
            names.centralWidget_TitleLabel_QLabel_3,
            "Continuous Wave Popup Title"
        ),

        (
            names.centralWidget_MessageLabel_QLabel_3,
            "Continuous Wave Popup Message"
        ),

        (
            names.centralWidget_OKButton_QPushButton,
            "Continuous Wave Popup OK Button"
        )
    ],


    # ========================================================
    # MRP POPUP
    # ========================================================

    "mrp": [

        (
            names.centralWidget_TitleLabel_QLabel_3,
            "MRP Popup Title"
        ),

        (
            names.centralWidget_MessageLabel_QLabel_3,
            "MRP Popup Message"
        ),

        (
            names.centralWidget_OKButton_QPushButton,
            "MRP Popup OK Button"
        )
    ],


    # ========================================================
    # FRAGMENTATION POPUP
    # ========================================================

    "fragmentation": [

        (
            names.centralWidget_TitleLabel_QLabel_3,
            "Fragmentation Popup Title"
        ),

        (
            names.centralWidget_MessageLabel_QLabel_3,
            "Fragmentation Popup Message"
        ),

        (
            names.centralWidget_OKButton_QPushButton,
            "Fragmentation Popup OK Button"
        )
    ],


    # ========================================================
    # CLEANING POPUP
    # ========================================================

    "cleaning": [

        (
            names.centralWidget_TitleLabel_QLabel_3,
            "Cleaning Popup Title"
        ),

        (
            names.centralWidget_MessageLabel_QLabel_3,
            "Cleaning Popup Message"
        ),

        (
            names.centralWidget_OKButton_QPushButton,
            "Cleaning Popup OK Button"
        )
    ],


    # ========================================================
    # ENUCLEATION POPUP
    # ========================================================

    "enucleation": [

        (
            names.centralWidget_TitleLabel_QLabel_3,
            "Enucleation Popup Title"
        ),

        (
            names.centralWidget_MessageLabel_QLabel_3,
            "Enucleation Popup Message"
        ),

        (
            names.centralWidget_OKButton_QPushButton,
            "Enucleation Popup OK Button"
        )
    ]
}


# ============================================================
# MAIN
# ============================================================

def main():

    global workbook
    global sheet


    # ========================================================
    # LOGIN
    # ========================================================

    # test.log(
    #     "Entering login PIN"
    # )

    doubleClick(
        waitForObject(
            names.numpad_pushButton_8_NumpadButton
        ),
        91,
        77,
        Qt.NoModifier,
        Qt.LeftButton
    )

    snooze(6)

    clickButton(
        waitForObject(
            names.numpad_pushButton_8_NumpadButton
        )
    )

    snooze(6)

    clickButton(
        waitForObject(
            names.numpad_pushButton_8_NumpadButton
        )
    )

    snooze(6)

    clickButton(
        waitForObject(
            names.mainFrame_okButton_QPushButton
        )
    )


    # ========================================================
    # OPEN SETTINGS
    # ========================================================

    snooze(6)

    # test.log(
    #     "Opening Settings"
    # )

    clickButton(
        waitForObject(
            names.homeScreen_settingsButton_QPushButton
        )
    )


    # ========================================================
    # OPEN INFO
    # ========================================================
    #
    # The application is already in English.
    # No language-selection step is required.
    #
    # ========================================================

    snooze(6)

    clickTab(
        waitForObject(
            names.settingsScreen_tbSystemInfo_TabWidget
        ),
        "INFO"
    )


    # ========================================================
    # RETURN HOME
    # ========================================================

    snooze(6)

    clickButton(
        waitForObject(
            names.buttonsBar_homeButton_QPushButton
        )
    )


    # ========================================================
    # EXPERT MODE
    # ========================================================

    snooze(6)

    clickButton(
        waitForObject(
            names.gbExpert_expertButton_QPushButton
        )
    )


    # ========================================================
    # OPEN MODE SELECTION
    # ========================================================

    snooze(6)

    mouseClick(
        waitForObject(
            names.modeButton_nameLabel_QLabel
        ),
        73,
        25,
        Qt.NoModifier,
        Qt.LeftButton
    )


    # ========================================================
    # LOAD ENGLISH EXCEL
    # ========================================================

    snooze(2)

    # test.log(
    #     "Loading English Gemini Split strings"
    # )

    try:

        workbook = load_workbook(
            EXCEL_PATH,
            read_only=True,
            data_only=True
        )

    except Exception as e:

        test.fail(
            "Failed to load English Gemini Split strings Excel: "
            + str(e)
        )

        return


    # ========================================================
    # CHECK SHEET
    # ========================================================

    if SHEET_NAME not in workbook.sheetnames:

        test.fail(
            "Worksheet '" +
            SHEET_NAME +
            "' does not exist. Available sheets: " +
            str(workbook.sheetnames)
        )

        workbook.close()

        return


    # ========================================================
    # GET TREATMENT MODES SHEET
    # ========================================================

    sheet = workbook[
        SHEET_NAME
    ]


    # ========================================================
    # MAIN SCREEN VERIFICATION
    # ========================================================

    verify_group(
        "main"
    )


    # ========================================================
    # STANDARD PULSE POPUP
    # ========================================================

    snooze(6)

    clickButton(
        waitForObject(
            names.square_icon_QPushButton
        )
    )

    verify_popup(
        "standard_pulse"
    )


    # ========================================================
    # CONTINUOUS WAVE POPUP
    # ========================================================

    snooze(6)

    clickButton(
        waitForObject(
            names.cW_icon_QPushButton
        )
    )

    verify_popup(
        "cw"
    )


    # ========================================================
    # MRP POPUP
    # ========================================================

    snooze(6)

    clickButton(
        waitForObject(
            names.mRP_icon_QPushButton
        )
    )

    verify_popup(
        "mrp"
    )


    # ========================================================
    # FRAGMENTATION POPUP
    # ========================================================

    snooze(6)

    clickButton(
        waitForObject(
            names.fragmentation_icon_QPushButton
        )
    )

    verify_popup(
        "fragmentation"
    )


    # ========================================================
    # CLEANING POPUP
    # ========================================================

    snooze(6)

    clickButton(
        waitForObject(
            names.cleaning_icon_QPushButton
        )
    )

    verify_popup(
        "cleaning"
    )


    # ========================================================
    # ENUCLEATION POPUP
    # ========================================================

    snooze(6)

    clickButton(
        waitForObject(
            names.enucleation_icon_QPushButton
        )
    )

    verify_popup(
        "enucleation"
    )


    # ========================================================
    # CANCEL MODE SELECTION
    # ========================================================

    snooze(6)

    clickButton(
        waitForObject(
            names.buttonsFrame_rejectButton_QPushButton
        )
    )


    # ========================================================
    # CLOSE EXCEL
    # ========================================================

    try:

        if workbook is not None:
            workbook.close()

    except:

        pass


    test.log(
        "English Treatment Modes localization verification completed"
    )

