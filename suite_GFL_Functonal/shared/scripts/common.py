from squish import *
import test
import names
import os
import datetime
import subprocess

def capture_screenshot(description="screenshot", category="GUI"):
    """Capture only the active window and save it under Screenshots/GUI or Screenshots/VP."""

    category = category.upper()

    if category not in ("GUI", "VP"):
        raise ValueError("Category must be GUI or VP")

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    safe_description = "".join(
        c if c.isalnum() or c in "_-" else "_"
        for c in description
    )

    # Save inside the test suite's Screenshots folder.
    screenshot_root = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
        "Screenshots"
    )

    screenshot_dir = os.path.join(screenshot_root, category)
    os.makedirs(screenshot_dir, exist_ok=True)

    screenshot_path = os.path.join(
        screenshot_dir,
        "{}_{}.png".format(safe_description, timestamp)
    )

    try:
        subprocess.run(
            ["gnome-screenshot", "-w", "-f", screenshot_path],
            check=True,
            timeout=15
        )

        test.log("Screenshot saved: {}".format(screenshot_path))
        return screenshot_path

    except Exception as error:
        test.warning(
            "Screenshot capture failed: {}".format(error)
        )
        return None

def open_expert_screen():
    click_and_report(
        names.gbExpert_expertButton_QPushButton,
        "Open Expert screen"
    )
def adjust_primary_pulse_energy_frequency():
    test.log("========== ADJUST PRIMARY PARAMETERS ==========")

    # Increase primary pulse energy 3 times
    for i in range(1, 4):
        click_and_report(
            names.pulseEnergyWidget_incrementButton_QPushButton,
            "Increase pulse energy - {}".format(i)
        )

    # Increase primary frequency 2 times
    for i in range(1, 3):
        click_and_report(
            names.frequencyWidget_incrementButton_QPushButton,
            "Increase frequency - {}".format(i)
        )

    # Decrease primary frequency once
    click_and_report(
        names.frequencyWidget_decrementButton_QPushButton,
        "Decrease frequency"
    )

    # Decrease primary pulse energy once
    click_and_report(
        names.pulseEnergyWidget_decrementButton_QPushButton,
        "Decrease pulse energy"
    )


def adjust_secondary_pulse_energy_frequency():
    test.log("========== ADJUST SECONDARY PARAMETERS ==========")

    # Increase secondary pulse energy 2 times
    for i in range(1, 3):
        click_and_report(
            names.pulseEnergyWidget_incrementButton_QPushButton_2,
            "Increase secondary pulse energy - {}".format(i)
        )

    # Increase secondary frequency 2 times
    for i in range(1, 3):
        click_and_report(
            names.frequencyWidget_incrementButton_QPushButton_2,
            "Increase secondary frequency - {}".format(i)
        )

    test.log("Secondary pulse energy and frequency adjustments completed")


def interact_with_value_and_fiber_labels():
    mouse_click_and_report(
        names.valueFrame_valueLabel_QLabel,
        83, 16,
        "Click value label"
    )

    mouse_click_and_report(
        names.fiberUsesFrame_nameLabel_QLabel,
        41, 39,
        "Click fiber uses label"
    )


def interact_with_pedal_preset_tabs():
    mouse_click_and_report(
        names.rightPedalWidget_wdPresetTabs_TabWidget,
        488, 25,
        "Click right pedal preset tabs"
    )

    mouse_click_and_report(
        names.leftPedalWidget_wdPresetTabs_TabWidget,
        466, 54,
        "Click left Pedal preset tabs"
    )


def change_standby_ready_states():
    click_and_report(
        names.stateSwitch_standbyButton_QPushButton,
        "Select Standby state"
    )

    click_and_report(
        names.stateSwitch_readyButton_QPushButton,
        "Select Ready state"
    )


def interact_with_quantity_value_labels():
    mouse_click_and_report(
        names.valueLabelBackgroundWithQuantityText_valueLabel_QLabel,
        157, 35,
        "Click quantity value label 1"
    )

    mouse_click_and_report(
        names.valueLabelBackgroundWithQuantityText_valueLabel_QLabel_2,
        214, 70,
        "Click quantity value label 2"
    )

    mouse_click_and_report(
        names.valueLabelBackgroundWithQuantityText_valueLabel_QLabel_3,
        189, 62,
        "Click quantity value label 3"
    )



def interact_with_pulse_mode_frequency_widget():
    mouse_click_and_report(
        names.pulseModeWidget_frequencyWidgetEmission_ParameterWithBoundedValueWidget,
        366, 0,
        "Click pulse mode frequency widget"
    )
  
# COMMON HOME-PAGE NAVIGATION
# ============================================================

