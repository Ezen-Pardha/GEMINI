
# -*- coding: utf-8 -*-

import names
from openpyxl import load_workbook


# ============================================================
# EXCEL CONFIGURATION
# ============================================================

EXCEL_PATH = (
    "/home/ezen/Test_Automation_Gemini/Localisation/"
    "suite_GFL_Estonian/"
    "tst_GEM-LOC-Estonian-PeakPower-SoftTissueCharacters/"
    "testdata/Gemini Split strings.xlsx"
)

EXCEL_SHEET_NAME = "Treatment Modes"

# Column B = English
ENGLISH_COLUMN = 2

# Column H = Estonian
ESTONIAN_COLUMN = 8


# ============================================================
# TEXT NORMALIZATION / CONCATENATION
# ============================================================

def normalize_text(value):

    if value is None:
        return ""

    text = str(value)

    # Replace line breaks
    text = text.replace("\n", " ")
    text = text.replace("\r", " ")

    # Replace non-breaking spaces
    text = text.replace("\xa0", " ")

    # Remove ALL whitespace
    #
    # Example:
    #
    # KESKMINE VÕIMSUS
    #
    # KESKMINE
    # VÕIMSUS
    #
    # KESKMINE    VÕIMSUS
    #
    # All become:
    #
    # KESKMINEVÕIMSUS

    text = "".join(text.split())

    # Case-insensitive comparison
    return text.casefold()


# ============================================================
# LOAD EXCEL DATA
#
# English Column B
# Estonian Column H
#
# Creates:
#
# normalized English -> Estonian translation
#
# No hard-coded row numbers.
# ============================================================

def load_excel_data():

    workbook = None

    try:

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

        sheet = workbook[EXCEL_SHEET_NAME]

        # ----------------------------------------------------
        # Create English -> Estonian dictionary
        # ----------------------------------------------------

        estonian_data = {}

        for row in sheet.iter_rows(
            min_row=2,
            min_col=ENGLISH_COLUMN,
            max_col=ESTONIAN_COLUMN
        ):

            english_value = row[0]

            estonian_value = row[
                ESTONIAN_COLUMN - ENGLISH_COLUMN
            ]

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
            # Convert empty Estonian cell to empty string
            # ------------------------------------------------

            if estonian_value is None:
                estonian_value = ""

            estonian_value = str(
                estonian_value
            ).strip()

            # ------------------------------------------------
            # Keep first non-empty translation
            # ------------------------------------------------

            if english_key not in estonian_data:

                estonian_data[
                    english_key
                ] = estonian_value

            else:

                existing_value = estonian_data[
                    english_key
                ]

                if (
                    normalize_text(existing_value) == ""
                    and
                    normalize_text(estonian_value) != ""
                ):

                    estonian_data[
                        english_key
                    ] = estonian_value

        # ----------------------------------------------------
        # Check whether data was loaded
        # ----------------------------------------------------

        if not estonian_data:

            test.fail(
                "No English/Estonian data found in Excel. "
                "Please check the sheet and columns."
            )

            workbook.close()
            return None, None

        return workbook, estonian_data

    except Exception as e:

        test.fail(
            "Unable to load/read Estonian localization Excel: "
            + str(e)
        )

        if workbook is not None:

            try:
                workbook.close()
            except:
                pass

        return None, None


# ============================================================
# GET ESTONIAN TEXT USING ENGLISH TEXT
# ============================================================

def get_estonian_text(
    estonian_data,
    english_text
):

    search_text = normalize_text(
        english_text
    )

    # --------------------------------------------------------
    # English text not found
    # --------------------------------------------------------

    if search_text not in estonian_data:

        test.fail(
            "English text not found in Excel Column B: "
            + str(english_text)
        )

        return None

    estonian_value = estonian_data[
        search_text
    ]

    # --------------------------------------------------------
    # Estonian translation empty
    # --------------------------------------------------------

    if normalize_text(
        estonian_value
    ) == "":

        test.fail(
            "Estonian translation is empty for English text: "
            + str(english_text)
        )

        return None

    return estonian_value


# ============================================================
# RECURSIVE SEARCH FOR OBJECT BY TEXT
#
# This is used when the generated names.py object name
# is unavailable.
# ============================================================

