# -*- coding: utf-8 -*-

import names
from common import *

EXPECTED_PULSE_ENERGY_VALUES = [2.5, 3, 4, 10, 20, 30, 40, 50]


def read_pulse_energy():

    
    
    value = waitForObjectExists(
        names.valueDrum_Cylinder, 3000
    ).displayedValue

    if callable(value):
        value = value()

    return float(str(value).strip())


def verify_pulse_energy(expected_value):
    try:
        actual_value = read_pulse_energy()

        if abs(actual_value - expected_value) < 0.001:
            test.passes(
                "PASS: Pulse energy verified. Expected: {} J | Actual: {} J".format(
                    expected_value, actual_value
                )
            )
            return True

        test.fail(
            "FAIL: Pulse energy mismatch. Expected: {} J | Actual: {} J".format(
                expected_value, actual_value
            )
        )
        return False

    except Exception as error:
        test.fail(
            "ERROR: Unable to read pulse energy. Expected: {} J | Details: {}".format(
                expected_value, error
            )
        )
        return False


def main():

    """Step 1: Login"""
    enter_login_pin()
    dismiss_fiber_verification_warning()
    """Step 2: Navigate to Expert mode"""
    clickButton(
        waitForObject(names.gbExpert_expertButton_QPushButton)
    )

    """Step 3: Open treatment mode selection"""
    mouseClick(
        waitForObject(names.modeButton_nameLabel_QLabel),
        99, 28,
        Qt.NoModifier,
        Qt.LeftButton
    )

    """Step 4: Select Fragmentation mode"""
    clickButton(
        waitForObject(names.centralWidget_Fragmentation_QPushButton)
    )

    """Step 5: Disable treatment if required"""
    clickButton(
        waitForObject(names.centralWidget_DisableButton_QPushButton)
    )

    snooze(1)

    """Step 6: Verify the initial pulse energy is 2 J"""
    if not verify_pulse_energy(2):
        return

    """Step 7: Increment and verify each remaining setting"""
    for expected_value in EXPECTED_PULSE_ENERGY_VALUES[1:]:

        try:
            increment_button = waitForObjectExists(
                names.pulseEnergyWidget_incrementButton_QPushButton,
                3000
            )

            if not increment_button.enabled:
                test.fail(
                    "ERROR: Pulse energy increment button is disabled. "
                    "Unable to reach {} J.".format(expected_value)
                )
                return

            clickButton(increment_button)
            snooze(0.5)

            if not verify_pulse_energy(expected_value):
                return

        except Exception as error:
            test.fail(
                "ERROR: Unable to increment or verify pulse energy at {} J. "
                "Details: {}".format(expected_value, error)
            )
            return

    test.passes(
        "PASS: Fragmentation Mode pulse energy verification completed "
        "successfully for 2 J, 3 J, 4 J, 10 J, 20 J, 30 J, 40 J, and 50 J."
    )