def navigate_soft_tissue_quick_start():
    test.log("========== SOFT TISSUE QUICK START ==========")

    click_and_report(
        names.homeScreen_pbSoftTissueQuickStart_QToolButton,
        "Open Soft Tissue Quick Start"
    )

    mouse_click_and_report(
        names.qt_tabwidget_stackedwidget_wdLeftPedalTreatmentLayout_QWidget,
        537, 2,
        "Click left pedal treatment area"
    )

    mouse_click_and_report(
        names.quickStartScreen_tbRightPedalTreatment_TabWidget,
        232, 5,
        "Click right pedal treatment tab"
    )

    click_and_report(
        names.buttonsBar_homeButton_QPushButton_5,
        "Return home from Soft Tissue Quick Start"
    )

# def navigate_stone_quick_start_Stonesense():
    
def navigate_stone_quick_start():
    test.log("========== STONE QUICK START ==========")

    click_and_report(
        names.homeScreen_pbStoneQuickStart_QToolButton,
        "Open Stone Quick Start"
    )

    mouse_click_and_report(
        names.topBar_buttonsBar_ButtonsBar_5,
        387, 8,
        "Click Stone Quick Start top bar"
    )

    mouse_click_and_report(
        names.quickStartScreen_wdTabWidgets_QWidget,
        847, 2,
        "Click Stone Quick Start tab"
    )

    click_and_report(
        names.buttonsBar_homeButton_QPushButton_5,
        "Return home from Stone Quick Start"
    )


def navigate_stone_assistant():
    test.log("========== STONE ASSISTANT ==========")

    click_and_report(
        names.homeScreen_pbStoneAssistant_QToolButton,
        "Open Stone Assistant"
    )

    mouse_click_and_report(
        names.stoneAssistantModeScreen_hintLabel_QLabel,
        299, 18,
        "Click Stone Assistant hint area 1"
    )

    mouse_click_and_report(
        names.stoneAssistantModeScreen_hintLabel_QLabel,
        1025, 56,
        "Click Stone Assistant hint area 2"
    )

    click_and_report(
        names.buttonsBar_homeButton_QPushButton_7,
        "Return home from Stone Assistant"
    )


def navigate_logoff():
    test.log("========== LOGOFF FLOW ==========")

    click_and_report(
        names.homeScreen_logoffButton_QPushButton,
        "Click Logoff button"
    )

    mouse_click_and_report(
        names.logOffSystem_centralWidget_QFrame,
        180, 566,
        "Click logoff confirmation area"
    )

    click_and_report(
        names.buttonsFrame_rejectButton_QPushButton_2,
        "Click logoff dialog Reject button"
    )


def navigate_logs():
    test.log("========== LOGS ==========")

    click_and_report(
        names.homeScreen_logButton_QPushButton,
        "Open Logs"
    )

    click_and_report(
        names.buttonsBar_homeButton_QPushButton_3,
        "Return home from Logs"
    )


def navigate_profiles():
    test.log("========== PROFILES ==========")

    click_and_report(
        names.homeScreen_profilesButton_QPushButton,
        "Open Profiles"
    )

    click_and_report(
        names.buttonsBar_homeButton_QPushButton_2,
        "Return home from Profiles"
    )


def navigate_settings_and_home():
    test.log("========== SETTINGS ==========")

    click_and_report(
        names.homeScreen_settingsButton_QPushButton,
        "Open Settings"
    )

    click_and_report(
        names.buttonsBar_homeButton_QPushButton_8,
        "Return home from Settings"
    )


def navigate_complete_home_page():
    """
    Run the recorded home-page navigation sequence.
    Assumes the application starts on the login screen.
    """

    enter_login_pin()
    capture_screenshot("HOME_PAGE")

    navigate_soft_tissue_quick_start()
    navigate_soft_tissue_assistant()

    # navigate_stone_quick_start()
    # navigate_stone_assistant()

    navigate_logoff()
    navigate_logs()
    navigate_profiles()
    navigate_settings_and_home()

    test.log("Completed common home-page navigation")