def find_text_recursively(
    parent_object,
    expected_normalized
):

    # --------------------------------------------------------
    # Check visibility
    # --------------------------------------------------------

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
# FIND LOCALIZED BUTTON
#
# IMPORTANT:
#
# We do NOT use:
#
# names.stateSwitch_readyButton_QPushButton
#
# The button is found by its localized text instead.
# ============================================================

def find_localized_button(
    estonian_data,
    english_text,
    description
):

    # --------------------------------------------------------
    # Get localized text from Excel
    # --------------------------------------------------------

    expected_text = get_estonian_text(
        estonian_data,
        english_text
    )

    if expected_text is None:

        test.fail(
            description
            + " skipped because Excel lookup failed"
        )

        return None

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

        return None

    # --------------------------------------------------------
    # Find button using localized text
    # --------------------------------------------------------

    found_object = find_text_recursively(
        screen_switcher,
        expected_normalized
    )

    if found_object is None:

        test.fail(
            description
            + " | Localized button not found: ["
            + str(expected_text)
            + "]"
        )

        return None

    return found_object


# ============================================================
# CLICK LOCALIZED BUTTON
#
# Uses Excel text instead of names.py object name.
# ============================================================

def click_localized_button(
    estonian_data,
    english_text,
    description
):

    button = find_localized_button(
        estonian_data,
        english_text,
        description
    )

    if button is None:
        return False

    try:

        clickButton(button)

        snooze(2)

        return True

    except Exception as e:

        test.fail(
            description
            + " | Unable to click localized button | "
            + str(e)
        )

        return False


# ============================================================
# VERIFY NORMAL OBJECT TEXT
#
# English text = Excel lookup key
# Estonian text = Excel expected value
#
# UI and Excel values are concatenated before comparison.
# ============================================================

def verify_text(
    estonian_data,
    object_name,
    english_text,
    description
):

    # --------------------------------------------------------
    # Wait for UI
    # --------------------------------------------------------

    snooze(2)

    # --------------------------------------------------------
    # Get Estonian expected value
    # --------------------------------------------------------

    expected_text = get_estonian_text(
        estonian_data,
        english_text
    )

    if expected_text is None:

        test.fail(
            description
            + " skipped because Excel lookup failed"
        )

        return

    # --------------------------------------------------------
    # Find object
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
    # Read actual UI text
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
    # CONCATENATE UI STRING
    # --------------------------------------------------------

    actual_normalized = normalize_text(
        actual_text
    )

    # --------------------------------------------------------
    # CONCATENATE EXCEL STRING
    # --------------------------------------------------------

    expected_normalized = normalize_text(
        expected_text
    )

    # --------------------------------------------------------
    # COMPARE
    # --------------------------------------------------------

    test.compare(
        actual_normalized,
        expected_normalized,
        description
        + " - Estonian text verification"
    )


# ============================================================
# VERIFY TREATMENT NAME
#
# The actual Estonian treatment name is obtained from Excel.
#
# No object name is constructed using Estonian text.
# ============================================================

