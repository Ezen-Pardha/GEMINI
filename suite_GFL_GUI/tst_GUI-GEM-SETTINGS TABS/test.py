# -*- coding: utf-8 -*-

from common import *

def main():
    enter_login_pin()
    clickButton(waitForObject(names.homeScreen_settingsButton_QPushButton))
    test.log("Navigating to Settings Screen")
    clickButton(waitForObject(names.settingsScreen_pbBack_QPushButton))
    test.log("SVV TAG:GUI-SET-001: Verifying navigation back to Home screen")
    
    try:
        waitForObject(names.homeScreen_settingsButton_QPushButton, 5000)
        test.passes("PASS: Program successfully reverted back to Home screen")
    except LookupError:
        test.fail("FAIL: Home screen was not displayed after clicking Back button")
    clickButton(waitForObject(names.homeScreen_settingsButton_QPushButton))
    
    test.log("Navigating to SYSTEM tab")
    clickTab(waitForObject(names.settingsScreen_tbSystemInfo_TabWidget),"SYSTEM")
    test.log("SVV TAG:GUI-SET-002: Verifying System Settings Tab is displayed on the screen")
    system_tab = waitForObject(names.settingsScreen_tbSystemInfo_TabWidget)
    if str(system_tab.tabText(system_tab.currentIndex)) == "SYSTEM":
        test.passes("SYSTEM tab is displayed on the screen")
    else:
        test.fail("SYSTEM tab is not displayed on the screen")
    test.log("Navigating back from SYSTEM tab")
    clickButton(waitForObject(names.settingsScreen_pbBack_QPushButton))
    test.log("Reopening Settings screen")
    clickButton(waitForObject(names.homeScreen_settingsButton_QPushButton))
    
    test.log("Navigating to USER PRESETS tab")
    clickTab(waitForObject(names.settingsScreen_tbSystemInfo_TabWidget),"USER\nPRESETS" )
    test.log("SVV TAG:GUI-SET-003: Verifying USER PRESETS Tab is displayed on the screen")
    user_presets_tab = waitForObject(names.settingsScreen_tbSystemInfo_TabWidget)
    if str(user_presets_tab.tabText(user_presets_tab.currentIndex)) == "USER\nPRESETS":
        test.passes("USER PRESETS tab is displayed on the screen")
    else:
        test.fail("USER PRESETS tab is not displayed on the screen")
    test.log("Navigating back from User Presets")
    clickButton(waitForObject(names.settingsScreen_pbBack_QPushButton))
    test.log("Reopening Settings screen")
    
    clickButton(waitForObject(names.homeScreen_settingsButton_QPushButton))
    test.log("Navigating to INFO tab")
    clickTab(waitForObject(names.settingsScreen_tbSystemInfo_TabWidget),"INFO")
    test.log("SVV TAG:GUI-SET-004: Verifying INFO Tab is displayed on the screen")
    info_tab = waitForObject(names.settingsScreen_tbSystemInfo_TabWidget)
    if str(info_tab.tabText(info_tab.currentIndex)) == "INFO":
        test.passes("INFO tab is displayed on the screen")
    else:
        test.fail("INFO tab is not displayed on the screen")
    test.log("Navigating back from INFO tab")
    
    clickButton(waitForObject(names.settingsScreen_pbBack_QPushButton))
    test.log("Reopening Settings screen")
    clickButton(waitForObject(names.homeScreen_settingsButton_QPushButton))
    test.log("Navigating to LOGS tab")
    clickTab(waitForObject(names.settingsScreen_tbSystemInfo_TabWidget),"LOGS")
    test.log("SVV TAG:GUI-SET-005: Verifying LOGS Tab is displayed on the screen")
    logs_tab = waitForObject(names.settingsScreen_tbSystemInfo_TabWidget)
    if str(logs_tab.tabText(logs_tab.currentIndex)) == "LOGS":
        test.passes("LOGS tab is displayed on the screen")
    else:
        test.fail("LOGS tab is not displayed on the screen")

    clickButton(waitForObject(names.settingsScreen_pbBack_QPushButton))
    test.log("Verifying navigation back to Home screen")
    clickButton(waitForObject(names.homeScreen_settingsButton_QPushButton))
    test.log("Navigating to Settings Screen")
    test.log("SVV TAG:GUI-SET-006: Verifying active profile is displayed on the screen")
    test.ocrTextPresent("PROFILE: DEFAULT")
    test.log("Confirming active profile is displayed in the top banner")
