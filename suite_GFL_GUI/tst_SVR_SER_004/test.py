# -*- coding: utf-8 -*-

from common import *

def main():
    
    navigate_service_mode()
    clickButton(waitForObject(names.userProfilesAndPresetsPanel_1_pbUserProfilesClear_QPushButton))

    mouseClick(waitForObject(names.centralWidget_lbDialogTitle_QLabel_2), 241, 28, Qt.NoModifier, Qt.LeftButton)
    label_obj = waitForObject(names.centralWidget_lbDialogTitle_QLabel_2)
    label_txt = str(label_obj.text)
    test.log("Popup title: " + label_txt)
       
    snooze(2)

    test.compare(str(waitForObjectExists(names.centralWidget_lbDialogTitle_QLabel_2).text), "Clear User Profiles and Presets")
    test.vp("popup")

    #test.breakpoint()
    #test.vp("Verifying clear all user presets popup")
    snooze(2)
    clickButton(waitForObject(names.buttonsFrame_acceptButton_QPushButton_2))
    clickButton(waitForObject(names.buttonsBar_backButton_QPushButton_4))
    clickTab(waitForObject(names.settingsScreen_tbSystemInfo_TabWidget), "USER\nPRESETS")
    test.log("Confirming  presets cleared in User stone presets tab")
    clickTab(waitForObject(names.wdPresetsLayout_tbPresetsForSettings_TabWidget), "STONE")
    test.vp("Verifying user stone presets")
    clickTab(waitForObject(names.wdPresetsLayout_tbPresetsForSettings_TabWidget), "SOFT TISSUE")
    test.log("Confirming  presets cleared in User soft tissue presets tab")
    test.vp("Verfiying user soft tissue presets")
