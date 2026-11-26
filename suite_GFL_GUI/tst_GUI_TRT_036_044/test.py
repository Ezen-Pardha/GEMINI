import common
import names
import test
from squish import *


def set_cw_power_and_standby():

    try:
        test.log("========== CW POWER TEST STARTED ==========")

        clickButton(
            waitForObject(names.gbExpert_expertButton_QPushButton)
        )
        test.log("PASS: Expert screen opened")
        mouseClick(
            waitForObject(names.modeButton_nameLabel_QLabel),
            49, 45,
            Qt.NoModifier,
            Qt.LeftButton
        )
        test.log("PASS: Mode selected")

        clickButton(
            waitForObject(names.centralWidget_CW_QPushButton)
        )
        test.log("PASS: CW mode selected")

        clickButton(
            waitForObject(names.centralWidget_DisableButton_QPushButton)
        )
        test.log("PASS: Disable selected")

        test.log("Reading initial CW power display")
        for count in range(10):

            test.log(
                "CW power increment - click {}".format(count + 1)
            )

            button = waitForObject(
                names.powerWidgetCW_incrementButton_QPushButton,
                20000
            )

            if not button.enabled:
                test.log(
                    "FAIL: CW increment button disabled at click {}".format(
                        count + 1
                    )
                )
                raise Exception(
                    "CW increment button is disabled at click {}".format(
                        count + 1
                    )
                )

            clickButton(button)

            test.log(
                "PASS: CW increment click {} completed".format(count + 1)
            )
        test.log("Selecting Standby state")

        clickButton(
            waitForObject(names.stateSwitch_standbyButton_QPushButton)
        )

        test.log("PASS: Standby state selected")

        test.log("========== CW POWER TEST COMPLETED ==========")

        test.passes(
            "PASS: CW power increment and Standby sequence completed"
        )
    except Exception as error:
        test.log("========== CW POWER TEST FAILED ==========")
        test.log("ERROR: {}".format(error))

        test.fail(
            "FAIL: CW power and Standby sequence - {}".format(error)
        )
        raise
def main():

    test.log("========== TEST CASE STARTED ==========")

    try:
        common.enter_login_pin()
        test.log("PASS: Login completed")
        set_cw_power_and_standby()
    except Exception as error:
        test.log("TEST CASE FAILED: {}".format(error))
        raise

