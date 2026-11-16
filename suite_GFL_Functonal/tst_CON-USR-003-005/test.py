# -*- coding: utf-8 -*-

import names
import json

def get_preset_count(view_name):
    return waitForObject(view_name).presetCount

# def get_preset(view_name, preset_name):
#     view = waitForObject(view_name)
#     data = json.loads(str(view.presetJsonByName(preset_name)))
#     test.verify(bool(data), "Preset '%s' found in list" % preset_name)
#     return data

def get_preset(view_name, preset_name):

    view = waitForObject(view_name)
    preset_names = view.presetNames

    for i in range(preset_names.size()):

        actual_name = str(preset_names.at(i)).strip()

        if actual_name == preset_name:

            data = json.loads(str(view.presetJsonAt(i)))

            # Verify that the retrieved JSON belongs to the requested preset.
            test.verify(
                data.get("name") == preset_name,
                "Preset '%s' retrieved correctly. Actual: %s" %
                (preset_name, data.get("name"))
            )

            return data

    test.fail("Preset '%s' not found in preset list" % preset_name)
    return None


def get_all_presets(view_name):

    view = waitForObject(view_name)
    preset_names = view.presetNames

    presets = {}

    for i in range(preset_names.size()):

        preset_name = str(preset_names.at(i)).strip()

        if not preset_name:
            continue

        data = json.loads(str(view.presetJsonAt(i)))

        if data.get("name") == preset_name:
            presets[preset_name] = data

            test.log("Captured preset: %s | %s" %
                     (preset_name, data))

        else:
            test.fail(
                "Preset data mismatch. Expected: %s | Actual: %s" %
                (preset_name, data.get("name"))
            )

    return presets

def get_preset_at(view_name, index):
    view = waitForObject(view_name)
    return json.loads(str(view.presetJsonAt(index)))

def dump_list(view_name):
    view = waitForObject(view_name)
    test.log("presetCount = %s" % view.presetCount)
    n = view.presetNames
    for i in range(n.size()):
        test.log("[%d] %s | %s | f=%s Hz | E=%s J | Pavg=%s W | Ppeak=%s W" % (
            i, n.at(i),
            view.presetPulseModes.at(i),
            view.presetFrequencies.at(i),
            view.presetEnergies.at(i),
            view.presetPowers.at(i),
            view.presetPeakPowers.at(i)))
    test.log("json = %s" % str(view.presetsJson))

def compare_num(label, expected, actual, tol=1e-3):
    test.verify(abs(float(expected) - float(actual)) <= tol,
                "%s: preset list=%s, treatment=%s" % (label, expected, actual))
    
def comparePresetValues(side, preset_name, expected, actual):

    test.log("{} | Comparing {}".format(side, preset_name))

    if actual is None or actual.get("status") == "ERROR":
        test.fail("{} | {} | Actual treatment values unavailable".format(
            side, preset_name
        ))
        return

    # Compare Pulse Energy
    compare_num(
        "{} | {} | Pulse Energy".format(side, preset_name),
        expected["pulseEnergy"],
        actual["pulse_energy"]
    )

    # Compare Average Power
    compare_num(
        "{} | {} | Average Power".format(side, preset_name),
        expected["averagePower"],
        actual["average_power"]
    )

    # Compare Frequency
    compare_num(
        "{} | {} | Frequency".format(side, preset_name),
        expected["frequency"],
        actual["frequency"]
    )

    # Compare Peak Power
    compare_num(
        "{} | {} | Peak Power".format(side, preset_name),
        expected["peakPower"],
        actual["peak_power"]
    )

    # Compare Pulse Mode
    expected_mode = str(expected["pulseMode"]).strip()
    actual_mode = str(actual["pulse_mode"]).strip()
    
    # Remove trademark symbol before comparison
    expected_mode = expected_mode.replace(u"\u2122", "").strip()
    actual_mode = actual_mode.replace(u"\u2122", "").strip()
    
    # Normalize extra spaces
    expected_mode = " ".join(expected_mode.split())
    actual_mode = " ".join(actual_mode.split())
    
    test.verify(
        expected_mode == actual_mode,
        "{} | {} | Pulse Mode: preset list={}, treatment={}".format(
            side, preset_name, expected_mode, actual_mode
        )
    )
    

