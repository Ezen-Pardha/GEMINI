import names
import test

from squish import *
from common import *


def close_confirmation_popup():
    if object.exists(names.centralWidget_okButton_QPushButton):
        clickButton(
            waitForObject(names.centralWidget_okButton_QPushButton, 20000)
        )
        test.passes("PASS: Confirmation popup closed")
    else:
        test.log("INFO: Confirmation popup was not displayed")


def open_expert_screen():
    if object.exists(names.gbExpert_expertButton_QPushButton):
        clickButton(
            waitForObject(names.gbExpert_expertButton_QPushButton, 20000)
        )
        test.passes("PASS: Expert screen opened")
    else:
        test.fail("FAIL: Expert button not found. Check current application screen.")
        raise Exception("Expert button not available")


def select_left_peak_power(level, button_object, x, y):
    try:
        mouseClick(
            waitForObject(names.peakPowerButton_iconLabel_QLabel, 20000),
            x, y, Qt.NoModifier, Qt.LeftButton
        )

        waitForObject(button_object, 20000)
        test.passes("PASS: Left {} peak power option is available".format(level))

        clickButton(waitForObject(button_object, 20000))

        test.passes("PASS: Left Peak Power selected: {} ({})".format(
            level, {"High": 500, "Medium": 250, "Low": 125}[level]
        ))

    except Exception as error:
        test.fail("FAIL: Left {} Peak Power selection failed - {}".format(level, error))
        raise


def select_right_peak_power(level, button_object, x, y):
    try:
        mouseClick(
            waitForObject(names.peakPowerButton_nameLabel_QLabel_2, 20000),
            x, y, Qt.NoModifier, Qt.LeftButton
        )

        waitForObject(button_object, 20000)
        test.passes("PASS: Right {} peak power option is available".format(level))

        clickButton(waitForObject(button_object, 20000))

        test.passes("PASS: Right Peak Power selected: {} ({})".format(
            level, {"High": 500, "Medium": 250, "Low": 125}[level]
        ))

    except Exception as error:
        test.fail("FAIL: Right {} Peak Power selection failed - {}".format(level, error))
        raise


def verify_peak_power_levels():

    try:
        close_confirmation_popup()
        open_expert_screen()

        # LEFT PEAK POWER

        select_left_peak_power(
            "High",
            names.centralWidget_pw500_QPushButton,
            21, 27
        )

        select_left_peak_power(
            "Medium",
            names.centralWidget_pw250_QPushButton,
            17, 40
        )

        select_left_peak_power(
            "Low",
            names.centralWidget_pw125_QPushButton,
            1, 46
        )

        test.passes("PASS: Left Peak Power levels tested")

        # RIGHT PEAK POWER

        mouseClick(
            waitForObject(names.peakPowerButton_nameLabel_QLabel_2, 20000),
            56, 31, Qt.NoModifier, Qt.LeftButton
        )

        waitForObject(names.centralWidget_pw500_QPushButton, 20000)
        test.passes("PASS: Right High peak power option is available")

        clickButton(
            waitForObject(names.centralWidget_pw500_QPushButton, 20000)
        )
        test.passes("PASS: Right Peak Power selected: High (500)")

        mouseClick(
            waitForObject(names.peakPowerButton_iconLabel_QLabel_2, 20000),
            15, 32, Qt.NoModifier, Qt.LeftButton
        )

        mouseClick(
            waitForObject(names.centralWidget_mainWidget_QWidget, 20000),
            301, 224, Qt.NoModifier, Qt.LeftButton
        )

        waitForObject(names.centralWidget_pw250_QPushButton, 20000)
        test.passes("PASS: Right Medium peak power option is available")

        clickButton(
            waitForObject(names.centralWidget_pw250_QPushButton, 20000)
        )
        test.passes("PASS: Right Peak Power selected: Medium (250)")

        mouseClick(
            waitForObject(names.peakPowerButton_nameLabel_QLabel_2, 20000),
            58, 42, Qt.NoModifier, Qt.LeftButton
        )

        waitForObject(names.centralWidget_pw125_QPushButton, 20000)
        test.passes("PASS: Right Low peak power option is available")

        clickButton(
            waitForObject(names.centralWidget_pw125_QPushButton, 20000)
        )
        test.passes("PASS: Right Peak Power selected: Low (125)")

        test.passes(
            "PASS: Left and Right Peak Power selections completed"
        )

    except Exception as error:
        test.fail("FAIL: Peak Power verification failed - {}".format(error))
        raise


def main():
    test.log("Starting Left and Right Peak Power Verification")
    enter_login_pin()
    verify_peak_power_levels()
    test.log("Left and Right Peak Power Verification Completed")
