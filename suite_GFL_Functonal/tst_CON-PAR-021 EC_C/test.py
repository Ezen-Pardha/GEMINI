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

    # Frequency objects
    frequency = names.valueDrum_Cylinder_2
    increment = names.frequencyWidget_incrementButton_QPushButton
    decrement = names.frequencyWidget_decrementButton_QPushButton

    def get_frequency():
        return float(str(
            waitForObjectExists(frequency).displayedValue
        ).strip())

    def button_enabled(button):
        try:
            obj = findObject(button)
            return obj.visible and obj.enabled
        except LookupError:
            return False

    # Find minimum frequency
    actual = get_frequency()

    while button_enabled(decrement):

        previous = actual

        clickButton(waitForObject(decrement))
        snooze(0.5)

        actual = get_frequency()

        if actual >= previous:
            break

    minimum = get_frequency()

    # Find maximum frequency
    while button_enabled(increment):

        previous = actual

        clickButton(waitForObject(increment))
        snooze(0.5)

        actual = get_frequency()

        if actual <= previous:
            break

    maximum = get_frequency()

    # Verify frequency range
    expected_minimum = 2.7
    expected_maximum = 300.0

    test.log(
        "Expected frequency range: " +
        str(expected_minimum) + " Hz - " +
        str(expected_maximum) + " Hz"
    )

    test.log(
        "Actual frequency range: " +
        str(minimum) + " Hz - " +
        str(maximum) + " Hz"
    )

    if (abs(minimum - expected_minimum) < 0.001 and
            abs(maximum - expected_maximum) < 0.001):

        test.passes(
            "PASS: Dusting pulse frequency range is "
            "2.7 Hz - 300 Hz"
        )

    else:

        test.fail(
            "FAIL: Dusting pulse frequency range is " +
            str(minimum) + " Hz - " +
            str(maximum) +
            " Hz. Expected: 2.7 Hz - 300 Hz"
        )

    runtime_path = os.path.expanduser(
        "/home/ntc/Downloads/Gemini"
    )

    configure_system_type(
        new_type="B",
        runtime_path=runtime_path
    )