def create_user_presets(preset_names):

    for i, preset_name in enumerate(preset_names):
        clickButton(waitForObject(names.settingsScreen_addButton_QPushButton))

        if i == 1:
            clickButton(waitForObject(names.pulseEnergyWidget_decrementButton_QPushButton))
            mouseClick(waitForObject(names.modeButton_nameLabel_QLabel_3), 89, 39, Qt.NoModifier, Qt.LeftButton)
            clickButton(waitForObject(names.centralWidget_MRP_QPushButton_2))
            snooze(.5)

        elif i == 2:
            clickButton(waitForObject(names.pulseEnergyWidget_decrementButton_QPushButton))
            snooze(.5)
            clickButton(waitForObject(names.frequencyWidget_decrementButton_QPushButton))
            mouseClick(waitForObject(names.modeButton_nameLabel_QLabel_3), 92, 3, Qt.NoModifier, Qt.LeftButton)
            clickButton(waitForObject(names.centralWidget_Fragmentation_QPushButton_2))
            snooze(.5)

        elif i == 3:
            mouseClick(waitForObject(names.modeButton_nameLabel_QLabel_3), 92, 16, Qt.NoModifier, Qt.LeftButton)
            clickButton(waitForObject(names.centralWidget_Cleaning_QPushButton_2))
            snooze(.5)

        elif i == 4:
            mouseClick(waitForObject(names.peakPowerButton_iconLabel_QLabel_3),8, 11, Qt.NoModifier, Qt.LeftButton)
            snooze(.5)
            clickButton(waitForObject(names.centralWidget_pw125_QPushButton))
            mouseClick(waitForObject(names.modeButton_nameLabel_QLabel_3), 75, 21, Qt.NoModifier, Qt.LeftButton)
            clickButton(waitForObject(names.centralWidget_Enucleation_QPushButton_2))
            snooze(.5)

        # Enter the runtime-provided name
        clickButton(waitForObject(names.centralWidget_pbName_QPushButton))

        type(waitForObject(names.keyboardPopup_wdEdit_WdLineEdit), preset_name)

        mouseClick(waitForObject(names.keyboardPopup_lbText_QLabel), 102, 34, Qt.NoModifier, Qt.LeftButton)
        clickButton(waitForObject(names.pulseModeWidget_saveButton_QPushButton))
        test.log("Created preset: %s" % preset_name)
    test.passes("Successful Confirmation of User Presets Created.")
        
def delete_all_user_presets():

    preset_view = waitForObject( names.tabSettingsPresetsUserStonePresets_presetListView_PresetListView)

    deleted_count = 0

    while preset_view.presetCount > 0:
        count_before = preset_view.presetCount

        clickButton(waitForObject(names.settingsScreen_deletePresetButton_QPushButton))

        mouseClick( waitForObjectItem(names.tabSettingsPresetsUserStonePresets_presetListView_PresetListView, "_1" ),
            475, 45, Qt.NoModifier, Qt.LeftButton)

        clickButton(waitForObject(names.buttonsFrame_acceptButton_QPushButton))

        # Wait until the model reflects the deletion
        waitFor("preset_view.presetCount < count_before", 5000)

        deleted_count += 1

        test.log("Deleted preset %d; remaining: %d" %
                 (deleted_count, preset_view.presetCount))

    test.verify(
        preset_view.presetCount == 0,
        "All user presets deleted"
    )
    
def get_user_profile_names(profiles_view):
    model = profiles_view.model()
    profile_names = []
    
    for i in range(model.rowCount()):
        index = model.index(i, 0)
        name = str(model.data(index, Qt.DisplayRole)).strip()
    
        if name:
            profile_names.append(name)    
    return profile_names


