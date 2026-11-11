
# -*- coding: utf-8 -*-

from common import *
import names
import re


MIN_POWER = 2.0
MAX_POWER = 60.0
MAX_FREQUENCY_ATTEMPTS = 100


def read_average_power():
    obj = waitForObjectExists(
        names.valueLabelBackgroundWithQuantityText_valueLabel_QLabel
    )

    power_text = str(obj.text).strip()
    test.log("Displayed average power: " + power_text)

    match = re.search(r"[-+]?\d+(?:\.\d+)?", power_text)

    if match is None:
        test.fail("Unable to read average power: " + power_text)
        return None

    return float(match.group())


def verify_power_range(power):
    if power is None:
        return False

    if MIN_POWER <= power <= MAX_POWER:
        test.passes(
            "PASS: Average power is within 2 W to 60 W: "
            + str(power) + " W"
        )
        return True

    test.fail(
        "Average power out of range. Actual: "
        + str(power) + " W; Expected: 2 W to 60 W"
    )
    return False


def main():

    # Step 1: Login and navigate to Home screen
    enter_login_pin()
    snooze(3)

    clickButton(
        waitForObject(names.mainFrame_okButton_QPushButton)
    )
    snooze(3)

    test.log("Step 1: Home screen navigation completed")

    # Step 2: Navigate to Manual / Expert
    mouseClick(
        waitForObject(names.homeScreen_HomeScreen),
        639, 80,
        Qt.NoModifier,
        Qt.LeftButton
    )
    snooze(3)

    clickButton(
        waitForObject(names.gbExpert_expertButton_QPushButton)
    )
    snooze(3)

    test.log("Step 2: Manual / Expert screen opened")

    # Step 3:
    # Add the actual Standard Pulse Mode selection and OK action
    # from your recording here if they are separate actions.
    snooze(3)

    test.log("Step 3: Treatment screen navigation")

    # Step 4A: Increase pulse energy using recorded actions
    for i in range(14):
        clickButton(
            waitForObject(
                names.pulseEnergyWidget_incrementButton_QPushButton
            )
        )
        snooze(3)

        power = read_average_power()

        if power is None:
            return

        if not verify_power_range(power):
            return

    # Step 4B: Increase frequency until average power reaches 60 W
    power = read_average_power()

    if power is None:
        return

    attempts = 0

    while power < MAX_POWER and attempts < MAX_FREQUENCY_ATTEMPTS:

        previous_power = power

        doubleClick(
            waitForObject(
                names.frequencyWidget_incrementButton_QPushButton
            ),
            21, 27,
            Qt.NoModifier,
            Qt.LeftButton
        )
        snooze(3)

        power = read_average_power()
        attempts += 1

        if power is None:
            return

        if not verify_power_range(power):
            return

        if power == previous_power:
            test.fail(
                "Average power did not increase after a frequency "
                "adjustment. Last displayed value: "
                + str(power) + " W. Unable to reach 60 W."
            )
            return

    # Verify that the upper limit was actually reached
    if power == MAX_POWER:
        test.passes(
            "PASS: Economy B reached the required maximum average "
            "power of 60 W."
        )
    elif power < MAX_POWER:
        test.fail(
            "FAIL: Economy B did not reach 60 W. Final displayed "
            "average power: " + str(power) + " W."
        )

    # Step 5: Economy C has no recording
    test.fail(
        "Economy C verification FAILED:"
    )
