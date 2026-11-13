
import os
import sys
import names
import builtins

SUITE_DIR = os.path.dirname(os.path.abspath(__file__))

if SUITE_DIR not in sys.path:
    sys.path.insert(0, SUITE_DIR)

import treatment_excel_compare as excel_check

SUITE_DIR = os.path.dirname(os.path.abspath(__file__))

EXCEL_FILE = os.path.join(
    SUITE_DIR,
    "testdata",
    "tables parse.xlsx"
)

def initialize_excel_validator():

    summary = excel_check.load_specification(EXCEL_FILE)

    test.log("EXCEL SPECIFICATION LOADED")
    test.log("General presets: {}".format(summary["table1"]))
    test.log("BPH / Soft Tissue: {}".format(summary["table2"]))
    test.log("Stone Assistant: {}".format(summary["table3"]))
    test.log("N/A routes: {}".format(summary["matrix_na"]))
    test.log("Total applicable records: {}".format(
        summary["total_records"]
    ))
    
PROCEDURE_MAP = {
    "kidneyPcnlLocationButton": "Kidney",
    "kidneyRirsLocationButton": "Kidney",
    "ureterLocationButton": "Ureter",
    "bladderLocationButton": "Bladder"
}


FLOW_RATE_MAP = {
    "lowFlowRateButton": "LOW FLOW",
    "mediumFlowRateButton": "MEDIUM FLOW",
    "highFlowRateButton": "HIGH FLOW",
    "unknownFlowRateButton": "UNKNOWN"
}


DENSITY_MAP = {
    "smallHardnessButton": "<500",
    "mediumHardnessButton": "500-1000",
    "largeHardnessButton":  ">1000",
    "unknownHardnessButton": "UNKNOWN"
}

RIGHT_SIDE_OBJECTS = {
    "mode":
        names.modeButton_nameLabel_QLabel_2,
    
    "CW":
        names.pulseModeWidget_powerWidgetCW_ParameterSettingsWidget_2,
    
    "peak_power":
        names.pulseModeWidget_peakPowerButton_ParameterSettingsButton_2,

    "average_power_value":
        names.valueLabelBackgroundWithQuantityText_valueLabel_QLabel_2,

    "average_power_limits":
        names.pulseModeWidget_averagePowerWidget_ParameterWithEnumerableValueWidget_2,

    "pulse_energy_value":
        names.valueDrum_Cylinder_5,

    "pulse_energy_limits":
        names.pulseModeWidget_pulseEnergyWidget_ParameterSettingsWidget_2,

    "frequency_value":
        names.valueDrum_Cylinder_6,

    "frequency_limits":
        names.pulseModeWidget_frequencyWidget_ParameterSettingsWidget_2
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

    "average_power_limits":
        names.pulseModeWidget_averagePowerWidget_ParameterWithEnumerableValueWidget,

    "pulse_energy_value":
        names.valueDrum_Cylinder,

    "pulse_energy_limits":
        names.pulseModeWidget_pulseEnergyWidget_ParameterSettingsWidget,

    "frequency_value":
        names.valueDrum_Cylinder_2,

    "frequency_limits":
        names.pulseModeWidget_frequencyWidget_ParameterSettingsWidget
}

def getObjectMapName(object_reference):
    return object_reference["name"]


def validateAllPresets(selection_data):
    presets = [
        "FRAGMENTATION",
        "DUSTING",
        "POPCORNING"
    ]

    results = {}

    tab_widget = waitForObjectExists(names.leftPedalWidget_wdPresetTabs_TabWidget)

    available_tabs = [
        str(tab_widget.tabText(i)).strip()
        for i in range(tab_widget.count)
    ]

    for preset in presets:
        test.log("\n-- {} --".format(preset))

        if preset not in available_tabs:
            test.fail("{} tab is missing".format(preset))
            results[preset] = {"status": "MISSING"}
            continue

        # Select the current preset
        clickTab(tab_widget, preset)
        snooze(3)

        # Extract values for the currently selected preset
        actual_values = getValues()

        # Validate against Excel
        result = excel_check.validate_selection(
            family="STONE_ASSISTANT",
            procedure=selection_data["procedure"],
            preset=preset,
            flow_rate=selection_data["flow_rate"],
            density=selection_data["density"],
            actual_values=actual_values
        )

        results[preset] = result

        print("\n-- {} VALIDATION RESULT --".format(preset))
        print(result)
        print("\n")

    return results