def delete_all_user_profiles():

    clickButton(waitForObject(names.homeScreen_profilesButton_QPushButton))
    profiles_view = waitForObject(names.gbProfilesView_profilesView_ProfilesTreeView)
    deleted_profiles = []

    while True:

        # Read the current list on every iteration
        profile_names = get_user_profile_names(profiles_view)

        # Empty rows are ignored; no profiles is a valid condition
        if not profile_names:
            test.log("No existing user profiles found. Cleanup not required.")
            break

        profile_name = profile_names[0]
        test.log("Deleting user profile: %s" % profile_name)

        clickButton(waitForObject(names.buttonsFrame_deleteButton_QPushButton))

        mouseClick(waitForObjectItem(names.gbProfilesView_profilesView_ProfilesTreeView,profile_name ),
            379, 83, Qt.NoModifier, Qt.LeftButton )

        clickButton(waitForObject(names.buttonsFrame_acceptButton_QPushButton))

        # Wait for the selected profile to disappear
        if not waitFor( "profile_name not in get_user_profile_names(profiles_view)", 5000):
            test.fail( "Profile '%s' was not removed. Stopping cleanup." % profile_name)
            return False

        deleted_profiles.append(profile_name)
        test.log("Successfully deleted profile: %s" % profile_name)
    remaining_profiles = get_user_profile_names(profiles_view)

    test.verify( len(remaining_profiles) == 0, "All existing user profiles deleted")
    test.log( "Total user profiles deleted: %d" % len(deleted_profiles))
    clickButton(waitForObject( names.buttonsBar_homeButton_QPushButton_4))
    return len(remaining_profiles) == 0
    
def create_user_profile(profile_name):

    clickButton(waitForObject(names.homeScreen_profilesButton_QPushButton))
    clickButton(waitForObject(names.buttonsFrame_addButton_QPushButton))

    type(waitForObject(names.keyboardPopup_wdEdit_WdLineEdit), profile_name)
    mouseClick(waitForObject(names.keyboardPopup_lbText_QLabel), 156, 18,
        Qt.NoModifier, Qt.LeftButton)
    snooze(0.5)

    profiles_view = waitForObject(names.gbProfilesView_profilesView_ProfilesTreeView)

    if not waitFor("profile_name in get_user_profile_names(profiles_view)", 5000):
        test.fail("Profile creation failed: %s" % profile_name)
        return False
    test.log("User profile created: %s" % profile_name)

    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton_3))
    return True

RIGHT_SIDE_OBJECTS = {
    "mode":
        names.modeButton_nameLabel_QLabel_2,
    
    "CW":
        names.pulseModeWidget_powerWidgetCW_ParameterSettingsWidget_2,
    
    "peak_power":
        names.pulseModeWidget_peakPowerButton_ParameterSettingsButton_2,

    "average_power_value":
        names.valueLabelBackgroundWithQuantityText_valueLabel_QLabel_2,

    "pulse_energy_value":
        names.valueDrum_Cylinder_5,

    "frequency_value":
        names.valueDrum_Cylinder_6
}

LEFT_SIDE_OBJECTS = {
    "mode":
        names.modeButton_nameLabel_QLabel,
    
    "CW":
        names.pulseModeWidget_powerWidgetCW_ParameterSettingsWidget,
    
    "peak_power":
        names.pulseModeWidget_peakPowerButton_ParameterSettingsButton,

    "average_power_value":
        names.valueLabelBackgroundWithQuantityText_valueLabel_QLabel,

    "pulse_energy_value":
        names.valueDrum_Cylinder,

    "frequency_value":
        names.valueDrum_Cylinder_2
}

def inspectPulseEnergy(pulse_obj):
    cylinder = waitForObject(pulse_obj)
    pulse_energy = float(str(cylinder.displayedValue).strip())
    return pulse_energy

def inspectFrequency(freq_obj):
    cylinder = waitForObject(freq_obj)
    frequency = float(str(cylinder.displayedValue).strip())
    return frequency

def inspectAveragePower(avg_obj):
    average_power_object = avg_obj
    average_power = float( str(waitForObjectExists(average_power_object).text).strip())    
    return average_power

