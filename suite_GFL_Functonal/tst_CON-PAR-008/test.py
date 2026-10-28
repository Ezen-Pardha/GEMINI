# # -*- coding: utf-8 -*-
#
# import names
#
#
# def main():
#     enter_login_pin()
#     clickButton(waitForObject(names.gbExpert_expertButton_QPushButton))
#     mouseClick(waitForObject(names.modeButton_nameLabel_QLabel), 68, 22, Qt.NoModifier, Qt.LeftButton)
#     clickButton(waitForObject(names.centralWidget_MRP_QPushButton))
#     clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
#     mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 93, 37, -85, 4, 1, Qt.LeftButton)
#     test.compare(waitForObjectExists(names.valueDrum_Cylinder_2).contextMenuPolicy, 1)
#     clickButton(waitForObject(names.frequencyWidget_incrementButton_QPushButton))
#     clickButton(waitForObject(names.frequencyWidget_incrementButton_QPushButton))
#     clickButton(waitForObject(names.frequencyWidget_incrementButton_QPushButton))
#     clickButton(waitForObject(names.frequencyWidget_incrementButton_QPushButton))
#     clickButton(waitForObject(names.frequencyWidget_incrementButton_QPushButton))
#     clickButton(waitForObject(names.frequencyWidget_incrementButton_QPushButton))
#     clickButton(waitForObject(names.frequencyWidget_incrementButton_QPushButton))
#     clickButton(waitForObject(names.frequencyWidget_incrementButton_QPushButton))
#     clickButton(waitForObject(names.frequencyWidget_incrementButton_QPushButton))
#     clickButton(waitForObject(names.frequencyWidget_incrementButton_QPushButton))
#     clickButton(waitForObject(names.frequencyWidget_incrementButton_QPushButton))
#     clickButton(waitForObject(names.frequencyWidget_incrementButton_QPushButton))
#     clickButton(waitForObject(names.frequencyWidget_incrementButton_QPushButton))
#     clickButton(waitForObject(names.frequencyWidget_incrementButton_QPushButton))
#     clickButton(waitForObject(names.frequencyWidget_incrementButton_QPushButton))
#     clickButton(waitForObject(names.frequencyWidget_incrementButton_QPushButton))
#     clickButton(waitForObject(names.frequencyWidget_incrementButton_QPushButton))
#     clickButton(waitForObject(names.frequencyWidget_incrementButton_QPushButton))
#     clickButton(waitForObject(names.frequencyWidget_incrementButton_QPushButton))
#     clickButton(waitForObject(names.frequencyWidget_incrementButton_QPushButton))
#     clickButton(waitForObject(names.frequencyWidget_incrementButton_QPushButton))
#     clickButton(waitForObject(names.frequencyWidget_incrementButton_QPushButton))
#     clickButton(waitForObject(names.frequencyWidget_incrementButton_QPushButton))
#     clickButton(waitForObject(names.frequencyWidget_incrementButton_QPushButton))
#     clickButton(waitForObject(names.frequencyWidget_incrementButton_QPushButton))
#     clickButton(waitForObject(names.frequencyWidget_incrementButton_QPushButton))
#     clickButton(waitForObject(names.frequencyWidget_incrementButton_QPushButton))
#     clickButton(waitForObject(names.frequencyWidget_incrementButton_QPushButton))
#     clickButton(waitForObject(names.frequencyWidget_incrementButton_QPushButton))
#     clickButton(waitForObject(names.frequencyWidget_incrementButton_QPushButton))
#     clickButton(waitForObject(names.frequencyWidget_incrementButton_QPushButton))
#     clickButton(waitForObject(names.frequencyWidget_incrementButton_QPushButton))
#     clickButton(waitForObject(names.frequencyWidget_incrementButton_QPushButton))
#     clickButton(waitForObject(names.frequencyWidget_incrementButton_QPushButton))
#     clickButton(waitForObject(names.frequencyWidget_incrementButton_QPushButton))
#     clickButton(waitForObject(names.frequencyWidget_incrementButton_QPushButton))
#     clickButton(waitForObject(names.frequencyWidget_incrementButton_QPushButton))
#     clickButton(waitForObject(names.frequencyWidget_incrementButton_QPushButton))
#     clickButton(waitForObject(names.frequencyWidget_incrementButton_QPushButton))
#     clickButton(waitForObject(names.frequencyWidget_incrementButton_QPushButton))
#     clickButton(waitForObject(names.frequencyWidget_incrementButton_QPushButton))
#     clickButton(waitForObject(names.frequencyWidget_incrementButton_QPushButton))
#     clickButton(waitForObject(names.frequencyWidget_incrementButton_QPushButton))
#     clickButton(waitForObject(names.frequencyWidget_incrementButton_QPushButton))
#     clickButton(waitForObject(names.frequencyWidget_incrementButton_QPushButton))
#     clickButton(waitForObject(names.frequencyWidget_incrementButton_QPushButton))
#     clickButton(waitForObject(names.frequencyWidget_incrementButton_QPushButton))
#     clickButton(waitForObject(names.frequencyWidget_incrementButton_QPushButton))
#     clickButton(waitForObject(names.frequencyWidget_incrementButton_QPushButton))
#     clickButton(waitForObject(names.frequencyWidget_incrementButton_QPushButton))
#     clickButton(waitForObject(names.frequencyWidget_incrementButton_QPushButton))

