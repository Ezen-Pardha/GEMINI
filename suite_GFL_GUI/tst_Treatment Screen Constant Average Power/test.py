# -*- coding: utf-8 -*-
from common import *
import names

def main():
    enter_login_pin()

    clickButton(waitForObject(names.gbExpert_expertButton_QPushButton))
    

    # Verify Frequency control before adjustment
    frequency = waitForObject(
        names.indexPicker_valuePicker_IntervalSlider_5
    )

    test.verify(
        frequency.visible,
        "Frequency control is visible before Pulse Energy adjustment."
    )

    # Increase Pulse Energy twice
    clickButton(
        waitForObject(
            names.pulseEnergyWidget_incrementButton_QPushButton
        )
    )

    clickButton(
        waitForObject(
            names.pulseEnergyWidget_incrementButton_QPushButton
        )
    )

    # Verify Frequency control remains visible
    frequency = waitForObject(
        names.indexPicker_valuePicker_IntervalSlider_5
    )

    test.verify(
        frequency.visible,
        "Frequency control is visible after Pulse Energy adjustment."
    )