def inspectPeakPower(peak_power_object):    
    try:
        peak_power = waitForObjectExists(peak_power_object)
        selected = str(peak_power.selectedPeakPower).strip()
        if not selected:
            raise ValueError("Peak Power parameter values are empty")
        return selected

    except Exception as error:
        test.fail("Peak Power extraction failed: {}".format(error)) 
        return None

def checkMode(mode_button_object):
    mode_label = waitForObjectExists(mode_button_object)
    selected_mode = str(mode_label.text).strip()
    selected_mode = " ".join(selected_mode.split())
    return selected_mode


def getPedalTabNames(tab_widget_object, side):

    tab_widget = waitForObjectExists(tab_widget_object)

    preset_names = [
        str(tab_widget.tabText(i)).strip()
        for i in range(tab_widget.count)
    ]

    test.log(
        "Available {} pedal presets: {}".format(
            side, preset_names
        )
    )

    return preset_names


def getSelectedPedalValues(parameter_objects, side):

    try:
        selected_mode = checkMode(
            parameter_objects["mode"]
        )

        average_power_def = inspectAveragePower(
            parameter_objects["average_power_value"]
        )

        pulse_energy_def = inspectPulseEnergy(
            parameter_objects["pulse_energy_value"]
        )

        frequency_def = inspectFrequency(
            parameter_objects["frequency_value"]
        )

        peak_power_data = inspectPeakPower(
            parameter_objects["peak_power"]
        )

        if peak_power_data is None:
            raise ValueError("Peak Power data unavailable")

        actual_values = {
            "pulse_energy": pulse_energy_def,
            "average_power": average_power_def,
            "frequency": frequency_def,
            "peak_power": float(peak_power_data),
            "pulse_mode": selected_mode
        }

        test.log(
            "{} PEDAL - SELECTED PARAMETER VALUES".format(side)
        )

        for parameter, value in actual_values.items():
            test.log("{}: {}".format(parameter, value))

        return actual_values

    except Exception as error:

        test.fail(
            "{} pedal parameter extraction failed: {}".format(
                side, error
            )
        )

        raise
    
def validatePedalPresets(tab_widget_object, parameter_objects, side):

    results = {}
    tab_widget = waitForObjectExists(tab_widget_object)

    presets = getPedalTabNames(tab_widget_object, side)

    for preset in presets:

        try:
            clickTab(tab_widget, preset)
            snooze(3)

            actual_values = getSelectedPedalValues(parameter_objects, side)
            results[preset] = actual_values
            test.passes("{} | {} | Parameter extraction successful".format(side, preset))           

        except Exception as error:

            results[preset] = {
                "status": "ERROR",
                "error": str(error)
            }

            test.fail("{} | {} | Parameter extraction failed: {}".format(side, preset, error))
    return results


def validateBothPedalPresets():

    results = {}

    results["LEFT"] = validatePedalPresets(
        tab_widget_object=names.leftPedalWidget_wdPresetTabs_TabWidget,
        parameter_objects=LEFT_SIDE_OBJECTS,
        side="LEFT"
    )

    results["RIGHT"] = validatePedalPresets(
        tab_widget_object=names.rightPedalWidget_wdPresetTabs_TabWidget,
        parameter_objects=RIGHT_SIDE_OBJECTS,
        side="RIGHT"
    )

    return results


