# -*- coding: utf-8 -*-

import names
from openpyxl import load_workbook

# ============================================================

# EXCEL CONFIGURATION

# ============================================================

EXCEL_PATH = ("/home/ezen/Test_Automation_Gemini/Localisation/suite_GFL_Dutch/tst_GEM-LOC-Dutch-PeakPower-SoftTissueCharacters/testdata/Gemini Split strings.xlsx")

EXCEL_SHEET_NAME = "Treatment Modes"

# Column B = English

ENGLISH_COLUMN = 2

# Column G = Dutch

DUTCH_COLUMN = 7

# ============================================================

# TEXT NORMALIZATION

# ============================================================

def normalize_text(value):


    if value is None:
        return ""
    
    return " ".join(
        str(value)
        .replace("\n", " ")
        .replace("\r", " ")
        .split()
    ).strip().casefold()
    
    
# ============================================================

# GET DUTCH TEXT FROM EXCEL

# ============================================================

def get_dutch_text(sheet, english_text):


    search_text = normalize_text(
        english_text
    )
    
    for row in sheet.iter_rows(
        min_row=1,
        min_col=ENGLISH_COLUMN,
        max_col=DUTCH_COLUMN,
        values_only=True
    ):
    
        english_value = row[0]
    
        if normalize_text(
            english_value
        ) == search_text:
    
            dutch_value = row[
                DUTCH_COLUMN - ENGLISH_COLUMN
            ]
    
            # Do not allow empty Excel translations
            if dutch_value is None:
    
                test.fail(
                    "Dutch translation is empty in Excel "
                    "for English text: "
                    + english_text
                )
    
                return ""
    
            dutch_text = str(
                dutch_value
            ).strip()
    
            if dutch_text == "":
    
                test.fail(
                    "Dutch translation is blank in Excel "
                    "for English text: "
                    + english_text
                )
    
                return ""
    
            return dutch_text
    
    test.fail(
        "English text not found in Excel Column B: "
        + english_text
    )
    
    return ""


# ============================================================

# GET ACTUAL OBJECT TEXT

# ============================================================

def get_actual_text(obj, description):

    actual_value = None

# --------------------------------------------------------
# First try the normal Qt text property
# --------------------------------------------------------

    try:
        actual_value = obj.text
    except Exception:
        actual_value = None


# --------------------------------------------------------
# If text is not available, try property("text")
# --------------------------------------------------------

    if actual_value is None:
    
        try:
            actual_value = obj.property(
                "text"
            )
        except Exception:
            actual_value = None


# --------------------------------------------------------
# If still unavailable, try windowTitle
# --------------------------------------------------------

    if actual_value is None:
    
        try:
            actual_value = obj.windowTitle
        except Exception:
            actual_value = None
    
    
    # --------------------------------------------------------
    # If still unavailable, try accessibleName
    # --------------------------------------------------------
    
    if actual_value is None:
    
        try:
            actual_value = obj.accessibleName
        except Exception:
            actual_value = None
    
    
    # --------------------------------------------------------
    # Normalize actual value
    # --------------------------------------------------------
    
    actual_text = normalize_text(
        actual_value
    )
    
    
    # --------------------------------------------------------
    # IMPORTANT:
    # Never allow empty/None text to pass comparison.
    # --------------------------------------------------------
    
    if actual_text == "":
    
        test.fail(
            "Application text is empty or None for: "
            + description
        )
    
        return None
    
    
    return actual_text
    
    
    # ============================================================
    
    # VERIFY TEXT AGAINST EXCEL
    
    # ============================================================
    
def verify_text(
        sheet,
        object_name,
        english_text,
        description
        ):
    
    
    # Wait before every verification
    snooze(6)
    
    
    # --------------------------------------------------------
    # Get expected Dutch value from Excel
    # --------------------------------------------------------
    
    expected_text = get_dutch_text(
        sheet,
        english_text
    )
    
    
    expected_normalized = normalize_text(
        expected_text
    )
    
    
    # --------------------------------------------------------
    # Validate expected Excel value
    # --------------------------------------------------------
    
    if expected_normalized == "":
    
        test.fail(
            "Expected Dutch text is empty for: "
            + description
        )
    
        return
    
    
    # --------------------------------------------------------
    # Get application object
    # --------------------------------------------------------
    
    obj = waitForObjectExists(
        getattr(
            names,
            object_name
        )
    )
    
    
    # --------------------------------------------------------
    # Get actual application text
    # --------------------------------------------------------
    
    actual_text = get_actual_text(
        obj,
        description
    )
    
    
    # --------------------------------------------------------
    # Stop if application text is unavailable
    # --------------------------------------------------------
    
    if actual_text is None:
    
        return
    
    
    # --------------------------------------------------------
    # Compare actual application text with Excel
    # --------------------------------------------------------
    
    test.compare(
        actual_text,
        expected_normalized,
        description + " - Dutch text verification"
    )
    
    
    # ============================================================
    
    # VERIFY LEFT MANUAL TAB
    
    # ============================================================
    