def navigate_system_date_time():
    test.log("========== SYSTEM DATE AND TIME CONFIGURATION ==========")

    enter_login_pin()
    click_and_report(
        names.homeScreen_settingsButton_QPushButton,
        "Open Settings"
    )

    try:
        clickTab(
            waitForObject(names.settingsScreen_tbSystemInfo_TabWidget, 20000),
            "LOGS"
        )
        test.passes("PASS: Open Logs tab")
    except Exception as error:
        test.fail("FAIL: Open Logs tab - {}".format(error))
        raise

    click_and_report(
        names.settingsScreen_pbService_QPushButton,
        "Open Service screen"
    )

    # Enter service PIN 9999
    for index in range(5):
        click_and_report(
            names.numpad_pushButton_9_NumpadButton,
            "Enter service PIN digit 9, press {} of 4".format(index + 1)
        )

    # Open date and time configuration
    mouse_click_and_report(
        names.systemConfigurationTab_dateAndTimePanel_QFrame,
        244, 51,
        "Open Date and Time panel"
    )

    click_and_report(
        names.frameSystemConfiguration_pbSysConfSetDateTime_QPushButton,
        "Open Set Date and Time dialog"
    )

    click_and_report(
        names.buttonsFrame_acceptButton_QPushButton_3,
        "Accept date and time dialog"
    )

    # Modify month, day, year and time
    click_and_report(
        names.npMonth_pbDecrement_QPushButton,
        "Decrease month once"
    )
    click_and_report(
        names.npMonth_pbDecrement_QPushButton,
        "Decrease month twice"
    )

    try:
        doubleClick(
            waitForObject(names.npDay_pbDecrement_QPushButton, 20000),
            56, 59, Qt.NoModifier, Qt.LeftButton
        )
        test.passes("PASS: Decrease day using double-click")
    except Exception as error:
        test.fail("FAIL: Decrease day - {}".format(error))
        raise

    click_and_report(
        names.npYear_pbDecrement_QPushButton,
        "Decrease year once"
    )
    click_and_report(
        names.npYear_pbDecrement_QPushButton,
        "Decrease year twice"
    )

    click_and_report(
        names.tpTime_pbPM_QPushButton,
        "Select PM"
    )
    click_and_report(
        names.tpTime_pbAM_QPushButton,
        "Select AM"
    )
    click_and_report(
        names.npMinute_pbIncrement_QPushButton,
        "Increment minute"
    )

    click_and_report(
        names.mainFrame_pbAccept_QPushButton,
        "Accept date and time changes"
    )

    # Repeat the recorded date/time dialog sequence
    click_and_report(
        names.frameSystemConfiguration_pbSysConfSetDateTime_QPushButton,
        "Reopen Set Date and Time dialog - first time"
    )
    click_and_report(
        names.buttonsFrame_acceptButton_QPushButton_3,
        "Accept date and time dialog - first repeat"
    )
    click_and_report(
        names.npYear_pbDecrement_QPushButton,
        "Decrease year again"
    )
    click_and_report(
        names.mainFrame_pbAccept_QPushButton,
        "Accept second date and time changes"
    )

    # Final recorded sequence
    click_and_report(
        names.frameSystemConfiguration_pbSysConfSetDateTime_QPushButton,
        "Reopen Set Date and Time dialog - final time"
    )
    click_and_report(
        names.buttonsFrame_rejectButton_QPushButton_3,
        "Reject final date and time dialog"
    )

    click_and_report(
        names.buttonsBar_backButton_QPushButton,
        "Navigate back from System Configuration"
    )

    click_and_report(
        names.buttonsBar_homeButton_QPushButton_8,
        "Return home from Settings"
    )

    test.passes("PASS: System date and time navigation completed")


def navigate_stone_quick_start_presets():
    test.log("========== STONE QUICK START PRESETS ==========")

    # Login
    enter_login_pin()

    # Open Stone Quick Start
    click_and_report(
        names.homeScreen_pbStoneQuickStart_QToolButton,
        "Open Stone Quick Start"
    )

    # Left Main Presets: next page twice
    for index in range(2):
        click_and_report(
            names.tabLeftMainPresets_nextPageButton_QPushButton,
            "Left Main Presets - Next Page {}".format(index + 1)
        )

    # Right Main Presets: next page three times
    for index in range(3):
        click_and_report(
            names.tabRightMainPresets_nextPageButton_QPushButton,
            "Right Main Presets - Next Page {}".format(index + 1)
        )

    # Open User Presets tab
    try:
        clickTab(
            waitForObject(
                names.wdLeftPedalTreatmentLayout_tbLeftPedalPresets_TabWidget,
                20000
            ),
            "USER PRESETS"
        )
        test.passes("PASS: Open Left Pedal USER PRESETS tab")
    except Exception as error:
        test.fail("FAIL: Open USER PRESETS tab - {}".format(error))
        raise

    # Left User Presets: next page twice
    for index in range(2):
        click_and_report(
            names.tabLeftUserPresets_nextPageButton_QPushButton,
            "Left User Presets - Next Page {}".format(index + 1)
        )

    # Right Main Presets: next page once more
    click_and_report(
        names.tabRightMainPresets_nextPageButton_QPushButton,
        "Right Main Presets - Additional Next Page"
    )

    # Return home
    click_and_report(
        names.buttonsBar_homeButton_QPushButton_5,
        "Return home from Stone Quick Start"
    )

    test.passes("PASS: Stone Quick Start preset navigation completed")
    
    
