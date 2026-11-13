# -*- coding: utf-8 -*-
import os
import names

from squish import *
from common import *

def main():

    # Change Economy Type to C and restart AUT
    runtime_path = os.path.expanduser(
        "/home/ntc/Downloads/Gemini"
    )

    configure_system_type(
        new_type="C",
        runtime_path=runtime_path
    )

    try:
        context = currentApplicationContext()
        context.detach()
        snooze(3)
        test.log("AUT context detached")

    except Exception as error:
        test.log("Error while closing AUT: " + str(error))

    startApplication(
        "bravo --disable-watchdog --watchdog-timeout=10 "
        "--disable-integrity-check "
        "--disable-fiber-use-check "
        "--disable-firmware-check "
        "--disable-ssm "
        "--disable-ports-check"
    )

    snooze(5)

    test.passes("Bravo AUT restart command executed successfully")
    
    # Login and navigate to Dusting Pulse Mode
    enter_login_pin()
    dismiss_fiber_verification_warning()
    
    verify_economyc_type()
    back_to_homescreen_from_servicemode()
    
    clickButton(waitForObject(names.gbExpert_expertButton_QPushButton))

    mouseClick(waitForObject(names.modeButton_nameLabel_QLabel),108, 26,Qt.NoModifier,Qt.LeftButton)

    clickButton(waitForObject(names.centralWidget_Dusting_QPushButton))

    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))

    snooze(2)
    
    waitForObject(names.valueLabelBackgroundWithQuantityText_valueLabel_QLabel)
    
    average_power = names.valueLabelBackgroundWithQuantityText_valueLabel_QLabel
    increment = names.frequencyWidget_incrementButton_QPushButton
    decrement = names.frequencyWidget_decrementButton_QPushButton
    
    
    def get_average_power():
        value = waitForObjectExists(average_power).text
        return float(str(value).replace("W", "").strip())
    
    
    def button_enabled(button):
        try:
            obj = findObject(button)
            return obj.visible and obj.enabled
        except LookupError:
            return False
    
    
    expected_power_values = [8.0, 10.0, 15.0, 20.0, 30.0, 40.0, 60.0]
    actual_power_values = []
    
    # Go to minimum power
    actual_power = get_average_power()
    
    while button_enabled(decrement):
    
        previous = actual_power
    
        clickButton(waitForObject(decrement))
        snooze(0.5)
    
        actual_power = get_average_power()
    
        if actual_power >= previous:
            break
    
    # Record minimum value
    actual_power_values.append(actual_power)
    
    test.log(
        "Minimum average power: " + str(actual_power) + " W"
    )
    
    # Increment and record every power value
    while button_enabled(increment):
    
        previous = actual_power
    
        clickButton(waitForObject(increment))
        snooze(0.5)
    
        actual_power = get_average_power()
    
        if actual_power <= previous:
            break
    
        actual_power_values.append(actual_power)
    
    maximum_power = get_average_power()

    test.log("Maximum average power: " + str(maximum_power) + " W")
    
    test.log(
        "Expected average power values: " +
        str(expected_power_values)
    )
    
    test.log(
        "Actual average power values: " +
        str(actual_power_values)
    )
    
    if actual_power_values == expected_power_values:
    
        test.passes(
            "PASS: All average power settings are correct"
        )
    
    else:
    
        test.fail(
            "FAIL: Average power settings do not match expected values"
        )
    
    runtime_path = os.path.expanduser(
        "/home/ntc/Downloads/Gemini"
    )
    
    configure_system_type(
        new_type="B",
        runtime_path=runtime_path
    )
    


