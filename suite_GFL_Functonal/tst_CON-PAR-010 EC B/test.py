
# -*- coding: utf-8 -*-

import names
from common import *

def main():

    enter_login_pin()
    dismiss_fiber_verification_warning()
    snooze(2)

    verify_economy_type()
    
   
    clickButton(waitForObject(names.buttonsBar_backButton_QPushButton))
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.gbExpert_expertButton_QPushButton))

    mouseClick(
        waitForObject(names.modeButton_nameLabel_QLabel, 49734),
        60, 38, Qt.NoModifier, Qt.LeftButton
    )

    clickButton(waitForObject(names.centralWidget_MRP_QPushButton))
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))

    frequency_object = names.valueLabelBackgroundWithQuantityText_valueLabel_QLabel
    average_power_object = names.valueLabelBackgroundWithQuantityText_valueLabel_QLabel
    increment_button = names.frequencyWidget_incrementButton_QPushButton

    target_power = 60
    max_clicks = 100
    click_count = 0

    average_power = float(
        str(waitForObjectExists(average_power_object).text).strip()
    )

    test.compare(
        average_power,
        2.0,
        "Initial Average Power is verified as 2 W"
    )

    while average_power < target_power and click_count < max_clicks:

        clickButton(waitForObject(increment_button))
        snooze(1)

        frequency = str(
            waitForObjectExists(frequency_object).text
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

        test.verify(
            average_power <= target_power,
            "Average Power is within the maximum limit of 60 W. Actual: {} W".format(
                average_power
            )
        )

    if average_power == target_power:

        test.passes(
            "Average Power successfully reached the maximum value of 60 W in MRP pulse mode."
        )

    else:

        test.fail(
            "Average Power did not reach 60 W. Final value: {} W".format(
                average_power
            )
        )
    