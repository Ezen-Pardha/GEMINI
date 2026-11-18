# -*- coding: utf-8 -*-

import names
import builtins

EXPECTED_AVERAGE_POWER = 70

left_frequency_increment_button = names.frequencyWidget_incrementButton_QPushButton
right_frequency_increment_button = names.frequencyWidget_incrementButton_QPushButton_2

LEFT_AVERAGE_POWER_LABEL = names.valueLabelBackgroundWithQuantityText_valueLabel_QLabel
RIGHT_AVERAGE_POWER_LABEL = names.valueLabelBackgroundWithQuantityText_valueLabel_QLabel_2

def inspectAveragePower(averagePower_object, valueType):        
    
    if (valueType == "Value"):
        average_power = float(str(waitForObjectExists(averagePower_object).text).strip())   
    
    if (valueType == "Cylinder"):
        average_power = float(str(waitForObjectExists(averagePower_object).displayedValue).strip())
        
    return average_power

def incrementButton(button_object, valueType, averagePower_object, expected_powers, max_clicks=50 ):
    clicks = 0
    while clicks <= max_clicks:
        
        current_power = inspectAveragePower(averagePower_object, valueType)

        # Check whether current power satisfies the condition
        if (current_power == expected_powers):
            test.passes("Successful Confirmation that maximum average power : {}".format(current_power))
            return True 
        
        # Check whether increment button exists
        if not object.exists(button_object):
            test.fail("Increment button does not exist. Maximum Frequency Reached.")
            return False
        
        if clicks == max_clicks:
            break       

        # Click increment button
        clickButton(waitForObject(button_object))
        
        clicks += 1
        snooze(0.5)
    
    return False


