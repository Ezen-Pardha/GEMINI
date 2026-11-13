# -*- coding: utf-8 -*-

import names
import re

ECONOMY_C_PEAK_POWER = {
    "Standard": [125, 250, 500, 750, 1000],
    "MRP": [500, 750, 1000],
    "Dusting": [1000],
    "Fragmentation": [500, 1000],
    "Enucleation": [500, 1000],
    "Minimal Vaporization": [500, 1000]
}

MODE_MAPPING = {
    "Square": "Standard",
    "MRP": "MRP",
    "Dusting": "Dusting",
    "Fragmentation": "Fragmentation",
    "Enucleation": "Enucleation",
    "Cleaning": "Minimal Vaporization",
    "CW": None
}

def getAllChildObjects(parent):

    all_children = []
    children = object.children(parent)

    for child in children:
        all_children.append(child)
        all_children.extend(getAllChildObjects(child))

    return all_children


def inspectAvailableModes(mode_button, pedal_name, x, y):

    mouseClick(
        waitForObject(mode_button),
        x, y,
        Qt.NoModifier,
        Qt.LeftButton
    )

    waitForObject(names.centralWidget_lbTitle_QLabel)

    popup = waitForObject(names.centralWidget_backgroundWidget_QWidget)

    children = getAllChildObjects(popup)

    available_modes = []

    test.log("========== {} MODE EXTRACTION ==========".format(pedal_name))

    for child in children:
        try:
            widget_class = str(className(child))
            object_name = str(child.objectName)
            text = str(child.text).strip()
        except:
            continue

        if widget_class != "QPushButton":
            continue

        if object_name == "rejectButton" or not text:
            continue

        mode_name = " ".join(text.split())

        available_modes.append({
            "object_name": object_name,
            "mode_name": mode_name
        })

        test.log("{} MODE: {} | {}".format(
            pedal_name, object_name, mode_name
        ))

    test.log("{} total modes: {}".format(
        pedal_name, len(available_modes)
    ))

    return available_modes

def extractPeakPowerOptions(mode_key, peak_power_button, x, y, pedal_name):

    excel_mode = MODE_MAPPING.get(mode_key)

    if excel_mode is None:
        test.log("Skipping {} - Peak Power is not applicable".format(mode_key))
        return None

    test.log("========== {} {} PEAK POWER VERIFICATION ==========".format(
        pedal_name, excel_mode
    ))

    mouseClick(
        waitForObject(peak_power_button),
        x, y,
        Qt.NoModifier,
        Qt.LeftButton
    )

    popup = waitForObject(names.centralWidget_backgroundWidget_QWidget)
    children = getAllChildObjects(popup)

    # Map button object names to their Peak Power values
    peak_power_mapping = {
        "pw125": 125,
        "pw250": 250,
        "pw500": 500,
        "pw750": 750,
        "pw1000": 1000
    }

    text_mapping = {
        "Low": 125,
        "Medium": 250,
        "High": 500
    }

    actual_values = []

    for child in children:
        try:
            widget_class = str(className(child))
            object_name = str(child.objectName).strip()
            text = str(child.text).strip()
        except:
            continue

        if widget_class != "QPushButton":
            continue

        value = peak_power_mapping.get(object_name)

        if value is None:
            value = text_mapping.get(text)

        if value is not None:
            actual_values.append(value)

            test.log("{} option found: {} | {} W".format(
                pedal_name, object_name, value
            ))

    actual_values = sorted(set(actual_values))
    expected_values = sorted(ECONOMY_C_PEAK_POWER[excel_mode])

    if actual_values == expected_values:
        test.passes(
            "PASS: {} {} | Actual: {} W | Expected: {} W".format(
                pedal_name, excel_mode, actual_values, expected_values
            )
        )
        result = True
    else:
        test.fail(
            "FAIL: {} {} | Actual: {} W | Expected: {} W".format(
                pedal_name, excel_mode, actual_values, expected_values
            )
        )
        result = False

    clickButton(waitForObject(names.buttonsFrame_rejectButton_QPushButton))

    return result