def getPedalParameterVariables(all_pedal_results):

    left_pedal_pulseEnergy = {}
    left_pedal_averagePower = {}
    left_pedal_Frequency = {}
    left_pedal_peakPower = {}
    left_pedal_pulseMode = {}

    right_pedal_pulseEnergy = {}
    right_pedal_averagePower = {}
    right_pedal_Frequency = {}
    right_pedal_peakPower = {}
    right_pedal_pulseMode = {}

    for preset, values in all_pedal_results["LEFT"].items():

        if values.get("status") == "ERROR":
            continue

        left_pedal_pulseEnergy[preset] = values["pulse_energy"]
        left_pedal_averagePower[preset] = values["average_power"]
        left_pedal_Frequency[preset] = values["frequency"]
        left_pedal_peakPower[preset] = values["peak_power"]
        left_pedal_pulseMode[preset] = values["pulse_mode"]

    for preset, values in all_pedal_results["RIGHT"].items():

        if values.get("status") == "ERROR":
            continue

        right_pedal_pulseEnergy[preset] = values["pulse_energy"]
        right_pedal_averagePower[preset] = values["average_power"]
        right_pedal_Frequency[preset] = values["frequency"]
        right_pedal_peakPower[preset] = values["peak_power"]
        right_pedal_pulseMode[preset] = values["pulse_mode"]

    return (
        left_pedal_pulseEnergy,
        left_pedal_averagePower,
        left_pedal_Frequency,
        left_pedal_peakPower,
        left_pedal_pulseMode,
        right_pedal_pulseEnergy,
        right_pedal_averagePower,
        right_pedal_Frequency,
        right_pedal_peakPower,
        right_pedal_pulseMode
    )

