# -*- coding: utf-8 -*-

from common import *
import names


def read_frequency():
    obj = waitForObjectExists(names.valueDrum_Cylinder_2)
    return float(str(obj.displayedValue).strip())


def verify_frequency(expected):
    """Compare the actual displayed frequency with the expected value."""
    try:
        actual = read_frequency()

        if actual == float(expected):
            test.passes(
                "PASS | Expected: {} Hz | Actual: {} Hz".format(
                    expected, actual
                )
            )
            return True

        test.fail(
            "FAIL | Expected: {} Hz | Actual: {} Hz".format(
                expected, actual
            )
        )
        return False

    except Exception as error:
        test.fail(
            "Unable to verify {} Hz. Error: {}".format(
                expected, error
            )
        )
        return False


def main():

    # --------------------------------------------------
    # STEP 1: Login and navigate to Home screen
    # --------------------------------------------------
    enter_login_pin()
    snooze(1)

    clickButton(waitForObject(names.mainFrame_okButton_QPushButton))
    snooze(1)

    try:
        waitForObjectExists(names.homeScreen_HomeScreen)
        test.passes("Home screen is displayed.")
    except Exception as error:
        test.fail("Home screen verification failed: {}".format(error))
        return

    # --------------------------------------------------
    # STEP 2: Select Manual button
    # --------------------------------------------------
    # Replace this object name only if your Object Spy
    # identifies a different Manual button.
    try:
        clickButton(waitForObject(names.gbExpert_expertButton_QPushButton))
        snooze(1)
        test.passes("Manual/Expert navigation button selected.")
    except Exception as error:
        test.fail("Could not select the Manual button: {}".format(error))
        return

    # --------------------------------------------------
    # STEP 3: Select Standard Pulse Mode and press OK
    # --------------------------------------------------
    # Keep the recorded configuration-selection actions.
    try:
        mouseDrag(
            waitForObject(names.indexPicker_valuePicker_IntervalSlider_2),
            59, 27, -156, -9,
            1,
            Qt.LeftButton
        )
        snooze(1)

        mouseDrag(
            waitForObject(names.indexPicker_valuePicker_IntervalSlider_2),
            48, 26, -45, -3,
            1,
            Qt.LeftButton
        )
        snooze(1)

        # If Standard Pulse Mode requires a separate button
        # and OK button, add the recorded actions here.
    except Exception as error:
        test.fail("Could not configure Standard Pulse Mode: {}".format(error))
        return

    # --------------------------------------------------
    # STEP 4: Expected frequency values
    # --------------------------------------------------
    expected_values = (
        list(range(1, 21)) +
        list(range(22, 41, 2)) +
        list(range(45, 101, 5)) +
        list(range(120, 401, 20)) +
        list(range(500, 2401, 100))
    )

    test.log(
        "Total frequency values to verify: {}".format(
            len(expected_values)
        )
    )

    # --------------------------------------------------
    # STEP 5: Reset frequency to 1 Hz
    # --------------------------------------------------
    try:
        current_frequency = read_frequency()
    except Exception as error:
        test.fail("Unable to read initial frequency: {}".format(error))
        return

    reset_count = 0

    while current_frequency > 1 and reset_count < 2500:
        clickButton(
            waitForObject(
                names.frequencyWidget_decrementButton_QPushButton
            )
        )
        snooze(1)
        reset_count += 1

        try:
            new_frequency = read_frequency()
        except Exception as error:
            test.fail("Unable to read frequency during reset: {}".format(error))
            return

        if new_frequency >= current_frequency:
            test.fail(
                "Frequency did not decrease. Previous: {} Hz, Current: {} Hz"
                .format(current_frequency, new_frequency)
            )
            return

        current_frequency = new_frequency

    if current_frequency != 1:
        test.fail(
            "Could not reset frequency to 1 Hz. Actual: {} Hz".format(
                current_frequency
            )
        )
        return

    test.passes("Frequency reset to 1 Hz.")

    if not verify_frequency(1):
        return

    # --------------------------------------------------
    # STEP 6: Verify every frequency value
    # --------------------------------------------------
    for index in range(1, len(expected_values)):
        expected = expected_values[index]
        previous_expected = expected_values[index - 1]

        test.log(
            "Checking frequency transition: {} Hz -> {} Hz".format(
                previous_expected, expected
            )
        )

        try:
            clickButton(
                waitForObject(
                    names.frequencyWidget_incrementButton_QPushButton
                )
            )
            snooze(1)

            if not verify_frequency(expected):
                test.fail(
                    "Frequency test stopped at {} Hz.".format(expected)
                )
                return

        except Exception as error:
            test.fail(
                "Error while checking {} Hz: {}".format(expected, error)
            )
            return

    # --------------------------------------------------
    # STEP 7: Final result
    # --------------------------------------------------
    test.passes(
        "SUCCESS: All {} frequency values verified up to 2400 Hz."
        .format(len(expected_values))
    )

    