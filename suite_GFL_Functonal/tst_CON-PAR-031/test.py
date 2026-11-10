
# -*- coding: utf-8 -*-

from common import *
import common
import names
import test


def verify_frequency_range():
    expected_minimum = 1.7
    expected_maximum = 20.0
    
    displayed_minimum = 2.5
    displayed_maximum = 15.0

    test.log("START: Frequency range verification")

    test.log(
        "Expected Frequency range: {} Hz to {} Hz".format(
            expected_minimum, expected_maximum
        )
    )

    test.log(
        "Observed Frequency range: {} Hz to {} Hz".format(
            displayed_minimum, displayed_maximum
        )
    )

    if (
        displayed_minimum != expected_minimum
        or displayed_maximum != expected_maximum
    ):
        test.fail(
            "Frequency range mismatch. "
            "Expected: {} Hz to {} Hz; "
            "Observed: {} Hz to {} Hz".format(
                expected_minimum,
                expected_maximum,
                displayed_minimum,
                displayed_maximum
            )
        )
        return

    test.passes(
        "Frequency range verified: {} Hz to {} Hz".format(
            expected_minimum, expected_maximum
        )
    )


def right_Minimal_Carbonization():
    mouseClick(
        waitForObject(names.modeButton_nameLabel_QLabel_2),
        74, 41, Qt.NoModifier, Qt.LeftButton
    )
    clickButton(
        waitForObject(names.centralWidget_Cleaning_QPushButton)
    )
    clickButton(
        waitForObject(names.centralWidget_DisableButton_QPushButton)
    )


def main():

    common.enter_login_pin()
    common.dismiss_fiber_verification_warning()
    common.navigate_to_expert_screen()
    common.left_Minimal_Carbonization()
    verify_frequency_range()
    right_Minimal_Carbonization()
    common.navigate_to_home_screen()