def main():
    doubleClick(waitForObject(names.numpad_pushButton_8_NumpadButton), 94, 56, Qt.NoModifier, Qt.LeftButton)
    doubleClick(waitForObject(names.numpad_pushButton_8_NumpadButton), 94, 56, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton))  
    
    #deletion of user profiles
    delete_all_user_profiles()
    #creation of user profile
    create_user_profile("USER1")     

    #selecting user profile
    clickButton(waitForObject(names.homeScreen_profilesButton_QPushButton))
    mouseClick(waitForObjectItem(names.gbProfilesView_profilesView_ProfilesTreeView, "USER1"), 404, 57, Qt.NoModifier, Qt.LeftButton)
    if clickButton(waitForObject(names.buttonsFrame_continueButton_QPushButton)):
        test.passes("Successful Confirmation of user profile selected")  
    else:
        test.fail("Failed to select user profile")
    snooze(.5)

    clickButton(waitForObject(names.homeScreen_settingsButton_QPushButton))
    clickTab(waitForObject(names.settingsScreen_tbSystemInfo_TabWidget), "USER\nPRESETS")
    
    #deletion of user presets
    delete_all_user_presets()
    #creation of user presets
    user_preset_names = [
        "MyPreset_1",
        "MyPreset_2",
        "MyPreset_3",
        "MyPreset_4",
        "MyPreset_5"
    ]
    create_user_presets(user_preset_names)

    # #navigate to home screen
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))

    clickButton(waitForObject(names.homeScreen_pbStoneQuickStart_QToolButton))
    snooze(.5)
    clickTab(waitForObject(names.wdLeftPedalTreatmentLayout_tbLeftPedalPresets_TabWidget), "USER PRESETS")  
    snooze(.5)  
    clickTab(waitForObject(names.wdRightPedalTreatmentLayout_tbRightPedalPresets_TabWidget), "USER PRESETS")
    snooze(.5)
    
    leftView  = names.tabLeftUserPresets_leftUserPresetsView_PresetListView
    rightView = names.tabRightUserPresetsLayout_rightUserPresetsView_PresetListView

    left_presets = get_all_presets(leftView)
    right_presets = get_all_presets(rightView)
    
    # Verify that all five presets are available on both sides
    test.verify(
    len(left_presets) == 5,
    "All 5 left presets captured. Actual: %d" % len(left_presets)
    )
    
    test.verify(
    len(right_presets) == 5,
    "All 5 right presets captured. Actual: %d" % len(right_presets)
    )
    
    # Store individual preset dictionaries
    left_preset_1 = left_presets["MyPreset_1"]
    left_preset_2 = left_presets["MyPreset_2"]
    left_preset_3 = left_presets["MyPreset_3"]
    left_preset_4 = left_presets["MyPreset_4"]
    left_preset_5 = left_presets["MyPreset_5"]
    
    right_preset_1 = right_presets["MyPreset_1"]
    right_preset_2 = right_presets["MyPreset_2"]
    right_preset_3 = right_presets["MyPreset_3"]
    right_preset_4 = right_presets["MyPreset_4"]
    right_preset_5 = right_presets["MyPreset_5"]
    
    # Extract individual values for MyPreset_1 on the left
    left_pulse = left_preset_1["pulseMode"]
    left_frequency = float(left_preset_1["frequency"])
    left_energy = float(left_preset_1["pulseEnergy"])
    left_average_power = float(left_preset_1["averagePower"])
    left_peak_power = float(left_preset_1["peakPower"])
    left_emission_mode = left_preset_1["emissionMode"]
    left_treatment_type = left_preset_1["treatmentType"]
    
    # Extract individual values for MyPreset_2 on the right
    right_pulse = right_preset_2["pulseMode"]
    right_freqency = float(right_preset_2["frequency"])
    right_energy = float(right_preset_2["pulseEnergy"])
    right_average_power = float(right_preset_2["averagePower"])
    right_peak_power = float(right_preset_2["peakPower"])
    right_emission_mode = right_preset_2["emissionMode"]
    right_treatment_type = right_preset_2["treatmentType"]

    mouseClick(waitForObjectItem(names.tabLeftUserPresets_leftUserPresetsView_PresetListView, "_1"), 304, 40, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.tabRightUserPresetsLayout_rightUserPresetsView_PresetListView, "_1"), 104, 35, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.quickStartScreen_pbContinue_QPushButton))
    snooze(1)
    
    
    all_pedal_results = validateBothPedalPresets()    
    (
        left_pedal_pulseEnergy,
        left_pedal_averagePower,
        left_pedal_Frequency,
        left_pedal_peakPower,
        left_pedal_pulseMode,
    
        right_pedal_pulseEnergy,
        right_pedal_averagePower,
        right_pedal_Frequency,
        right_pedal_peakPower,
        right_pedal_pulseMode
    ) = getPedalParameterVariables(all_pedal_results)
    
    left_actual = all_pedal_results["LEFT"].get("MyPreset_1")
    
    comparePresetValues(
        side="LEFT",
        preset_name="MyPreset_1",
        expected=left_preset_1,
        actual=left_actual
    )
    
    # Compare RIGHT pedal - MyPreset_1
    right_actual = all_pedal_results["RIGHT"].get("MyPreset_1")
    
    comparePresetValues(
        side="RIGHT",
        preset_name="MyPreset_1",
        expected=right_presets["MyPreset_1"],
        actual=right_actual
    )    
    #treatmentScreen

    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton_5))
    clickButton(waitForObject(names.homeScreen_pbStoneQuickStart_QToolButton))
    clickTab(waitForObject(names.wdLeftPedalTreatmentLayout_tbLeftPedalPresets_TabWidget), "USER PRESETS")
    clickTab(waitForObject(names.wdRightPedalTreatmentLayout_tbRightPedalPresets_TabWidget), "USER PRESETS")
    mouseClick(waitForObjectItem(names.tabLeftUserPresets_leftUserPresetsView_PresetListView, "_2"), 507, 78, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.tabRightUserPresetsLayout_rightUserPresetsView_PresetListView, "_2"), 166, 60, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.quickStartScreen_pbContinue_QPushButton))
    snooze(2)
    
    all_pedal_results = validateBothPedalPresets()
    
    # Get LEFT pedal values
    left_actual = all_pedal_results["LEFT"].get("MyPreset_2")
    
    comparePresetValues(
        side="LEFT",
        preset_name="MyPreset_2",
        expected=left_preset_2,
        actual=left_actual
    )
    
    # Get RIGHT pedal values
    right_actual = all_pedal_results["RIGHT"].get("MyPreset_2")
    
    comparePresetValues(
        side="RIGHT",
        preset_name="MyPreset_2",
        expected=right_preset_2,
        actual=right_actual
    )
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton_5))
    clickButton(waitForObject(names.homeScreen_pbStoneQuickStart_QToolButton))
    clickTab(waitForObject(names.wdLeftPedalTreatmentLayout_tbLeftPedalPresets_TabWidget), "USER PRESETS")
    clickTab(waitForObject(names.wdRightPedalTreatmentLayout_tbRightPedalPresets_TabWidget), "USER PRESETS")
    mouseClick(waitForObjectItem(names.tabLeftUserPresets_leftUserPresetsView_PresetListView, "_3"), 576, 76, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.tabRightUserPresetsLayout_rightUserPresetsView_PresetListView, "_3"), 190, 45, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.quickStartScreen_pbContinue_QPushButton))
    snooze(2)
    
    all_pedal_results = validateBothPedalPresets()
    
    # Get LEFT pedal values
    left_actual = all_pedal_results["LEFT"].get("MyPreset_3")
    
    comparePresetValues(
        side="LEFT",
        preset_name="MyPreset_3",
        expected=left_preset_3,
        actual=left_actual
    )
    
    # Get RIGHT pedal values
    right_actual = all_pedal_results["RIGHT"].get("MyPreset_3")
    
    comparePresetValues(
        side="RIGHT",
        preset_name="MyPreset_3",
        expected=right_preset_3,
        actual=right_actual
    )
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton_5))
    clickButton(waitForObject(names.homeScreen_pbStoneQuickStart_QToolButton))
    clickTab(waitForObject(names.wdLeftPedalTreatmentLayout_tbLeftPedalPresets_TabWidget), "USER PRESETS")
    clickTab(waitForObject(names.wdRightPedalTreatmentLayout_tbRightPedalPresets_TabWidget), "USER PRESETS")
    mouseClick(waitForObjectItem(names.tabLeftUserPresets_leftUserPresetsView_PresetListView, "_4"), 552, 34, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.tabRightUserPresetsLayout_rightUserPresetsView_PresetListView, "_4"), 313, 30, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.quickStartScreen_pbContinue_QPushButton))
    snooze(2)
    
    all_pedal_results = validateBothPedalPresets()
    
    # Get LEFT pedal values
    left_actual = all_pedal_results["LEFT"].get("MyPreset_4")
    
    comparePresetValues(
        side="LEFT",
        preset_name="MyPreset_4",
        expected=left_preset_4,
        actual=left_actual
    )
    
    # Get RIGHT pedal values
    right_actual = all_pedal_results["RIGHT"].get("MyPreset_4")
    
    comparePresetValues(
        side="RIGHT",
        preset_name="MyPreset_4",
        expected=right_preset_4,
        actual=right_actual
    )
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton_5))
    clickButton(waitForObject(names.homeScreen_pbStoneQuickStart_QToolButton))
    clickTab(waitForObject(names.wdLeftPedalTreatmentLayout_tbLeftPedalPresets_TabWidget), "USER PRESETS")
    clickButton(waitForObject(names.tabLeftUserPresets_nextPageButton_QPushButton))
    clickTab(waitForObject(names.wdRightPedalTreatmentLayout_tbRightPedalPresets_TabWidget), "USER PRESETS")
    clickButton(waitForObject(names.tabRightUserPresetsLayout_nextPageButton_QPushButton))
    mouseClick(waitForObject(names.tabRightUserPresetsLayout_rightUserPresetsView_PresetListView), 85, 43, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.tabLeftUserPresets_leftUserPresetsView_PresetListView), 487, 54, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.quickStartScreen_pbContinue_QPushButton))
    snooze(2)
    
    all_pedal_results = validateBothPedalPresets()
    
    # Get LEFT pedal values
    left_actual = all_pedal_results["LEFT"].get("MyPreset_5")
    
    comparePresetValues(
        side="LEFT",
        preset_name="MyPreset_5",
        expected=left_preset_5,
        actual=left_actual
    )
    
    # Get RIGHT pedal values
    right_actual = all_pedal_results["RIGHT"].get("MyPreset_5")
    
    comparePresetValues(
        side="RIGHT",
        preset_name="MyPreset_5",
        expected=right_preset_5,
        actual=right_actual
    )
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton_5))
    

