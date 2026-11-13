# -*- coding: utf-8 -*-

import names


def main():
    doubleClick(waitForObject(names.numpad_pushButton_8_NumpadButton), 59, 68, Qt.NoModifier, Qt.LeftButton)
    doubleClick(waitForObject(names.numpad_pushButton_8_NumpadButton), 59, 68, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton))
    
    clickButton(waitForObject(names.homeScreen_settingsButton_QPushButton))

    if test.vp("settingScreen"):
        test.passes("Successful Confirmation program displays Settings screen")
    else:
        test.fail("Failed Confirmation program displays Settings screen")
    
    if test.vp("eventLogsTab"):
        test.passes("Successful Confirmation program displays the system event logs tab")
    else:
        test.fail("Failed Confirmation program displays the system event logs tab")

    clickTab(waitForObject(names.settingsScreen_tbSystemInfo_TabWidget), "LOGS")
    clickButton(waitForObject(names.settingsScreen_pbService_QPushButton))

    if test.vp("numericKeypad"):
        test.passes("Successful Confirmation program displays numeric keypad provide on Service Mode passcode screen")
    else:
        test.fail("Failed Confirmation program displays numeric keypad provide on Service Mode passcode screen")  
    clickButton(waitForObject(names.buttonsBar_backButton_QPushButton_2))    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton_5))
    
    clickButton(waitForObject(names.homeScreen_settingsButton_QPushButton))
    
    if test.vp("settingScreen"):
        test.passes("Successful Confirmation program displays Settings screen")
    else:
        test.fail("Failed Confirmation program displays Settings screen")
    
    if test.vp("eventLogsTab"):
        test.passes("Successful Confirmation program displays the system event logs tab")
    else:
        test.fail("Failed Confirmation program displays the system event logs tab")
        
    clickTab(waitForObject(names.settingsScreen_tbSystemInfo_TabWidget), "LOGS")
    clickButton(waitForObject(names.settingsScreen_pbService_QPushButton))
    if test.vp("numericKeypad"):
        test.passes("Successful Confirmation program displays numeric keypad provide on Service Mode passcode screen")
    else:
        test.fail("Failed Confirmation program displays numeric keypad provide on Service Mode passcode screen")      
    clickButton(waitForObject(names.buttonsBar_backButton_QPushButton_2))

    if test.vp("eventLogsScreen"):
        test.passes("Successful Confirmation program reverts back to system event logs screen")
    else:
        test.fail("Failed Confirmation program reverts back to system event logs screen")
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton_5))

    clickButton(waitForObject(names.homeScreen_settingsButton_QPushButton))
    clickTab(waitForObject(names.settingsScreen_tbSystemInfo_TabWidget), "LOGS")
    clickButton(waitForObject(names.settingsScreen_pbService_QPushButton))
    clickButton(waitForObject(names.numpad_pushButton_9_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_9_NumpadButton))

    if test.vp("hastrickInput"):
        test.passes("Successful Confirmation program displays entries as “*”")
    else:
        test.fail("Failed Confirmation program displays entries as “*”")
    
    clickButton(waitForObject(names.numpad_pushButton_9_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_9_NumpadButton))
    
    test.log("Clicking BACK button after PIN entry")
    clickButton(waitForObject(names.buttonsBar_backButton_QPushButton))
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton_5))

    clickButton(waitForObject(names.homeScreen_settingsButton_QPushButton))
    clickTab(waitForObject(names.settingsScreen_tbSystemInfo_TabWidget), "LOGS")
    clickButton(waitForObject(names.settingsScreen_pbService_QPushButton))
    
    if test.vp("numericKeypad"):
        test.passes("Successful Confirmation program displays numeric keypad provide on Service Mode passcode screen")
    else:
        test.fail("Failed Confirmation program displays numeric keypad provide on Service Mode passcode screen") 
        
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    doubleClick(waitForObject(names.numpad_pushButton_9_NumpadButton), 72, 72, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.numpad_pushButton_9_NumpadButton))

    if test.vp("invalidPasscode"):
        test.passes("Successful Confirmation program displays the “Invalid passcode” message")
    else:
        test.fail("Failed Confirmation program displays the “Invalid passcode” message")     

    clickButton(waitForObject(names.buttonsBar_backButton_QPushButton_2))
    clickButton(waitForObject(names.settingsScreen_pbService_QPushButton))
    clickButton(waitForObject(names.numpad_pushButton_9_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_9_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_9_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_9_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_9_NumpadButton))
    mouseClick(waitForObject(names.systemConfigurationTab_staticVersions_3_QFrame), 567, 6, Qt.NoModifier, Qt.LeftButton)

    if test.vp("serivceScreen"):
        test.passes("Successful Confirmation program advances to service mode screen")
    else:
        test.fail("Failed Confirmation program advances to service mode screen") 
    clickButton(waitForObject(names.userProfilesAndPresetsPanel_1_pbUserProfilesClear_QPushButton))

    if test.vp("clearPresetsPopup"):
        test.passes("Successful Confirmation program displays a confirmation popup")
    else:
        test.fail("Failed Confirmation program displays a confirmation popup") 

    clickButton(waitForObject(names.centralWidget_acceptButton_QPushButton))
    clickButton(waitForObject(names.buttonsBar_backButton_QPushButton_4))
    clickTab(waitForObject(names.settingsScreen_tbSystemInfo_TabWidget), "USER\nPRESETS")

    if test.vp("userPresetsSelectedTab"):
        test.passes("Successful Confirmation program displays selection User Presets tab")
    else:
        test.fail("Failed Confirmation program displays selection User Presets tab") 
        
    if test.vp("stoneUserPresets"):
        test.passes("Successful Confirmation program deletes all user profiles and user Stone presets except for default and factory presets")
    else:
        test.fail("Failed Confirmation program deletes all user profiles and user Stone presets except for default and factory presets") 

    mouseClick(waitForObject(names.tabSettingsPresetsUserStonePresets_presetListView_PresetListView), 292, 63, Qt.NoModifier, Qt.LeftButton)
    clickTab(waitForObject(names.wdPresetsLayout_tbPresetsForSettings_TabWidget), "SOFT TISSUE")

    if test.vp("softTissueUserPresets"):
        test.passes("Successful Confirmation program deletes all user profiles and user Soft Tissue presets except for default and factory presets")
    else:
        test.fail("Failed Confirmation program deletes all user profiles and user Soft Tissue presets except for default and factory presets") 

    mouseClick(waitForObject(names.tabSettingsPresetsUserSoftTissuePresets_presetListView_PresetListView), 610, 52, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton_5))

    clickButton(waitForObject(names.homeScreen_profilesButton_QPushButton))
    if test.vp("profileViewScreen"):
        test.passes("Successful Confirmation program deletes all user profiles and user presets except for default and factory presets")
    else:
        test.fail("Failed Confirmation program deletes all user profiles and user presets except for default and factory presets") 
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton_6))
