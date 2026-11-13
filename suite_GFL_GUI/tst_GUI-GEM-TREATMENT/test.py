
# -*- coding: utf-8 -*-

from common import *
import names


def main():
    enter_login_pin()

    # Open Expert Mode
    clickButton(waitForObject(
        names.gbExpert_expertButton_QPushButton
    ))
    test.log("Expert Mode opened successfully")

    # Verify Average Power adjustment area
    average_power_label = waitForObject(
        names.averagePowerWidget_nameLabel_QLabel
    )
    test.verify(
        average_power_label.visible,
        "Average Power adjustment area is visible"
    )

    mouseClick(
        average_power_label,
        111, 44,
        Qt.NoModifier,
        Qt.LeftButton
    )
    test.log("Average Power area verified")

    # Verify second adjustment area
    second_adjustment_area = waitForObject(
        names.averagePowerWidget_nameLabel_QLabel_2
    )
    test.verify(
        second_adjustment_area.visible,
        "Second adjustment area is visible"
    )

    mouseClick(
        second_adjustment_area,
        128, 30,
        Qt.NoModifier,
        Qt.LeftButton
    )
    test.log("Second adjustment area verified")

    # Verify Peak Power adjustment button
    peak_power_button = waitForObject(
        names.peakPowerButton_iconLabel_QLabel_2
    )
    test.verify(
        peak_power_button.visible,
        "Peak Power adjustment control is visible"
    )

    mouseClick(
        peak_power_button,
        9, 35,
        Qt.NoModifier,
        Qt.LeftButton
    )
    test.log("Peak Power adjustment control clicked")

    # Verify Peak Power setting
    peak_power_setting = waitForObject(
        names.centralWidget_pw250_QPushButton_2
    )
    test.verify(
        peak_power_setting.visible,
        "Peak Power setting is displayed"
    )

    clickButton(peak_power_setting)
    test.log("Peak Power setting selected")

    # Verify Pulse Mode button
    pulse_mode_button = waitForObject(
        names.modeButton_nameLabel_QLabel
    )
    test.verify(
        pulse_mode_button.visible,
        "Pulse Mode button is visible"
    )

    mouseClick(
        pulse_mode_button,
        84, 26,
        Qt.NoModifier,
        Qt.LeftButton
    )
    test.log("Pulse Mode button clicked")

    # Verify Pulse Mode popup
    pulse_mode_popup_option = waitForObject(
        names.centralWidget_CW_QPushButton_2
    )
    test.verify(
        pulse_mode_popup_option.visible,
        "Pulse Mode popup option is visible"
    )

    clickButton(pulse_mode_popup_option)
    test.log("CW Pulse Mode option selected")

    # Verify popup message
    message_label = waitForObject(
        names.centralWidget_MessageLabel_QLabel
    )
    test.verify(
        message_label.visible,
        "Pulse Mode message is displayed"
    )

    # Cancel popup/message
    cancel_button = waitForObject(
        names.centralWidget_CancelButton_QPushButton_2
    )
    test.verify(
        cancel_button.visible,
        "Cancel button is visible"
    )

    clickButton(cancel_button)
    test.log("Pulse Mode popup cancelled")

  