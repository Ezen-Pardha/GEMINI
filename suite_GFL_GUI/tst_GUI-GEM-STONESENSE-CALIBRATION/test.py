# -*- coding: utf-8 -*-

import names

def main():
     
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton))
    
# SVV TAG GUI-TRT-066

    test.log("Stone")
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
    
# SVV TAG GUI-TRT-067

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
        
# SVV  TAG GUI-TRT-068

    test.log("Soft tissue")
    mouseClick(waitForObject(names.pInitiateCalibrationFrame_frame_QFrame), 918, 194, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.frame_pCancelButton_QPushButton))
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbSoftTissueAssistant_QToolButton))
    clickButton(waitForObject(names.gbSoftTissueProcedures_pbIncision_QPushButton))
    mouseDrag(waitForObject(names.softTissueAssistantModeScreen_wdTabWidgets_QWidget), 1279, 342, -18, -92, 1, Qt.LeftButton) 
    clickButton(waitForObject(names.softTissueAssistantModeScreen_pbContinue_QPushButton)) 
    test.log("Guide mode Treatment screen verified")
    
    if object.exists(names.stoneSenseFrame_pbStoneSense_QPushButton):
        test.fail("StoneSense button is available on the Quick start mode Treatment Screen")
       
    else:
        test.passes("StoneSense button is not available on the Treatment Screen")
        
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbSoftTissueQuickStart_QToolButton))
    doubleClick(waitForObjectItem(names.tabLeftMainPresets_leftPresetsView_PresetListView, "_1"), 295, 70, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.tabRightMainPresets_rightPresetsView_PresetListView, "_1"), 110, 40, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.quickStartScreen_pbContinue_QPushButton))
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton_2))
    doubleClick(waitForObject(names.pulseModeWidget_frequencyWidget_ParameterSettingsWidget), 4, 107, Qt.NoModifier, Qt.LeftButton)
    test.log("Quick Start mode Treatment screen verified")
    
    if object.exists(names.stoneSenseFrame_pbStoneSense_QPushButton):
        
        test.fail("StoneSense button is available on the Quick start mode Treatment Screen")
    else:
        
        test.passes("StoneSense button is not available on the Treatment Screen")
        
    test.log("manual")    
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.gbExpert_expertButton_QPushButton))
    test.log("Manual Treatment screen verified")
    snooze(5)
    
    if object.exists(names.stoneSenseFrame_pbStoneSense_QPushButton):
        test.fail("StoneSense button is available in Treatment screen")
        
    else:
        test.passes("manual screen StoneSense button is not available")
        
 # SVV  TAG GUI-TRT-071     
   
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
    test.log("Stone Guided Treatment screen verified")
    if test.imagePresent("Stone Sense Disable"):
        
        test.passes("Stone Sense Disable")
    else:
        test.fail("Stone Sense Disable image is not present on the Treatment Screen")
        
# SVV  TAG GUI-TRT-072

    mouseClick(waitForObject(names.pulseModeWidget_buttonsWidget_QWidget), 143, 2, Qt.NoModifier, Qt.LeftButton)
    test.log("Stone Guided Treatment screen verified")
    clickButton(waitForObject(names.stoneSenseFrame_pbStoneSense_QPushButton))
    clickButton(waitForObject(names.calibrationPopupDialog_pbMiddleButton_QPushButton))
    clickButton(waitForObject(names.pCalibrationSuccessFrame_pOKButton_QPushButton))
    test.log("Calibration Procedure is completed")
    if test.imagePresent("Stone sense active"):
        
        test.passes("Stone Sense button Enabled")
    else:
        test.fail("Stone Sense enabled image is not present on the Treatment Screen")
        
# SVV  TAG GUI-TRT-073

    clickButton(waitForObject(names.stoneSenseFrame_pbStoneSense_QPushButton))
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    clickButton(waitForObject(names.stoneSenseFrame_pbStoneSense_QPushButton))
    setWindowState(waitForObject(names.o_ScreenSwitcher, 31945), WindowState.Minimize)
    snooze(6)
    
    if test.imagePresent("Stone Sense Popup"):
        
        test.passes("Stone Sense popup is populated")   
    else:
        test.fail("Stone Sense popup is not populated")
    
