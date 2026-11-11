import os
import names
import test
from squish import *
from common import *


def close_confirmation_popup():

    try:
        if object.exists(names.centralWidget_okButton_QPushButton):

            clickButton(
                waitForObject(
                    names.centralWidget_okButton_QPushButton,
                    20000
                )
            )

            test.passes("PASS: Confirmation popup closed")

        else:
            test.log("INFO: Confirmation popup was not displayed")

    except Exception as error:
        test.fail(
            "FAIL: Unable to close confirmation popup - {}".format(error)
        )
        raise


def open_peak_power_expert_screen():

    try:
        if object.exists(names.gbExpert_expertButton_QPushButton):

            clickButton(
                waitForObject(
                    names.gbExpert_expertButton_QPushButton,
                    20000
                )
            )

            test.passes("PASS: Expert screen opened")

        else:
            test.fail(
                "FAIL: Expert button not found. "
                "Check whether the application is on the Home screen."
            )

            raise Exception("Expert button not available")

    except Exception as error:
        test.fail(
            "FAIL: Unable to open Expert screen - {}".format(error)
        )
        raise



def select_left_peak_power(level, button_object, x, y):

    try:
        mouseClick(
            waitForObject(
                names.peakPowerButton_iconLabel_QLabel,
                20000
            ),
            x,
            y,
            Qt.NoModifier,
            Qt.LeftButton
        )

        waitForObject(button_object, 20000)

        test.passes(
            "PASS: Left {} Peak Power option is available".format(level)
        )

        clickButton(
            waitForObject(button_object, 20000)
        )

        test.passes(
            "PASS: Left Peak Power selected: {} ({})".format(
                level,
                {"High": 500, "Medium": 250, "Low": 125}[level]
            )
        )

    except Exception as error:
        test.fail(
            "FAIL: Left {} Peak Power selection failed - {}".format(
                level,
                error
            )
        )
        raise


def select_right_high_peak_power():

    try:
        mouseClick(
            waitForObject(
                names.peakPowerButton_nameLabel_QLabel_2,
                20000
            ),
            56,
            31,
            Qt.NoModifier,
            Qt.LeftButton
        )

        waitForObject(
            names.centralWidget_pw500_QPushButton,
            20000
        )

        test.passes(
            "PASS: Right High Peak Power option is available"
        )

        clickButton(
            waitForObject(
                names.centralWidget_pw500_QPushButton,
                20000
            )
        )

        test.passes(
            "PASS: Right Peak Power selected: High (500)"
        )

    except Exception as error:
        test.fail(
            "FAIL: Right High Peak Power selection failed - {}".format(error)
        )
        raise


def select_right_medium_peak_power():

    try:
        mouseClick(
            waitForObject(
                names.peakPowerButton_iconLabel_QLabel_2,
                20000
            ),
            15,
            32,
            Qt.NoModifier,
            Qt.LeftButton
        )

        mouseClick(
            waitForObject(
                names.centralWidget_mainWidget_QWidget,
                20000
            ),
            301,
            224,
            Qt.NoModifier,
            Qt.LeftButton
        )

        waitForObject(
            names.centralWidget_pw250_QPushButton,
            20000
        )

        test.passes(
            "PASS: Right Medium Peak Power option is available"
        )

        clickButton(
            waitForObject(
                names.centralWidget_pw250_QPushButton,
                20000
            )
        )

        test.passes(
            "PASS: Right Peak Power selected: Medium (250)"
        )

    except Exception as error:
        test.fail(
            "FAIL: Right Medium Peak Power selection failed - {}".format(error)
        )
        raise

def select_right_low_peak_power():

    try:
        mouseClick(
            waitForObject(
                names.peakPowerButton_nameLabel_QLabel_2,
                20000
            ),
            58,
            42,
            Qt.NoModifier,
            Qt.LeftButton
        )

        waitForObject(
            names.centralWidget_pw125_QPushButton,
            20000
        )

        test.passes(
            "PASS: Right Low Peak Power option is available"
        )

        clickButton(
            waitForObject(
                names.centralWidget_pw125_QPushButton,
                20000
            )
        )

        test.passes(
            "PASS: Right Peak Power selected: Low (125)"
        )

    except Exception as error:
        test.fail(
            "FAIL: Right Low Peak Power selection failed - {}".format(error)
        )
        raise


def verify_peak_power_levels():
    try:
        close_confirmation_popup()
        open_peak_power_expert_screen()
        test.log("Starting Left Peak Power verification")
        select_left_peak_power(
            "High",
            names.centralWidget_pw500_QPushButton,
            21,
            27
        )
        select_left_peak_power(
            "Medium",
            names.centralWidget_pw250_QPushButton,
            17,
            40
        )
        select_left_peak_power(
            "Low",
            names.centralWidget_pw125_QPushButton,
            1,
            46
        )

        test.passes(
            "PASS: Left Peak Power High, Medium and Low selections completed"
        )

        test.log("Starting Right Peak Power verification")
        select_right_high_peak_power()
        select_right_medium_peak_power()
        select_right_low_peak_power()
        test.passes(
            "PASS: Right Peak Power High, Medium and Low selections completed"
        )
        test.passes(
            "PASS: Left and Right Peak Power verification completed"
        )

    except Exception as error:

        test.fail(
            "FAIL: Peak Power verification failed - {}".format(error)
        )
        raise
def main():

    test.log("Starting Peak Power Verification")

    runtime_path = os.path.expanduser(
        "~/Downloads/WORK/Gemini_GFL_2.5_Codebase_8May2026/"
        "build-gemini-Desktop-Debug"
    )

    configure_system_type(
        new_type="C",
        runtime_path=runtime_path
    )
    try:
        context = currentApplicationContext()

        context.detach()
        snooze(3)
        test.log("AUT context detached")

    except Exception as error:
        test.log(
            "Error while closing AUT: {}".format(error)
        )
    startApplication(
        "bravo --disable-watchdog --watchdog-timeout=10 "
        "--disable-integrity-check "
        "--disable-fiber-use-check "
        "--disable-firmware-check "
        "--disable-ssm "
        "--disable-ports-check"
    )

    snooze(5)
    enter_login_pin()
    test.passes("PASS: Login completed")
    verify_economyc_type()
    clickButton(waitForObject(names.buttonsBar_backButton_QPushButton))
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton_2)) 
    verify_peak_power_levels()

    test.log(
        "Left and Right Peak Power Verification Completed"
    )
