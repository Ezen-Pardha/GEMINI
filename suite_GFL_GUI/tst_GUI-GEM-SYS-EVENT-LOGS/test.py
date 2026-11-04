# -*- coding: utf-8 -*-

from common import *

def main():
    enter_login_pin() 
    clickButton(waitForObject(names.homeScreen_settingsButton_QPushButton))
    test.log("Navigating to Settings")
    test.log("SVV TAG:GEN-LOG-001: Verifying Settings screen view")
    
    try:
        waitForObject(names.settingsScreen_tbSystemInfo_TabWidget, 5000)
        test.passes("PASS: Program successfully displays the Settings screen")
    except LookupError:
        test.fail("FAIL: Settings screen is not displayed")

    clickTab(waitForObject(names.settingsScreen_tbSystemInfo_TabWidget), "LOGS")
    test.log("Navigation to Settings Logs Tab")
    clickButton(waitForObject(names.settingsScreen_pbService_QPushButton))
    test.log("Verifying Service Mode passcode screen")
    
    try:
        login_screen = waitForObject(names.loginScreen_LoginScreen, 5000)
    
        if login_screen.visible:
            test.passes("PASS: Service Mode passcode screen is displayed")
        else:
            test.fail("FAIL: Service Mode passcode screen is not visible")
    
    except LookupError:
        test.fail("FAIL: Service Mode passcode screen is not displayed")
        
    for index in range(5):
        click_and_report(
            names.numpad_pushButton_9_NumpadButton,
            "Enter service PIN digit 9, press {} of 4".format(index + 1)
        )
    test.log("Verifying Service Mode active window")
    
    try:
        service_screen = waitForObject(
            names.serviceScreen_ServiceScreen,
            5000
        )
        if service_screen.isActiveWindow:
            test.passes(
                "PASS: Service Mode window is active"
            )
        else:
            test.fail(
                "FAIL: Service Mode window is not active"
            )
            return
    except Exception as error:
        test.fail(
            "FAIL: Unable to verify Service Mode window: {}".format(error)
        )
        return
    
    clickTab(waitForObject(names.serviceScreenTabWidget_QTabWidget), "SYSTEM EVENT LOG")
    test.log("Navigating to System Event Log Tab")
    test.log("Verifying System Event Log tab widget")
    
    try:
        event_log_tab = waitForObject(
            names.serviceScreenTabWidget_QTabWidget
        )
        if event_log_tab.isActiveWindow:
            test.passes(
                "PASS: System Event Log tab widget is active"
            )
        else:
            test.fail(
                "FAIL: System Event Log tab widget is not active"
            )
    except Exception as error:
        test.fail(
            "FAIL: Unable to verify System Event Log tab widget: "
            + str(error)
        )
    
