
# -*- coding: utf-8 -*-

import names
from common import *
import re

MIN_POWER = 2.0
MAX_POWER = 60.0
MAX_FREQUENCY_ATTEMPTS = 100

def read_average_power():

    obj = waitForObjectExists(
        names.valueLabelBackgroundWithQuantityText_valueLabel_QLabel
    )

    power_text = str(obj.text).strip()

    test.log("Displayed Average Power: " + power_text)

    match = re.search(r"[-+]?\d+(?:\.\d+)?", power_text)

    if match is None:
        test.fail("Unable to read Average Power: " + power_text)
        return None

    return float(match.group())


def verify_power_range(power):

    if power is None:
        return False

    if MIN_POWER <= power <= MAX_POWER:

        test.passes(
            "PASS: Average Power within 2 W to 60 W: "
            + str(power) + " W"
        )

        return True

    test.fail(
        "FAIL: Average Power out of range. Actual: "
        + str(power) + " W. Expected: 2 W to 60 W"
    )

    return False


def increase_pulse_energy(count):

    for i in range(count):

        clickButton(waitForObject(
            names.pulseEnergyWidget_incrementButton_QPushButton
        ))

        snooze(1)

        power = read_average_power()

        if not verify_power_range(power):
            return False

    return True


def increase_frequency_until_60W():

    power = read_average_power()

    if not verify_power_range(power):
        return False

    attempts = 0

    while power < MAX_POWER and attempts < MAX_FREQUENCY_ATTEMPTS:

        previous_power = power

        # Increase frequency
        clickButton(waitForObject(
            names.frequencyWidget_incrementButton_QPushButton
        ))

        snooze(1)

        new_power = read_average_power()

        attempts += 1

        if new_power is None:
            return False

      
        if new_power > MAX_POWER:

            test.log(
                "Average Power exceeded 60 W: "
                + str(new_power) + " W"
            )

            clickButton(waitForObject(
                names.frequencyWidget_decrementButton_QPushButton
            ))

            snooze(1)

            restored_power = read_average_power()

            if restored_power is None:
                return False

            if MIN_POWER <= restored_power <= MAX_POWER:

                test.passes(
                    "PASS: Frequency restored successfully. "
                    "Average Power: "
                    + str(restored_power) + " W"
                )

                test.passes(
                    "PASS: Average Power did not remain above "
                    "the maximum limit of 60 W."
                )

                return True

            test.fail(
                "FAIL: Frequency restoration unsuccessful. "
                "Actual Average Power: "
                + str(restored_power) + " W"
            )

            return False

        if new_power < MIN_POWER:

            test.fail(
                "FAIL: Average Power below minimum 2 W. "
                "Actual: " + str(new_power) + " W"
            )

            return False

        power = new_power

        test.passes(
            "Frequency adjustment " + str(attempts) +
            ": Average Power = " + str(power) + " W"
        )

        if power == MAX_POWER:

            test.passes(
                "PASS: Average Power reached exactly 60 W."
            )

            return True

    if attempts >= MAX_FREQUENCY_ATTEMPTS and power < MAX_POWER:

        test.fail(
            "FAIL: Maximum frequency adjustment attempts reached. "
            "Final Average Power: " + str(power) + " W"
        )

        return False

    return True




def main():

    # Step 1: Login
    enter_login_pin()
    snooze(3)

    clickButton(waitForObject(
        names.centralWidget_okButton_QPushButton
    ))

    snooze(2)

    test.log("Step 1: Login completed")

  
    clickButton(waitForObject(
        names.gbExpert_expertButton_QPushButton
    ))

    clickButton(waitForObject(
        names.mainFrame_okButton_QPushButton
    ))

    snooze(3)

    test.log("Step 2: Expert screen opened")

  
    if not increase_pulse_energy(3):
        return

  
    for i in range(6):

        clickButton(waitForObject(
            names.frequencyWidget_incrementButton_QPushButton
        ))

        snooze(1)

        power = read_average_power()

        if not verify_power_range(power):
            return

   
    if not increase_pulse_energy(1):
        return

   
    for i in range(8):

        clickButton(waitForObject(
            names.frequencyWidget_incrementButton_QPushButton
        ))

        snooze(1)

        power = read_average_power()

        if not verify_power_range(power):
            return

    mouseClick(
        waitForObject(
            names.pulseModeWidget_pulseEnergyWidget_ParameterSettingsWidget
        ),
        579, 82,
        Qt.NoModifier,
        Qt.LeftButton
    )

    snooze(2)

    test.log("Step 7: Pulse Mode interaction completed")

    
    result = increase_frequency_until_60W()

    if not result:
        return

    test.passes(
        "TEST CASE PASSED: Average Power verification "
        "completed successfully within 2 W to 60 W."
    )