#Soft Tussue------------------------


def click_and_report(object_name, description):
    try:
        obj = waitForObject(object_name, 20000)
        clickButton(obj)
        test.passes("PASS: " + description)

    except Exception as error:
        test.fail(
            "FAIL: {} - {}".format(description, error)
        )
        raise


# --------------------------------------------------
# MOUSE CLICK AND REPORT RESULT
# --------------------------------------------------

def mouse_click_and_report(
    object_name, x, y, description
):
    try:
        obj = waitForObject(object_name, 20000)

        mouseClick(
            obj,
            x,
            y,
            Qt.NoModifier,
            Qt.LeftButton
        )

        test.passes("PASS: " + description)

    except Exception as error:
        test.fail(
            "FAIL: {} - {}".format(description, error)
        )
        raise


# --------------------------------------------------
# VERIFICATION POINT: OBJECT EXISTS
# --------------------------------------------------

def verify_object_exists(object_name, description):
    try:
        waitForObject(object_name, 20000)
        test.passes("PASS: " + description)

    except Exception as error:
        test.fail(
            "FAIL: {} - {}".format(description, error)
        )
        raise


# --------------------------------------------------
# LOGIN USING PIN 8888
# --------------------------------------------------

def enter_login_pin():
    """
    Method Used for login page 
    """
    for i in range(4):
        clickButton(
            waitForObject(
                names.numpad_pushButton_8_NumpadButton,
                20000
            )
        )

    click_and_report(
        names.mainFrame_okButton_QPushButton,
        "Click login OK button"
    )


# --------------------------------------------------
# SOFT TISSUE ASSISTANT PROCEDURE NAVIGATION
# --------------------------------------------------

def navigate_soft_tissue_assistant():
    enter_login_pin()
    verify_object_exists(
        names.homeScreen_pbSoftTissueAssistant_QToolButton,
        "Soft Tissue Assistant option is available on Home screen"
    )
    click_and_report(
        names.homeScreen_pbSoftTissueAssistant_QToolButton,
        "Open Soft Tissue Assistant"
    )
    
    verify_object_exists(
        names.softTissueAssistantModeScreen_gbSoftTissueProcedures_QFrame,
        "Soft Tissue Assistant procedure screen is displayed"
    )
    
    capture_screenshot("Soft_Tissue_Assistant_Procedure_Screen")
    mouse_click_and_report(
        names.softTissueAssistantModeScreen_gbSoftTissueProcedures_QFrame,
        177, 99,
        "Select Soft Tissue procedures area"
    )
    click_and_report(
        names.gbSoftTissueProcedures_pbTumor_QPushButton,
        "Select Tumor procedure"
    )

    verify_object_exists(
        names.fiberFrame_recommendedFiberName_QLabel,
        "Recommended fiber name label is available for Tumor"
    )
    click_and_report(
        names.gbSoftTissueProcedures_pbIncision_QPushButton,
        "Select Incision procedure"
    )
    click_and_report(
        names.gbBphProcedures_pbEnucleation_QPushButton,
        "Select Enucleation procedure"
    )

    click_and_report(
        names.gbBphProcedures_pbEnucleationLow_ButtoWithCaptionAndSmallerSubCaption,
        "Select Enucleation Low procedure"
    )
    click_and_report(
        names.gbBphProcedures_pbVaporize_QPushButton,
        "Select Vaporize procedure"
    )

    mouse_click_and_report(
        names.fiberFrame_recommendedFiberName_QLabel,
        223, 11,
        "Click recommended fiber name after Vaporize"
    )

    click_and_report(
        names.gbBphProcedures_pbEnucleationLow_ButtoWithCaptionAndSmallerSubCaption,
        "Select Enucleation Low again"
    )
    mouse_click_and_report(
        names.fiberFrame_recommendedFiberName_QLabel,
        207, 20,
        "Click recommended fiber name after Enucleation Low"
    )
    click_and_report(
        names.gbBphProcedures_pbEnucleation_QPushButton,
        "Select Enucleation procedure again"
    )
    mouse_click_and_report(
        names.fiberFrame_recommendedFiberIcon_QLabel,
        21, 7,
        "Click recommended fiber icon"
    )

    click_and_report(
        names.gbSoftTissueProcedures_pbTumor_QPushButton,
        "Select Tumor procedure again"
    )
    mouse_click_and_report(
        names.fiberFrame_recommendedFiberLabel_QLabel,
        202, 10,
        "Click recommended fiber label"
    )

    click_and_report(
        names.gbSoftTissueProcedures_pbIncision_QPushButton,
        "Select Incision procedure again"
    )
    mouse_click_and_report(
        names.fiberFrame_recommendedFiberName_QLabel,
        116, 25,
        "Click recommended fiber name after Incision"
    )

    click_and_report(
        names.buttonsBar_homeButton_QPushButton_6,
        "Return to Home screen"
    )
    verify_object_exists(
        names.homeScreen_pbSoftTissueAssistant_QToolButton,
        "Home screen is displayed after procedure navigation"
    )

