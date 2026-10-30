# -*- coding: utf-8 -*-

from common import *
import names


def read_frequency():
    """Read the actual frequency displayed on the screen."""
    obj = waitForObjectExists(names.valueDrum_Cylinder_2)
    return float(str(obj.displayedValue).strip())


def verify_frequency(expected):
    """Compare expected frequency with actual displayed frequency."""
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
    # STEP 1: Login and verify Home screen
    # --------------------------------------------------
    enter_login_pin()
    snooze(1)

    clickButton(
        waitForObject(names.mainFrame_okButton_QPushButton)
    )
    snooze(1)

    try:
        waitForObjectExists(names.homeScreen_HomeScreen)
        test.passes("PASS | Home screen is displayed.")
    except Exception as error:
        test.fail(
            "FAIL | Home screen verification failed: {}".format(error)
        )
        return

    # --------------------------------------------------
    # STEP 2: Navigate to Manual/Expert screen
    # --------------------------------------------------
    mouseClick(
        waitForObject(names.homeScreen_HomeScreen),
        639, 118,
        Qt.NoModifier,
        Qt.LeftButton
    )
    snooze(1)

    try:
        clickButton(
            waitForObject(names.gbExpert_expertButton_QPushButton)
        )
        snooze(1)
        test.passes(
            "PASS | Manual/Expert navigation action completed."
        )
    except Exception as error:
        test.fail(
            "FAIL | Could not navigate to Manual/Expert screen: {}".format(
                error
            )
        )
        return

    # --------------------------------------------------
    # STEP 3: Configure Standard Pulse Mode
    # --------------------------------------------------
    try:
        mouseDrag(
            waitForObject(
                names.indexPicker_valuePicker_IntervalSlider_2
            ),
            59, 27, -156, -9,
            1,
            Qt.LeftButton
        )
        snooze(1)

        mouseDrag(
            waitForObject(
                names.indexPicker_valuePicker_IntervalSlider_2
            ),
            48, 26, -45, -3,
            1,
            Qt.LeftButton
        )
        snooze(1)

        test.log(
            "Configuration selection actions completed."
        )

        # If Standard Pulse Mode has a separate selection
        # button and OK button, insert your recorded actions
        # here using their actual Object Spy names.

    except Exception as error:
        test.fail(
            "FAIL | Standard Pulse Mode configuration failed: {}".format(
                error
            )
        )
        return

    # --------------------------------------------------
    # STEP 4: Define expected frequency values
    # --------------------------------------------------
    expected_values = (
        list(range(1, 21)) +
        list(range(22, 41, 2)) +
        list(range(45, 101, 5)) +
        list(range(120, 401, 20)) +
        list(range(500, 2401, 100))
    )

    test.log(
        "Total expected frequency values: {}".format(
            len(expected_values)
        )
    )

    test.log(
        "Frequency tiers: 1-20 Hz (1 Hz increments); "
        "20-40 Hz (2 Hz increments); "
        "40-100 Hz (5 Hz increments); "
        "100-400 Hz (20 Hz increments); "
        "above 400 Hz (100 Hz increments)."
    )

    # --------------------------------------------------
    # STEP 5: Read current frequency
    # --------------------------------------------------
    try:
        current_frequency = read_frequency()
        test.log(
            "Initial displayed frequency: {} Hz".format(
                current_frequency
            )
        )
    except Exception as error:
        test.fail(
            "FAIL | Cannot read initial frequency: {}".format(error)
        )
        return

    # --------------------------------------------------
    # STEP 6: Reset frequency to 1 Hz
    # --------------------------------------------------
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
            test.fail(
                "FAIL | Cannot read frequency during reset: {}".format(
                    error
                )
            )
            return

        if new_frequency >= current_frequency:
            test.fail(
                "FAIL | Frequency did not decrease. "
                "Previous: {} Hz | Current: {} Hz".format(
                    current_frequency, new_frequency
                )
            )
            return

        current_frequency = new_frequency

    if current_frequency != 1:
        test.fail(
            "FAIL | Could not reset frequency to 1 Hz. "
            "Actual: {} Hz".format(current_frequency)
        )
        return

    test.passes("PASS | Frequency reset successfully to 1 Hz.")

    if not verify_frequency(1):
        return

    # --------------------------------------------------
    # STEP 7: Verify frequency values and log tier changes
    # --------------------------------------------------
    for index in range(1, len(expected_values)):

        previous_expected = expected_values[index - 1]
        expected = expected_values[index]

        # Log the beginning of each new tier.
        if expected == 2:
            test.log(
                "FREQUENCY TIER STARTED: "
                "1-20 Hz with 1 Hz increments."
            )

        elif expected == 22:
            test.log(
                "FREQUENCY TIER CHANGE: "
                "20-40 Hz with 2 Hz increments."
            )

        elif expected == 45:
            test.log(
                "FREQUENCY TIER CHANGE: "
                "40-100 Hz with 5 Hz increments."
            )

        elif expected == 120:
            test.log(
                "FREQUENCY TIER CHANGE: "
                "100-400 Hz with 20 Hz increments."
            )

        elif expected == 500:
            test.log(
                "FREQUENCY TIER CHANGE: "
                "Above 400 Hz with 100 Hz increments."
            )

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

            actual = read_frequency()

            test.log(
                "Frequency result | Expected: {} Hz | Actual: {} Hz".format(
                    expected, actual
                )
            )

            if not verify_frequency(expected):
                test.fail(
                    "FAIL | Frequency verification stopped. "
                    "Previous expected: {} Hz | Next expected: {} Hz".format(
                        previous_expected, expected
                    )
                )
                return

        except Exception as error:
            test.fail(
                "FAIL | Error while checking {} Hz: {}".format(
                    expected, error
                )
            )
            return

    # --------------------------------------------------
    # STEP 8: Final result
    # --------------------------------------------------
    test.passes(
        "SUCCESS | All {} expected frequency values verified "
        "up to 2400 Hz.".format(len(expected_values))
    )
