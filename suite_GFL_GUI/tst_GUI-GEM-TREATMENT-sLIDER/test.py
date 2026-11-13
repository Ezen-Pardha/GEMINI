# -*- coding: utf-8 -*-
from common import *
import names

def main():
    enter_login_pin()

    # Open Expert / Treatment screen
    clickButton(waitForObject(names.gbExpert_expertButton_QPushButton))

    # Verify Pulse Energy adjustment area
    pulse_energy_slider = waitForObject(
        names.indexPicker_valuePicker_IntervalSlider
    )

    test.verify(
        pulse_energy_slider.visible,
        "Pulse Energy adjustment control is displayed."
    )

    # Verify Frequency adjustment area
    frequency_slider = waitForObject(
        names.indexPicker_valuePicker_IntervalSlider_5
    )

    test.verify(
        frequency_slider.visible,
        "Frequency adjustment control is displayed."
    )