
# -*- coding: utf-8 -*-

import names
from common import *


def main():

    enter_login_pin()
    dismiss_fiber_verification_warning()

    verify_economyc_type()

    """Navigate to manual screen"""
    clickButton(waitForObject(names.buttonsBar_backButton_QPushButton))
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.gbExpert_expertButton_QPushButton))

    mouseClick(
        waitForObject(names.modeButton_nameLabel_QLabel),
        52, 21, Qt.NoModifier, Qt.LeftButton
    )

    """Select MRP pulse mode"""
    clickButton(waitForObject(names.centralWidget_MRP_QPushButton))
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))

    snooze(2)

    """Verify initial Average Power"""
    average_power_object = names.valueLabelBackgroundWithQuantityText_valueLabel_QLabel

    initial_average_power = float(
        str(waitForObjectExists(average_power_object).text).strip()
    )

    test.compare(
        initial_average_power,
        2.0,
        "Initial Average Power is verified as 2 W"
    )

    """Increment Pulse Energy 8 times"""
    for _ in range(8):

        clickButton(
            waitForObject(names.pulseEnergyWidget_incrementButton_QPushButton)
        )

        snooze(1)

    """Verify Pulse Energy"""
    pulse_energy = str(
        waitForObjectExists(names.valueDrum_Cylinder).displayedValue
    ).strip()

    test.compare(
        pulse_energy,
        "1",
        "Pulse Energy is verified as 1"
    )

    """Increment Frequency until Average Power reaches 70 W"""
    target_average_power = 70.0
    max_clicks = 100
    click_count = 0

    while click_count < max_clicks:

        clickButton(
            waitForObject(names.frequencyWidget_incrementButton_QPushButton)
        )

        snooze(1)

        frequency = str(
            waitForObjectExists(names.valueDrum_Cylinder_2).displayedValue
        ).strip()

        average_power = float(
            str(waitForObjectExists(average_power_object).text).strip()
        )

        click_count += 1

        test.log(
            "Frequency: {} | Average Power: {} W".format(
                frequency, average_power
            )
        )

        print(
            "Frequency: {} | Average Power: {} W".format(
                frequency, average_power
            )
        )

        """Verify Average Power does not exceed 70 W"""
        test.verify(
            average_power <= target_average_power,
            "Average Power is within 70 W limit. Actual: {} W".format(
                average_power
            )
        )

        """Stop when Average Power reaches 70 W"""
        if average_power == target_average_power:

            test.passes(
                "Average Power successfully reached 70 W in MRP pulse mode."
            )

            break

        elif average_power > target_average_power:

            test.fail(
                "Average Power exceeded 70 W. Actual value: {} W".format(
                    average_power
                )
            )

            break

    else:

        test.fail(
            "Average Power did not reach 70 W within {} Frequency increments.".format(
                max_clicks
            )
        )
