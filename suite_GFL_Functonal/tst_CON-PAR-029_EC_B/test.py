
# -*- coding: utf-8 -*-

import os
import re
import names
import test
import common


def increment_frequency():

    test.log("Incrementing Frequency and Reading Display Values")

    average_power_object = (
        names.valueLabelBackgroundWithQuantityText_valueLabel_QLabel
    )

    frequency_increment_button = (
        names.frequencyWidget_incrementButton_QPushButton
    )

    expected_values = [10, 20, 30, 40, 60]

    power_label = waitForObject(
        average_power_object
    )

    initial_text = str(
        power_label.text
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

    if initial_power in expected_values:

        current_index = expected_values.index(
            initial_power
        )

        test.passes(
            "Initial Average Power verified: {} W".format(
                initial_power
            )
        )

    else:

        test.fail(
            "Unexpected initial Average Power: {} W".format(
                initial_power
            )
        )

        return False

    for expected_power in expected_values[current_index + 1:]:

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

        actual_power = float(
            match.group()
        )

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
        "All remaining Average Power values verified successfully"
    )

    return True


def main():

    test.log("Starting Economy B and Frequency Test")

    runtime_path = os.path.expanduser(
        "~/Downloads/WORK/Gemini_GFL_2.5_Codebase_8May2026/"
        "build-gemini-Desktop-Debug"
    )

    common.configure_system_type(
        new_type="B",
        runtime_path=runtime_path
    )
    common.enter_login_pin()
    
    common.dismiss_fiber_verification_warning()
    
    common.verify_economyB_type()
    mouseClick(
        waitForObject(
            names.staticVersions_3_systemTypeVersion_QLabel
        ),
        57,
        17,
        Qt.NoModifier,
        Qt.LeftButton
    )
    
    clickButton(
        waitForObject(
            names.buttonsBar_backButton_QPushButton
        )
    )
    
    clickButton(
        waitForObject(
            names.buttonsBar_homeButton_QPushButton
        )
    )
    common.navigate_to_expert_screen()
    
    common.left_navigate_to_enucleation_disable()
    increment_frequency()
    
    test.log("Economy B and Frequency Test Completed")
