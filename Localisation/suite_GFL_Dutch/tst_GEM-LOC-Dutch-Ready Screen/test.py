# -*- coding: utf-8 -*-

import names
from openpyxl import load_workbook

# ============================================================

# EXCEL CONFIGURATION

# ============================================================

EXCEL_PATH = (
"/home/ezen/Test_Automation_Gemini/Localisation/"
"suite_GFL_Dutch/"
"tst_GEM-LOC-Dutch-PeakPower-SoftTissueCharacters/"
"testdata/Gemini Split strings.xlsx"
)

EXCEL_SHEET_NAME = "Treatment Modes"

# ------------------------------------------------------------

# Column B = English

# ------------------------------------------------------------

ENGLISH_COLUMN = 2

# ------------------------------------------------------------

# Column G = Dutch

# ------------------------------------------------------------

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
        .replace("\xa0", " ")
        .split()
    ).strip().casefold()
    

# ============================================================

# LOAD EXCEL DATA

#

# English Column B

# Dutch Column G

#

# Creates:

#

# English text -> Dutch text

#

# No row numbers are used.

# ============================================================

def load_excel_data():


    workbook = None

    try:
    
        # test.log(
        #     "Loading Dutch localization Excel..."
        # )
    
    
        # ----------------------------------------------------
        # Open workbook
        # ----------------------------------------------------
    
        workbook = load_workbook(
            EXCEL_PATH,
            read_only=True,
            data_only=True
        )
    
    
        # ----------------------------------------------------
        # Check sheet
        # ----------------------------------------------------
    
        if EXCEL_SHEET_NAME not in workbook.sheetnames:
    
            test.fail(
                "Excel sheet not found: "
                + EXCEL_SHEET_NAME
                + " | Available sheets: "
                + ", ".join(workbook.sheetnames)
            )
    
            workbook.close()
    
            return None, None
    
    
        sheet = workbook[
            EXCEL_SHEET_NAME
        ]
    
    
        # ----------------------------------------------------
        # Create English -> Dutch dictionary
        # ----------------------------------------------------
    
        dutch_data = {}
    
    
        for row in sheet.iter_rows(
            min_row=2,
            min_col=ENGLISH_COLUMN,
            max_col=DUTCH_COLUMN
        ):
    
            english_value = row[0].value
    
            dutch_value = row[
                DUTCH_COLUMN - ENGLISH_COLUMN
            ].value
    
    
            # ------------------------------------------------
            # Ignore empty English cells
            # ------------------------------------------------
    
            if english_value is None:
    
                continue
    
    
            english_key = normalize_text(
                english_value
            )
    
    
            if english_key == "":
    
                continue
    
    
            # ------------------------------------------------
            # Convert empty Dutch value to empty string
            # ------------------------------------------------
    
            if dutch_value is None:
    
                dutch_value = ""
    
    
            dutch_value = str(
                dutch_value
            ).strip()
    
    
            # ------------------------------------------------
            # Keep first non-empty translation
            # ------------------------------------------------
    
            if english_key not in dutch_data:
    
                dutch_data[
                    english_key
                ] = dutch_value
    
            else:
    
                existing_value = dutch_data[
                    english_key
                ]
    
                if (
                    normalize_text(existing_value) == ""
                    and
                    normalize_text(dutch_value) != ""
                ):
    
                    dutch_data[
                        english_key
                    ] = dutch_value
    
    
        # ----------------------------------------------------
        # Make sure data was actually loaded
        # ----------------------------------------------------
    
        if not dutch_data:
    
            test.fail(
                "No English/Dutch data found in Excel. "
                "Please check the sheet and column configuration."
            )
    
            workbook.close()
    
            return None, None
    
    
        # test.log(
        #     "Dutch Excel loaded successfully"
        # )
        #
        # test.log(
        #     "Excel sheet: "
        #     + EXCEL_SHEET_NAME
        # )
    
        # test.log(
        #     "English column: "
        #     + str(ENGLISH_COLUMN)
        #     )

        # test.log(
        #     "Dutch column: "
        #     + str(DUTCH_COLUMN)
        # )
    
        
    
    
        # ----------------------------------------------------
        # IMPORTANT:
        # Always return TWO values
        # ----------------------------------------------------
    
        return workbook, dutch_data
    
    
    except Exception as e:
    
        test.fail(
            "Unable to load/read Dutch localization Excel: "
            + str(e)
        )
    
    
        if workbook is not None:
    
            try:
    
                workbook.close()
    
            except:
    
                pass
    
    
        # ----------------------------------------------------
        # IMPORTANT:
        # Always return TWO values
        # ----------------------------------------------------
    
        return None, None
    
    
    # ============================================================
    
    # GET DUTCH TEXT USING ENGLISH TEXT
    
    # ============================================================
    