#Presets--------------------


    PRESET_LIST_OBJECTS = {
        "STONE":
            names.tabSettingsPresetsUserStonePresets_presetListView_PresetListView,
    
        "SOFT TISSUE":
            names.tabSettingsPresetsUserSoftTissuePresets_presetListView_PresetListView
    }
    
    SOFT_TISSUE_PRESET_NAMES = [
        "Soft Tissue 1",
        "Soft Tissue 2",
        "Soft Tissue 3",
        "Soft Tissue 4",
        "Soft Tissue 5",
        "Soft Tissue 6"
    ]
    
    STONE_PRESET_NAMES = [
        "Stone 1",
        "Stone 2",
        "Stone 3",
        "Stone 4",
        "Stone 5",
        "Stone 6"
    ]


def _preset_object_exists(object_name, timeout=1000):
    """Return True if a Squish object appears within timeout milliseconds."""
    try:
        waitForObjectExists(object_name, timeout)
        return True
    except LookupError:
        return False
    except Exception as error:
        test.log("Object existence check failed for {}: {}".format(object_name, error))
        return False


def navigate_to_preset_category(category):
    """Open USER PRESETS and select a category without reopening Settings unnecessarily."""
    category = category.strip().upper()

    if category not in PRESET_LIST_OBJECTS:
        raise ValueError(
            "Invalid category: {}. Use STONE or SOFT TISSUE.".format(category)
        )

    test.log("========== NAVIGATE TO {} PRESETS ==========".format(category))

    # If a preset list is already present, the test is already in USER PRESETS.
    # Do not click the HomeScreen Settings button again: HomeScreen may no longer
    # be the active screen, which causes Squish LookupError.
    presets_tab = names.wdPresetsLayout_tbPresetsForSettings_TabWidget
    already_in_presets = _preset_object_exists(presets_tab, 1000)

    if not already_in_presets:
        settings_button = names.homeScreen_settingsButton_QPushButton
        if not _preset_object_exists(settings_button, 1000):
            test.fail(
                "Cannot open USER PRESETS: neither the USER PRESETS tab nor "
                "the HomeScreen Settings button is available. Check the current screen."
            )
            return False

        click_and_report(settings_button, "Open Settings")

    settings_tabs = names.settingsScreen_tbSystemInfo_TabWidget
    if not _preset_object_exists(settings_tabs, 5000):
        test.fail("Settings tabs are not visible; cannot select USER PRESETS")
        return False

    # Select USER PRESETS only when it is not already the active screen.
    if not already_in_presets:
        clickTab(waitForObject(settings_tabs, 20000), "USER\nPRESETS")
        test.passes("Opened USER PRESETS")

    category_tabs = names.wdPresetsLayout_tbPresetsForSettings_TabWidget
    clickTab(waitForObject(category_tabs, 20000), category)
    test.passes("Selected {} category".format(category))

    waitForObject(PRESET_LIST_OBJECTS[category], 20000)
    test.passes("{} preset list is visible".format(category))
    return True


def read_preset_names(category):
    """Read preset names from a Qt model-backed list view."""

    category = category.strip().upper()

    if category not in PRESET_LIST_OBJECTS:
        raise ValueError("Category must be STONE or SOFT TISSUE")

    view = waitForObject(PRESET_LIST_OBJECTS[category], 20000)
    model = view.model()
    preset_names = []

    for row in range(model.rowCount()):
        index = model.index(row, 0)
        value = model.data(index, Qt.DisplayRole)

        if value is not None and str(value).strip():
            preset_names.append(str(value).strip())

    test.log(
        "{} preset count: {}".format(category, len(preset_names))
    )

    for index, preset_name in enumerate(preset_names, 1):
        test.log("Preset {}: {}".format(index, preset_name))

    return preset_names


def verify_six_presets(category):
    """Verify that six presets exist in the selected category."""

    preset_names = read_preset_names(category)

    if len(preset_names) == 6:
        test.passes(
            "PASS: Exactly six presets exist in {}".format(
                category.upper()
        )  
    )
        return True

    test.fail(
        "FAIL: Expected 6 presets in {}, found {}".format(
            category.upper(), len(preset_names)
        )
    )
    return False