def verify_treatment_name(
    estonian_data,
    english_text,
    description
):

    # --------------------------------------------------------
    # Wait for treatment screen
    # --------------------------------------------------------

    snooze(6)

    # --------------------------------------------------------
    # Get Estonian treatment name from Excel
    # --------------------------------------------------------

    expected_text = get_estonian_text(
        estonian_data,
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
    # Search screen recursively
    # --------------------------------------------------------

    found_object = find_text_recursively(
        screen_switcher,
        expected_normalized
    )

    if found_object is None:

        test.fail(
            "{} | Estonian treatment text not found "
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
    # Compare concatenated strings
    # --------------------------------------------------------

    test.compare(
        actual_text,
        expected_normalized,
        description
        + " - Estonian treatment verification"
    )


# ============================================================
# VERIFY LEFT TREATMENT NAME
# ============================================================

def verify_left_treatment_name(
    estonian_data,
    english_text,
    description
):

    verify_treatment_name(
        estonian_data,
        english_text,
        description
    )


# ============================================================
# VERIFY RIGHT TREATMENT NAME
# ============================================================

def verify_right_treatment_name(
    estonian_data,
    english_text,
    description
):

    verify_treatment_name(
        estonian_data,
        english_text,
        description
    )


# ============================================================
# MAIN
# ============================================================

def main():

    workbook = None
    estonian_data = None

    # ========================================================
    # LOAD EXCEL ONCE
    # ========================================================

    result = load_excel_data()

    if result is None:

        test.fail(
            "load_excel_data() returned None"
        )

        return

    # --------------------------------------------------------
    # Unpack
    # --------------------------------------------------------

    try:

        workbook, estonian_data = result

    except Exception as e:

        test.fail(
            "Unable to unpack Excel data: "
            + str(e)
        )

        return

    if (
        workbook is None
        or estonian_data is None
    ):

        test.fail(
            "Estonian Excel data could not be loaded"
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
        # SELECT ESTONIAN
        # ====================================================

        clickButton(
            waitForObject(
                names.languagesFrame_pbEstonia_QPushButton
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
        snooze(2)
        clickButton(waitForObject(names.stateSwitch_readyButton_QPushButton))
        # ====================================================
        # SELECT READY
        #
        # IMPORTANT:
        # Do NOT use:
        #
        # names.stateSwitch_readyButton_QPushButton
        #
        # Ready button is located dynamically using the
        # Estonian translation from Excel.
        # ====================================================
        snooze(3)
        

        click_localized_button(
            estonian_data,
            "Ready",
            "Select Ready"
        )

        # ====================================================
        # LEFT TREATMENT NAME
        # ====================================================

        verify_left_treatment_name(
            estonian_data,
            "PROSTATE ENUCLEATION-(HIGH ENERGY)",
            "Left Treatment Name"
        )

        # ====================================================
        # LEFT AVERAGE POWER
        # ====================================================

        verify_text(
            estonian_data,
            "averagePowerWidgetEmission_nameLabel_QLabel",
            "Average Power",
            "Left Average Power"
        )

        # ====================================================
        # LEFT PULSE ENERGY
        # ====================================================

        verify_text(
            estonian_data,
            "pulseEnergyWidgetEmission_nameLabel_QLabel",
            "Pulse Energy",
            "Left Pulse Energy"
        )

        # ====================================================
        # LEFT FREQUENCY
        # ====================================================

        verify_text(
            estonian_data,
            "frequencyWidgetEmission_nameLabel_QLabel",
            "Frequency",
            "Left Frequency"
        )

        # ====================================================
        # LEFT PULSE MODE
        # ====================================================

        verify_text(
            estonian_data,
            "modeButtonEmission_nameLabel_QLabel",
            "Pulse Mode",
            "Left Pulse Mode"
        )

        # ====================================================
        # LEFT PEAK POWER
        # ====================================================

        verify_text(
            estonian_data,
            "peakPowerButtonEmission_nameLabel_QLabel",
            "Peak Power",
            "Left Peak Power"
        )

        # ====================================================
        # LEFT TOTAL ENERGY
        # ====================================================

        verify_text(
            estonian_data,
            "totalEnergyFrame_nameLabel_QLabel",
            "Total Energy",
            "Left Total Energy"
        )

        # ====================================================
        # LEFT TOTAL LASING TIME
        # ====================================================

        verify_text(
            estonian_data,
            "totalTimeFrame_nameLabel_QLabel",
            "Total Lasing Time",
            "Left Total Lasing Time"
        )

        # ====================================================
        # LEFT POWER UNIT
        # ====================================================

        verify_text(
            estonian_data,
            "averagePowerWidgetEmission_unitsOfMeasureLabel_QLabel",
            "W",
            "Left Power Unit"
        )

        # ====================================================
        # LEFT ENERGY UNIT
        # ====================================================

        verify_text(
            estonian_data,
            "pulseEnergyWidgetEmission_unitsOfMeasureLabel_QLabel",
            "J",
            "Left Energy Unit"
        )

        # ====================================================
        # LEFT FREQUENCY UNIT
        # ====================================================

        verify_text(
            estonian_data,
            "frequencyWidgetEmission_unitsOfMeasureLabel_QLabel",
            "Hz",
            "Left Frequency Unit"
        )

        # ====================================================
        # LEFT FIBER
        # ====================================================

        verify_text(
            estonian_data,
            "fiberFrame_nameLabel_QLabel",
            "Fiber",
            "Left Fiber"
        )

        # ====================================================
        # LEFT FIBER USES REMAINING
        # ====================================================

        verify_text(
            estonian_data,
            "fiberUsesFrame_nameLabel_QLabel",
            "Fiber Uses Remaining",
            "Left Fiber Uses Remaining"
        )

        # ====================================================
        # LEFT AIMING BEAM
        # ====================================================

        verify_text(
            estonian_data,
            "bottomBar_aimingBeamButton_AimingBeamModeButton",
            "Aiming Beam",
            "Left Aiming Beam"
        )

        # ====================================================
        # LEFT STANDBY
        # ====================================================

        verify_text(
            estonian_data,
            "stateSwitch_standbyButton_QPushButton",
            "Standby",
            "Left Standby"
        )

        # ====================================================
        # LEFT READY
        #
        # The object name is no longer used.
        # ====================================================

        verify_text(
            estonian_data,
            "stateSwitch_standbyButton_QPushButton",
            "Ready",
            "Left Ready"
        )

        # ====================================================
        # RIGHT TREATMENT NAME
        # ====================================================

        verify_right_treatment_name(
            estonian_data,
            "PROSTATE ENUCLEATION-(HIGH ENERGY)",
            "Right Treatment Name"
        )

        # ====================================================
        # RIGHT AVERAGE POWER
        # ====================================================

        verify_text(
            estonian_data,
            "averagePowerWidgetEmission_nameLabel_QLabel_2",
            "Average Power",
            "Right Average Power"
        )

        # ====================================================
        # RIGHT PULSE ENERGY
        # ====================================================

        verify_text(
            estonian_data,
            "pulseEnergyWidgetEmission_nameLabel_QLabel_2",
            "Pulse Energy",
            "Right Pulse Energy"
        )

        # ====================================================
        # RIGHT FREQUENCY
        # ====================================================

        verify_text(
            estonian_data,
            "frequencyWidgetEmission_nameLabel_QLabel_2",
            "Frequency",
            "Right Frequency"
        )

        # ====================================================
        # RIGHT PULSE MODE
        # ====================================================

        verify_text(
            estonian_data,
            "modeButtonEmission_nameLabel_QLabel_2",
            "Pulse Mode",
            "Right Pulse Mode"
        )

        # ====================================================
        # RIGHT PEAK POWER
        # ====================================================

        verify_text(
            estonian_data,
            "peakPowerButtonEmission_nameLabel_QLabel_2",
            "Peak Power",
            "Right Peak Power"
        )

        # ====================================================
        # RIGHT POWER UNIT
        # ====================================================

        verify_text(
            estonian_data,
            "averagePowerWidgetEmission_unitsOfMeasureLabel_QLabel_2",
            "W",
            "Right Power Unit"
        )

        # ====================================================
        # RIGHT ENERGY UNIT
        # ====================================================

        verify_text(
            estonian_data,
            "pulseEnergyWidgetEmission_unitsOfMeasureLabel_QLabel_2",
            "J",
            "Right Energy Unit"
        )

        # ====================================================
        # RIGHT FREQUENCY UNIT
        # ====================================================

        verify_text(
            estonian_data,
            "frequencyWidgetEmission_unitsOfMeasureLabel_QLabel_2",
            "Hz",
            "Right Frequency Unit"
        )

        # ====================================================
        # READY SCREEN
        #
        # Use localized Excel-driven button.
        # ====================================================

        click_localized_button(
            estonian_data,
            "Ready",
            "Open Ready Screen"
        )

        # ====================================================
        # READY SCREEN IMAGE
        # ====================================================

        test.imagePresent(
            "Ready screen header image"
        )

        # ====================================================
        # RETURN TO STANDBY
        #
        # Use localized Excel-driven button.
        # ====================================================

        click_localized_button(
            estonian_data,
            "Ready",
            "Return to Standby"
        )

    except Exception as e:

        test.fail(
            "Estonian Treatment Modes localization test failed: "
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
