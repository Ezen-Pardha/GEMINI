# -*- coding: utf-8 -*-

import names

ECONOMY_A_PEAK_POWER = {
    "Standard": [125, 250, 500],
    "MRP": [500],
    "Fragmentation": [500],
    "Enucleation": [500],
    "Minimal Vaporization": [500]
}

MODE_MAPPING = {
    "Square": "Standard",
    "MRP": "MRP",
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
        all_children.extend( getAllChildObjects(child))

    return all_children
    
def verifyStandardPeakPower(peak_power_options):

    expected = ECONOMY_A_PEAK_POWER["Standard"]
    actual = sorted(peak_power_options)
    if actual == sorted(expected):
        test.passes("PASS: Standard Peak Power options match {}".format(expected))
        return True

    test.fail("FAIL: Standard Peak Power options. Actual: {}, Expected: {}".format(actual, expected))
    return False


#
def verifyMaximumPeakPower(mode_key, peak_power_object):

    excel_mode = MODE_MAPPING.get(mode_key)

    if excel_mode is None:
        test.log("Skipping CW - Peak Power is not applicable")
        return None

    try:
        expected_maximum = max(ECONOMY_A_PEAK_POWER[excel_mode])
        peak_power = waitForObjectExists(peak_power_object)

        actual_maximum = float(str(peak_power.maximumPeakPower).strip())

        if actual_maximum == expected_maximum:
            test.passes("PASS: {} | Actual Maximum: {} W | Expected: {} W".format(
                    excel_mode, actual_maximum, expected_maximum))
            return True

        else:
            test.fail( "FAIL: {} | Actual Maximum: {} W | Expected: {} W".format(
                    excel_mode, actual_maximum, expected_maximum))
            return False

    except Exception as error:
        test.fail("Peak Power verification failed for {}: {}".format(
                mode_key, error))
        return False

def extractStandardPeakPowerOptions(peak_power_button, x, y, pedal_name):

    # Open the Peak Power popup
    mouseClick(
        waitForObject(peak_power_button),
        x, y,
        Qt.NoModifier,
        Qt.LeftButton
    )

    popup = waitForObject(names.centralWidget_backgroundWidget_QWidget)
    children = getAllChildObjects(popup)

    # Map the displayed button text to its Peak Power value
    peak_power_mapping = {
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

        if widget_class == "QPushButton" and text in peak_power_mapping:
            value = peak_power_mapping[text]
            actual_values.append(value)

            test.log(
                "Peak Power option found: {} | {} W".format(
                    object_name, value
                )
            )

    actual_values = sorted(set(actual_values))
    expected_values = sorted(ECONOMY_A_PEAK_POWER["Standard"])

    if actual_values == expected_values:
        test.passes("PASS: Standard Peak Power options. Actual: {}, Expected: {}".format(
                actual_values, expected_values
            )
        )
        result = True
    else:
        test.fail("FAIL: Standard Peak Power options. Actual: {}, Expected: {}".format(
                actual_values, expected_values
            )
        )
        result = False

    # Close the Peak Power popup
    clickButton(waitForObject(names.buttonsFrame_rejectButton_QPushButton))

    return result

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

    test.log("{} MODE EXTRACTION".format(pedal_name))

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

        test.log(
            "{} MODE: {} | {}".format(
                pedal_name,
                object_name,
                mode_name
            )
        )

    test.log(
        "{} total modes: {}".format(
            pedal_name,
            len(available_modes)
        )
    )

    return available_modes



def main():
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton))
    clickButton(waitForObject(names.gbExpert_expertButton_QPushButton))
    
    #mouseClick(waitForObject(names.modeButton_nameLabel_QLabel), 52, 22, Qt.NoModifier, Qt.LeftButton)
    #mouseClick(waitForObject(names.centralWidget_label_2_QLabel), 551, 7, Qt.NoModifier, Qt.LeftButton)
    
    left_modes = inspectAvailableModes( names.modeButton_nameLabel_QLabel, "LEFT", 52, 22)
    
    clickButton(waitForObject(names.buttonsFrame_rejectButton_QPushButton))
    test.log("LEFT PEDAL AVAILABLE MODES: {}".format(left_modes))
    
    # mouseClick(waitForObject(names.peakPowerButton_iconLabel_QLabel), 40, 26, Qt.NoModifier, Qt.LeftButton)
    # mouseClick(waitForObject(names.centralWidget_mainWidget_QWidget), 540, 0, Qt.NoModifier, Qt.LeftButton)
    # clickButton(waitForObject(names.buttonsFrame_rejectButton_QPushButton))
    standard_result = extractStandardPeakPowerOptions(names.peakPowerButton_iconLabel_QLabel, 40, 26, "LEFT")
    
    mouseClick(waitForObject(names.modeButton_nameLabel_QLabel), 67, 32, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_MRP_QPushButton))
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    
    mrp_result = verifyMaximumPeakPower( "MRP", names.pulseModeWidget_peakPowerButton_ParameterSettingsButton)
    
    mouseClick(waitForObject(names.modeButton_nameLabel_QLabel), 105, 14, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_Fragmentation_QPushButton))
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    
    fragmentation_result = verifyMaximumPeakPower( "Fragmentation", names.pulseModeWidget_peakPowerButton_ParameterSettingsButton)
    
    mouseClick(waitForObject(names.modeButton_nameLabel_QLabel), 117, 5, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_Cleaning_QPushButton))
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    
    cleaning_result = verifyMaximumPeakPower( "Cleaning", names.pulseModeWidget_peakPowerButton_ParameterSettingsButton)
    
    mouseClick(waitForObject(names.pulseModeWidget_modeButton_ModeButton), 52, 3, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_Enucleation_QPushButton))
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    
    enucleation_result = verifyMaximumPeakPower( "Enucleation", names.pulseModeWidget_peakPowerButton_ParameterSettingsButton)
    
    #RIGHT
    
    right_modes = inspectAvailableModes(names.modeButton_nameLabel_QLabel_2, "RIGHT", 109, 14)
    
    # mouseClick(waitForObject(names.modeButton_nameLabel_QLabel_2), 68, 27, Qt.NoModifier, Qt.LeftButton)
    # mouseClick(waitForObject(names.centralWidget_mainWidget_QWidget), 8, 22, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.buttonsFrame_rejectButton_QPushButton))
    
    test.log("RIGHT MODES: {}".format(right_modes))
    
    # mouseClick(waitForObject(names.peakPowerButton_nameLabel_QLabel_2), 63, 43, Qt.NoModifier, Qt.LeftButton)
    # mouseClick(waitForObject(names.centralWidget_backgroundWidget_QWidget), 553, 35, Qt.NoModifier, Qt.LeftButton)
    # clickButton(waitForObject(names.buttonsFrame_rejectButton_QPushButton))
    right_standard_result = extractStandardPeakPowerOptions(names.peakPowerButton_nameLabel_QLabel_2, 63, 43, "RIGHT")
    
    mouseClick(waitForObject(names.modeButton_nameLabel_QLabel_2), 83, 30, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_MRP_QPushButton))
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    
    right_mrp_result = verifyMaximumPeakPower( "MRP",  names.pulseModeWidget_peakPowerButton_ParameterSettingsButton_2)
    
    mouseClick(waitForObject(names.modeButton_nameLabel_QLabel_2), 42, 16, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_Fragmentation_QPushButton))
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    
    right_fragmentation_result = verifyMaximumPeakPower("Fragmentation",  names.pulseModeWidget_peakPowerButton_ParameterSettingsButton_2)
    
    mouseClick(waitForObject(names.modeButton_nameLabel_QLabel_2), 69, 20, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_Cleaning_QPushButton))
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    
    right_cleaning_result = verifyMaximumPeakPower("Cleaning",  names.pulseModeWidget_peakPowerButton_ParameterSettingsButton_2)
    
    mouseClick(waitForObject(names.modeButton_nameLabel_QLabel_2), 38, 24, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_Enucleation_QPushButton))
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    
    right_enucleation_result = verifyMaximumPeakPower("Enucleation",  names.pulseModeWidget_peakPowerButton_ParameterSettingsButton_2)
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    
    
    
    
