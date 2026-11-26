
# -*- coding: utf-8 -*-

from common import *
import names


def main():
    enter_login_pin()

    # Open Expert Mode
    clickButton(waitForObject(names.gbExpert_expertButton_QPushButton))

    # Verify Home Button
    home_button = waitForObject(
        names.buttonsBar_homeButton_QPushButton_4
    )
    test.verify(home_button.visible, "Home button is visible")
    test.verify(home_button.enabled, "Home button is enabled")
    clickButton(home_button)
    test.log("Home button clicked successfully")

    # Open Expert Mode again
    clickButton(waitForObject(names.gbExpert_expertButton_QPushButton))

    # Verify Save Button
    save_button = waitForObject(
        names.pulseModeWidget_saveButton_QPushButton
    )
    test.verify(save_button.visible, "Save button is visible")
    test.verify(save_button.enabled, "Save button is enabled")
    clickButton(save_button)
    test.log("Save button clicked successfully")

    # Close the popup if displayed
    close_button = waitForObject(
        names.centralWidget_pbClose_QPushButton
    )
    clickButton(close_button)
    test.log("Popup closed successfully")

    # Verify Pulse Energy Increment Button
    pulse_energy_increment = waitForObject(
        names.pulseEnergyWidget_incrementButton_QPushButton
    )
    test.verify(
        pulse_energy_increment.visible,
        "Pulse Energy Increment button is visible"
    )
    test.verify(
        pulse_energy_increment.enabled,
        "Pulse Energy Increment button is enabled"
    )
    clickButton(pulse_energy_increment)
    test.log("Pulse Energy Increment button clicked successfully")

    # Verify Pulse Energy Decrement Button
    pulse_energy_decrement = waitForObject(
        names.pulseEnergyWidget_decrementButton_QPushButton
    )
    test.verify(
        pulse_energy_decrement.visible,
        "Pulse Energy Decrement button is visible"
    )
    test.verify(
        pulse_energy_decrement.enabled,
        "Pulse Energy Decrement button is enabled"
    )
    clickButton(pulse_energy_decrement)
    test.log("Pulse Energy Decrement button clicked successfully")

    # Verify Frequency Increment Button
    frequency_increment = waitForObject(
        names.frequencyWidget_incrementButton_QPushButton
    )
    test.verify(
        frequency_increment.visible,
        "Frequency Increment button is visible"
    )
    test.verify(
        frequency_increment.enabled,
        "Frequency Increment button is enabled"
    )
    clickButton(frequency_increment)
    test.log("Frequency Increment button clicked successfully")

    # Verify Frequency Decrement Button
    frequency_decrement = waitForObject(
        names.frequencyWidget_decrementButton_QPushButton
    )
    test.verify(
        frequency_decrement.visible,
        "Frequency Decrement button is visible"
    )
    test.verify(
        frequency_decrement.enabled,
        "Frequency Decrement button is enabled"
    )

    test.vp("Verified Treatment Screen")

    clickButton(frequency_decrement)
    test.log("Frequency Decrement button clicked successfully")

    # Verify Standby Button
    standby_button = waitForObject(
        names.stateSwitch_standbyButton_QPushButton
    )
    test.verify(standby_button.visible, "Standby button is visible")
    test.verify(standby_button.enabled, "Standby button is enabled")
    clickButton(standby_button)
    test.log("Standby button clicked successfully")

    # Verify Ready Button
    ready_button = waitForObject(
        names.stateSwitch_readyButton_QPushButton
    )
    test.verify(ready_button.visible, "Ready button is visible")
    test.verify(ready_button.enabled, "Ready button is enabled")
    clickButton(ready_button)
    test.log("Ready button clicked successfully")

    # Verify Ready Screen
   

    test.log("Treatment Screen button verification completed")
