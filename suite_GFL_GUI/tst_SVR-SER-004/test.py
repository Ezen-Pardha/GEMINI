# -*- coding: utf-8 -*-

from common import *

def main():
    navigate_service_mode()
    clickButton(waitForObject(names.userProfilesAndPresetsPanel_1_pbUserProfilesClear_QPushButton))
    test.vp("Verifying clear all user presets popup")
    clickButton(waitForObject(names.buttonsFrame_acceptButton_QPushButton_2))
    clickButton(waitForObject(names.buttonsBar_backButton_QPushButton))
    clickTab(waitForObject(names.settingsScreen_tbSystemInfo_TabWidget), "USER\nPRESETS")
    test.log("Confirming  presets cleared in User stone presets tab")
    clickTab(waitForObject(names.wdPresetsLayout_tbPresetsForSettings_TabWidget), "STONE")
    test.vp("Verifying user stone presets")
    clickTab(waitForObject(names.wdPresetsLayout_tbPresetsForSettings_TabWidget), "SOFT TISSUE")
    test.log("Confirming  presets cleared in User soft tissue presets tab")
    test.vp("Verfiying user soft tissue presets")