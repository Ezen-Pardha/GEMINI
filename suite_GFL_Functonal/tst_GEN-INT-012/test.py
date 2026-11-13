
# -*- coding: utf-8 -*-

from common import *
import names


def verify_treatment_screen():
    try:
        treatment_button = waitForObjectExists(
            names.stoneSenseFrame_pbStoneSense_QPushButton
        )

        test.compare(
            treatment_button.visible,
            True,
            "PASS: StoneSense toggle button is visible on Treatment screen"
        )

        test.passes("PASS: Treatment screen verification completed")

    except LookupError:
        test.fail("FAIL: StoneSense toggle button not found on Treatment screen")


def navigate_to_guided_mode():
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    clickButton(waitForObject(names.locationFrame_kidneyPcnlLocationButton_QPushButton))
    clickButton(waitForObject(names.flowRateFrame_lowFlowRateButton_QPushButton))
    clickButton(waitForObject(names.hardnessFrame_smallHardnessButton_QPushButton))
    clickButton(waitForObject(names.stoneAssistantModeScreen_continueButton_QPushButton))

    verify_treatment_screen()

    mouseClick(
        waitForObject(names.leftPedalWidget_wdPresetTabs_TabWidget),
        624, 42, Qt.NoModifier, Qt.LeftButton
    )


def main():
    enter_login_pin()
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton))

    test.log("Scenario: Stone Guided Mode")
    navigate_to_guided_mode()

