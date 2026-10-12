# -*- coding: utf-8 -*-

import names

def main():
    
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton))
    
    clickButton(waitForObject(names.homeScreen_pbStoneQuickStart_QToolButton))
    mouseClick(waitForObjectItem(names.tabLeftMainPresets_leftPresetsView_PresetListView, "_1"), 320, 35, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.tabRightMainPresets_rightPresetsView_PresetListView, "_1"), 111, 43, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.quickStartScreen_pbContinue_QPushButton))
    test.log("Quick start mode Treatment screen verified")
    
    if object.exists(names.stoneSenseFrame_pbStoneSense_QPushButton):
        
        test.passes("StoneSense button is available on the Quick start mode (Treatment Screen)")
    else:
        test.fail("StoneSense button is not available on the Treatment Screen")
     
    clickButton(waitForObject(names.stoneSenseFrame_pbStoneSense_QPushButton))
    clickButton(waitForObject(names.frame_pCancelButton_QPushButton))

    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    clickButton(waitForObject(names.locationFrame_kidneyPcnlLocationButton_QPushButton))
    clickButton(waitForObject(names.flowRateFrame_lowFlowRateButton_QPushButton))
    clickButton(waitForObject(names.hardnessFrame_smallHardnessButton_QPushButton))
    clickButton(waitForObject(names.stoneAssistantModeScreen_continueButton_QPushButton))
    test.log("Quick start mode Treatment screen verified")
    clickButton(waitForObject(names.stoneSenseFrame_pbStoneSense_QPushButton))
    if object.exists(names.stoneSenseFrame_pbStoneSense_QPushButton):
        
        test.passes("StoneSense button is available on the on the Guided Mode (Treatment Screen)")
    else:
        test.fail("StoneSense button is not available on the Guided Mode Treatment Screen")

    mouseClick(waitForObject(names.frame_emissionTextIcon_QLabel), 510, 118, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.frame_pCancelButton_QPushButton))
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.gbExpert_expertButton_QPushButton))
    test.log("Manual Treatment screen verified")
    snooze(5)
    if object.exists(names.stoneSenseFrame_pbStoneSense_QPushButton):
        test.fail("StoneSense button is available in Treatment screen")
        
    else:
        test.passes("manual screen StoneSense button is not available")
        
    mouseClick(waitForObject(names.rightPedalWidget_wdPresetTabs_TabWidget), 103, 38, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneQuickStart_QToolButton))
    mouseClick(waitForObjectItem(names.tabLeftMainPresets_leftPresetsView_PresetListView, "_1"), 537, 73, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.tabRightMainPresets_rightPresetsView_PresetListView, "_1"), 309, 66, Qt.NoModifier, Qt.LeftButton)

    clickButton(waitForObject(names.quickStartScreen_pbContinue_QPushButton))
    clickButton(waitForObject(names.stoneSenseFrame_pbStoneSense_QPushButton, 30933))
    clickButton(waitForObject(names.calibrationPopupDialog_pbMiddleButton_QPushButton))
    clickButton(waitForObject(names.pCalibrationSuccessFrame_pOKButton_QPushButton))
    clickButton(waitForObject(names.stoneSenseFrame_pbStoneSense_QPushButton, 31194))
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    if test.imagePresent("Stone Sense Disable"):
        
        test.passes("Stone Sense Disable")
    else:
        test.fail("Stone Sense Disable image is not present on the Treatment Screen")
    
    
    
    
    
    
    

    
    
    
