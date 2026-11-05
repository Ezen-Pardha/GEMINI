# -*- coding: utf-8 -*-

import names
from common import *


def read_power():
    """Read the currently displayed CW power."""

    obj = waitForObjectExists(names.valueDrum_Cylinder_3)
    value = obj.displayedValue

    if callable(value):
        value = value()

    return float(str(value).strip())


def main():

    """Step 1: Login and navigate to CW Mode"""

    enter_login_pin()
    dismiss_fiber_verification_warning()
    try:
        clickButton(
            waitForObject(names.gbExpert_expertButton_QPushButton, 32151)
        )

        mouseClick(
            waitForObject(names.modeButton_nameLabel_QLabel),
            91, 38, Qt.NoModifier, Qt.LeftButton
        )

        clickButton(
            waitForObject(names.centralWidget_CW_QPushButton)
        )

        clickButton(
            waitForObject(names.centralWidget_DisableButton_QPushButton)
        )

        test.passes("CW Mode selected successfully.")

    except Exception as error:
        test.fail(
            "ERROR: Unable to navigate to CW Mode. Details: {}"
            .format(error)
        )
        return

    """Step 2: Read the initial power value"""

    try:
        previous_power = read_power()

        test.log(
            "Initial CW power: {} W".format(previous_power)
        )

    except Exception as error:
        test.fail(
            "ERROR: Unable to read initial CW power. Details: {}"
            .format(error)
        )
        return

    """Step 3: Verify power increments of 5 W"""

    increment_count = 10

    for count in range(1, increment_count + 1):

        expected_power = previous_power + 5

        test.log(
            "Checking CW power increment {}: {} W -> {} W"
            .format(count, previous_power, expected_power)
        )

        try:
            increment_button = waitForObjectExists(
                names.powerWidgetCW_incrementButton_QPushButton,
                1000
            )

            if not increment_button.visible:
                test.fail(
                    "ERROR: CW power increment button is not visible "
                    "at {} W.".format(previous_power)
                )
                return

            if not increment_button.enabled:
                test.fail(
                    "ERROR: CW power increment button is disabled "
                    "at {} W. Cannot verify the next 5 W increment."
                    .format(previous_power)
                )
                return

            clickButton(increment_button)
            snooze(0.5)

            actual_power = read_power()

        except Exception as error:
            test.fail(
                "ERROR: Unable to increment or read CW power. "
                "Previous power: {} W. Expected power: {} W. "
                "Details: {}"
                .format(previous_power, expected_power, error)
            )
            return

        """Verify the power increases by exactly 5 W"""

        if actual_power == expected_power:

            test.passes(
                "PASS: CW power increment verified. "
                "Previous: {} W | Expected: {} W | Actual: {} W"
                .format(previous_power, expected_power, actual_power)
            )

        else:

            test.fail(
                "FAIL: Incorrect CW power increment. "
                "Previous: {} W | Expected: {} W | Actual: {} W. "
                "Expected increment: 5 W."
                .format(previous_power, expected_power, actual_power)
            )
            return

        previous_power = actual_power

    """Step 4: Final result"""

    test.passes(
        "SUCCESS: CW Mode power increments verified successfully. "
        "The power increased by 5 W for all {} increments."
        .format(increment_count)
    )