# SVV  TAG GUI-TRT-074
        
    setWindowState(waitForObject(names.o_ScreenSwitcher), WindowState.Normal)
    clickButton(waitForObject(names.frame_pCancelButton_QPushButton))
    test.log("Stone Guided Treatment screen verified")
    clickButton(waitForObject(names.stoneSenseFrame_pbStoneSense_QPushButton))
    if test.imagePresent("Stone Sense Popup"):
        test.passes("Stone Sense popup is populated")   
    else:
        test.fail("Stone Sense popup is not populated")
    
    clickButton(waitForObject(names.calibrationPopupDialog_pbMiddleButton_QPushButton))
    clickButton(waitForObject(names.pCalibrationSuccessFrame_pOKButton_QPushButton))
    mouseClick(waitForObject(names.treatmentScreen_leftPedalWidgetBorder_QWidget), 630, 36, Qt.NoModifier, Qt.LeftButton)
    if test.imagePresent("Stone sense active"):
        
        test.passes("Stone Sense Enabled")
    else:
        test.fail("Stone Sense enabled image is not present on the Treatment Screen")
    clickButton(waitForObject(names.stoneSenseFrame_pbStoneSense_QPushButton)) 
    
    if test.imagePresent("Disable Stone Sense"):
        
        test.passes("Stone Disabled conform Popup is populated")
    else:
        test.fail("Stone Disabled conform Popup is not populated")
        
#  SVV TAG GUI-TRT-075


    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    mouseClick(waitForObject(names.treatmentScreen_StoneSenseFrame_StoneSenseFrame), 168, 97, Qt.NoModifier, Qt.LeftButton)
    test.passes("Stone Guided Treatment screen verified")
    clickButton(waitForObject(names.stoneSenseFrame_pbStoneSense_QPushButton))
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton)) 
    mouseClick(waitForObject(names.pulseModeWidget_frequencyWidget_ParameterSettingsWidget_2, 86860), 623, 63, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.stoneSenseFrame_pbStoneSense_QPushButton))
    if test.imagePresent("Stone Sense Popup"):
        test.passes("Stone Sense popup is populated")   
    else:
        test.fail("Stone Sense popup is not populated")
    clickButton(waitForObject(names.calibrationPopupDialog_pbMiddleButton_QPushButton))
    clickButton(waitForObject(names.pCalibrationSuccessFrame_pOKButton_QPushButton))
    test.log("Calibration Procedure is completed")
    if test.imagePresent("Stone sense active"):
        
        test.passes("Stone Sense Enabled")
    else:
        test.fail("Stone Sense enabled image is not present on the Treatment Screen")
    clickButton(waitForObject(names.stoneSenseFrame_pbStoneSense_QPushButton))
    mouseClick(waitForObject(names.centralWidget_TitleLabel_QLabel), 200, 88, Qt.NoModifier, Qt.LeftButton)
    test.compare(str(waitForObjectExists(names.centralWidget_DisableButton_QPushButton).text), "DISABLE")
    if test.imagePresent("Disable Stone Sense"):
        
        test.passes("Stone Disabled conform Popup is populated")
    else:
        test.fail("Stone Disabled conform Popup is not populated")
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    if test.imagePresent("Stone Sense Disable"):
        
        test.passes("Stone Sense Button is Disable")
    else:
        test.fail("Stone Sense Button Disable image is not present on the Treatment Screen")
        
#  SVV TAG GUI-TRT-076


    mouseClick(waitForObject(names.leftPedalWidget_wdPresetTabs_TabWidget), 420, 40, Qt.NoModifier, Qt.LeftButton)
    test.passes("Stone Guided Treatment screen verified")
    clickButton(waitForObject(names.stoneSenseFrame_pbStoneSense_QPushButton))
    if test.imagePresent("Stone Sense Popup"):
        test.passes("Stone Sense popup is populated")   
    else:
        test.fail("Stone Sense popup is not populated")
    clickButton(waitForObject(names.calibrationPopupDialog_pbMiddleButton_QPushButton, 116640))
    clickButton(waitForObject(names.pCalibrationSuccessFrame_pOKButton_QPushButton, 187780))
    test.log("Calibration Procedure is completed")
    if test.imagePresent("Stone sense active"):
        
        test.passes("Stone Sense Enabled")
    else:
        test.fail("Stone Sense enabled image is not present on the Treatment Screen")
    clickButton(waitForObject(names.stoneSenseFrame_pbStoneSense_QPushButton))
    if test.imagePresent("Disable Stone Sense"):
        
        test.passes("Stone Disabled conform Popup is populated")
    else:
        test.fail("Stone Disabled conform Popup is not populated")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    test.passes("Stone Sense Disable confirmation is cancelled")
    mouseClick(waitForObject(names.treatmentScreen_leftPedalWidgetBorder_QWidget), 631, 406, Qt.NoModifier, Qt.LeftButton)

   
    
   
    
    

    
    
    
    
    
    
    
    
    

    
    
    
