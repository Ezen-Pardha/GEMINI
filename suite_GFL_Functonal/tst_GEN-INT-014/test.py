
# -*- coding: utf-8 -*-

from common import *
import names


def verify_calibration_popup():
    try:
        popup = waitForObject(
            names.calibrationPopupDialog_CalibrationPopupDialog
        )

        test.compare(
            popup.visible,
            True,
            "StoneSense calibration popup should be visible"
        )

        test.passes(
            "PASS: StoneSense calibration popup is displayed in Quick Start Mode."
        )
        return True

    except LookupError:
        test.fail(
            "FAIL: StoneSense calibration popup was not found in Quick Start Mode."
        )
        return False


def main():
    enter_login_pin()

    clickButton(
        waitForObject(names.mainFrame_okButton_QPushButton)
    )

    test.log("Scenario: Stone Quick Start Mode")

    clickButton(
        waitForObject(names.homeScreen_pbStoneQuickStart_QToolButton)
    )

    mouseClick(
        waitForObjectItem(
            names.tabLeftMainPresets_leftPresetsView_PresetListView,
            "_1"
        ),
        431, 50, Qt.NoModifier, Qt.LeftButton
    )

    mouseClick(
        waitForObjectItem(
            names.tabRightMainPresets_rightPresetsView_PresetListView,
            "_1"
        ),
        153, 53, Qt.NoModifier, Qt.LeftButton
    )

    clickButton(
        waitForObject(names.quickStartScreen_pbContinue_QPushButton)
    )

    test.passes("PASS: Quick Start Treatment screen navigation completed.")

    clickButton(
        waitForObject(names.stoneSenseFrame_pbStoneSense_QPushButton)
    )

    if not verify_calibration_popup():
        return

    mouseClick(
        waitForObject(names.pInitiateCalibrationFrame_checkBoxFrame_QFrame),
        58, 155, Qt.NoModifier, Qt.LeftButton
    )

    mouseClick(
        waitForObject(names.pInitiateCalibrationFrame_pAnimationIconLabel_QLabel),
        57, 232, Qt.NoModifier, Qt.LeftButton
    )