def verifyDisabledModePeakPower(mode_key, peak_power_object, pedal_name):

    excel_mode = MODE_MAPPING.get(mode_key)
    expected_values = ECONOMY_C_PEAK_POWER[excel_mode]

    try:
        peak_power = waitForObjectExists(peak_power_object)

        actual_maximum = float(
            str(peak_power.maximumPeakPower).strip()
        )

        expected_value = expected_values[0]

        test.log(
            "{} {} | Actual Maximum: {} W | Expected: {} W".format(
                pedal_name, excel_mode,
                actual_maximum, expected_value
            )
        )

        if actual_maximum == expected_value:
            test.passes(
                "PASS: {} {} | Peak Power: {} W".format(
                    pedal_name, excel_mode, actual_maximum
                )
            )
            return True

        test.fail(
            "FAIL: {} {} | Actual: {} W | Expected: {} W".format(
                pedal_name, excel_mode,
                actual_maximum, expected_value
            )
        )
        return False

    except Exception as error:
        test.fail(
            "{} {} verification failed: {}".format(
                pedal_name, excel_mode, error
            )
        )
        return False


def main():
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton))
    snooze(5)
    clickButton(waitForObject(names.centralWidget_okButton_QPushButton))
    clickButton(waitForObject(names.gbExpert_expertButton_QPushButton))
    
    left_modes = inspectAvailableModes( names.modeButton_nameLabel_QLabel, "LEFT", 74, 33,)
    
    clickButton(waitForObject(names.buttonsFrame_rejectButton_QPushButton))
    test.log("LEFT PEDAL AVAILABLE MODES: {}".format(left_modes))
    
    standard_result = extractPeakPowerOptions("Square", names.peakPowerButton_iconLabel_QLabel, 4, 18, "LEFT")
    
    # mouseClick(waitForObject(names.modeButton_nameLabel_QLabel), 74, 33, Qt.NoModifier, Qt.LeftButton)
    # clickButton(waitForObject(names.buttonsFrame_rejectButton_QPushButton))
    # mouseClick(waitForObject(names.peakPowerButton_iconLabel_QLabel), 4, 18, Qt.NoModifier, Qt.LeftButton)
    # clickButton(waitForObject(names.buttonsFrame_rejectButton_QPushButton))
    
    mouseClick(waitForObject(names.modeButton_nameLabel_QLabel), 63, 25, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_MRP_QPushButton))
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    # mouseClick(waitForObject(names.peakPowerButton_iconLabel_QLabel), 3, 18, Qt.NoModifier, Qt.LeftButton)
    # clickButton(waitForObject(names.buttonsFrame_rejectButton_QPushButton))
    
    left_mrp_result = extractPeakPowerOptions( "MRP", names.peakPowerButton_iconLabel_QLabel, 3, 18, "LEFT")
    
    mouseClick(waitForObject(names.modeButton_nameLabel_QLabel), 87, 20, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_Fragmentation_QPushButton))
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    # mouseClick(waitForObject(names.peakPowerButton_iconLabel_QLabel), 0, 26, Qt.NoModifier, Qt.LeftButton)
    # clickButton(waitForObject(names.buttonsFrame_rejectButton_QPushButton))
    
    left_fragmentation_result = extractPeakPowerOptions( "Fragmentation", names.peakPowerButton_iconLabel_QLabel, 0, 26, "LEFT")
    
    mouseClick(waitForObject(names.modeButton_nameLabel_QLabel), 94, 22, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_Dusting_QPushButton))
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))

    left_dusting_result = verifyDisabledModePeakPower( "Dusting", names.pulseModeWidget_peakPowerButton_ParameterSettingsButton, "LEFT")
    
    mouseClick(waitForObject(names.modeButton_nameLabel_QLabel), 71, 16, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_Enucleation_QPushButton))
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    # mouseClick(waitForObject(names.peakPowerButton_iconLabel_QLabel), 28, 23, Qt.NoModifier, Qt.LeftButton)
    # clickButton(waitForObject(names.buttonsFrame_rejectButton_QPushButton))
    
    left_Enucleation_result = extractPeakPowerOptions( "Enucleation", names.peakPowerButton_iconLabel_QLabel, 28, 23, "LEFT")
    
    mouseClick(waitForObject(names.modeButton_nameLabel_QLabel), 73, 28, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_Cleaning_QPushButton))
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    # mouseClick(waitForObject(names.peakPowerButton_iconLabel_QLabel), 25, 51, Qt.NoModifier, Qt.LeftButton)
    # clickButton(waitForObject(names.buttonsFrame_rejectButton_QPushButton))
    
    left_Cleaning_result = extractPeakPowerOptions( "Cleaning", names.peakPowerButton_iconLabel_QLabel, 25, 51, "LEFT")
    
    
    right_modes = inspectAvailableModes(names.modeButton_nameLabel_QLabel_2, "RIGHT", 69, 27)   
     
    # mouseClick(waitForObject(names.modeButton_nameLabel_QLabel_2), 57, 21, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.buttonsFrame_rejectButton_QPushButton))
    test.log("RIGHT MODES: {}".format(right_modes))
    

    right_standard_result = extractPeakPowerOptions( "Square", names.peakPowerButton_nameLabel_QLabel_2, 7, 54, "RIGHT")
    
    # mouseClick(waitForObject(names.modeButton_nameLabel_QLabel_2), 69, 27, Qt.NoModifier, Qt.LeftButton)
    # clickButton(waitForObject(names.buttonsFrame_rejectButton_QPushButton))
    # mouseClick(waitForObject(names.peakPowerButton_nameLabel_QLabel_2), 35, 30, Qt.NoModifier, Qt.LeftButton)
    # clickButton(waitForObject(names.buttonsFrame_rejectButton_QPushButton))
    
    mouseClick(waitForObject(names.modeButton_nameLabel_QLabel_2), 73, 50, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_MRP_QPushButton))
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    # mouseClick(waitForObject(names.peakPowerButton_nameLabel_QLabel_2), 14, 27, Qt.NoModifier, Qt.LeftButton)
    # clickButton(waitForObject(names.buttonsFrame_rejectButton_QPushButton))
    
    right_mrp_result = extractPeakPowerOptions( "MRP", names.peakPowerButton_iconLabel_QLabel_2, 14, 27, "RIGHT")
    
    mouseClick(waitForObject(names.modeButton_nameLabel_QLabel_2), 27, 11, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_Fragmentation_QPushButton))
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    # mouseClick(waitForObject(names.peakPowerButton_nameLabel_QLabel_2), 40, 56, Qt.NoModifier, Qt.LeftButton)
    # clickButton(waitForObject(names.buttonsFrame_rejectButton_QPushButton))
    
    right_fragmentation_result = extractPeakPowerOptions( "Fragmentation", names.peakPowerButton_iconLabel_QLabel_2, 40, 56, "RIGHT")
    
    mouseClick(waitForObject(names.modeButton_nameLabel_QLabel_2), 28, 28, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_Dusting_QPushButton))
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    
    right_dusting_result = verifyDisabledModePeakPower( "Dusting", names.pulseModeWidget_peakPowerButton_ParameterSettingsButton_2, "RIGHT")
    
    mouseClick(waitForObject(names.modeButton_nameLabel_QLabel_2), 70, 26, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_Enucleation_QPushButton))
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    # mouseClick(waitForObject(names.peakPowerButton_nameLabel_QLabel_2), 53, 21, Qt.NoModifier, Qt.LeftButton)
    # clickButton(waitForObject(names.buttonsFrame_rejectButton_QPushButton))
    
    right_Enucleation_result = extractPeakPowerOptions( "Enucleation", names.peakPowerButton_iconLabel_QLabel_2, 53, 21, "RIGHT")
    
    mouseClick(waitForObject(names.modeButton_nameLabel_QLabel_2), 83, 1, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_Cleaning_QPushButton))
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    # mouseClick(waitForObject(names.peakPowerButton_nameLabel_QLabel_2), 49, 24, Qt.NoModifier, Qt.LeftButton)
    # clickButton(waitForObject(names.buttonsFrame_rejectButton_QPushButton))
    
    right_Cleaning_result = extractPeakPowerOptions( "Cleaning", names.peakPowerButton_iconLabel_QLabel_2, 49, 24, "RIGHT")
    
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
