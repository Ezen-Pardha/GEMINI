# -*- coding: utf-8 -*-

from common import *
import names


def main():
    test.log("START: GUI-GEM-SETTINGS-WIRELESS-FOOTPEDAL")
    test.log("Preparing application and opening System Settings")

    enter_login_pin()
    navigate_to_settings()

    test.log("GUI-SET-053: Verify Settings screen provides Wireless Footswitch tab")
    clickTab(waitForObject(names.settingsScreen_tbSystemInfo_TabWidget), "WIRELESS \nFOOTSWITCH")
    test.log("Opened Wireless Footswitch tab")
    test.vp("Settings - Wireless Footswitch")

    test.log("GUI-SET-054: Verify Wired Footpedal Connected popup")
    test.log("Selecting Pair button")
    clickButton(waitForObject(names.frame_pairButton_QPushButton))

    test.log("Wired Footpedal Connected popup verification")
    test.vp("Wired Footpedal Connected Popup")
    test.log("KNOWN ISSUE: Wireless Footpedal Pairing popup specified in the test case is not available in the current emulator build.")

    test.log("GUI-SET-053 to GUI-SET-054 execution completed")

    test.fail("Wireless Footpedal Pairing Popup is Not Available in the Current Emulator Build")

    test.log("GUI-SET-057: Verify OK button on Wired Footpedal Connected popup")
    clickButton(waitForObject(names.centralWidget_OKButton_QPushButton_2))
    test.log("Clicked OK on Wired Footpedal Connected popup")

    test.log("GUI-SET-057: Select Back button")
    sendEvent("QMouseEvent", waitForObject(names.frame_lbCenterLeftImage_QLabel), QEvent.MouseButtonDblClick, 602, 480, Qt.LeftButton, 1, 0)
    openContextMenu(waitForObject(names.frame_lbCenterLeftImage_QLabel), 602, 480, 1)
    clickButton(waitForObject(names.settingsScreen_pbBack_QPushButton))
    test.log("Clicked Back button")

    test.log("GUI-SET-057: Verify navigation to Home screen")
    test.vp("Returned to Home Screen Tab")
    test.log("Returned to Home screen after closing the Wired Footpedal Connected popup and selecting Back")

    test.log("GUI-SET-061: Pairing step-1 Back navigation cannot be verified because the pairing popup is unavailable in the current build")
    test.log("GUI-SET-062: Settings tab navigation is available after closing the popup and selecting Back")

    test.log("GUI-SET-057 to GUI-SET-062 execution completed")
    test.log("FINAL VALIDATION: GUI-GEM-SETTINGS-WIRELESS-FOOTPEDAL test execution finished")