def main():
    doubleClick(waitForObject(names.numpad_pushButton_8_NumpadButton), 67, 71, Qt.NoModifier, Qt.LeftButton)
    doubleClick(waitForObject(names.numpad_pushButton_8_NumpadButton), 67, 71, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton))
    clickButton(waitForObject(names.centralWidget_okButton_QPushButton))
    clickButton(waitForObject(names.gbExpert_expertButton_QPushButton))
    
    # clickButton(waitForObject(names.frequencyWidget_incrementButton_QPushButton))
    # clickButton(waitForObject(names.frequencyWidget_incrementButton_QPushButton))
    # clickButton(waitForObject(names.frequencyWidget_incrementButton_QPushButton))
    # clickButton(waitForObject(names.frequencyWidget_incrementButton_QPushButton))
    # clickButton(waitForObject(names.frequencyWidget_incrementButton_QPushButton))
    # doubleClick(waitForObject(names.frequencyWidget_incrementButton_QPushButton_2), 43, 16, Qt.NoModifier, Qt.LeftButton)
    # doubleClick(waitForObject(names.frequencyWidget_incrementButton_QPushButton_2), 43, 16, Qt.NoModifier, Qt.LeftButton)
    # clickButton(waitForObject(names.frequencyWidget_incrementButton_QPushButton_2))
    # mouseClick(waitForObject(names.valueLabelBackgroundWithQuantityText_valueLabel_QLabel_2), 199, 17, Qt.NoModifier, Qt.LeftButton)
    # mouseClick(waitForObject(names.valueLabelBackgroundWithQuantityText_valueLabel_QLabel), 174, 23, Qt.NoModifier, Qt.LeftButton)
    
    #Regular Pulse    
    if incrementButton(left_frequency_increment_button, "Value", LEFT_AVERAGE_POWER_LABEL, EXPECTED_AVERAGE_POWER):
        test.passes("Left Pedal REGULAR PULSE MAX POWER : {}". format(EXPECTED_AVERAGE_POWER))
    else:
        test.fail("Left Pedal REGULAR PULSE MAX POWER is not : {}". format(EXPECTED_AVERAGE_POWER))        
    
    if incrementButton(right_frequency_increment_button, "Value", RIGHT_AVERAGE_POWER_LABEL, EXPECTED_AVERAGE_POWER):
        test.passes("RIGHT Pedal REGULAR PULSE MAX POWER : {}". format(EXPECTED_AVERAGE_POWER))
    else:
        test.fail("RIGHT Pedal REGULAR PULSE MAX POWER is not : {}". format(EXPECTED_AVERAGE_POWER))
    
    mouseClick(waitForObject(names.modeButton_nameLabel_QLabel), 94, 21, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_CW_QPushButton))
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    mouseClick(waitForObject(names.modeButton_nameLabel_QLabel_2), 44, 22, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_CW_QPushButton))
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    
    # mouseClick(waitForObject(names.valueDrum_Cylinder_4), 223, 11, Qt.NoModifier, Qt.LeftButton)
    # mouseClick(waitForObject(names.valueDrum_Cylinder_3), 204, 3, Qt.NoModifier, Qt.LeftButton)
    #
    # clickButton(waitForObject(names.powerWidgetCW_incrementButton_QPushButton))
    # doubleClick(waitForObject(names.powerWidgetCW_incrementButton_QPushButton), 34, 20, Qt.NoModifier, Qt.LeftButton)
    # doubleClick(waitForObject(names.powerWidgetCW_incrementButton_QPushButton_2), 35, 33, Qt.NoModifier, Qt.LeftButton)
    # clickButton(waitForObject(names.powerWidgetCW_incrementButton_QPushButton_2))
    
    if incrementButton(names.powerWidgetCW_incrementButton_QPushButton, "Cylinder",  names.valueDrum_Cylinder_3, EXPECTED_AVERAGE_POWER):
        test.passes("Left Pedal CONTINOUS WAVE PULSE MAX POWER : {}". format(EXPECTED_AVERAGE_POWER))
    else:
        test.fail("Left Pedal CONTINOUS WAVE PULSE MAX POWER is not : {}". format(EXPECTED_AVERAGE_POWER))        
    
    if incrementButton(names.powerWidgetCW_incrementButton_QPushButton_2,"Cylinder", names.valueDrum_Cylinder_4, EXPECTED_AVERAGE_POWER):
        test.passes("RIGHT Pedal CONTINOUS WAVE PULSE MAX POWER : {}". format(EXPECTED_AVERAGE_POWER))
    else:
        test.fail("RIGHT Pedal CONTINOUS WAVE PULSE MAX POWER is not : {}". format(EXPECTED_AVERAGE_POWER))
    
    mouseClick(waitForObject(names.modeButtonCW_nameLabel_QLabel), 105, 17, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_MRP_QPushButton))
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    mouseClick(waitForObject(names.modeButtonCW_nameLabel_QLabel_2), 35, 19, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_MRP_QPushButton))
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    # doubleClick(waitForObject(names.frequencyWidget_incrementButton_QPushButton), 37, 24, Qt.NoModifier, Qt.LeftButton)
    # clickButton(waitForObject(names.frequencyWidget_incrementButton_QPushButton_2))
    # clickButton(waitForObject(names.frequencyWidget_incrementButton_QPushButton_2))
    
    if incrementButton(left_frequency_increment_button,"Value", LEFT_AVERAGE_POWER_LABEL, EXPECTED_AVERAGE_POWER):
        test.passes("Left Pedal MRP PULSE MAX POWER : {}". format(EXPECTED_AVERAGE_POWER))
    else:
        test.fail("Left Pedal MRP PULSE MAX POWER is not : {}". format(EXPECTED_AVERAGE_POWER))        
    
    if incrementButton(right_frequency_increment_button,"Value", RIGHT_AVERAGE_POWER_LABEL, EXPECTED_AVERAGE_POWER):
        test.passes("RIGHT Pedal MRP PULSE MAX POWER : {}". format(EXPECTED_AVERAGE_POWER))
    else:
        test.fail("RIGHT Pedal MRP PULSE MAX POWER is not : {}". format(EXPECTED_AVERAGE_POWER))
    
    mouseClick(waitForObject(names.modeButton_nameLabel_QLabel), 7, 32, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_Fragmentation_QPushButton))
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    mouseClick(waitForObject(names.modeButton_nameLabel_QLabel_2), 29, 28, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_Fragmentation_QPushButton))
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    # clickButton(waitForObject(names.frequencyWidget_incrementButton_QPushButton))
    # clickButton(waitForObject(names.frequencyWidget_incrementButton_QPushButton))
    # doubleClick(waitForObject(names.frequencyWidget_incrementButton_QPushButton_2), 14, 25, Qt.NoModifier, Qt.LeftButton)
    
    if incrementButton(left_frequency_increment_button,"Value", LEFT_AVERAGE_POWER_LABEL, EXPECTED_AVERAGE_POWER):
        test.passes("Left Pedal Fragmentation PULSE MAX POWER : {}". format(EXPECTED_AVERAGE_POWER))
    else:
        test.fail("Left Pedal Fragmentation PULSE MAX POWER is not : {}". format(EXPECTED_AVERAGE_POWER))        
    
    if incrementButton(right_frequency_increment_button,"Value", RIGHT_AVERAGE_POWER_LABEL, EXPECTED_AVERAGE_POWER):
        test.passes("RIGHT Pedal Fragmentation PULSE MAX POWER : {}". format(EXPECTED_AVERAGE_POWER))
    else:
        test.fail("RIGHT Pedal Fragmentation PULSE MAX POWER is not : {}". format(EXPECTED_AVERAGE_POWER))
    
    mouseClick(waitForObject(names.modeButton_nameLabel_QLabel), 56, 20, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_Dusting_QPushButton))
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    mouseClick(waitForObject(names.modeButton_nameLabel_QLabel_2), 28, 9, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_Dusting_QPushButton))
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    # clickButton(waitForObject(names.frequencyWidget_incrementButton_QPushButton_2))
    # clickButton(waitForObject(names.frequencyWidget_incrementButton_QPushButton))
    
    if incrementButton(left_frequency_increment_button,"Value", LEFT_AVERAGE_POWER_LABEL, EXPECTED_AVERAGE_POWER):
        test.passes("Left Pedal Dusting PULSE MAX POWER : {}". format(EXPECTED_AVERAGE_POWER))
    else:
        test.fail("Left Pedal Dusting PULSE MAX POWER is not : {}". format(EXPECTED_AVERAGE_POWER))        
    
    if incrementButton(right_frequency_increment_button,"Value", RIGHT_AVERAGE_POWER_LABEL, EXPECTED_AVERAGE_POWER):
        test.passes("RIGHT Pedal Dusting PULSE MAX POWER : {}". format(EXPECTED_AVERAGE_POWER))
    else:
        test.fail("RIGHT Pedal Dusting PULSE MAX POWER is not : {}". format(EXPECTED_AVERAGE_POWER))
    
    mouseClick(waitForObject(names.modeButton_nameLabel_QLabel), 93, 23, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_Enucleation_QPushButton))
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    mouseClick(waitForObject(names.modeButton_nameLabel_QLabel_2), 41, 5, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_Enucleation_QPushButton))
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    # doubleClick(waitForObject(names.frequencyWidget_incrementButton_QPushButton), 11, 7, Qt.NoModifier, Qt.LeftButton)
    # clickButton(waitForObject(names.frequencyWidget_incrementButton_QPushButton_2))
    
    if incrementButton(left_frequency_increment_button,"Value", LEFT_AVERAGE_POWER_LABEL, EXPECTED_AVERAGE_POWER):
        test.passes("Left Pedal Enucleation PULSE MAX POWER : {}". format(EXPECTED_AVERAGE_POWER))
    else:
        test.fail("Left Pedal Enucleation PULSE MAX POWER is not : {}". format(EXPECTED_AVERAGE_POWER))        
    
    if incrementButton(right_frequency_increment_button,"Value", RIGHT_AVERAGE_POWER_LABEL, EXPECTED_AVERAGE_POWER):
        test.passes("RIGHT Pedal Enucleation PULSE MAX POWER : {}". format(EXPECTED_AVERAGE_POWER))
    else:
        test.fail("RIGHT Pedal Enucleation PULSE MAX POWER is not : {}". format(EXPECTED_AVERAGE_POWER))
    
    mouseClick(waitForObject(names.modeButton_nameLabel_QLabel), 50, 16, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_Cleaning_QPushButton))
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    mouseClick(waitForObject(names.modeButton_nameLabel_QLabel_2), 50, 13, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_Cleaning_QPushButton))
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    
    if incrementButton(left_frequency_increment_button,"Value", LEFT_AVERAGE_POWER_LABEL, EXPECTED_AVERAGE_POWER):
        test.passes("Left Pedal Minimal Vaporization PULSE MAX POWER : {}". format(EXPECTED_AVERAGE_POWER))
    else:
        test.fail("Left Pedal Minimal Vaporization PULSE MAX POWER is not : {}". format(EXPECTED_AVERAGE_POWER))        
    
    if incrementButton(right_frequency_increment_button,"Value", RIGHT_AVERAGE_POWER_LABEL, EXPECTED_AVERAGE_POWER):
        test.passes("RIGHT Pedal Minimal Vaporization PULSE MAX POWER : {}". format(EXPECTED_AVERAGE_POWER))
    else:
        test.fail("RIGHT Pedal Minimal Vaporization PULSE MAX POWER is not : {}". format(EXPECTED_AVERAGE_POWER))
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