def selectParameters(locationButton, flowButton, hardnessButton):
    clickButton(waitForObject(locationButton))
    clickButton(waitForObject(flowButton))
    clickButton(waitForObject(hardnessButton))
    
    procedure_key = getObjectMapName(locationButton)
    flow_key = getObjectMapName(flowButton)
    density_key = getObjectMapName(hardnessButton)

    procedure = PROCEDURE_MAP.get(procedure_key)
    flow_rate = FLOW_RATE_MAP.get(flow_key)
    density = DENSITY_MAP.get(density_key)
    
    if None in (procedure, flow_rate, density):
        raise ValueError(
            "Missing mapping: {}, {}, {}".format(
                procedure_key, flow_key, density_key
            )
        )
    
    clickButton(waitForObject(names.stoneAssistantModeScreen_continueButton_QPushButton))
    
    #validatePresetTabs()
    
    return {
        "procedure": procedure,
        "flow_rate": flow_rate,
        "density": density
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
    
def inspectParameterProperties(parameter_object):

    parameter = waitForObject(parameter_object)

    current_value = str(parameter.displayedValue).strip()
    minimum = str(parameter.displayedMinimum).strip()
    maximum = str(parameter.displayedMaximum).strip()
    local_minimum = str(parameter.displayedLocalMinimum).strip()
    local_maximum = str(parameter.displayedLocalMaximum).strip()

    # test.log("Actual Parameter Value: {}".format(current_value))
    # test.log("Actual Parameter Minimum: {}".format(minimum))
    # test.log("Actual Parameter Maximum: {}".format(maximum))
    # test.log("Actual Local Minimum: {}".format(local_minimum))
    # test.log("Actual Local Maximum: {}".format(local_maximum))

    return {
        "localMinimum": local_minimum,
        "localMaximum": local_maximum
    }
    
def inspectCWProperties(parameter_object):
    parameter = waitForObject(parameter_object)

    current_value = str(parameter.displayedValue).strip()
    minimum = str(parameter.displayedMinimum).strip()
    maximum = str(parameter.displayedMaximum).strip()
    local_minimum = str(parameter.displayedLocalMinimum).strip()
    local_maximum = str(parameter.displayedLocalMaximum).strip()
    
    return {
        "current_value": current_value,
        "localMinimum": local_minimum,
        "localMaximum": local_maximum
    }

    
def inspectAveragePowerLimits(widget_object):

    widget = waitForObject(widget_object)

    minimum = str(widget.displayedMinimum).strip()
    maximum = str(widget.displayedMaximum).strip()
    
    local_minimum = str(widget.displayedLocalMinimum).strip()
    local_maximum = str(widget.displayedLocalMaximum).strip()

    # test.log("Average Power Actual Minimum: {}".format(minimum))
    # test.log("Average Power Actual Maximum: {}".format(maximum))

    return {
        "minimum": builtins.float(local_minimum),
        "maximum": builtins.float(local_maximum)
    }

def inspectPeakPower(peak_power_object):    
    try:
        peak_power = waitForObjectExists(peak_power_object)

        selected = str(peak_power.selectedPeakPower).strip()
        minimum = str(peak_power.minimumPeakPower).strip()
        maximum = str(peak_power.maximumPeakPower).strip()

        if not selected or not minimum or not maximum:
            raise ValueError("Peak Power parameter values are empty")

        return {
            "selected": builtins.float(selected),
            "minimum": builtins.float(minimum),
            "maximum": builtins.float(maximum)
        }

    except Exception as error:
        test.fail("Peak Power extraction failed: {}".format(error)) 
        return None

def (mode_button_object):
    mode_label = waitForObjectExists(mode_button_object)
    selected_mode = str(mode_label.text).strip()

    selected_mode = " ".join(selected_mode.split())
    return selected_mode

def getValues():

    try:
        selected_mode = (names.modeButton_nameLabel_QLabel)
        
        if selected_mode.strip().upper() == "REGULAR PULSE":
            test.passes("Successful Confirmation of Preset is in Mode: {}".format(selected_mode))
        else:
            test.fail("Failed Confirmation of Preset is in Mode: REGULAR PULSE")
            test.passes("Mode: {}".format(selected_mode))    
    except Exception as error:
        selected_mode = None
        test.fail("Mode extraction failed: {}".format(error))        
    
    peak_power_data = inspectPeakPower(names.pulseModeWidget_peakPowerButton_ParameterSettingsButton)
    if peak_power_data is None:
        test.fail("Peak Power data unavailable. Continuing with remaining validations. {}". format(peak_power_data))        
    
    average_power_def = inspectAveragePower(names.valueLabelBackgroundWithQuantityText_valueLabel_QLabel)
    average_power_limits = inspectAveragePowerLimits(names.pulseModeWidget_averagePowerWidget_ParameterWithEnumerableValueWidget)
    
    pulse_energy_def = inspectPulseEnergy(names.valueDrum_Cylinder)   
    pulse_energy_limits = inspectParameterProperties(names.pulseModeWidget_pulseEnergyWidget_ParameterSettingsWidget)
    
    frequency_def = inspectFrequency(names.valueDrum_Cylinder_2)   
    frequency_limits = inspectParameterProperties(names.pulseModeWidget_frequencyWidget_ParameterSettingsWidget) 

    actual_values = {    
        "frequency": {
            "default": frequency_def,
            "min": float(frequency_limits["localMinimum"]),
            "max": float(frequency_limits["localMaximum"])
        },
    
        "pulse_energy": {
            "default": pulse_energy_def,
            "min": float(pulse_energy_limits["localMinimum"]),
            "max": float(pulse_energy_limits["localMaximum"])
        },
    
        "average_power": {
            "default": average_power_def,
            "min": average_power_limits["minimum"],
            "max": average_power_limits["maximum"]
        },
    
        "peak_power": {
            "default": peak_power_data["selected"],
            "min": peak_power_data["minimum"],
            "max": peak_power_data["maximum"]
        }
    }
    
    # for parameter, values in actual_values.items():
    #     test.log("{}: {}".format(parameter, values))
        
    return actual_values

def validatePresets(assistant_type, tab_widget_object,
                    parameter_objects, side, use_cw_detection =False):

    results = {}

    tab_widget = waitForObjectExists(tab_widget_object)

    presets = [
        str(tab_widget.tabText(i)).strip()
        for i in range(tab_widget.count)
    ]

    test.log("Available {} presets: {}".format(assistant_type, presets))

    for preset in presets:
        test.log("Validating preset: {}".format(preset))
        
        test.log("{} | {} | {}".format(assistant_type, side, preset))

        try:
            clickTab(tab_widget, preset)
            snooze(3)
            
            preset_upper = " ".join(preset.upper().split())
            
            is_cw_preset = (
                use_cw_detection and
                ("CW" in preset_upper or "VAPORIZE" in preset_upper))

            if is_cw_preset:
                test.log("{} side: CW/Vaporize preset detected".format(side, preset))
                actual_values = getVaporizeValues(parameter_objects)

            else:
                test.log("Using normal BPH parameter extraction")
                actual_values = getBPHValues(parameter_objects)

            result = excel_check.validate_selection(
                family="PROCEDURE_TABLE",
                procedure=assistant_type,
                preset=preset,
                actual_values=actual_values
            )

            results[preset] = result

        except Exception as error:

            results[preset] = {
                "status": "ERROR",
                "error": str(error)
            }
            
            test.fail("{} | {} | {} validation failed: {}".format(assistant_type, side, preset, error))

    return results

def validateAssistantPresets(assistant_type,
                             left_tab_widget,
                             right_tab_widget, use_cw_detection = False):

    results = {}

    # Process first set of widgets
    # results["LEFT"] = validatePresets(
    #     assistant_type,
    #     left_tab_widget,
    #     LEFT_SIDE_OBJECTS,
    #     use_cw_detection
    # )
    #
    # # Process second set of widgets
    # results["RIGHT"] = validatePresets(
    #     assistant_type,
    #     right_tab_widget,
    #     RIGHT_SIDE_OBJECTS,
    #     use_cw_detection
    # )
    
    results["LEFT"] = validatePresets(
        assistant_type=assistant_type,
        tab_widget_object=left_tab_widget,
        parameter_objects=LEFT_SIDE_OBJECTS,
        side="LEFT",
        use_cw_detection=use_cw_detection
    )

    results["RIGHT"] = validatePresets(
        assistant_type=assistant_type,
        tab_widget_object=right_tab_widget,
        parameter_objects=RIGHT_SIDE_OBJECTS,
        side="RIGHT",
        use_cw_detection=use_cw_detection
    )

    return results

def runProcedureValidation(assistant_type, procedure_button,
                           left_tab_widget, right_tab_widget,
                           confirmation_button=None,
                           use_cw_detection=False):

    # Navigate to Home
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))

    # Open Soft Tissue / BPH Assistant
    clickButton(
        waitForObject(names.homeScreen_pbSoftTissueAssistant_QToolButton)
    )

    # Select the procedure
    clickButton(waitForObject(procedure_button))

    # Continue to treatment screen
    clickButton(
        waitForObject(names.softTissueAssistantModeScreen_pbContinue_QPushButton)
    )

    # Handle confirmation dialog when required
    if confirmation_button is not None:
        clickButton(waitForObject(confirmation_button))

    snooze(3)

    # Validate all presets from both widget sets
    return validateAssistantPresets(
        assistant_type=assistant_type,
        left_tab_widget=left_tab_widget,
        right_tab_widget=right_tab_widget,
        use_cw_detection = use_cw_detection
    )

def getVaporizeValues(objects):

    if "CW" not in objects:
        raise KeyError(
            "CW Object Map reference is missing for this side"
        )

    cw_values = inspectCWProperties(objects["CW"])

    actual_values = {
        "average_power": {
            "default": builtins.float(cw_values["current_value"]),
            "min": builtins.float(cw_values["localMinimum"]),
            "max": builtins.float(cw_values["localMaximum"])
        }
    }

    test.log("CW Average Power: {}".format(
        actual_values["average_power"]
    ))

    return actual_values

