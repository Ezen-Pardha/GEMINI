
# -*- coding: utf-8 -*-

from common import *
import test


def verify_frequency_range():
    test.log("Starting frequency range verification")

    expected_min = 1.3
    expected_max = 60.0

    test.log(
        "Expected minimum frequency: {} Hz".format(expected_min)
    )
    test.log(
        "Expected maximum frequency: {} Hz".format(expected_max)
    )

    frequency_drum = waitForObject(
        names.valueDrum_Cylinder_3
    )

    try:
        internal_value = frequency_drum.value
        test.log(
            "Frequency drum internal value: {}".format(
                internal_value
            )
        )
    except Exception as error:
        test.log(
            "Could not read internal frequency value: {}".format(
                error
            )
        )

    test.fail(
        "Frequency range verification incomplete: actual minimum "
        "and maximum frequency properties have not been identified."
    )


def main():
    test.log("START: Expert Frequency test")

    try:
        enter_login_pin()
        dismiss_fiber_verification_warning()
        navigate_to_expert_screen()
        left_navigate_to_enucleation_disable()

        verify_frequency_range()

    except Exception as error:
        test.fail(
            "Expert Frequency test failed: {}".format(error)
        )
        raise
