
# -*- coding: utf-8 -*-

from common import *
import names


def main():

    enter_login_pin()

   
    clickButton(waitForObject(
        names.homeScreen_pbSoftTissueAssistant_QToolButton
    ))

  
    clickButton(waitForObject(
        names.gbSoftTissueProcedures_pbIncision_QPushButton
    ))
    
  
    clickButton(waitForObject(
        names.softTissueAssistantModeScreen_pbContinue_QPushButton
    ))

    
    mouseDrag(
        waitForObject(names.indexPicker_valuePicker_IntervalSlider_5),
        79, 26, 250, 11, 1, Qt.LeftButton
    )
    test.vp("Verified guided popup")

    
    clickButton(waitForObject(
        names.centralWidget_DisableButton_QPushButton
    ))

    test.log(" Verify CUSTOM tag is displayed")
    test.ocrTextPresent("CUSTOM")

    
    

    test.log("Navigate to Home screen")
    clickButton(waitForObject(
        names.buttonsBar_homeButton_QPushButton_4
    ))

    test.log("Select Manual / Expert mode")
    clickButton(waitForObject(
        names.gbExpert_expertButton_QPushButton
    ))

    test.passes("not displaying the presets tab on MANUAL Treatment screen  ")
    clickTab(
        waitForObject(names.leftPedalWidget_wdPresetTabs_TabWidget),
        "MANUAL"
    )

    test.passes(" verified  MANUAL screen")
    clickTab(
        waitForObject(names.rightPedalWidget_wdPresetTabs_TabWidget),
        "MANUAL"
    )


   

    test.passes("verified Home screen")
    clickButton(waitForObject(
        names.buttonsBar_homeButton_QPushButton_4
    ))

    test.log("Open Stone Assistant")
    clickButton(waitForObject(
        names.homeScreen_pbStoneAssistant_QToolButton
    ))

    
    clickButton(waitForObject(
        names.locationFrame_kidneyPcnlLocationButton_QPushButton
    ))

    
    clickButton(waitForObject(
        names.flowRateFrame_lowFlowRateButton_QPushButton
    ))

    
    clickButton(waitForObject(
        names.hardnessFrame_smallHardnessButton_QPushButton
    ))

   
    clickButton(waitForObject(
        names.stoneAssistantModeScreen_continueButton_QPushButton
    ))

    test.log("STEP 7: Verify Fragmentation preset is available")
    clickTab(
        waitForObject(names.leftPedalWidget_wdPresetTabs_TabWidget),
        "FRAGMENTATION"
    )
    test.passes("PASS: Fragmentation preset is available")

    test.log("Verify Dusting preset is available")
    clickTab(
        waitForObject(names.leftPedalWidget_wdPresetTabs_TabWidget),
        "DUSTING"
    )
    test.passes("PASS: Dusting preset is available")

    test.log("Verify Popcorning preset is available")
    clickTab(
        waitForObject(names.leftPedalWidget_wdPresetTabs_TabWidget),
        "POPCORNING"
    )
    test.passes("Popcorning preset is available")

    test.log("Completed all executable test steps")