def verify_preset_count(category, expected_count):
    """Verify an exact preset count, useful after create/edit/delete flows."""
    actual_names = read_preset_names(category)
    actual_count = len(actual_names)
    if actual_count == expected_count:
        test.passes("PASS: {} has exactly {} presets".format(category.upper(), expected_count))
        return True
    test.fail("FAIL: {} expected {} presets, found {}".format(category.upper(), expected_count, actual_count))
    return False


def select_preset_by_name(category, preset_name):
    """Select a preset using its displayed name."""

    category = category.strip().upper()

    if category not in PRESET_LIST_OBJECTS:
        raise ValueError("Category must be STONE or SOFT TISSUE")

    view = waitForObject(PRESET_LIST_OBJECTS[category], 20000)
    model = view.model()

    for row in range(model.rowCount()):
        index = model.index(row, 0)
        value = model.data(index, Qt.DisplayRole)

        if value is not None and str(value).strip() == preset_name:
            rect = view.visualRect(index)

            mouseClick(
                view,
                rect.x() + rect.width() // 2,
                rect.y() + rect.height() // 2,
                Qt.NoModifier,
                Qt.LeftButton
            )

            test.passes(
                "Selected {} preset: {}".format(category, preset_name)
            )
            return True

    test.fail(
        "Preset '{}' not found in {}".format(preset_name, category)
    )
    return False


def create_six_presets(category, preset_names, add_button, name_field, save_button):
    """Create six presets using the supplied Squish Object Map references.

    name_field must identify the editable field visible after Add opens
    the keyboard popup. Use the exact Object Map reference from names.py.
    """
    category = category.strip().upper()
    if category not in PRESET_LIST_OBJECTS:
        raise ValueError("Category must be STONE or SOFT TISSUE")
    if len(preset_names) != 6:
        raise ValueError("Provide exactly six preset names")

    navigate_to_preset_category(category)

    for preset_name in preset_names:
        test.log("Creating {} preset '{}'".format(category, preset_name))
        try:
            clickButton(waitForObject(add_button, 20000))
            # Wait for the editor only after Add has opened the keyboard popup.
            field = waitForObject(name_field, 20000)
            setFocus(field)
            setText(field, preset_name)
            clickButton(waitForObject(save_button, 20000))
            test.passes("PASS: Created {} preset '{}'".format(category, preset_name))
        except Exception as error:
            test.fail(
                "FAIL: Could not create {} preset '{}'. Verify the Add button, "
                "keyboard popup timing, and editor Object Map reference. Error: {}".format(
                    category, preset_name, error
                )
            )
            raise

    if not verify_six_presets(category):
        raise AssertionError(
            "Preset creation finished, but {} does not contain exactly six presets".format(category)
        )


def run_stone_and_soft_tissue_preset_checks():
    """Navigate to both categories and verify six presets in each."""

    navigate_to_preset_category("SOFT TISSUE")
    soft_tissue_ok = verify_six_presets("SOFT TISSUE")

    navigate_to_preset_category("STONE")
    stone_ok = verify_six_presets("STONE")

    if soft_tissue_ok and stone_ok:
        test.passes("PASS: Both categories contain six presets")
    else:
        test.fail("FAIL: Preset count verification failed")

        raise AssertionError(
            "STONE or SOFT TISSUE does not contain exactly six presets"
        )
        

# ============================================================
# EDIT AN EXISTING PRESET
# ============================================================

def edit_preset(category, old_name, new_name):
    """
    Select an existing preset, open Edit, change its name,
    save it, and verify the updated name.

    Uses the existing Object Map and helper functions.
    """

    category = category.strip().upper()

    test.log(
        "========== EDIT PRESET: {} ==========".format(category)
    )

    # Navigate to the requested category
    navigate_to_preset_category(category)

    # Select the preset to edit
    if not select_preset_by_name(category, old_name):
        raise AssertionError(
            "Cannot edit preset '{}': preset was not found".format(
                old_name
            )
        )

    # Click Edit
    click_and_report(
        names.settingsScreen_editButton_QPushButton,
        "Click Edit for preset '{}'".format(old_name)
    )

    # Open the preset-name editor
    click_and_report(
        names.centralWidget_pbName_QPushButton,
        "Open preset name editor"
    )

    # Enter the new name
    name_field = waitForObject(
        names.keyboardPopup_wdEdit_WdLineEdit, 20000
    )
    setText(name_field, new_name)

    # Confirm the name dialog
    click_and_report(
        names.centralWidget_okButton_QPushButton_2,
        "Confirm new preset name"
    )

    # Save the edited preset
    click_and_report(
        names.pulseModeWidget_saveButton_QPushButton,
        "Save edited preset"
    )

    # Verify the new name is present
    updated_names = read_preset_names(category)

    if new_name in updated_names:
        test.passes(
            "PASS: Renamed '{}' to '{}' in {}".format(
                old_name, new_name, category
            )
        )
        return True

    test.fail(
        "Edited preset '{}' was not found after saving in {}".format(
            new_name, category
        )
    )

    raise AssertionError(
        "Preset rename verification failed: {}".format(new_name)
    )


