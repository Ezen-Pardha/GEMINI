
# -*- coding: utf-8 -*-

import names
from common import *


def main():
    runtime_path = os.path.expanduser(
        "/home/ezen/Gemini_v1"
    )
    configure_system_type(
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

    clickButton(waitForObject(names.buttonsBar_backButton_QPushButton))
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.gbExpert_expertButton_QPushButton))

    mouseClick(
        waitForObject(names.modeButton_nameLabel_QLabel),
        79, 40, Qt.NoModifier, Qt.LeftButton
    )

    clickButton(waitForObject(names.centralWidget_CW_QPushButton))
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))

    power_object = names.valueDrum_Cylinder_3
    increment_button = names.powerWidgetCW_incrementButton_QPushButton

    target_power = 70
    max_clicks = 100
    click_count = 0

    """Verify initial Power"""
    current_power = float(
        str(waitForObjectExists(power_object).displayedValue).strip()
    )

    test.compare(
        current_power,
        10.0,
        "Initial CW Power is verified as 10 W"
    )

    """Increment Power until it reaches 70 W"""
    while current_power < target_power and click_count < max_clicks:

        clickButton(waitForObject(increment_button))
        snooze(1)

        current_power = float(
            str(waitForObjectExists(power_object).displayedValue).strip()
        )

        click_count += 1

        test.log(
            "CW Power after increment: {} W".format(current_power)
        )

        print(
            "CW Power after increment: {} W".format(current_power)
        )

        test.verify(
            current_power <= target_power,
            "CW Power is within 70 W limit. Actual: {} W".format(
                current_power
            )
        )

        if current_power > target_power:
            break

    """Verify final Power"""
    if current_power == target_power:

        test.passes(
            "CW Mode Power successfully reached the maximum value of 70 W."
        )

    else:

        test.fail(
            "CW Mode Power did not reach 70 W. Actual value: {} W".format(
                current_power
            )
        )
    runtime_path = os.path.expanduser(
        "/home/ezen/Gemini_v1"
    )
    configure_system_type(
        new_type="B",
        runtime_path=runtime_path
    )
