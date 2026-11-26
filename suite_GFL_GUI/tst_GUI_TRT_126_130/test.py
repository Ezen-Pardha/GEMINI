# -*- coding: utf-8 -*-

from common import *
import names


def main():
    test.log("START: GUI-TRT-126 - Treatment Screen Stone Sense Availability on Economy A")

    enter_login_pin()

    test.log("STEP 1: Verify Economy A system configuration")

    clickButton(waitForObject(names.homeScreen_settingsButton_QPushButton))
    clickTab(waitForObject(names.settingsScreen_tbSystemInfo_TabWidget), "LOGS")
    clickButton(waitForObject(names.settingsScreen_pbService_QPushButton))

    snooze(2)

    clickButton(waitForObject(names.numpad_pushButton_9_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_9_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_9_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_9_NumpadButton))

    snooze(2)

    test.log("VERIFY: Confirm the configured system type is Economy A")

    if not test.imagePresent("economyA"):
        test.fail("FAIL: System type is not Economy A. Stopping GUI-TRT-126 execution.")
        return

    test.passes("PASS: Economy A system configuration verified")

    clickButton(waitForObject(names.buttonsBar_backButton_QPushButton))
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton_8))

    test.log("STEP 2: Navigate to Treatment screen through Stone Quick Start")

    clickButton(waitForObject(names.homeScreen_pbStoneQuickStart_QToolButton))

    mouseClick(waitForObjectItem(names.tabLeftMainPresets_leftPresetsView_PresetListView, "_1"), 329, 43, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.tabRightMainPresets_rightPresetsView_PresetListView, "_1"), 110, 61, Qt.NoModifier, Qt.LeftButton)

    clickButton(waitForObject(names.quickStartScreen_pbContinue_QPushButton))

    test.log("STEP 3: Verify Stone Sense is not present on the Treatment screen for Economy A")

    if not test.imageNotPresent("Stone Sense Disable"):
        test.fail("FAIL: Stone Sense image is present on the Treatment screen")
    else:
        test.log("PASS: Stone Sense image is not present on the Treatment screen")

        test.vp("StoneSenseNotExistsVerification ")
        test.log("Stone Sense absence visual verification completed")

    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton_4))

    test.log("GUI-TRT-126: Verified that Stone Sense is not present on the Treatment screen for Economy A")
    test.log("END: GUI-TRT-126")