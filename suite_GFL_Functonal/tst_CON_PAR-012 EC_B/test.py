
# -*- coding: utf-8 -*-

import names
from common import *


def main():

    enter_login_pin()
    dismiss_fiber_verification_warning()
    verify_economy_type()

    clickButton(waitForObject(names.buttonsBar_backButton_QPushButton))
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
        
    clickButton(
        waitForObject(names.gbExpert_expertButton_QPushButton)
    )

    mouseClick(
        waitForObject(names.modeButton_nameLabel_QLabel),
        43, 43, Qt.NoModifier, Qt.LeftButton
    )

    clickButton(waitForObject(names.centralWidget_CW_QPushButton))
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))

    power_object = names.valueDrum_Cylinder_3

    """Verify initial Power"""
    initial_power = str(
        waitForObjectExists(power_object).displayedValue
    ).strip()

    test.compare(
        initial_power,
        "10",
        "Initial CW Power is verified as 10 W"
    )

    """Increment Power until it reaches 60 W"""
    target_power = 60
    max_clicks = 100
    click_count = 0

    while click_count < max_clicks:

        current_power = float(
            str(waitForObjectExists(power_object).displayedValue).strip()
        )

        if current_power == target_power:
            break

        clickButton(
            waitForObject(names.powerWidgetCW_incrementButton_QPushButton)
        )

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
            "CW Power is within 60 W maximum limit. Actual: {} W".format(
                current_power
            )
        )

        if current_power > target_power:
            break

    """Final verification"""
    final_power = str(
        waitForObjectExists(power_object).displayedValue
    ).strip()

    if float(final_power) == target_power:

        test.passes(
            "CW Power successfully reached the maximum value of 60 W."
        )

    else:

        test.fail(
            "CW Power did not reach 60 W. Actual value: {} W".format(
                final_power
            )
        )
