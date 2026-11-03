# -*- coding: utf-8 -*-

from common import *
import names


def read_frequency():
    """Read the currently displayed frequency."""

    obj = waitForObjectExists(names.valueDrum_Cylinder_2)
    value = obj.displayedValue

    if callable(value):
        value = value()

    return float(str(value).strip())


def verify_frequency(expected):
    """Verify the displayed frequency against the expected value."""

    try:
        actual = read_frequency()

        if actual == float(expected):
            test.passes(
                "PASS: Frequency verified. Expected: {} Hz | Actual: {} Hz"
                .format(expected, actual)
            )
            return True

        test.fail(
            "FAIL: Frequency mismatch. Expected: {} Hz | Actual: {} Hz"
            .format(expected, actual)
        )
        return False

    except Exception as error:
        test.fail(
            "ERROR: Unable to verify {} Hz. Details: {}"
            .format(expected, error)
        )
        return False


def check_increment_button(current_frequency):
    """Check whether the increment button exists, is visible, and is enabled."""

    try:
        increment_button = waitForObjectExists(
            names.frequencyWidget_incrementButton_QPushButton,
            1000
        )

        if not increment_button.visible:
            test.fail(
                "ERROR: Frequency increment button disappeared at {} Hz. "
                "Expected to continue up to 400 Hz."
                .format(current_frequency)
            )
            return False

        if not increment_button.enabled:
            test.fail(
                "ERROR: Frequency increment button is disabled at {} Hz. "
                "Expected to continue up to 400 Hz."
                .format(current_frequency)
            )
            return False

        return True

    except Exception:
        test.fail(
            "ERROR: Frequency increment button disappeared at {} Hz. "
            "Expected to continue up to 400 Hz."
            .format(current_frequency)
        )
        return False


def main():

    """Step 1: Login and navigate to Home screen"""

    enter_login_pin()
    dismiss_fiber_verification_warning()
    snooze(1)

    try:
        waitForObjectExists(names.homeScreen_HomeScreen)
        test.passes("Home screen is displayed.")

    except Exception as error:
        test.fail(
            "Home screen verification failed: {}".format(error)
        )
        return

    """Step 2: Select Manual/Expert mode"""

    try:
        clickButton(
            waitForObject(names.gbExpert_expertButton_QPushButton)
        )
        snooze(1)

        mouseClick(
            waitForObject(names.modeButton_nameLabel_QLabel),
            46, 14, Qt.NoModifier, Qt.LeftButton
        )

        clickButton(
            waitForObject(names.centralWidget_MRP_QPushButton)
        )

        clickButton(
            waitForObject(names.centralWidget_DisableButton_QPushButton)
        )

        test.passes("Manual/Expert navigation button selected.")

    except Exception as error:
        test.fail(
            "Could not select the Manual button: {}".format(error)
        )
        return

    """Step 3: Configure Standard Pulse Mode"""

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

    except Exception as error:
        test.fail(
            "Could not configure Standard Pulse Mode: {}"
            .format(error)
        )
        return

    """Step 4: Define expected frequency values"""

    expected_values = (
        list(range(1, 21)) +
        list(range(22, 41, 2)) +
        list(range(45, 101, 5)) +
        list(range(120, 401, 20))
    )

    test.log(
        "Total frequency values to verify: {}"
        .format(len(expected_values))
    )

    test.log("Frequency ranges to verify:")
    test.log("1-20 Hz in 1 Hz increments.")
    test.log("20-40 Hz in 2 Hz increments.")
    test.log("40-100 Hz in 5 Hz increments.")
    test.log("100-400 Hz in 20 Hz increments.")

    """Step 5: Reset frequency to 1 Hz"""

    try:
        current_frequency = read_frequency()

    except Exception as error:
        test.fail(
            "Unable to read initial frequency: {}".format(error)
        )
        return

    reset_count = 0

    while current_frequency > 1 and reset_count < 500:

        try:
            decrement_button = waitForObject(
                names.frequencyWidget_decrementButton_QPushButton
            )

            if not decrement_button.enabled:
                test.fail(
                    "ERROR: Decrement button is disabled at {} Hz "
                    "while resetting frequency to 1 Hz."
                    .format(current_frequency)
                )
                return

            clickButton(decrement_button)
            snooze(1)

            new_frequency = read_frequency()
            reset_count += 1

        except Exception as error:
            test.fail(
                "Unable to reset frequency to 1 Hz. "
                "Current frequency: {} Hz. Details: {}"
                .format(current_frequency, error)
            )
            return

        if new_frequency >= current_frequency:
            test.fail(
                "ERROR: Frequency did not decrease. "
                "Previous: {} Hz | Current: {} Hz"
                .format(current_frequency, new_frequency)
            )
            return

        current_frequency = new_frequency

    if current_frequency != 1:
        test.fail(
            "ERROR: Could not reset frequency to 1 Hz. "
            "Actual frequency: {} Hz"
            .format(current_frequency)
        )
        return

    test.passes("Frequency reset to 1 Hz.")

    if not verify_frequency(1):
        return

    """Step 6: Verify all frequency values and ranges"""

    for index in range(1, len(expected_values)):

        expected = expected_values[index]
        previous_expected = expected_values[index - 1]

        test.log(
            "Checking frequency transition: {} Hz -> {} Hz"
            .format(previous_expected, expected)
        )

        # Check increment button before clicking.

        if not check_increment_button(previous_expected):
            return

        try:
            increment_button = waitForObjectExists(
                names.frequencyWidget_incrementButton_QPushButton,
                1000
            )

            clickButton(increment_button)
            snooze(1)

        except Exception as error:

            if previous_expected >= 300:
                test.fail(
                    "ERROR: Frequency increment button disappeared "
                    "at {} Hz. Expected to continue up to 400 Hz. "
                    "Details: {}"
                    .format(previous_expected, error)
                )
            else:
                test.fail(
                    "ERROR: Unable to increment frequency from "
                    "{} Hz to {} Hz. Details: {}"
                    .format(previous_expected, expected, error)
                )

            return

        """Verify the actual frequency after incrementing"""

        if not verify_frequency(expected):
            test.fail(
                "ERROR: Frequency test stopped while checking {} Hz."
                .format(expected)
            )
            return

        """Report PASS only after completing each frequency range"""

        if expected == 20:
            test.passes(
                "PASS: Frequency range 1-20 Hz verified "
                "in 1 Hz increments."
            )

        elif expected == 40:
            test.passes(
                "PASS: Frequency range 20-40 Hz verified "
                "in 2 Hz increments."
            )

        elif expected == 100:
            test.passes(
                "PASS: Frequency range 40-100 Hz verified "
                "in 5 Hz increments."
            )

        """Specifically check increment availability at 300 Hz"""

        if expected == 300:

            test.log(
                "Frequency reached 300 Hz. Checking increment button "
                "availability before continuing toward 400 Hz."
            )

            if not check_increment_button(300):
                return

            test.passes(
                "PASS: Frequency reached 300 Hz and the increment "
                "button is available to continue toward 400 Hz."
            )

        

        elif expected == 400:
            test.passes(
                "PASS: Frequency range 100-400 Hz verified "
                "in 20 Hz increments."
            )

    """Step 7: Final result"""

    test.passes(
        "SUCCESS: All {} expected frequency values verified "
        "successfully up to 400 Hz."
        .format(len(expected_values))
    )