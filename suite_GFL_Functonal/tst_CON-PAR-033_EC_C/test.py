import names
from common import*
import test
import re
import re


import re
import test


def increment_frequency():

    test.log("Checking Average Power")

    average_power_object = (
        names.valueLabelBackgroundWithQuantityText_valueLabel_QLabel
    )

    frequency_increment_button = (
        names.frequencyWidget_incrementButton_QPushButton
    )

    target_average_power = 70.0
    max_clicks = 100
    click_count = 0

    while click_count < max_clicks:

        power_text = str(
            waitForObjectExists(
                average_power_object
            ).text
        ).strip()

        test.log(
            "Current Average Power: {}".format(power_text)
        )

        match = re.search(
            r"[-+]?\d*\.?\d+",
            power_text
        )

        if not match:
            test.fail(
                "Unable to extract Average Power from: {}".format(
                    power_text
                )
            )
            return False

        average_power = float(match.group())

        if average_power >= target_average_power:

            if average_power == target_average_power:

                test.passes(
                    "Average Power successfully reached 70 W."
                )

                return True

            else:

                test.fail(
                    "Average Power exceeded 70 W. Actual: {} W".format(
                        average_power
                    )
                )

                return False

        clickButton(
            waitForObject(
                frequency_increment_button
            )
        )

        snooze(1)

        click_count += 1

        test.log(
            "Frequency increment: {} | "
            "Previous Average Power: {} W".format(
                click_count,
                average_power
            )
        )

    test.fail(
        "Average Power did not reach 60 W within {} increments.".format(
            max_clicks
        )
    )

    return False


import os
import common
from common import *


def main():

    runtime_path = os.path.expanduser(
        "/home/ezen/Gemini_v1"
    )

    common.configure_system_type(
        new_type="C",
        runtime_path=runtime_path
    )
    
    try: 
        context = currentApplicationContext()
        context.detach()
        snooze(3)
        test.log("AUT context detached")
    except Exception as error:
        test.log("Error while closing AUT: " + str(error))

    startApplication(
        "bravo --disable-watchdog --watchdog-timeout=10 "
        "--disable-integrity-check "
        "--disable-fiber-use-check "
        "--disable-firmware-check "
        "--disable-ssm "
        "--disable-ports-check"
    )
    snooze(5)
    
    test.passes("Bravo AUT restart command executed successfully")
    
    enter_login_pin()
    dismiss_fiber_verification_warning()
    verify_economyc_type()
    mouseClick(waitForObject(names.staticVersions_3_systemTypeVersion_QLabel), 57, 17, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.buttonsBar_backButton_QPushButton))
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    navigate_to_expert_screen()
    left_Minimal_Carbonization()
    increment_frequency()
    runtime_path = os.path.expanduser(
        "/home/ezen/Gemini_v1"
    )
    common.configure_system_type(
        new_type="B",
        runtime_path=runtime_path
    )
