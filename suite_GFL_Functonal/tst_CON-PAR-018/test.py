import os
import re
import names
import test
import common

def verify_frequency_average_power():

    test.log("Verifying Average Power Frequency Increments")

    average_power_object = (
        names.valueLabelBackgroundWithQuantityText_valueLabel_QLabel
    )

    frequency_increment_button = (
        names.frequencyWidget_incrementButton_QPushButton
    )

    expected_values = [
        10, 15, 20,
        30, 40, 50, 60, 70
    ]

    initial_text = str(
        waitForObject(
            average_power_object
        ).text
    ).strip()

    match = re.search(
        r"[-+]?\d*\.?\d+",
        initial_text
    )

    if not match:

        test.fail(
            "Unable to read initial Average Power: {}".format(
                initial_text
            )
        )

        return False

    initial_power = float(match.group())

    test.log(
        "Initial Average Power: {} W".format(
            initial_power
        )
    )

    if initial_power != 5:

        test.fail(
            "Expected initial Average Power: 5 W | Actual: {} W".format(
                initial_power
            )
        )

        return False

    test.passes(
        "Initial Average Power is 5 W"
    )

    for expected_power in expected_values:

        clickButton(
            waitForObject(
                frequency_increment_button
            )
        )

        snooze(1)

        actual_text = str(
            waitForObject(
                average_power_object
            ).text
        ).strip()

        test.log(
            "Displayed Average Power: {}".format(
                actual_text
            )
        )

        match = re.search(
            r"[-+]?\d*\.?\d+",
            actual_text
        )

        if not match:

            test.fail(
                "Unable to read Average Power: {}".format(
                    actual_text
                )
            )

            return False

        actual_power = float(match.group())
        
        if actual_power == expected_power:

            test.passes(
                "Expected: {} W | Actual: {} W".format(
                    expected_power,
                    actual_power
                )
            )

        else:

            test.fail(
                "Expected: {} W | Actual: {} W".format(
                    expected_power,
                    actual_power
                )
            )

            return False

    test.passes(
        "All Average Power frequency values verified successfully"
    )

    return True


def main():
    test.log("Starting Economy B and Frequency Test")
    common.enter_login_pin()
    common.dismiss_fiber_verification_warning()
    common.verify_economyB_type()
    mouseClick(waitForObject(names.staticVersions_3_systemTypeVersion_QLabel), 57, 17, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.buttonsBar_backButton_QPushButton))
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    common.navigate_to_expert_screen()
    common.left_fragmentation_pulse()
    verify_frequency_average_power
    
