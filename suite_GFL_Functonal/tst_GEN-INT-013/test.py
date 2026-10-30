
# -*- coding: utf-8 -*-

from common import *
import names


def verify_calibration_popup():
    try:
        waitForObject(names.pInitiateCalibrationFrame_pAnimationIconLabel_QLabel)
        test.passes("PASS: StoneSense calibration popup is displayed.")
        return True
    except LookupError:
        test.fail("FAIL: StoneSense calibration popup is not displayed.")
        return False


def main():
    enter_login_pin()

    clickButton(waitForObject(names.mainFrame_okButton_QPushButton))

    test.log("Scenario: Stone Guided Mode - StoneSense Calibration")

    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    clickButton(waitForObject(names.locationFrame_kidneyPcnlLocationButton_QPushButton))
    clickButton(waitForObject(names.flowRateFrame_lowFlowRateButton_QPushButton))
    clickButton(waitForObject(names.hardnessFrame_smallHardnessButton_QPushButton))
    clickButton(waitForObject(names.stoneAssistantModeScreen_continueButton_QPushButton))

    test.passes("PASS: Treatment screen navigation completed.")

    clickButton(waitForObject(names.stoneSenseFrame_pbStoneSense_QPushButton))

    if not verify_calibration_popup():
        return

    mouseClick(
        waitForObject(names.pInitiateCalibrationFrame_pAnimationIconLabel_QLabel),
        69, 204, Qt.NoModifier, Qt.LeftButton
    )

    mouseDrag(
        waitForObject(names.pInitiateCalibrationFrame_checkBoxFrame_QFrame),
        70, 222, 8, -13, 1, Qt.LeftButton
    )

    mouseClick(
        waitForObject(names.calibrationPopupDialog_CalibrationPopupDialog),
        94, 40, Qt.NoModifier, Qt.LeftButton
    )

    test.passes("PASS: StoneSense calibration popup interaction completed.")