def get_dutch_text(
    dutch_data,
    english_text
    ):
    
    
    search_text = normalize_text(
        english_text
    )
    
    
    # --------------------------------------------------------
    # English text not found
    # --------------------------------------------------------
    
    if search_text not in dutch_data:
    
        test.fail(
            "English text not found in Excel Column B: "
            + str(english_text)
        )
    
        return None
    
    
    dutch_value = dutch_data[
        search_text
    ]
    
    
    # --------------------------------------------------------
    # Dutch translation empty
    # --------------------------------------------------------
    
    if normalize_text(
        dutch_value
    ) == "":
    
        test.fail(
            "Dutch translation is empty for English text: "
            + str(english_text)
        )
    
        return None
    
    
    return dutch_value
    
    
    # ============================================================
    
    # VERIFY NORMAL OBJECT TEXT
    
    #
    
    # object_name:
    
    # Name of object-map variable
    
    #
    
    # english_text:
    
    # English text from Excel Column B
    
    #
    
    # Expected Dutch value is obtained automatically from Excel.
    
    # ============================================================
    
def verify_text(
    dutch_data,
    object_name,
    english_text,
    description
    ):
    
    
    # --------------------------------------------------------
    # Wait before verification
    # --------------------------------------------------------
    
    snooze(2)
    
    
    # --------------------------------------------------------
    # Get Dutch expected value
    # --------------------------------------------------------
    
    expected_text = get_dutch_text(
        dutch_data,
        english_text
    )
    
    
    if expected_text is None:
    
        test.fail(
            description
            + " skipped because Excel lookup failed"
        )
    
        return
    
    
    # --------------------------------------------------------
    # Find Squish object
    # --------------------------------------------------------
    
    try:
    
        obj = waitForObjectExists(
            getattr(
                names,
                object_name
            )
        )
    
    
    except Exception as e:
    
        test.fail(
            description
            + " | Object not found: "
            + object_name
            + " | "
            + str(e)
        )
    
        return
    
    
    # --------------------------------------------------------
    # Read actual object text
    # --------------------------------------------------------
    
    try:
    
        actual_text = obj.text
    
    except Exception as e:
    
        test.fail(
            description
            + " | Unable to read object text | "
            + str(e)
        )
    
        return
    
    
    # --------------------------------------------------------
    # Normalize values
    # --------------------------------------------------------
    
    actual_normalized = normalize_text(
        actual_text
    )
    
    expected_normalized = normalize_text(
        expected_text
    )
    
    
    # --------------------------------------------------------
    # Compare
    # --------------------------------------------------------
    
    test.compare(
        actual_normalized,
        expected_normalized,
        description
        + " - Dutch text verification"
    )
    
    
    # ============================================================
    
    # RECURSIVE SEARCH FOR TREATMENT NAME
    
    #
    
    # Does not create an object name from Dutch text.
    
    # ============================================================
    
