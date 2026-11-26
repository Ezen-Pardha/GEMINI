import names
from common import*
import test
import re
import re

def increment_frequency():

    average_power_object = (
        names.valueLabelBackgroundWithQuantityText_valueLabel_QLabel
    )

    frequency_increment_button = (
        names.frequencyWidget_incrementButton_QPushButton
    )

    target_average_power = 60.0
    max_clicks = 100
    click_count = 0

    while click_count < max_clicks:

        power_text = str(
            waitForObjectExists(average_power_object).text
        ).strip()

        average_power = float(
            re.search(r"[-+]?\d*\.?\d+", power_text).group()
        )

        if average_power >= target_average_power:

            if average_power == target_average_power:
                test.passes(
                    "Average Power successfully reached 60 W."
                )
            else:
                test.fail(
                    "Average Power exceeded 60 W. Actual: {} W".format(
                        average_power
                    )
                )

            break

        clickButton(
            waitForObject(frequency_increment_button)
        )

        snooze(1)

        click_count += 1

        test.log(
            "Frequency increment: {} | Previous Average Power: {} W".format(
                click_count,
                average_power
            )
        )

    else:

        test.fail(
            "Average Power did not reach 60 W within {} increments.".format(
                max_clicks
            )
        )
def main():

    enter_login_pin()
    dismiss_fiber_verification_warning()
    navigate_to_expert_screen()
    left_Minimal_Carbonization()
    increment_frequency()
