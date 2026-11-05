# -*- coding: utf-8 -*-

from common import *

def main():
    enter_login_pin()
    clickButton(waitForObject(names.homeScreen_settingsButton_QPushButton))
    test.log("Navigating to settings screen")
    clickTab(waitForObject(names.settingsScreen_tbSystemInfo_TabWidget), "LOGS")
    test.log("Navigating to Logs tab")
    clickButton(waitForObject(names.settingsScreen_pbService_QPushButton))
    test.log("SVV TAG:GEN-GUI-003: Navigating to Service Mode")
    
    for index in range(5):
        click_and_report(
            names.numpad_pushButton_9_NumpadButton,
            "Enter service PIN digit 9, press {} of 4".format(index + 1)
        )
    test.log("Service mode entered")
    
    service_screen = waitForObject(names.serviceScreen_ServiceScreen)
    if service_screen.visible:
        test.passes("PASS: Service Mode is visible")
    else:
        test.fail("FAIL: Service Mode is not visible")
        return
    
    test.log("Verifying Demo Mode toggle button is present")
    demo_on = waitForObject(names.demoModePanel_pbDemoModeOn_QToolButton)
    demo_off = waitForObject(names.demoModePanel_pbDemoModeOff_QToolButton)
    if demo_on.visible and demo_off.visible:
        test.passes("PASS: Demo Mode toggle buttons are present")
    else:
        test.fail("FAIL: Demo Mode toggle buttons are not present")
    
    clickButton(waitForObject(names.demoModePanel_pbDemoModeOn_QToolButton))
    clickButton(waitForObject(names.buttonsFrame_acceptButton_QPushButton))
    test.log("Verifying Demo Mode is active")
    demo_on = waitForObject(names.demoModePanel_pbDemoModeOn_QToolButton)
    if demo_on.down:
        test.passes("PASS: Demo Mode ON button is active")
    else:
        test.fail("FAIL: Demo Mode ON button is inactive")
    
    clickButton(waitForObject(names.buttonsBar_backButton_QPushButton))
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    test.log("Navigating back to Home Screen")
    snooze(2)
    test.ocrTextPresent("HOME - DEMO")
    test.log("Confirming 'DEMO' displayed in banner")
    clickButton(waitForObject(names.homeScreen_settingsButton_QPushButton))
    test.log("Navigating to settings screen")
    clickTab(waitForObject(names.settingsScreen_tbSystemInfo_TabWidget), "LOGS")
    test.log("Navigating to Logs tab")
    clickButton(waitForObject(names.settingsScreen_pbService_QPushButton))
    test.log("Navigating to Service Mode")
    
    for index in range(5):
        click_and_report(
            names.numpad_pushButton_9_NumpadButton,
            "Enter service PIN digit 9, press {} of 4".format(index + 1)
        )
    service_screen = waitForObject(names.serviceScreen_ServiceScreen)
    if service_screen.visible:
        test.passes("PASS: Service Mode is entered again")
    else:
        test.fail("FAIL: Service Mode is not visible")
        return
    
    clickButton(waitForObject(names.demoModePanel_pbDemoModeOff_QToolButton))
    clickButton(waitForObject(names.buttonsFrame_acceptButton_QPushButton))
    test.log("Verifying Demo Mode is inactive")
    demo_off = waitForObject(names.demoModePanel_pbDemoModeOff_QToolButton)
    if demo_off.down:
        test.passes("PASS: Demo Mode is inactive")
    else:
        test.fail("FAIL: Demo Mode is active")
    
    clickButton(waitForObject(names.buttonsBar_backButton_QPushButton))
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    test.log("Navigating back to Home Screen")
    snooze(2)
    test.ocrTextPresent("HOME")
    test.log("Confirming 'DEMO' is no longer displayed in screen banner")