def verify_left_manual_tab(
        sheet,
        english_text,
        description
        ):
    
    
    snooze(6)
    
    
    # --------------------------------------------------------
    # Get expected Dutch value from Excel
    # --------------------------------------------------------
    
    expected_text = get_dutch_text(
        sheet,
        english_text
    )
    
    expected_normalized = normalize_text(
        expected_text
    )
    
    
    if expected_normalized == "":
    
        test.fail(
            "Expected Dutch text is empty for: "
            + description
        )
    
        return
    
    
    # --------------------------------------------------------
    # Get recorded object definition
    # --------------------------------------------------------
    
    manual_tab_object = getattr(
        names,
        "mANUEL_TabItem"
    ).copy()
    
    
    # --------------------------------------------------------
    # Remove localized text property
    # --------------------------------------------------------
    # Original object contains text='MANUEL'.
    # After Dutch localization the text changes.
    # Therefore remove the text property and locate
    # the tab using the remaining recorded properties.
    # --------------------------------------------------------
    
    if "text" in manual_tab_object:
    
        del manual_tab_object["text"]
    
    
    # --------------------------------------------------------
    # Find Manual tab
    # --------------------------------------------------------
    
    obj = waitForObjectExists(
        manual_tab_object
    )
    
    
    # --------------------------------------------------------
    # Get actual application text
    # --------------------------------------------------------
    
    actual_text = get_actual_text(
        obj,
        description
    )
    
    
    if actual_text is None:
    
        return
    
    
    # --------------------------------------------------------
    # Compare
    # --------------------------------------------------------
    
    test.compare(
        actual_text,
        expected_normalized,
        description + " - Dutch text verification"
    )
    
    
    # ============================================================
    
    # VERIFY RIGHT MANUAL TAB
    
    # ============================================================
    
def verify_right_manual_tab(
        sheet,
        english_text,
        description
        ):
    
    
    snooze(6)
    
    
    # --------------------------------------------------------
    # Get expected Dutch value from Excel
    # --------------------------------------------------------
    
    expected_text = get_dutch_text(
        sheet,
        english_text
    )
    
    expected_normalized = normalize_text(
        expected_text
    )
    
    
    if expected_normalized == "":
    
        test.fail(
            "Expected Dutch text is empty for: "
            + description
        )
    
        return
    
    
    # --------------------------------------------------------
    # Get recorded object definition
    # --------------------------------------------------------
    
    manual_tab_object = getattr(
        names,
        "mANUEL_TabItem_2"
    ).copy()
    
    
    # --------------------------------------------------------
    # Remove localized text property
    # --------------------------------------------------------
    
    if "text" in manual_tab_object:
    
        del manual_tab_object["text"]
    
    
    # --------------------------------------------------------
    # Find Manual tab
    # --------------------------------------------------------
    
    obj = waitForObjectExists(
        manual_tab_object
    )
    
    
    # --------------------------------------------------------
    # Get actual application text
    # --------------------------------------------------------
    
    actual_text = get_actual_text(
        obj,
        description
    )
    
    
    if actual_text is None:
    
        return
    
    
    # --------------------------------------------------------
    # Compare
    # --------------------------------------------------------
    
    test.compare(
        actual_text,
        expected_normalized,
        description + " - Dutch text verification"
    )
    
    
    # ============================================================
    
    # MAIN
    
    # ============================================================
    