def getBPHValues(objects):

    try:
        selected_mode = (objects["mode"])
        test.log("Mode: {}".format(selected_mode))
    except Exception as error:
        selected_mode = None
        test.fail("Mode extraction failed: {}".format(error))

    peak_power_data = inspectPeakPower(objects["peak_power"])

    if peak_power_data is None:
        raise ValueError("Peak Power extraction failed")

    average_power_def = inspectAveragePower(
        objects["average_power_value"]
    )

    average_power_limits = inspectAveragePowerLimits(
        objects["average_power_limits"]
    )

    pulse_energy_def = inspectPulseEnergy(
        objects["pulse_energy_value"]
    )

    pulse_energy_limits = inspectParameterProperties(
        objects["pulse_energy_limits"]
    )

    frequency_def = inspectFrequency(
        objects["frequency_value"]
    )

    frequency_limits = inspectParameterProperties(
        objects["frequency_limits"]
    )

    actual_values = {
        "frequency": {
            "default": frequency_def,
            "min": float(frequency_limits["localMinimum"]),
            "max": float(frequency_limits["localMaximum"])
        },

        "pulse_energy": {
            "default": pulse_energy_def,
            "min": float(pulse_energy_limits["localMinimum"]),
            "max": float(pulse_energy_limits["localMaximum"])
        },

        "average_power": {
            "default": average_power_def,
            "min": average_power_limits["minimum"],
            "max": average_power_limits["maximum"]
        },

        "peak_power": {
            "default": peak_power_data["selected"],
            "min": peak_power_data["minimum"],
            "max": peak_power_data["maximum"]
        }
    }

    for parameter, values in actual_values.items():
        test.log("{}: {}".format(parameter, values))

    return actual_values
 
 
 
 
 
 
 
 
 
def validateGeneralPresets(category,
                           tab_widget_object,
                           parameter_objects,
                           side,
                           use_cw_detection=False):

    results = {}

    tab_widget = waitForObjectExists(tab_widget_object)

    presets = [
        str(tab_widget.tabText(i)).strip()
        for i in range(tab_widget.count)
    ]

    for preset in presets:

        test.log(
            "GENERAL PRESET | {} ".format(
                preset
            )
        )

        try:
            clickTab(tab_widget, preset)
            snooze(3)

            preset_upper = " ".join(preset.upper().split())

            is_cw_preset = (
                use_cw_detection and
                ("CW" in preset_upper or
                 "VAPORIZE" in preset_upper)
            )

            if is_cw_preset:
                test.log(
                    "{} | {} | CW preset detected".format(
                        category, side
                    )
                )

                actual_values = getVaporizeValues(parameter_objects)

            else:
                test.log(
                    "{} | {} | Normal preset extraction successful".format(
                        category, side
                    )
                )

                actual_values = getBPHValues(parameter_objects)

            result = excel_check.validate_selection(
                family="PRESET_LIST",
                procedure=category,
                preset=preset,
                actual_values=actual_values,
                fail_test_on_mismatch=False
            )

            results[preset] = result

            test.log(
                "GENERAL PRESET RESULT | {} | {}".format(
                    preset, result
                )
            )

        except Exception as error:

            results[preset] = {
                "status": "ERROR",
                "error": str(error)
            }

            test.fail(
                "GENERAL PRESET ERROR | {} | {} | {} | {}".format(
                    category, side, preset, error
                )
            )

    return results

def validateGeneralPresetsBothSides(category,
                                    left_tab_widget,
                                    right_tab_widget,
                                    use_cw_detection=False):

    results = {}

    results["LEFT"] = validateGeneralPresets(
        category=category,
        tab_widget_object=left_tab_widget,
        parameter_objects=LEFT_SIDE_OBJECTS,
        side="LEFT",
        use_cw_detection=use_cw_detection
    )

    results["RIGHT"] = validateGeneralPresets(
        category=category,
        tab_widget_object=right_tab_widget,
        parameter_objects=RIGHT_SIDE_OBJECTS,
        side="RIGHT",
        use_cw_detection=use_cw_detection
    )

    return results