def find_text_recursively(
    parent_object,
    expected_normalized
    ):
    
    
    try:
    
        if not parent_object.visible:
    
            return None
    
    except Exception:
    
        pass
    
    
    # --------------------------------------------------------
    # Check current object
    # --------------------------------------------------------
    
    try:
    
        current_text = normalize_text(
            parent_object.text
        )
    
        if current_text == expected_normalized:
    
            return parent_object
    
    except Exception:
    
        pass
    
    
    # --------------------------------------------------------
    # Get children
    # --------------------------------------------------------
    
    try:
    
        children = object.children(
            parent_object
        )
    
    except Exception:
    
        children = []
    
    
    # --------------------------------------------------------
    # Search children recursively
    # --------------------------------------------------------
    
    for child in children:
    
        found = find_text_recursively(
            child,
            expected_normalized
        )
    
        if found is not None:
    
            return found
    
    
    return None
    
    
    # ============================================================
    
    # VERIFY TREATMENT NAME
    
    #
    
    # English treatment name is used only as Excel lookup key.
    
    #
    
    # Actual Dutch treatment name comes from Excel.
    
    # ============================================================
    
def verify_treatment_name(
    dutch_data,
    english_text,
    description
    ):
    
    
    # --------------------------------------------------------
    # Wait before verification
    # --------------------------------------------------------
    
    snooze(6)
    
    
    # --------------------------------------------------------
    # Get Dutch translation
    # --------------------------------------------------------
    
    expected_text = get_dutch_text(
        dutch_data,
        english_text
    )
    
    
    if expected_text is None:
    
        test.fail(
            description
            + " skipped because Excel lookup failed"
        )
    
        return
    
    
    expected_normalized = normalize_text(
        expected_text
    )
    
    
    # --------------------------------------------------------
    # Find ScreenSwitcher
    # --------------------------------------------------------
    
    try:
    
        screen_switcher = waitForObjectExists(
            names.o_ScreenSwitcher
        )
    
    
    except Exception as e:
    
        test.fail(
            description
            + " | ScreenSwitcher not found | "
            + str(e)
        )
    
        return
    
    
    # --------------------------------------------------------
    # Search for Dutch treatment text
    # --------------------------------------------------------
    
    found_object = find_text_recursively(
        screen_switcher,
        expected_normalized
    )
    
    
    if found_object is None:
    
        test.fail(
            "{} | Dutch treatment text not found "
            "on screen: [{}]".format(
                description,
                expected_text
            )
        )
    
        return
    
    
    # --------------------------------------------------------
    # Read actual text
    # --------------------------------------------------------
    
    try:
    
        actual_text = normalize_text(
            found_object.text
        )
    
    except Exception:
    
        actual_text = ""
    
    
    # --------------------------------------------------------
    # Compare
    # --------------------------------------------------------
    
    test.compare(
        actual_text,
        expected_normalized,
        description
        + " - Dutch treatment verification"
    )
    
    
    # ============================================================
    
    # VERIFY LEFT TREATMENT NAME
    
    # ============================================================
    
def verify_left_treatment_name(
    dutch_data,
    english_text,
    description
    ):
    
    
    verify_treatment_name(
        dutch_data,
        english_text,
        description
    )
    
    
    # ============================================================
    
    # VERIFY RIGHT TREATMENT NAME
    
    # ============================================================
    
def verify_right_treatment_name(
    dutch_data,
    english_text,
    description
    ):
    
    
    verify_treatment_name(
        dutch_data,
        english_text,
        description
    )
    
    
    # ============================================================
    
    # MAIN
    
    # ============================================================
    