# ============================================================
# DELETE AN EXISTING PRESET
# ============================================================

def delete_preset(category, preset_name):
    """
    Select an existing preset, delete it, confirm deletion,
    and verify that it is no longer present.
    """

    category = category.strip().upper()

    test.log(
        "========== DELETE PRESET: {} ==========".format(category)
    )

    # Navigate to the requested category
    navigate_to_preset_category(category)

    # Read the list before deleting
    names_before = read_preset_names(category)

    if preset_name not in names_before:
        raise AssertionError(
            "Cannot delete preset '{}': preset was not found".format(
                preset_name
            )
        )

    # Select the preset
    if not select_preset_by_name(category, preset_name):
        raise AssertionError(
            "Cannot select preset '{}' for deletion".format(
                preset_name
            )
        )

    # Click Delete
    click_and_report(
        names.settingsScreen_deletePresetButton_QPushButton,
        "Click Delete for preset '{}'".format(preset_name)
    )

    # Confirm deletion
    click_and_report(
        names.buttonsFrame_acceptButton_QPushButton_4,
        "Confirm deletion of preset '{}'".format(preset_name)
    )

    # Verify deletion
    names_after = read_preset_names(category)

    if preset_name not in names_after:
        test.passes(
            "PASS: Deleted preset '{}' from {}".format(
                preset_name, category
            )
        )
        return True

    test.fail(
        "Preset '{}' still exists after deletion in {}".format(
            preset_name, category
        )
    )

    raise AssertionError(
        "Preset deletion verification failed: {}".format(preset_name)
    )
    
def move_treatment_screen_sliders_to_right():
    test.log("========== MOVE TREATMENT SLIDERS TO RIGHT ==========")

    mouseDrag(
        waitForObject(names.indexPicker_valuePicker_IntervalSlider_4),
        82, 20, 409, -3, 1, Qt.LeftButton
    )
    test.passes("PASS: Treatment slider 4 moved to right")

    mouseDrag(
        waitForObject(names.indexPicker_valuePicker_IntervalSlider_5),
        43, 18, 508, 15, 1, Qt.LeftButton
    )
    test.passes("PASS: Treatment slider 5 moved to right")

    mouseDrag(
        waitForObject(names.indexPicker_valuePicker_IntervalSlider_6),
        68, 24, 408, 17, 1, Qt.LeftButton
    )
    test.passes("PASS: Treatment slider 6 moved to right")

    mouseDrag(
        waitForObject(names.indexPicker_valuePicker_IntervalSlider_7),
        45, 31, 539, -22, 1, Qt.LeftButton
    )
    test.passes("PASS: Treatment slider 7 moved to right")


def move_treatment_screen_sliders_to_both_extremes():
    test.log("========== TREATMENT SLIDER EXTREME TEST ==========")

    # Move all sliders toward the right using recorded coordinates
    move_treatment_screen_sliders_to_right()

    test.log(
        "Rightward slider drags completed. "
        "Verify visually that each slider reached its endpoint."
    )

# ============================================================
# COMPLETE RECORDED NAVIGATION FLOW
# Uses the object names and order supplied for the current test.
# ============================================================