def main():
    
    initialize_excel_validator()
    
    doubleClick(waitForObject(names.numpad_pushButton_8_NumpadButton), 65, 45, Qt.NoModifier, Qt.LeftButton)
    doubleClick(waitForObject(names.numpad_pushButton_8_NumpadButton), 65, 45, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton))  

    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selection_data = selectParameters(
        names.locationFrame_kidneyPcnlLocationButton_QPushButton,        
        names.flowRateFrame_lowFlowRateButton_QPushButton,        
        names.hardnessFrame_smallHardnessButton_QPushButton)   
    
    results = validateAllPresets(selection_data)
    for preset, result in results.items():
        test.log("{} : {}".format(preset, result))

    
    # test.log("Right Pedal Average Power: {}". format(inspectAveragePower(names.valueLabelBackgroundWithQuantityText_valueLabel_QLabel_2)))
    # test.log("Right Pedal Pulse Energy: {}". format(inspectPulseEnergy(names.valueDrum_Cylinder_5)))
    # test.log("Right Pedal Frequency: {}". format(inspectFrequency(names.valueDrum_Cylinder_6)))   
    # right_avgPower = inspectAveragePowerLimits(names.pulseModeWidget_averagePowerWidget_ParameterWithEnumerableValueWidget_2)

    # mouseClick(waitForObject(names.progressFrame_valueProgress_QProgressBar), 305, 4, Qt.NoModifier, Qt.LeftButton)
    # mouseClick(waitForObject(names.indexPicker_valuePicker_IntervalSlider_4), 359, 27, Qt.NoModifier, Qt.LeftButton)
    # mouseClick(waitForObject(names.indexPicker_valuePicker_IntervalSlider_5), 348, 21, Qt.NoModifier, Qt.LeftButton)
    # mouseClick(waitForObject(names.progressFrame_valueProgress_QProgressBar), 185, 3, Qt.NoModifier, Qt.LeftButton)
    # mouseClick(waitForObject(names.progressFrame_minimumLabel_QLabel), 5, 15, Qt.NoModifier, Qt.LeftButton)
    # mouseClick(waitForObject(names.progressFrame_maximumLabel_QLabel), 9, 15, Qt.NoModifier, Qt.LeftButton)
    #
    # mouseClick(waitForObject(names.progressFrame_valueProgress_QProgressBar_2), 218, 3, Qt.NoModifier, Qt.LeftButton)
    # mouseClick(waitForObject(names.progressFrame_minimumLabel_QLabel_2), 2, 17, Qt.NoModifier, Qt.LeftButton)
    # mouseClick(waitForObject(names.progressFrame_maximumLabel_QLabel_2), 18, 13, Qt.NoModifier, Qt.LeftButton)
    # mouseClick(waitForObject(names.averagePowerWidget_progressFrame_QFrame_2), 506, 30, Qt.NoModifier, Qt.LeftButton)
    # mouseClick(waitForObject(names.indexPicker_valuePicker_IntervalSlider_6), 341, 18, Qt.NoModifier, Qt.LeftButton)
    #
    # mouseClick(waitForObject(names.pulseModeWidget_buttonsWidget_QWidget), 254, 22, Qt.NoModifier, Qt.LeftButton)
    # mouseClick(waitForObject(names.pulseModeWidget_buttonsWidget_QWidget_2), 414, 19, Qt.NoModifier, Qt.LeftButton)
    # mouseClick(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 355, 23, Qt.NoModifier, Qt.LeftButton)    
      
    # test.passes("PEAK POWER") 
    # peak_power_data = None
    #
    # try:
    #     peak_power_data = inspectPeakPower(
    #         names.pulseModeWidget_peakPowerButton_ParameterSettingsButton
    #     )
    #
    #     test.log("Peak Power Data: {}".format(peak_power_data))
    #     test.passes("Peak Power properties extracted successfully")
    #
    # except Exception as error:
    #     test.fail("Peak Power extraction failed: {}".format(error))
    #     test.log("Continuing with remaining test steps...")
    #
    # test.log("Peak Power Data: {}".format(peak_power_data))
    # test.passes("Peak Power properties extracted successfull")
    #
    # left_avgPower = inspectAveragePowerLimits(names.pulseModeWidget_averagePowerWidget_ParameterWithEnumerableValueWidget)
    # right_avgPower = inspectAveragePowerLimits(names.pulseModeWidget_averagePowerWidget_ParameterWithEnumerableValueWidget_2)
    #
    # test.passes("LEFT PULSE ENERGY")
    # left_pulse_energy = inspectParameterProperties(names.pulseModeWidget_pulseEnergyWidget_ParameterSettingsWidget)
    # test.passes("LEFT FREQUENCY")
    # left_frequency = inspectParameterProperties(names.pulseModeWidget_frequencyWidget_ParameterSettingsWidget)
    #
    # test.passes("RIGHT PULSE ENERGY")
    # right_pulse_energy = inspectParameterProperties(names.pulseModeWidget_pulseEnergyWidget_ParameterSettingsWidget_2)
    # test.passes("RIGHT FREQUENCY")
    # right_frequency = inspectParameterProperties(names.pulseModeWidget_frequencyWidget_ParameterSettingsWidget_2)      
    #
    # mouseClick(waitForObject(names.valueLabelBackgroundWithQuantityText_valueLabel_QLabel), 205, 27, Qt.NoModifier, Qt.LeftButton)
    # mouseClick(waitForObject(names.valueDrum_Cylinder), 210, 4, Qt.NoModifier, Qt.LeftButton)
    # mouseClick(waitForObject(names.valueDrum_Cylinder_2), 204, 19, Qt.NoModifier, Qt.LeftButton)
    #
    # mouseClick(waitForObject(names.valueLabelBackgroundWithQuantityText_valueLabel_QLabel_2), 191, 19, Qt.NoModifier, Qt.LeftButton)
    # mouseClick(waitForObject(names.valueDrum_Cylinder_5), 214, 27, Qt.NoModifier, Qt.LeftButton)
    # mouseClick(waitForObject(names.valueDrum_Cylinder_6), 211, 4, Qt.NoModifier, Qt.LeftButton)
    # clickTab(waitForObject(names.leftPedalWidget_wdPresetTabs_TabWidget), "FRAGMENTATION")
    # clickTab(waitForObject(names.rightPedalWidget_wdPresetTabs_TabWidget), "POPCORNING")
     
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selection_data = selectParameters(
        names.locationFrame_kidneyPcnlLocationButton_QPushButton,
        names.flowRateFrame_lowFlowRateButton_QPushButton,
        names.hardnessFrame_mediumHardnessButton_QPushButton)
    
    results = validateAllPresets(selection_data)
    for preset, result in results.items():
        test.log("{} : {}".format(preset, result))   
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selection_data = selectParameters(
        names.locationFrame_kidneyPcnlLocationButton_QPushButton,
        names.flowRateFrame_lowFlowRateButton_QPushButton,
        names.hardnessFrame_largeHardnessButton_QPushButton)  
    
    results = validateAllPresets(selection_data)
    for preset, result in results.items():
        test.log("{} : {}".format(preset, result))  
    
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selection_data = selectParameters(
        names.locationFrame_kidneyPcnlLocationButton_QPushButton,
        names.flowRateFrame_lowFlowRateButton_QPushButton,
        names.hardnessFrame_unknownHardnessButton_QPushButton)
    
    results = validateAllPresets(selection_data)
    for preset, result in results.items():
        test.log("{} : {}".format(preset, result))   
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selection_data = selectParameters(
        names.locationFrame_kidneyPcnlLocationButton_QPushButton,
        names.flowRateFrame_mediumFlowRateButton_QPushButton,
        names.hardnessFrame_smallHardnessButton_QPushButton
    )
    
    results = validateAllPresets(selection_data)
    for preset, result in results.items():
        test.log("{} : {}".format(preset, result)) 
    
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selection_data = selectParameters(
        names.locationFrame_kidneyPcnlLocationButton_QPushButton,
        names.flowRateFrame_mediumFlowRateButton_QPushButton,
        names.hardnessFrame_mediumHardnessButton_QPushButton
    )
    
    results = validateAllPresets(selection_data)
    for preset, result in results.items():
        test.log("{} : {}".format(preset, result))     
    
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selection_data = selectParameters(
        names.locationFrame_kidneyPcnlLocationButton_QPushButton,
        names.flowRateFrame_mediumFlowRateButton_QPushButton,
        names.hardnessFrame_largeHardnessButton_QPushButton
    )
    results = validateAllPresets(selection_data)
    for preset, result in results.items():
        test.log("{} : {}".format(preset, result)) 
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selection_data = selectParameters(
        names.locationFrame_kidneyPcnlLocationButton_QPushButton,
        names.flowRateFrame_mediumFlowRateButton_QPushButton,
        names.hardnessFrame_unknownHardnessButton_QPushButton
    )
    results = validateAllPresets(selection_data)
    for preset, result in results.items():
        test.log("{} : {}".format(preset, result)) 
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selection_data = selectParameters(
        names.locationFrame_kidneyPcnlLocationButton_QPushButton,
        names.flowRateFrame_highFlowRateButton_QPushButton,
        names.hardnessFrame_smallHardnessButton_QPushButton
    )
    
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton_2))
    
    results = validateAllPresets(selection_data)
    for preset, result in results.items():
        test.log("{} : {}".format(preset, result)) 
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selection_data = selectParameters(
        names.locationFrame_kidneyPcnlLocationButton_QPushButton,
        names.flowRateFrame_highFlowRateButton_QPushButton,
        names.hardnessFrame_mediumHardnessButton_QPushButton
    )
    
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton_2))
    results = validateAllPresets(selection_data)
    for preset, result in results.items():
        test.log("{} : {}".format(preset, result)) 
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selection_data = selectParameters(
        names.locationFrame_kidneyPcnlLocationButton_QPushButton,
        names.flowRateFrame_highFlowRateButton_QPushButton,
        names.hardnessFrame_largeHardnessButton_QPushButton
    )
    
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton_2))
    results = validateAllPresets(selection_data)
    for preset, result in results.items():
        test.log("{} : {}".format(preset, result)) 
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selection_data = selectParameters(
        names.locationFrame_kidneyPcnlLocationButton_QPushButton,
        names.flowRateFrame_highFlowRateButton_QPushButton,
        names.hardnessFrame_unknownHardnessButton_QPushButton
    )
    
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton_2))
    results = validateAllPresets(selection_data)
    for preset, result in results.items():
        test.log("{} : {}".format(preset, result)) 
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selection_data = selectParameters(
        names.locationFrame_kidneyPcnlLocationButton_QPushButton,
        names.flowRateFrame_unknownFlowRateButton_QPushButton,
        names.hardnessFrame_smallHardnessButton_QPushButton
    )
    
    results = validateAllPresets(selection_data)
    for preset, result in results.items():
        test.log("{} : {}".format(preset, result)) 
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selection_data = selectParameters(
        names.locationFrame_kidneyPcnlLocationButton_QPushButton,
        names.flowRateFrame_unknownFlowRateButton_QPushButton,
        names.hardnessFrame_mediumHardnessButton_QPushButton
    )
    
    results = validateAllPresets(selection_data)
    for preset, result in results.items():
        test.log("{} : {}".format(preset, result)) 
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selection_data = selectParameters(
        names.locationFrame_kidneyPcnlLocationButton_QPushButton,
        names.flowRateFrame_unknownFlowRateButton_QPushButton,
        names.hardnessFrame_largeHardnessButton_QPushButton
    )
    
    results = validateAllPresets(selection_data)
    for preset, result in results.items():
        test.log("{} : {}".format(preset, result)) 
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selection_data = selectParameters(
        names.locationFrame_kidneyPcnlLocationButton_QPushButton,
        names.flowRateFrame_unknownFlowRateButton_QPushButton,
        names.hardnessFrame_unknownHardnessButton_QPushButton
    )
    
    results = validateAllPresets(selection_data)
    for preset, result in results.items():
        test.log("{} : {}".format(preset, result)) 
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selection_data = selectParameters(
        names.locationFrame_kidneyRirsLocationButton_QPushButton,
        names.flowRateFrame_lowFlowRateButton_QPushButton,
        names.hardnessFrame_smallHardnessButton_QPushButton
    )
    
    results = validateAllPresets(selection_data)
    for preset, result in results.items():
        test.log("{} : {}".format(preset, result)) 
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selection_data = selectParameters(
        names.locationFrame_kidneyRirsLocationButton_QPushButton,
        names.flowRateFrame_lowFlowRateButton_QPushButton,
        names.hardnessFrame_mediumHardnessButton_QPushButton
    )
    results = validateAllPresets(selection_data)
    for preset, result in results.items():
        test.log("{} : {}".format(preset, result)) 
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selection_data = selectParameters(
        names.locationFrame_kidneyRirsLocationButton_QPushButton,
        names.flowRateFrame_lowFlowRateButton_QPushButton,
        names.hardnessFrame_largeHardnessButton_QPushButton
    )
    
    results = validateAllPresets(selection_data)
    for preset, result in results.items():
        test.log("{} : {}".format(preset, result)) 
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selection_data = selectParameters(
        names.locationFrame_kidneyRirsLocationButton_QPushButton,
        names.flowRateFrame_lowFlowRateButton_QPushButton,
        names.hardnessFrame_unknownHardnessButton_QPushButton
    )
    
    results = validateAllPresets(selection_data)
    for preset, result in results.items():
        test.log("{} : {}".format(preset, result)) 
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selection_data = selectParameters(
        names.locationFrame_kidneyRirsLocationButton_QPushButton,
        names.flowRateFrame_mediumFlowRateButton_QPushButton,
        names.hardnessFrame_smallHardnessButton_QPushButton
    )
    
    results = validateAllPresets(selection_data)
    for preset, result in results.items():
        test.log("{} : {}".format(preset, result)) 
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selection_data = selectParameters(
        names.locationFrame_kidneyRirsLocationButton_QPushButton,
        names.flowRateFrame_mediumFlowRateButton_QPushButton,
        names.hardnessFrame_mediumHardnessButton_QPushButton
    )
    
    results = validateAllPresets(selection_data)
    for preset, result in results.items():
        test.log("{} : {}".format(preset, result)) 
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selection_data = selectParameters(
        names.locationFrame_kidneyRirsLocationButton_QPushButton,
        names.flowRateFrame_mediumFlowRateButton_QPushButton,
        names.hardnessFrame_largeHardnessButton_QPushButton
    )
    
    results = validateAllPresets(selection_data)
    for preset, result in results.items():
        test.log("{} : {}".format(preset, result)) 
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selection_data = selectParameters(
        names.locationFrame_kidneyRirsLocationButton_QPushButton,
        names.flowRateFrame_mediumFlowRateButton_QPushButton,
        names.hardnessFrame_unknownHardnessButton_QPushButton
    )
    
    results = validateAllPresets(selection_data)
    for preset, result in results.items():
        test.log("{} : {}".format(preset, result)) 
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selection_data = selectParameters(
        names.locationFrame_kidneyRirsLocationButton_QPushButton,
        names.flowRateFrame_unknownFlowRateButton_QPushButton,
        names.hardnessFrame_smallHardnessButton_QPushButton
    )
    
    results = validateAllPresets(selection_data)
    for preset, result in results.items():
        test.log("{} : {}".format(preset, result)) 
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selection_data = selectParameters(
        names.locationFrame_kidneyRirsLocationButton_QPushButton,
        names.flowRateFrame_unknownFlowRateButton_QPushButton,
        names.hardnessFrame_mediumHardnessButton_QPushButton
    )
    
    results = validateAllPresets(selection_data)
    for preset, result in results.items():
        test.log("{} : {}".format(preset, result)) 
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selection_data = selectParameters(
        names.locationFrame_kidneyRirsLocationButton_QPushButton,
        names.flowRateFrame_unknownFlowRateButton_QPushButton,
        names.hardnessFrame_largeHardnessButton_QPushButton
    )
    
    results = validateAllPresets(selection_data)
    for preset, result in results.items():
        test.log("{} : {}".format(preset, result)) 
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selection_data = selectParameters(
        names.locationFrame_kidneyRirsLocationButton_QPushButton,
        names.flowRateFrame_unknownFlowRateButton_QPushButton,
        names.hardnessFrame_unknownHardnessButton_QPushButton
    )
    
    results = validateAllPresets(selection_data)
    for preset, result in results.items():
        test.log("{} : {}".format(preset, result)) 
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selection_data = selectParameters(
        names.locationFrame_ureterLocationButton_QPushButton,
        names.flowRateFrame_lowFlowRateButton_QPushButton,
        names.hardnessFrame_smallHardnessButton_QPushButton
    )
    
    results = validateAllPresets(selection_data)
    for preset, result in results.items():
        test.log("{} : {}".format(preset, result)) 
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selection_data = selectParameters(
        names.locationFrame_ureterLocationButton_QPushButton,
        names.flowRateFrame_lowFlowRateButton_QPushButton,
        names.hardnessFrame_mediumHardnessButton_QPushButton
    )
    
    results = validateAllPresets(selection_data)
    for preset, result in results.items():
        test.log("{} : {}".format(preset, result)) 
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selection_data = selectParameters(
        names.locationFrame_ureterLocationButton_QPushButton,
        names.flowRateFrame_lowFlowRateButton_QPushButton,
        names.hardnessFrame_largeHardnessButton_QPushButton
    )
    
    results = validateAllPresets(selection_data)
    for preset, result in results.items():
        test.log("{} : {}".format(preset, result)) 
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selection_data = selectParameters(
        names.locationFrame_ureterLocationButton_QPushButton,
        names.flowRateFrame_lowFlowRateButton_QPushButton,
        names.hardnessFrame_unknownHardnessButton_QPushButton
    )
    
    results = validateAllPresets(selection_data)
    for preset, result in results.items():
        test.log("{} : {}".format(preset, result)) 
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selection_data = selectParameters(
        names.locationFrame_ureterLocationButton_QPushButton,
        names.flowRateFrame_mediumFlowRateButton_QPushButton,
        names.hardnessFrame_smallHardnessButton_QPushButton
    )
    
    results = validateAllPresets(selection_data)
    for preset, result in results.items():
        test.log("{} : {}".format(preset, result)) 
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selection_data = selectParameters(
        names.locationFrame_ureterLocationButton_QPushButton,
        names.flowRateFrame_mediumFlowRateButton_QPushButton,
        names.hardnessFrame_mediumHardnessButton_QPushButton
    )
    
    results = validateAllPresets(selection_data)
    for preset, result in results.items():
        test.log("{} : {}".format(preset, result)) 
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selection_data = selectParameters(
        names.locationFrame_ureterLocationButton_QPushButton,
        names.flowRateFrame_mediumFlowRateButton_QPushButton,
        names.hardnessFrame_largeHardnessButton_QPushButton
    )
    
    results = validateAllPresets(selection_data)
    for preset, result in results.items():
        test.log("{} : {}".format(preset, result)) 
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selection_data = selectParameters(
        names.locationFrame_ureterLocationButton_QPushButton,
        names.flowRateFrame_mediumFlowRateButton_QPushButton,
        names.hardnessFrame_unknownHardnessButton_QPushButton
    )
    
    results = validateAllPresets(selection_data)
    for preset, result in results.items():
        test.log("{} : {}".format(preset, result)) 
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selection_data = selectParameters(
        names.locationFrame_ureterLocationButton_QPushButton,
        names.flowRateFrame_unknownFlowRateButton_QPushButton,
        names.hardnessFrame_smallHardnessButton_QPushButton
    )
    
    results = validateAllPresets(selection_data)
    for preset, result in results.items():
        test.log("{} : {}".format(preset, result)) 
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selection_data = selectParameters(
        names.locationFrame_ureterLocationButton_QPushButton,
        names.flowRateFrame_unknownFlowRateButton_QPushButton,
        names.hardnessFrame_mediumHardnessButton_QPushButton
    )
    
    results = validateAllPresets(selection_data)
    for preset, result in results.items():
        test.log("{} : {}".format(preset, result)) 
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selection_data = selectParameters(
        names.locationFrame_ureterLocationButton_QPushButton,
        names.flowRateFrame_unknownFlowRateButton_QPushButton,
        names.hardnessFrame_largeHardnessButton_QPushButton
    )
    
    results = validateAllPresets(selection_data)
    for preset, result in results.items():
        test.log("{} : {}".format(preset, result)) 
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selection_data = selectParameters(
        names.locationFrame_ureterLocationButton_QPushButton,
        names.flowRateFrame_unknownFlowRateButton_QPushButton,
        names.hardnessFrame_unknownHardnessButton_QPushButton
    )
    
    results = validateAllPresets(selection_data)
    for preset, result in results.items():
        test.log("{} : {}".format(preset, result)) 
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selection_data = selectParameters(
        names.locationFrame_bladderLocationButton_QPushButton,
        names.flowRateFrame_highFlowRateButton_QPushButton,
        names.hardnessFrame_smallHardnessButton_QPushButton
    )
    
    results = validateAllPresets(selection_data)
    for preset, result in results.items():
        test.log("{} : {}".format(preset, result)) 
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selection_data = selectParameters(
        names.locationFrame_bladderLocationButton_QPushButton,
        names.flowRateFrame_highFlowRateButton_QPushButton,
        names.hardnessFrame_mediumHardnessButton_QPushButton
    )
    
    results = validateAllPresets(selection_data)
    for preset, result in results.items():
        test.log("{} : {}".format(preset, result)) 
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selection_data = selectParameters(
        names.locationFrame_bladderLocationButton_QPushButton,
        names.flowRateFrame_highFlowRateButton_QPushButton,
        names.hardnessFrame_largeHardnessButton_QPushButton
    )
    
    results = validateAllPresets(selection_data)
    for preset, result in results.items():
        test.log("{} : {}".format(preset, result)) 
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selection_data = selectParameters(
        names.locationFrame_bladderLocationButton_QPushButton,
        names.flowRateFrame_highFlowRateButton_QPushButton,
        names.hardnessFrame_unknownHardnessButton_QPushButton
    )
    
    results = validateAllPresets(selection_data)
    for preset, result in results.items():
        test.log("{} : {}".format(preset, result)) 
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selection_data = selectParameters(
        names.locationFrame_bladderLocationButton_QPushButton,
        names.flowRateFrame_unknownFlowRateButton_QPushButton,
        names.hardnessFrame_smallHardnessButton_QPushButton
    )
    results = validateAllPresets(selection_data)
    for preset, result in results.items():
        test.log("{} : {}".format(preset, result)) 
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selection_data = selectParameters(
        names.locationFrame_bladderLocationButton_QPushButton,
        names.flowRateFrame_unknownFlowRateButton_QPushButton,
        names.hardnessFrame_mediumHardnessButton_QPushButton
    )
    
    results = validateAllPresets(selection_data)
    for preset, result in results.items():
        test.log("{} : {}".format(preset, result)) 
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selection_data = selectParameters(
        names.locationFrame_bladderLocationButton_QPushButton,
        names.flowRateFrame_unknownFlowRateButton_QPushButton,
        names.hardnessFrame_largeHardnessButton_QPushButton
    )
    
    results = validateAllPresets(selection_data)
    for preset, result in results.items():
        test.log("{} : {}".format(preset, result)) 
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selection_data = selectParameters(
        names.locationFrame_bladderLocationButton_QPushButton,
        names.flowRateFrame_unknownFlowRateButton_QPushButton,
        names.hardnessFrame_unknownHardnessButton_QPushButton
    )
    
    results = validateAllPresets(selection_data)
    for preset, result in results.items():
        test.log("{} : {}".format(preset, result)) 
        
    # clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))  
    # clickButton(waitForObject(names.homeScreen_pbSoftTissueAssistant_QToolButton))
    # clickButton(waitForObject(names.gbSoftTissueProcedures_pbIncision_QPushButton))
    # clickButton(waitForObject(names.softTissueAssistantModeScreen_pbContinue_QPushButton))
    
    all_results = {}

    # all_results["SOFT_TISSUE_INCISION"] = runProcedureValidation(
    #     assistant_type="Soft Tissue",
    #     procedure_button=names.gbSoftTissueProcedures_pbIncision_QPushButton,
    #     left_tab_widget=names.leftPedalWidget_wdPresetTabs_TabWidget,
    #     right_tab_widget=names.rightPedalWidget_wdPresetTabs_TabWidget
    # )
    
    all_results["INCISION"] = runProcedureValidation(
        assistant_type="Soft Tissue",
        procedure_button=names.gbSoftTissueProcedures_pbIncision_QPushButton,
        left_tab_widget= names.leftPedalWidget_wdPresetTabs_TabWidget,
        right_tab_widget= names.rightPedalWidget_wdPresetTabs_TabWidget,
        use_cw_detection=False
    )

    # clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    # clickButton(waitForObject(names.homeScreen_pbSoftTissueAssistant_QToolButton))
    # clickButton(waitForObject(names.gbSoftTissueProcedures_pbTumor_QPushButton))
    # clickButton(waitForObject(names.softTissueAssistantModeScreen_pbContinue_QPushButton))
    
    # all_results["SOFT_TISSUE_TUMOR"] = runProcedureValidation(
    #     assistant_type="Soft Tissue",
    #     procedure_button=names.gbSoftTissueProcedures_pbTumor_QPushButton,
    #     left_tab_widget=names.leftPedalWidget_wdPresetTabs_TabWidget,
    #     right_tab_widget=names.rightPedalWidget_wdPresetTabs_TabWidget
    # )
    
    all_results["TUMOR"] = runProcedureValidation(
        assistant_type="Soft Tissue",
        procedure_button=names.gbSoftTissueProcedures_pbTumor_QPushButton,
        left_tab_widget= names.leftPedalWidget_wdPresetTabs_TabWidget,
        right_tab_widget= names.rightPedalWidget_wdPresetTabs_TabWidget,
        use_cw_detection=False
    )

    # clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    # clickButton(waitForObject(names.homeScreen_pbSoftTissueAssistant_QToolButton))
    # clickButton(waitForObject(names.gbBphProcedures_pbEnucleation_QPushButton))
    # clickButton(waitForObject(names.softTissueAssistantModeScreen_pbContinue_QPushButton))
    # clickButton(waitForObject(names.mainFrame_okButton_QPushButton_2))
    
    # all_results["BPH_ENUCLEATION"] = runProcedureValidation(
    #     assistant_type="BPH",
    #     procedure_button=names.gbBphProcedures_pbEnucleation_QPushButton,
    #     left_tab_widget=names.leftPedalWidget_wdPresetTabs_TabWidget,
    #     right_tab_widget=names.rightPedalWidget_wdPresetTabs_TabWidget,
    #     confirmation_button=names.mainFrame_okButton_QPushButton_2
    # )
    
    all_results["ENUCLEATION"] = runProcedureValidation(
        assistant_type="BPH",
        procedure_button=names.gbBphProcedures_pbEnucleation_QPushButton,
        left_tab_widget= names.leftPedalWidget_wdPresetTabs_TabWidget,
        right_tab_widget= names.rightPedalWidget_wdPresetTabs_TabWidget,
        confirmation_button=names.mainFrame_okButton_QPushButton_2,
        use_cw_detection=False
    )

    # clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    # clickButton(waitForObject(names.homeScreen_pbSoftTissueAssistant_QToolButton))
    # clickButton(waitForObject(names.gbBphProcedures_pbEnucleationLow_ButtoWithCaptionAndSmallerSubCaption))
    # clickButton(waitForObject(names.softTissueAssistantModeScreen_pbContinue_QPushButton))
    # clickButton(waitForObject(names.mainFrame_okButton_QPushButton_2))
    #
    # all_results["BPH_ENUCLEATION_LOW"] = runProcedureValidation(
    #     assistant_type="BPH",
    #     procedure_button=names.gbBphProcedures_pbEnucleationLow_ButtoWithCaptionAndSmallerSubCaption,
    #     left_tab_widget=names.leftPedalWidget_wdPresetTabs_TabWidget,
    #     right_tab_widget=names.rightPedalWidget_wdPresetTabs_TabWidget,
    #     confirmation_button=names.mainFrame_okButton_QPushButton_2
    # )
    
    all_results["ENUCLEATION_LOW"] = runProcedureValidation(
        assistant_type="BPH",
        procedure_button=names.gbBphProcedures_pbEnucleationLow_ButtoWithCaptionAndSmallerSubCaption,
        left_tab_widget=names.leftPedalWidget_wdPresetTabs_TabWidget,
        right_tab_widget=names.rightPedalWidget_wdPresetTabs_TabWidget,
        confirmation_button=names.mainFrame_okButton_QPushButton_2,
        use_cw_detection=False
    )

    # clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    # clickButton(waitForObject(names.homeScreen_pbSoftTissueAssistant_QToolButton))
    # clickButton(waitForObject(names.gbBphProcedures_pbVaporize_QPushButton))
    # clickButton(waitForObject(names.softTissueAssistantModeScreen_pbContinue_QPushButton))
    # clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    
    # all_results["BPH_VAPORIZE"] = runProcedureValidation(
    #     assistant_type="BPH",
    #     procedure_button=names.gbBphProcedures_pbVaporize_QPushButton,
    #     left_tab_widget=names.leftPedalWidget_wdPresetTabs_TabWidget,
    #     right_tab_widget=names.rightPedalWidget_wdPresetTabs_TabWidget,
    #     vaporize=True
    # )
    
    all_results["VAPORIZE"] = runProcedureValidation(
        assistant_type="Soft Tissue",
        procedure_button=names.gbBphProcedures_pbVaporize_QPushButton,
        left_tab_widget=names.leftPedalWidget_wdPresetTabs_TabWidget,
        right_tab_widget=names.rightPedalWidget_wdPresetTabs_TabWidget,
        use_cw_detection=True
    )
    
    test.log("FINAL SOFT TISSUE GUIDED VALIDATION RESULTS")
    for selection, result in all_results.items():
        test.log("{} : {}".format(selection, result))

    # return all_results
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbSoftTissueQuickStart_QToolButton))
    mouseClick(waitForObjectItem(names.tabLeftMainPresets_leftPresetsView_PresetListView, "_1"), 432, 47, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.tabRightMainPresets_nextPageButton_QPushButton))
    mouseClick(waitForObjectItem(names.tabRightMainPresets_rightPresetsView_PresetListView, "_1"), 319, 61, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.quickStartScreen_pbContinue_QPushButton))
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton_2))
    
    soft_tissue_results = validateGeneralPresetsBothSides(
        category="SOFT TISSUE",
        left_tab_widget=names.leftPedalWidget_wdPresetTabs_TabWidget,
        right_tab_widget=names.rightPedalWidget_wdPresetTabs_TabWidget,
        use_cw_detection=True
    )
    
    snooze(1)


    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbSoftTissueQuickStart_QToolButton))
    mouseClick(waitForObjectItem(names.tabLeftMainPresets_leftPresetsView_PresetListView, "_2"), 443, 37, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.tabRightMainPresets_nextPageButton_QPushButton))
    mouseClick(waitForObjectItem(names.tabRightMainPresets_rightPresetsView_PresetListView, "_2"), 360, 62, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.quickStartScreen_pbContinue_QPushButton))
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton_2))
    
    soft_tissue_results_2 = validateGeneralPresetsBothSides(
        category="SOFT TISSUE",
        left_tab_widget=names.leftPedalWidget_wdPresetTabs_TabWidget,
        right_tab_widget=names.rightPedalWidget_wdPresetTabs_TabWidget,
        use_cw_detection=True
    )
    snooze(1)

    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbSoftTissueQuickStart_QToolButton))
    mouseClick(waitForObjectItem(names.tabLeftMainPresets_leftPresetsView_PresetListView, "_3"), 524, 43, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.tabRightMainPresets_nextPageButton_QPushButton))
    mouseClick(waitForObjectItem(names.tabRightMainPresets_rightPresetsView_PresetListView, "_3"), 399, 67, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.quickStartScreen_pbContinue_QPushButton))
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton_2))
    
    soft_tissue_results_3 = validateGeneralPresetsBothSides(
        category="SOFT TISSUE",
        left_tab_widget=names.leftPedalWidget_wdPresetTabs_TabWidget,
        right_tab_widget=names.rightPedalWidget_wdPresetTabs_TabWidget,
        use_cw_detection=True
    )
    snooze(1)

    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbSoftTissueQuickStart_QToolButton))
    mouseClick(waitForObjectItem(names.tabLeftMainPresets_leftPresetsView_PresetListView, "_4"), 527, 49, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.tabRightMainPresets_nextPageButton_QPushButton))
    mouseClick(waitForObjectItem(names.tabRightMainPresets_rightPresetsView_PresetListView, "_3"), 445, 91, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.quickStartScreen_pbContinue_QPushButton))
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton_2))
    
    soft_tissue_results_4 = validateGeneralPresetsBothSides(
        category="SOFT TISSUE",
        left_tab_widget=names.leftPedalWidget_wdPresetTabs_TabWidget,
        right_tab_widget=names.rightPedalWidget_wdPresetTabs_TabWidget,
        use_cw_detection=True
    )
    snooze(1)


    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneQuickStart_QToolButton))
    mouseClick(waitForObjectItem(names.tabLeftMainPresets_leftPresetsView_PresetListView, "_1"), 473, 53, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.tabRightMainPresets_nextPageButton_QPushButton))
    mouseClick(waitForObjectItem(names.tabRightMainPresets_rightPresetsView_PresetListView, "_1"), 418, 46, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.quickStartScreen_pbContinue_QPushButton))
    
    stone_results = validateGeneralPresetsBothSides(
        category="STONE",
        left_tab_widget=names.leftPedalWidget_wdPresetTabs_TabWidget,
        right_tab_widget=names.rightPedalWidget_wdPresetTabs_TabWidget
    )
    snooze(1)


    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneQuickStart_QToolButton))
    clickButton(waitForObject(names.tabRightMainPresets_nextPageButton_QPushButton))
    mouseClick(waitForObjectItem(names.tabLeftMainPresets_leftPresetsView_PresetListView, "_2"), 579, 62, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.tabRightMainPresets_rightPresetsView_PresetListView, "_2"), 211, 60, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.quickStartScreen_pbContinue_QPushButton))
    
    stone_results_2 = validateGeneralPresetsBothSides(
        category="STONE",
        left_tab_widget=names.leftPedalWidget_wdPresetTabs_TabWidget,
        right_tab_widget=names.rightPedalWidget_wdPresetTabs_TabWidget
    )
    snooze(1)

    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneQuickStart_QToolButton))
    mouseClick(waitForObjectItem(names.tabLeftMainPresets_leftPresetsView_PresetListView, "_3"), 562, 68, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.tabRightMainPresets_nextPageButton_QPushButton))
    mouseClick(waitForObjectItem(names.tabRightMainPresets_rightPresetsView_PresetListView, "_3"), 401, 62, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.quickStartScreen_pbContinue_QPushButton))
    
    stone_results_3 = validateGeneralPresetsBothSides(
        category="STONE",
        left_tab_widget=names.leftPedalWidget_wdPresetTabs_TabWidget,
        right_tab_widget=names.rightPedalWidget_wdPresetTabs_TabWidget
    )
    snooze(1)

    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneQuickStart_QToolButton))
    mouseClick(waitForObjectItem(names.tabLeftMainPresets_leftPresetsView_PresetListView, "_4"), 511, 53, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.tabRightMainPresets_nextPageButton_QPushButton))
    mouseClick(waitForObjectItem(names.tabRightMainPresets_rightPresetsView_PresetListView, "_4"), 324, 49, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.quickStartScreen_pbContinue_QPushButton))
    
    stone_result_4 = validateGeneralPresetsBothSides(
        category="STONE",
        left_tab_widget=names.leftPedalWidget_wdPresetTabs_TabWidget,
        right_tab_widget=names.rightPedalWidget_wdPresetTabs_TabWidget
    )
    snooze(1)

    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneQuickStart_QToolButton))
    clickButton(waitForObject(names.tabLeftMainPresets_nextPageButton_QPushButton))
    clickButton(waitForObject(names.tabRightMainPresets_nextPageButton_QPushButton))
    clickButton(waitForObject(names.tabLeftMainPresets_nextPageButton_QPushButton))
    clickButton(waitForObject(names.tabRightMainPresets_nextPageButton_QPushButton))
    mouseClick(waitForObjectItem(names.tabLeftMainPresets_leftPresetsView_PresetListView, "_1"), 568, 67, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.tabRightMainPresets_rightPresetsView_PresetListView, "_1"), 158, 62, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.quickStartScreen_pbContinue_QPushButton))
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton_2))
    
    stone_results_5 = validateGeneralPresetsBothSides(
        category="STONE",
        left_tab_widget=names.leftPedalWidget_wdPresetTabs_TabWidget,
        right_tab_widget=names.rightPedalWidget_wdPresetTabs_TabWidget
    )
    snooze(1)

    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneQuickStart_QToolButton))
    doubleClick(waitForObject(names.tabLeftMainPresets_nextPageButton_QPushButton), 80, 43, Qt.NoModifier, Qt.LeftButton)
    doubleClick(waitForObject(names.tabRightMainPresets_nextPageButton_QPushButton), 75, 37, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.tabLeftMainPresets_leftPresetsView_PresetListView, "_2"), 566, 67, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.tabRightMainPresets_rightPresetsView_PresetListView, "_2"), 175, 26, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.quickStartScreen_pbContinue_QPushButton))
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton_2))
    
    stone_results_6 = validateGeneralPresetsBothSides(
        category="STONE",
        left_tab_widget=names.leftPedalWidget_wdPresetTabs_TabWidget,
        right_tab_widget=names.rightPedalWidget_wdPresetTabs_TabWidget
    )
    snooze(1)

    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneQuickStart_QToolButton))
    doubleClick(waitForObject(names.tabLeftMainPresets_nextPageButton_QPushButton), 58, 34, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.tabLeftMainPresets_leftPresetsView_PresetListView, "_3"), 466, 69, Qt.NoModifier, Qt.LeftButton)
    doubleClick(waitForObject(names.tabRightMainPresets_nextPageButton_QPushButton), 33, 36, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.tabRightMainPresets_nextPageButton_QPushButton))
    mouseClick(waitForObjectItem(names.tabRightMainPresets_rightPresetsView_PresetListView, "_3"), 364, 73, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.quickStartScreen_pbContinue_QPushButton))
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton_2))
    
    stone_results_7 = validateGeneralPresetsBothSides(
        category="STONE",
        left_tab_widget=names.leftPedalWidget_wdPresetTabs_TabWidget,
        right_tab_widget=names.rightPedalWidget_wdPresetTabs_TabWidget
    )
    snooze(1)

    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneQuickStart_QToolButton))
    doubleClick(waitForObject(names.tabLeftMainPresets_nextPageButton_QPushButton), 48, 43, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.tabLeftMainPresets_nextPageButton_QPushButton))
    mouseClick(waitForObjectItem(names.tabLeftMainPresets_leftPresetsView_PresetListView, "_4"), 487, 49, Qt.NoModifier, Qt.LeftButton)
    doubleClick(waitForObject(names.tabRightMainPresets_nextPageButton_QPushButton), 45, 26, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.tabRightMainPresets_nextPageButton_QPushButton))
    mouseClick(waitForObjectItem(names.tabRightMainPresets_rightPresetsView_PresetListView, "_4"), 467, 54, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.quickStartScreen_pbContinue_QPushButton))
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton_2))
    
    stone_results_8 = validateGeneralPresetsBothSides(
        category="STONE",
        left_tab_widget=names.leftPedalWidget_wdPresetTabs_TabWidget,
        right_tab_widget=names.rightPedalWidget_wdPresetTabs_TabWidget
    )
    snooze(1)

    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    
    
  
    