def main():
    
    
    workbook = None
    dutch_data = None
    
    
    # ========================================================
    # LOAD EXCEL
    # ========================================================
    
    result = load_excel_data()
    
    
    # --------------------------------------------------------
    # Safety check
    # --------------------------------------------------------
    
    if result is None:
    
        test.fail(
            "load_excel_data() returned None"
        )
    
        return
    
    
    # --------------------------------------------------------
    # Unpack only after checking result
    # --------------------------------------------------------
    
    try:
    
        workbook, dutch_data = result
    
    except Exception as e:
    
        test.fail(
            "Unable to unpack Excel data: "
            + str(e)
        )
    
        return
    
    
    if workbook is None or dutch_data is None:
    
        test.fail(
            "Dutch Excel data could not be loaded"
        )
    
        return
    
    
    try:
    
        # ====================================================
        # LOGIN
        # ====================================================
    
        for i in range(4):
    
            clickButton(
                waitForObject(
                    names.numpad_pushButton_8_NumpadButton
                )
            )
    
            snooze(1)
    
    
        clickButton(
            waitForObject(
                names.mainFrame_okButton_QPushButton
            )
        )
    
    
        # ====================================================
        # OPEN SETTINGS
        # ====================================================
    
        clickButton(
            waitForObject(
                names.homeScreen_settingsButton_QPushButton
            )
        )
    
        
    
    
        # ====================================================
        # OPEN SYSTEM INFORMATION
        # ====================================================
    
        clickTab(
            waitForObject(
                names.settingsScreen_tbSystemInfo_TabWidget
            ),
            "INFO"
        )
    
    
        # ====================================================
        # OPEN LANGUAGE SETTINGS
        # ====================================================
    
        clickButton(
            waitForObject(
                names.gbSystemInformation_pbLanguageSettingsUpdate_QPushButton
            )
        )
    
    
        # ====================================================
        # SELECT DUTCH
        # ====================================================
    
        clickButton(
            waitForObject(
                names.languagesFrame_pbDutch_QPushButton
            )
        )
    
    
        # ====================================================
        # ACCEPT LANGUAGE
        # ====================================================
    
        clickButton(
            waitForObject(
                names.buttonsFrame_acceptButton_QPushButton
            )
        )
    
    
        # ====================================================
        # RETURN HOME
        # ====================================================
    
        clickButton(
            waitForObject(
                names.buttonsBar_homeButton_QPushButton
            )
        )
    
    
        # ====================================================
        # OPEN SOFT TISSUE QUICK START
        # ====================================================
    
        clickButton(
            waitForObject(
                names.homeScreen_pbSoftTissueQuickStart_QToolButton
            )
        )
    
    
        # ====================================================
        # SELECT LEFT TREATMENT
        # ====================================================
    
        mouseClick(
            waitForObjectItem(
                names.tabLeftMainPresets_leftPresetsView_PresetListView,
                "_1"
            ),
            238,
            58,
            Qt.NoModifier,
            Qt.LeftButton
        )
    
    
        # ====================================================
        # SELECT RIGHT TREATMENT
        # ====================================================
    
        mouseClick(
            waitForObjectItem(
                names.tabRightMainPresets_rightPresetsView_PresetListView,
                "_1"
            ),
            148,
            32,
            Qt.NoModifier,
            Qt.LeftButton
        )
    
    
        # ====================================================
        # QUICK START BOTTOM WIDGET
        # ====================================================
    
        mouseClick(
            waitForObject(
                names.quickStartScreen_wdBottom_QWidget
            ),
            1167,
            9,
            Qt.NoModifier,
            Qt.LeftButton
        )
    
        
    
    
        # ====================================================
        # MOVE SCREEN
        # ====================================================
    
        sendEvent(
            "QMoveEvent",
            waitForObject(
                names.o_ScreenSwitcher
            ),
            0,
            -51,
            1286,
            61
        )
    
    
        # ====================================================
        # CONTINUE
        # ====================================================
    
        clickButton(
            waitForObject(
                names.quickStartScreen_pbContinue_QPushButton
            )
        )
    
    
        # ====================================================
        # OK
        # ====================================================
    
        clickButton(
            waitForObject(
                names.mainFrame_okButton_QPushButton_2
            )
        )
    
    
        # ====================================================
        # SELECT READY
        # ====================================================
    
        clickButton(
            waitForObject(
                names.stateSwitch_readyButton_QPushButton
            )
        )
    
    
        # ====================================================
        # LEFT TREATMENT NAME
        # ====================================================
    
        verify_left_treatment_name(
            dutch_data,
            "PROSTATE ENUCLEATION-(HIGH ENERGY)",
            "Left Treatment Name"
        )
    
    
        # ====================================================
        # LEFT AVERAGE POWER
        # ====================================================
    
        verify_text(
            dutch_data,
            "averagePowerWidgetEmission_nameLabel_QLabel",
            "Average Power",
            "Left Average Power"
        )
    
    
        # ====================================================
        # LEFT PULSE ENERGY
        # ====================================================
    
        verify_text(
            dutch_data,
            "pulseEnergyWidgetEmission_nameLabel_QLabel",
            "Pulse Energy",
            "Left Pulse Energy"
        )
    
    
        # ====================================================
        # LEFT FREQUENCY
        # ====================================================
    
        verify_text(
            dutch_data,
            "frequencyWidgetEmission_nameLabel_QLabel",
            "Frequency",
            "Left Frequency"
        )
    
    
        # ====================================================
        # LEFT PULSE MODE
        # ====================================================
    
        verify_text(
            dutch_data,
            "modeButtonEmission_nameLabel_QLabel",
            "Pulse Mode",
            "Left Pulse Mode"
        )
    
    
        # ====================================================
        # LEFT PEAK POWER
        # ====================================================
    
        verify_text(
            dutch_data,
            "peakPowerButtonEmission_nameLabel_QLabel",
            "Peak Power",
            "Left Peak Power"
        )
    
    
        # ====================================================
        # LEFT TOTAL ENERGY
        # ====================================================
    
        verify_text(
            dutch_data,
            "totalEnergyFrame_nameLabel_QLabel",
            "Total Energy",
            "Left Total Energy"
        )
    
    
        # ====================================================
        # LEFT TOTAL LASING TIME
        # ====================================================
    
        verify_text(
            dutch_data,
            "totalTimeFrame_nameLabel_QLabel",
            "Total Lasing Time",
            "Left Total Lasing Time"
        )
    
    
        # ====================================================
        # LEFT POWER UNIT
        # ====================================================
    
        verify_text(
            dutch_data,
            "averagePowerWidgetEmission_unitsOfMeasureLabel_QLabel",
            "W",
            "Left Power Unit"
        )
    
    
        # ====================================================
        # LEFT ENERGY UNIT
        # ====================================================
    
        verify_text(
            dutch_data,
            "pulseEnergyWidgetEmission_unitsOfMeasureLabel_QLabel",
            "J",
            "Left Energy Unit"
        )
    
    
        # ====================================================
        # LEFT FREQUENCY UNIT
        # ====================================================
    
        verify_text(
            dutch_data,
            "frequencyWidgetEmission_unitsOfMeasureLabel_QLabel",
            "Hz",
            "Left Frequency Unit"
        )
    
    
        # ====================================================
        # LEFT FIBER
        # ====================================================
    
        verify_text(
            dutch_data,
            "fiberFrame_nameLabel_QLabel",
            "Fiber",
            "Left Fiber"
        )
    
    
        # ====================================================
        # LEFT FIBER USES REMAINING
        # ====================================================
    
        verify_text(
            dutch_data,
            "fiberUsesFrame_nameLabel_QLabel",
            "Fiber Uses Remaining",
            "Left Fiber Uses Remaining"
        )
    
    
        # ====================================================
        # LEFT AIMING BEAM
        # ====================================================
    
        verify_text(
            dutch_data,
            "bottomBar_aimingBeamButton_AimingBeamModeButton",
            "Aiming Beam",
            "Left Aiming Beam"
        )
    
    
        # ====================================================
        # LEFT STANDBY
        # ====================================================
    
        verify_text(
            dutch_data,
            "stateSwitch_standbyButton_QPushButton",
            "Standby",
            "Left Standby"
        )
    
    
        # ====================================================
        # LEFT READY
        # ====================================================
    
        verify_text(
            dutch_data,
            "stateSwitch_readyButton_QPushButton",
            "Ready",
            "Left Ready"
        )
    
    
        # ====================================================
        # RIGHT TREATMENT NAME
        # ====================================================
    
        verify_right_treatment_name(
            dutch_data,
            "PROSTATE ENUCLEATION-(HIGH ENERGY)",
            "Right Treatment Name"
        )
    
    
        # ====================================================
        # RIGHT AVERAGE POWER
        # ====================================================
    
        verify_text(
            dutch_data,
            "averagePowerWidgetEmission_nameLabel_QLabel_2",
            "Average Power",
            "Right Average Power"
        )
    
    
        # ====================================================
        # RIGHT PULSE ENERGY
        # ====================================================
    
        verify_text(
            dutch_data,
            "pulseEnergyWidgetEmission_nameLabel_QLabel_2",
            "Pulse Energy",
            "Right Pulse Energy"
        )
    
    
        # ====================================================
        # RIGHT FREQUENCY
        # ====================================================
    
        verify_text(
            dutch_data,
            "frequencyWidgetEmission_nameLabel_QLabel_2",
            "Frequency",
            "Right Frequency"
        )
    
    
        # ====================================================
        # RIGHT PULSE MODE
        # ====================================================
    
        verify_text(
            dutch_data,
            "modeButtonEmission_nameLabel_QLabel_2",
            "Pulse Mode",
            "Right Pulse Mode"
        )
    
    
        # ====================================================
        # RIGHT PEAK POWER
        # ====================================================
    
        verify_text(
            dutch_data,
            "peakPowerButtonEmission_nameLabel_QLabel_2",
            "Peak Power",
            "Right Peak Power"
        )
    
    
        # ====================================================
        # RIGHT POWER UNIT
        # ====================================================
    
        verify_text(
            dutch_data,
            "averagePowerWidgetEmission_unitsOfMeasureLabel_QLabel_2",
            "W",
            "Right Power Unit"
        )
    
    
        # ====================================================
        # RIGHT ENERGY UNIT
        # ====================================================
    
        verify_text(
            dutch_data,
            "pulseEnergyWidgetEmission_unitsOfMeasureLabel_QLabel_2",
            "J",
            "Right Energy Unit"
        )
    
    
        # ====================================================
        # RIGHT FREQUENCY UNIT
        # ====================================================
    
        verify_text(
            dutch_data,
            "frequencyWidgetEmission_unitsOfMeasureLabel_QLabel_2",
            "Hz",
            "Right Frequency Unit"
        )
    
    
        # ====================================================
        # READY SCREEN
        # ====================================================
    
        clickButton(
            waitForObject(
                names.stateSwitch_readyButton_QPushButton
            )
        )
    
    
        # ====================================================
        # READY SCREEN IMAGE
        # ====================================================
    
        test.imagePresent(
            "Ready screen header image"
        )
    
    
        # ====================================================
        # RETURN TO STANDBY
        # ====================================================
    
        clickButton(
            waitForObject(
                names.stateSwitch_readyButton_QPushButton
            )
        )
    
    
        # ====================================================
        # VISUAL VERIFICATION POINT
        # ====================================================
        #
        # test.vp(
        #     "Readyscreen"
        # )
    
    
    except Exception as e:
    
        test.fail(
            "Dutch Ready Screen test failed: "
            + str(e)
        )
    
    
    finally:
    
        # ====================================================
        # CLOSE EXCEL
        # ====================================================
    
        if workbook is not None:
    
            try:
    
                workbook.close()
    
            except:
    
                pass
    
    
        test.log(
            "Dutch Treatment Modes localization verification completed"
        )
    
