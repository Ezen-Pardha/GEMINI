# -*- coding: utf-8 -*-

import names
import builtins
    
EXPECTED_AVERAGE_POWER = 60

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
    
    doubleClick(waitForObject(names.numpad_pushButton_8_NumpadButton), 96, 76, Qt.NoModifier, Qt.LeftButton)
    doubleClick(waitForObject(names.numpad_pushButton_8_NumpadButton), 96, 76, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton))
    clickButton(waitForObject(names.gbExpert_expertButton_QPushButton))
    mouseClick(waitForObject(names.valueLabelBackgroundWithQuantityText_valueLabel_QLabel_2), 150, 24, Qt.NoModifier, Qt.LeftButton)

    #Regular Pulse    
    if incrementButton(left_frequency_increment_button, "Value", LEFT_AVERAGE_POWER_LABEL, EXPECTED_AVERAGE_POWER):
        test.passes("Left Pedal REGULAR PULSE MAX POWER : {}". format(EXPECTED_AVERAGE_POWER))
    else:
        test.fail("Left Pedal REGULAR PULSE MAX POWER is not : {}". format(EXPECTED_AVERAGE_POWER))        
    
    if incrementButton(right_frequency_increment_button, "Value", RIGHT_AVERAGE_POWER_LABEL, EXPECTED_AVERAGE_POWER):
        test.passes("RIGHT Pedal REGULAR PULSE MAX POWER : {}". format(EXPECTED_AVERAGE_POWER))
    else:
        test.fail("RIGHT Pedal REGULAR PULSE MAX POWER is not : {}". format(EXPECTED_AVERAGE_POWER))
    
    mouseClick(waitForObject(names.modeButton_nameLabel_QLabel), 117, 35, Qt.NoModifier, Qt.LeftButton)    
    clickButton(waitForObject(names.centralWidget_CW_QPushButton))
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))

    mouseClick(waitForObject(names.modeButton_nameLabel_QLabel_2), 66, 10, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_CW_QPushButton))
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))

    if incrementButton(names.powerWidgetCW_incrementButton_QPushButton, "Cylinder",  names.valueDrum_Cylinder_3, EXPECTED_AVERAGE_POWER):
        test.passes("Left Pedal CONTINOUS WAVE PULSE MAX POWER : {}". format(EXPECTED_AVERAGE_POWER))
    else:
        test.fail("Left Pedal CONTINOUS WAVE PULSE MAX POWER is not : {}". format(EXPECTED_AVERAGE_POWER))        
    
    if incrementButton(names.powerWidgetCW_incrementButton_QPushButton_2,"Cylinder", names.valueDrum_Cylinder_4, EXPECTED_AVERAGE_POWER):
        test.passes("RIGHT Pedal CONTINOUS WAVE PULSE MAX POWER : {}". format(EXPECTED_AVERAGE_POWER))
    else:
        test.fail("RIGHT Pedal CONTINOUS WAVE PULSE MAX POWER is not : {}". format(EXPECTED_AVERAGE_POWER))
    
    mouseClick(waitForObject(names.modeButtonCW_nameLabel_QLabel), 90, 35, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_MRP_QPushButton))
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    
    mouseClick(waitForObject(names.modeButtonCW_nameLabel_QLabel_2), 66, 14, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_MRP_QPushButton))
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    
    if incrementButton(left_frequency_increment_button,"Value", LEFT_AVERAGE_POWER_LABEL, EXPECTED_AVERAGE_POWER):
        test.passes("Left Pedal MRP PULSE MAX POWER : {}". format(EXPECTED_AVERAGE_POWER))
    else:
        test.fail("Left Pedal MRP PULSE MAX POWER is not : {}". format(EXPECTED_AVERAGE_POWER))        
    
    if incrementButton(right_frequency_increment_button,"Value", RIGHT_AVERAGE_POWER_LABEL, EXPECTED_AVERAGE_POWER):
        test.passes("RIGHT Pedal MRP PULSE MAX POWER : {}". format(EXPECTED_AVERAGE_POWER))
    else:
        test.fail("RIGHT Pedal MRP PULSE MAX POWER is not : {}". format(EXPECTED_AVERAGE_POWER))
    
    mouseClick(waitForObject(names.modeButton_nameLabel_QLabel), 77, 7, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_Fragmentation_QPushButton))
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    mouseClick(waitForObject(names.modeButton_nameLabel_QLabel_2), 40, 15, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_Fragmentation_QPushButton))
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    
    if incrementButton(left_frequency_increment_button,"Value", LEFT_AVERAGE_POWER_LABEL, EXPECTED_AVERAGE_POWER):
        test.passes("Left Pedal Fragmentation PULSE MAX POWER : {}". format(EXPECTED_AVERAGE_POWER))
    else:
        test.fail("Left Pedal Fragmentation PULSE MAX POWER is not : {}". format(EXPECTED_AVERAGE_POWER))        
    
    if incrementButton(right_frequency_increment_button,"Value", RIGHT_AVERAGE_POWER_LABEL, EXPECTED_AVERAGE_POWER):
        test.passes("RIGHT Pedal Fragmentation PULSE MAX POWER : {}". format(EXPECTED_AVERAGE_POWER))
    else:
        test.fail("RIGHT Pedal Fragmentation PULSE MAX POWER is not : {}". format(EXPECTED_AVERAGE_POWER))  
    
    
    mouseClick(waitForObject(names.modeButton_nameLabel_QLabel), 96, 28, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_Cleaning_QPushButton))
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    mouseClick(waitForObject(names.modeButton_nameLabel_QLabel_2), 69, 10, Qt.NoModifier, Qt.LeftButton)
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
    
    mouseClick(waitForObject(names.modeButton_nameLabel_QLabel), 66, 40, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_Enucleation_QPushButton))
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    mouseClick(waitForObject(names.modeButton_nameLabel_QLabel_2), 51, 4, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_Enucleation_QPushButton))
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    
    if incrementButton(left_frequency_increment_button,"Value", LEFT_AVERAGE_POWER_LABEL, EXPECTED_AVERAGE_POWER):
        test.passes("Left Pedal Enucleation PULSE MAX POWER : {}". format(EXPECTED_AVERAGE_POWER))
    else:
        test.fail("Left Pedal Enucleation PULSE MAX POWER is not : {}". format(EXPECTED_AVERAGE_POWER))        
    
    if incrementButton(right_frequency_increment_button,"Value", RIGHT_AVERAGE_POWER_LABEL, EXPECTED_AVERAGE_POWER):
        test.passes("RIGHT Pedal Enucleation PULSE MAX POWER : {}". format(EXPECTED_AVERAGE_POWER))
    else:
        test.fail("RIGHT Pedal Enucleation PULSE MAX POWER is not : {}". format(EXPECTED_AVERAGE_POWER))
        
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