def main():
    
    
    # ========================================================
    # LOAD EXCEL
    # ========================================================
    
    workbook = load_workbook(
        EXCEL_PATH,
        read_only=True,
        data_only=True
    )
    
    
    # ========================================================
    # CHECK SHEET
    # ========================================================
    
    if EXCEL_SHEET_NAME not in workbook.sheetnames:
    
        test.fail(
            "Excel sheet not found: "
            + EXCEL_SHEET_NAME
        )
    
        workbook.close()
    
        return
    
    
    sheet = workbook[
        EXCEL_SHEET_NAME
    ]
    
    
    # ========================================================
    # LOGIN
    # ========================================================
    
    doubleClick(
        waitForObject(
            names.numpad_pushButton_8_NumpadButton,
            100461
        ),
        96,
        56,
        Qt.NoModifier,
        Qt.LeftButton
    )
    
    snooze(1)
    
    
    doubleClick(
        waitForObject(
            names.numpad_pushButton_8_NumpadButton
        ),
        96,
        56,
        Qt.NoModifier,
        Qt.LeftButton
    )
    
    snooze(1)
    
    
    clickButton(
        waitForObject(
            names.mainFrame_okButton_QPushButton
        )
    )
    
    snooze(2)
    
    
    # ========================================================
    # OPEN SETTINGS
    # ========================================================
    
    clickButton(
        waitForObject(
            names.homeScreen_settingsButton_QPushButton
        )
    )
    
    snooze(2)
    
    
    # ========================================================
    # OPEN SYSTEM INFORMATION
    # ========================================================
    
    clickTab(
        waitForObject(
            names.settingsScreen_tbSystemInfo_TabWidget
        ),
        "INFO"
    )
    
    snooze(2)
    
    
    # ========================================================
    # OPEN LANGUAGE SETTINGS
    # ========================================================
    
    clickButton(
        waitForObject(
            names.gbSystemInformation_pbLanguageSettingsUpdate_QPushButton
        )
    )
    
    snooze(2)
    
    
    # ========================================================
    # SELECT DUTCH
    # ========================================================
    
    clickButton(
        waitForObject(
            names.languagesFrame_pbDutch_QPushButton
        )
    )
    
    snooze(1)
    
    
    # ========================================================
    # ACCEPT LANGUAGE
    # ========================================================
    
    clickButton(
        waitForObject(
            names.buttonsFrame_acceptButton_QPushButton
        )
    )
    
    snooze(3)
    
    
    # ========================================================
    # RETURN TO HOME
    # ========================================================
    
    clickButton(
        waitForObject(
            names.buttonsBar_homeButton_QPushButton
        )
    )
    
    snooze(2)
    
    
    # ========================================================
    # OPEN EXPERT MODE
    # ========================================================
    
    clickButton(
        waitForObject(
            names.gbExpert_expertButton_QPushButton
        )
    )
    
    snooze(3)
    
    
    # ========================================================
    # LEFT SIDE VERIFICATION
    # ========================================================
    
    
    # --------------------------------------------------------
    # MANUAL TAB
    # --------------------------------------------------------
    
    verify_left_manual_tab(
        sheet,
        "MANUAL",
        "Left Manual Tab"
    )
    
    
    # --------------------------------------------------------
    # AVERAGE POWER
    # --------------------------------------------------------
    
    verify_text(
        sheet,
        "averagePowerWidget_nameLabel_QLabel_2",
        "AVERAGE POWER",
        "Left Average Power"
    )
    
    
    # --------------------------------------------------------
    # POWER UNIT
    # --------------------------------------------------------
    
    verify_text(
        sheet,
        "averagePowerWidget_unitsOfMeasureLabel_QLabel_2",
        "W",
        "Left Power Unit"
    )
    
    
    # --------------------------------------------------------
    # PULSE ENERGY
    # --------------------------------------------------------
    
    verify_text(
        sheet,
        "pulseEnergyWidget_nameLabel_QLabel_2",
        "PULSE ENERGY",
        "Left Pulse Energy"
    )
    
    
    # --------------------------------------------------------
    # ENERGY UNIT
    # --------------------------------------------------------
    
    verify_text(
        sheet,
        "pulseEnergyWidget_unitsOfMeasureLabel_QLabel_2",
        "J",
        "Left Energy Unit"
    )
    
    
    # --------------------------------------------------------
    # FREQUENCY
    # --------------------------------------------------------
    
    verify_text(
        sheet,
        "frequencyWidget_nameLabel_QLabel_2",
        "FREQUENCY",
        "Left Frequency"
    )
    
    
    # --------------------------------------------------------
    # FREQUENCY UNIT
    # --------------------------------------------------------
    
    verify_text(
        sheet,
        "frequencyWidget_unitsOfMeasureLabel_QLabel_2",
        "Hz",
        "Left Frequency Unit"
    )
    
    
    # --------------------------------------------------------
    # REGULAR PULSE
    # --------------------------------------------------------
    
    verify_text(
        sheet,
        "modeButton_nameLabel_QLabel",
        "REGULAR PULSE",
        "Left Pulse Mode"
    )
    
    
    # --------------------------------------------------------
    # PEAK POWER
    # --------------------------------------------------------
    
    verify_text(
        sheet,
        "peakPowerButton_nameLabel_QLabel",
        "PEAK POWER",
        "Left Peak Power"
    )
    
    
    # --------------------------------------------------------
    # SAVE
    # --------------------------------------------------------
    
    verify_text(
        sheet,
        "pulseModeWidget_saveButton_QPushButton_2",
        "SAVE",
        "Left Save Button"
    )
    
    
    # --------------------------------------------------------
    # TOTAL ENERGY
    # --------------------------------------------------------
    
    verify_text(
        sheet,
        "totalEnergyFrame_nameLabel_QLabel",
        "TOTAL ENERGY",
        "Left Total Energy"
    )
    
    
    # --------------------------------------------------------
    # TOTAL LASING TIME
    # --------------------------------------------------------
    
    verify_text(
        sheet,
        "totalTimeFrame_nameLabel_QLabel",
        "TOTAL LASING TIME",
        "Left Total Lasing Time"
    )
    
    
    # ========================================================
    # RIGHT SIDE VERIFICATION
    # ========================================================
    
    
    # --------------------------------------------------------
    # MANUAL TAB
    # --------------------------------------------------------
    
    verify_right_manual_tab(
        sheet,
        "MANUAL",
        "Right Manual Tab"
    )
    
    
    # --------------------------------------------------------
    # AVERAGE POWER
    # --------------------------------------------------------
    
    verify_text(
        sheet,
        "averagePowerWidget_nameLabel_QLabel_3",
        "AVERAGE POWER",
        "Right Average Power"
    )
    
    
    # --------------------------------------------------------
    # POWER UNIT
    # --------------------------------------------------------
    
    verify_text(
        sheet,
        "averagePowerWidget_unitsOfMeasureLabel_QLabel_3",
        "W",
        "Right Power Unit"
    )
    
    
    # --------------------------------------------------------
    # PULSE ENERGY
    # --------------------------------------------------------
    
    verify_text(
        sheet,
        "pulseEnergyWidget_nameLabel_QLabel_3",
        "PULSE ENERGY",
        "Right Pulse Energy"
    )
    
    
    # --------------------------------------------------------
    # ENERGY UNIT
    # --------------------------------------------------------
    
    verify_text(
        sheet,
        "pulseEnergyWidget_unitsOfMeasureLabel_QLabel_3",
        "J",
        "Right Energy Unit"
    )
    
    
    # --------------------------------------------------------
    # FREQUENCY
    # --------------------------------------------------------
    
    verify_text(
        sheet,
        "frequencyWidget_nameLabel_QLabel_3",
        "FREQUENCY",
        "Right Frequency"
    )
    
    
    # --------------------------------------------------------
    # SAVE
    # --------------------------------------------------------
    
    verify_text(
        sheet,
        "pulseModeWidget_saveButton_QPushButton_3",
        "SAVE",
        "Right Save Button"
    )
    
    
    # --------------------------------------------------------
    # PEAK POWER
    # --------------------------------------------------------
    
    verify_text(
        sheet,
        "peakPowerButton_nameLabel_QLabel_3",
        "PEAK POWER",
        "Right Peak Power"
    )
    
    
    # --------------------------------------------------------
    # REGULAR PULSE
    # --------------------------------------------------------
    
    verify_text(
        sheet,
        "modeButton_nameLabel_QLabel_2",
        "REGULAR PULSE",
        "Right Pulse Mode"
    )
    
    
    # ========================================================
    # READY BUTTON
    # ========================================================
    
    verify_text(
        sheet,
        "stateSwitch_readyButton_QPushButton",
        "READY",
        "Ready Button"
    )
    
    
    # ========================================================
    # STANDBY BUTTON
    # ========================================================
    
    verify_text(
        sheet,
        "stateSwitch_standbyButton_QPushButton",
        "STANDBY",
        "Standby Button"
    )
    
    
    # ========================================================
    # FIBER
    # ========================================================
    
    verify_text(
        sheet,
        "fiberFrame_nameLabel_QLabel",
        "FIBER",
        "Fiber"
    )
    
    
    # ========================================================
    # FIBER USES REMAINING
    # ========================================================
    
    verify_text(
        sheet,
        "fiberUsesFrame_nameLabel_QLabel",
        "FIBER USES REMAINING",
        "Fiber Uses Remaining"
    )
    
    
    # ========================================================
    # AIMING BEAM
    # ========================================================
    
    verify_text(
        sheet,
        "bottomBar_aimingBeamButton_AimingBeamModeButton",
        "AIMING BEAM",
        "Aiming Beam"
    )
    
    
    # ========================================================
    # CLOSE EXCEL
    # ========================================================
    
    workbook.close()
    
    
    # ========================================================
    # COMPLETION LOG
    # ========================================================
    
    test.log(
        "Dutch Expert Manual Treatment Modes "
        "verification completed"
    )
    
