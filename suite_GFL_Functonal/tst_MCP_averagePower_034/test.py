# -*- coding: utf-8 -*-

import names

def inspectPulseEnergy():
    cylinder = waitForObject(names.valueDrum_Cylinder)
    pulse_energy = str(cylinder.displayedValue).strip()
    test.log("Pulse Energy: {}".format(pulse_energy))

    return pulse_energy

def inspectFrequency():
    cylinder = waitForObject(names.valueDrum_Cylinder_2)
    frequency = str(cylinder.displayedValue).strip()
    test.log("Frequency after conversion: {}".format(frequency))

    return frequency

def inspectAveragePower():
    average_power_object = names.valueLabelBackgroundWithQuantityText_valueLabel_QLabel
    average_power = float( str(waitForObjectExists(average_power_object).text).strip())
    
    return average_power

def checkAveragePower(expected_watts):
    average_power = inspectAveragePower()
    test.log("Displayed average power: {} W".format(average_power))
    test.log("Expected average power: {} W". format(expected_watts))
    if test.compare(average_power, expected_watts):
        test.passes("Successful Confirmation of Average Power setting is {} W".format(expected_watts))
    else:
        test.fail("Failed confirmation of Average Power setting is {} W". format(expected_watts))
    snooze(3)

def main():
    
    EXPECTED_AVERAGE_POWERS = [10, 20, 30, 40, 60]
    frequency_increment_button = names.frequencyWidget_incrementButton_QPushButton
    
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton))

    if test.vp("homescreen"):
        test.passes("Successful display of program displays HOME SCREEN")
    else:
        test.fail("Failed display of program displays HOME SCREEN")

    clickButton(waitForObject(names.gbExpert_expertButton_QPushButton))

    if test.vp("manualScreen"):
        test.passes("Successful display of program displays MANUAL SCREEN")
    else:
        test.fail("Failed display of program displays MANUAL SCREEN")

    mouseClick(waitForObject(names.modeButton_nameLabel_QLabel), 49, 50, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_Cleaning_QPushButton))
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    mouseClick(waitForObject(names.valueLabelBackgroundWithQuantityText_valueLabel_QLabel), 173, 36, Qt.NoModifier, Qt.LeftButton)
     
    mouseClick(waitForObject(names.valueDrum_Cylinder), 238, 6, Qt.NoModifier, Qt.LeftButton) 
    mouseClick(waitForObject(names.valueDrum_Cylinder_2), 239, 11, Qt.NoModifier, Qt.LeftButton) 
    
    checkAveragePower(EXPECTED_AVERAGE_POWERS[0])
    for expected_watts in EXPECTED_AVERAGE_POWERS[1:]:
        clickButton(waitForObject(frequency_increment_button))
        snooze(3)
        checkAveragePower(expected_watts)
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))