# -*- coding: utf-8 -*-
    # Decrement frequency until 1 Hz is reached
   # -*- coding: utf-8 -*-

import names
from common import *


def main():

    enter_login_pin()

    clickButton(waitForObject(names.gbExpert_expertButton_QPushButton))

    # Select MRP pulse mode
    mouseClick(
        waitForObject(names.modeButton_nameLabel_QLabel),
        68, 22,
        Qt.NoModifier,
        Qt.LeftButton
    )

    clickButton(waitForObject(names.centralWidget_MRP_QPushButton))
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))

    snooze(2)

    frequency_object = names.valueDrum_Cylinder_2
    increment_button = names.frequencyWidget_incrementButton_QPushButton
    decrement_button = names.frequencyWidget_decrementButton_QPushButton

    # Read the displayed frequency
    def read_frequency():
        value = waitForObjectExists(frequency_object).displayedValue
        return float(str(value).strip())

    # Wait until the displayed frequency changes
    def wait_for_frequency_change(previous_frequency, direction):

        for _ in range(30):
            snooze(0.1)
            current_frequency = read_frequency()

            if direction == "decrease":
                if current_frequency < previous_frequency:
                    return current_frequency

            elif direction == "increase":
                if current_frequency > previous_frequency:
                    return current_frequency

        return read_frequency()

    # Verify the frequency control
    test.compare(
        waitForObjectExists(frequency_object).contextMenuPolicy,
        1,
        "Frequency control is available in MRP pulse mode"
    )

    # Decrement until the minimum frequency of 1 Hz is reached
    actual_frequency = read_frequency()
    decrement_count = 0
    max_decrement_count = 500

    while actual_frequency > 1.0 and decrement_count < max_decrement_count:

        previous_frequency = actual_frequency

        clickButton(waitForObject(decrement_button))

        actual_frequency = wait_for_frequency_change(
            previous_frequency, "decrease"
        )

        if actual_frequency >= previous_frequency:
            test.fail(
                "Frequency did not decrease after clicking decrement. "
                "Previous: " + str(previous_frequency) +
                " Hz, Actual: " + str(actual_frequency) + " Hz"
            )
            return

        decrement_count += 1

        test.log(
            "PASS: Frequency decreased from " +
            str(previous_frequency) + " Hz to " +
            str(actual_frequency) + " Hz"
        )

    # Verify minimum frequency
    actual_frequency = read_frequency()

    if abs(actual_frequency - 1.0) < 0.001:
        test.passes(
            "Minimum MRP pulse frequency verified: 1 Hz"
        )
    else:
        test.fail(
            "Minimum frequency verification failed. "
            "Expected: 1 Hz, Actual: " +
            str(actual_frequency) + " Hz"
        )
        return

    # Increment until the maximum frequency of 400 Hz is reached
    increment_count = 0
    max_increment_count = 500

    while actual_frequency < 400.0 and increment_count < max_increment_count:

        previous_frequency = actual_frequency

        clickButton(waitForObject(increment_button))

        actual_frequency = wait_for_frequency_change(
            previous_frequency, "increase"
        )

        if actual_frequency <= previous_frequency:
            test.fail(
                "Frequency did not increase after clicking increment. "
                "Previous: " + str(previous_frequency) +
                " Hz, Actual: " + str(actual_frequency) + " Hz"
            )
            return

        if actual_frequency > 400.0:
            test.fail(
                "Frequency exceeded the maximum of 400 Hz. "
                "Actual: " + str(actual_frequency) + " Hz"
            )
            return

        increment_count += 1

        test.log(
            "PASS: Frequency increased from " +
            str(previous_frequency) + " Hz to " +
            str(actual_frequency) + " Hz"
        )

    # Verify maximum frequency
    actual_frequency = read_frequency()

    if abs(actual_frequency - 400.0) < 0.001:
        test.passes(
            "Maximum MRP pulse frequency verified: 400 Hz"
        )
        test.passes(
            "MRP pulse frequency range validation completed "
            "successfully from 1 Hz to 400 Hz."
        )
    else:
        test.fail(
            "Maximum frequency verification failed. "
            "Expected: 400 Hz, Actual: " +
            str(actual_frequency) + " Hz"
            )