def navigate_complete_recorded_flow():
    test.log("========== START COMPLETE RECORDED NAVIGATION FLOW ==========")

    # Login PIN: 8888
    enter_login_pin()

    # Soft Tissue Quick Start
    click_and_report(
        names.homeScreen_pbSoftTissueQuickStart_QToolButton,
        "Open Soft Tissue Quick Start"
    )
    click_and_report(
        names.tabLeftMainPresets_nextPageButton_QPushButton,
        "Soft Tissue Quick Start - Left Main Presets Next Page"
    )
    click_and_report(
        names.tabRightMainPresets_nextPageButton_QPushButton,
        "Soft Tissue Quick Start - Right Main Presets Next Page"
    )
    clickTab(
        waitForObject(names.wdLeftPedalTreatmentLayout_tbLeftPedalPresets_TabWidget, 20000),
        "USER PRESETS"
    )
    clickTab(
        waitForObject(names.wdRightPedalTreatmentLayout_tbRightPedalPresets_TabWidget, 20000),
        "USER PRESETS"
    )
    clickTab(
        waitForObject(names.quickStartScreen_tbLeftPedalTreatment_TabWidget, 20000),
        "SELECT LEFT PEDAL TREATMENT"
    )
    clickTab(
        waitForObject(names.quickStartScreen_tbRightPedalTreatment_TabWidget, 20000),
        "SELECT RIGHT PEDAL TREATMENT"
    )
    click_and_report(names.buttonsBar_homeButton_QPushButton_5,
                     "Return home from Soft Tissue Quick Start")

    # Soft Tissue Assistant
    click_and_report(names.homeScreen_pbSoftTissueAssistant_QToolButton,
                     "Open Soft Tissue Assistant")
    click_and_report(names.gbSoftTissueProcedures_pbIncision_QPushButton,
                     "Select Incision procedure")
    click_and_report(names.gbSoftTissueProcedures_pbTumor_QPushButton,
                     "Select Tumor procedure")
    click_and_report(names.gbBphProcedures_pbEnucleation_QPushButton,
                     "Select Enucleation procedure")
    click_and_report(
        names.gbBphProcedures_pbEnucleationLow_ButtoWithCaptionAndSmallerSubCaption,
        "Select Low Enucleation procedure"
    )
    click_and_report(names.gbBphProcedures_pbVaporize_QPushButton,
                     "Select Vaporize procedure")
    click_and_report(names.buttonsBar_homeButton_QPushButton_6,
                     "Return home from Soft Tissue Assistant")

    # Stone Quick Start
    click_and_report(names.homeScreen_pbStoneQuickStart_QToolButton,
                     "Open Stone Quick Start")
    click_and_report(names.tabLeftMainPresets_nextPageButton_QPushButton,
                     "Stone Quick Start - Left Main Presets Next Page 1")
    click_and_report(names.tabLeftMainPresets_nextPageButton_QPushButton,
                     "Stone Quick Start - Left Main Presets Next Page 2")
    clickTab(
        waitForObject(names.wdLeftPedalTreatmentLayout_tbLeftPedalPresets_TabWidget, 20000),
        "USER PRESETS"
    )
    click_and_report(names.tabRightMainPresets_nextPageButton_QPushButton,
                     "Stone Quick Start - Right Main Presets Next Page 1")
    click_and_report(names.tabRightMainPresets_nextPageButton_QPushButton,
                     "Stone Quick Start - Right Main Presets Next Page 2")
    clickTab(
        waitForObject(names.wdRightPedalTreatmentLayout_tbRightPedalPresets_TabWidget, 20000),
        "USER PRESETS"
    )
    click_and_report(names.buttonsBar_homeButton_QPushButton_5,
                     "Return home from Stone Quick Start")

    # Stone Assistant
    click_and_report(names.homeScreen_pbStoneAssistant_QToolButton,
                     "Open Stone Assistant")
    mouse_click_and_report(names.locationFrame_label_3_QLabel, 158, 26,
                           "Click Stone Assistant location label")
    mouse_click_and_report(names.stoneAssistantModeScreen_hintLabel_QLabel, 776, 21,
                           "Click Stone Assistant hint label")
    click_and_report(names.buttonsBar_homeButton_QPushButton_7,
                     "Return home from Stone Assistant")

    # Logs, Profiles, Settings, and Logoff
    click_and_report(names.homeScreen_logButton_QPushButton, "Open Logs")
    click_and_report(names.buttonsBar_homeButton_QPushButton_3, "Return home from Logs")
    click_and_report(names.homeScreen_profilesButton_QPushButton, "Open Profiles")
    click_and_report(names.buttonsBar_homeButton_QPushButton_2, "Return home from Profiles")
    click_and_report(names.homeScreen_settingsButton_QPushButton, "Open Settings")
    click_and_report(names.buttonsBar_homeButton_QPushButton_8, "Return home from Settings")
    click_and_report(names.homeScreen_logoffButton_QPushButton, "Open Logoff")
    click_and_report(names.buttonsFrame_rejectButton_QPushButton_2,
                     "Confirm/close Logoff dialog")

    test.passes("PASS: Complete recorded navigation flow finished")

def navigateto_Treatmentscreen_stone_QuickStart():
    clickButton(waitForObject(names.homeScreen_pbStoneQuickStart_QToolButton))
    mouseClick(waitForObjectItem(names.tabLeftMainPresets_leftPresetsView_PresetListView, "_1"), 445, 65, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.tabRightMainPresets_rightPresetsView_PresetListView, "_1"), 187, 63, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.quickStartScreen_pbContinue_QPushButton))
# -*- coding: utf-8 -*-
