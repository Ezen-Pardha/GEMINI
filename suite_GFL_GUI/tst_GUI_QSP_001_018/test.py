# -*- coding: utf-8 -*-

import names


def main():
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    doubleClick(waitForObject(names.numpad_pushButton_8_NumpadButton), 82, 48, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton))
    
    #stone
    clickButton(waitForObject(names.homeScreen_pbStoneQuickStart_QToolButton))

    if test.vp("stoneQuickStartModePreset"):
        test.passes("Successful Confirmation program displays Stone Quick Start mode preset screen")
    else:
        test.fail("Failed Confirmation program displays Stone Quick Start mode preset screen")
    
    if test.vp("disabledContinue"):
        test.passes("Successful Confirmation program displays Continue button when no preset is selected")
    else:
        test.fail("Failed Confirmation program displays Continue button when no preset is selected")

    if test.vp("disabledContinue"):
        test.passes("Successful Confirmation program displays Continue button Disabled when no preset is selected")
    else:
        test.fail("Failed Confirmation program displays Continue button Disabled when no preset is selected")

    if test.vp("profileWidget"):
        test.passes("Successful Confirmation program displays the Active Profile in top banner")
    else:
        test.fail("Failed Confirmation program displays the Active Profile in top banner")
        
    if test.vp("stoneQuickStartModePreset"):
        test.passes("Successful Confirmation program displays the preset name on the buttons") 
    else:
        test.fail("Failed Confirmation program displays the preset name on the buttons")
        
    if test.vp("stoneQuickStartModePreset"):
        test.passes("Successful Confirmation program displays the laser parameters for the preset on the button") 
    else:
        test.fail("Failed Confirmation program displays the laser parameters for the preset on the button")

    if test.vp("pageNavigationButtons"):
        test.passes("Successful Confirmation program displays the page navigation buttons")
        test.passes("Successful Confirmation program displays the page numbers")
    else:
        test.fail("Failed Confirmation program displays the page navigation buttons")
        test.fail("Failed Confirmation program displays the page numbers")

    clickButton(waitForObject(names.tabLeftMainPresets_nextPageButton_QPushButton))
    
    if test.vp("nextPageNavigation"):
        test.passes("Successful Confirmation program goes to next page")
    else:
        test.fail("Failed Confirmation program goes to next page")        
    clickButton(waitForObject(names.tabLeftMainPresets_backPageButton_QPushButton))
    
    if test.vp("pageNavigationButtons"):
        test.passes("Successful Confirmation program goes back to the previous page")
    else:
        test.fail("Failed Confirmation program goes back to the previous page")  

    if test.vp("factoryPresetsTabStone"):
        test.passes("Successful Confirmation program displays Factory presets tab")
    else:
        test.fail("Failed Confirmation program displays Factory presets tab")
        
    if test.vp("userPresetsTabStone"):
        test.passes("Successful Confirmation program displays User presets tab")
    else:
        test.fail("Failed Confirmation program displays User presets tab")

    mouseClick(waitForObjectItem(names.tabLeftMainPresets_leftPresetsView_PresetListView, "_1"), 466, 29, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.tabRightMainPresets_rightPresetsView_PresetListView, "_2"), 299, 74, Qt.NoModifier, Qt.LeftButton)

    if test.vp("enabledContinueStone"):
        test.passes("Successful Confirmation program displays and enables Continue button")
    else:
        test.fail("Failed Confirmation program displays and enables Continue button")
    
    if test.vp("enabledContinueStone"):
        test.passes("Successful Confirmation program displays Continue button selection as Yellow")
    else:
        test.fail("Failed Confirmation program displays Continue button selection as Yellow")

    if test.vp("selectStoneQuickStart"):
        test.passes("Successful Confirmation program allows selection of presets for left and right pedals")
    else:
        test.fail("Failed Confirmation program allows selection of presets for left and right pedals")

    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton_4))
    
    if test.vp("homeScreen"):
        test.passes("Successful Confirmation program navigates to Home screen")
    else:
        test.fail("Failed Confirmation program navigates to Home screen")
        
    #Soft Tissue
    clickButton(waitForObject(names.homeScreen_pbSoftTissueQuickStart_QToolButton))

    if test.vp("softTissueQuickStartModePreset"):
        test.passes("Successful Confirmation program displays Soft Tissue Quick Start mode preset screen")
    else:
        test.fail("Failed Confirmation program displays Soft Tissue Quick Start mode preset screen")
        
    if test.vp("disabledContinueSoftTissue"):
        test.passes("Successful Confirmation program displays Continue button when no preset is selected")
    else:
        test.fail("Failed Confirmation program displays Continue button when no preset is selected")

    if test.vp("disabledContinueSoftTissue"):
        test.passes("Successful Confirmation program displays Continue button Disabled when no preset is selected")
    else:
        test.fail("Failed Confirmation program displays Continue button Disabled when no preset is selected")
        
    if test.vp("profileWidget"):
        test.passes("Successful Confirmation program displays the Active Profile in top banner")
    else:
        test.fail("Failed Confirmation program displays the Active Profile in top banner")
        
    if test.vp("softTissueQuickStartModePreset"):
        test.passes("Successful Confirmation program displays displays the preset name on the buttons")
    else:
        test.fail("Failed Confirmation program displays displays the preset name on the buttons")
     
    if test.vp("softTissueQuickStartModePreset"):
        test.passes("Successful Confirmation program displays the laser parameters for the preset on the button")
    else:
        test.fail("Failed Confirmation program displays the laser parameters for the preset on the button")

    if test.vp("pageNavigationButtonsSoftTissue"):
        test.passes("Successful Confirmation program displays the page navigation buttons")
        test.passes("Successful Confirmation program displays the page numbers")
    else:
        test.fail("Failed Confirmation program displays the page navigation buttons")
        test.fail("Failed Confirmation program displays the page numbers")
                
    clickButton(waitForObject(names.tabLeftMainPresets_nextPageButton_QPushButton))
    
    if test.vp("nextPageNavigationSoftTissue"):
        test.passes("Successful Confirmation program goes to next page")
    else:
        test.fail("Failed Confirmation program goes to next page") 
    clickButton(waitForObject(names.tabLeftMainPresets_backPageButton_QPushButton))
    
    if test.vp("pageNavigationButtonsSoftTissue"):
        test.passes("Successful Confirmation program goes back to the previous page")
    else:
        test.fail("Failed Confirmation program goes back to the previous page")

    if test.vp("factoryPresetsTabSoftTissue"):
        test.passes("Successful Confirmation program displays Factory presets tab")
    else:
        test.fail("Failed Confirmation program displays Factory presets tab")
    
    if test.vp("userPresetsTabSoftTissue"):
        test.passes("Successful Confirmation program displays User presets tab")
    else:
        test.fail("Failed Confirmation program displays User presets tab")

    mouseClick(waitForObjectItem(names.tabLeftMainPresets_leftPresetsView_PresetListView, "_1"), 453, 39, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.tabRightMainPresets_rightPresetsView_PresetListView, "_3"), 249, 42, Qt.NoModifier, Qt.LeftButton)

    if test.vp("enabledContinueSoftTissue"):
        test.passes("Successful Confirmation program displays and enables Continue button")
    else:
        test.fail("Failed Confirmation program displays and enables Continue button")
        
    if test.vp("enabledContinueSoftTissue"):
        test.passes("Successful Confirmation program displays Continue button selection as Blue")
    else:
        test.fail("Failed Confirmation program displaysContinue button selection as Blue")

    if test.vp("selectSoftTissueQuickStart"):
        test.passes("Successful Confirmation program allows selection of presets for left and right pedals")
    else:
        test.fail("Failed Confirmation program allows selection of presets for left and right pedals")

    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton_4))
    
    if test.vp("homeScreen"):
        test.passes("Successful Confirmation program navigates to Home screen")
    else:
        test.fail("Failed Confirmation program navigates to Home screen")
    
    clickButton(waitForObject(names.homeScreen_pbStoneQuickStart_QToolButton))
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton_4))
    
    clickButton(waitForObject(names.homeScreen_pbSoftTissueQuickStart_QToolButton))
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton_4))

    clickButton(waitForObject(names.homeScreen_pbSoftTissueQuickStart_QToolButton))
    mouseClick(waitForObjectItem(names.tabLeftMainPresets_leftPresetsView_PresetListView, "_1"), 429, 40, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.tabRightMainPresets_rightPresetsView_PresetListView, "_2"), 153, 28, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.quickStartScreen_pbContinue_QPushButton))
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton_2))

    if test.vp("leftPedalSoftTissue"):
        test.passes("Successful Confirmation program navigates with presets loaded onto treatment screen LEFT PEDAL")
    else:
        test.fail("Failed Confirmation program navigates with presets loaded onto treatment screen LEFT PEDAL")
        
    if test.vp("rightPedalSoftTissue"):
        test.passes("Successful Confirmation program navigates with presets loaded onto treatment screen RIGHT PEDAL")
    else:
        test.fail("Failed Confirmation program navigates with presets loaded onto treatment screen RIGHT PEDAL")

    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    
    clickButton(waitForObject(names.homeScreen_pbStoneQuickStart_QToolButton))
    mouseClick(waitForObjectItem(names.tabLeftMainPresets_leftPresetsView_PresetListView, "_1"), 481, 76, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.tabRightMainPresets_rightPresetsView_PresetListView, "_2"), 230, 72, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.quickStartScreen_pbContinue_QPushButton))

    if test.vp("leftPedalStone"):
        test.passes("Successful Confirmation program navigates with presets loaded onto treatment screen LEFT PEDAL")
    else:
        test.fail("Failed Confirmation program navigates with presets loaded onto treatment screen LEFT PEDAL")
        
    if test.vp("rightPedalStone"):
        test.passes("Successful Confirmation program navigates with presets loaded onto treatment screen RIGHT PEDAL")
    else:
        test.fail("Failed Confirmation program navigates with presets loaded onto treatment screen RIGHT PEDAL")

    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
        
    clickButton(waitForObject(names.homeScreen_pbSoftTissueQuickStart_QToolButton))
    
    if test.vp("userPresetsTabSoftTissue"):
        test.passes("Successful Confirmation program displays User presets tab")
    else:
        test.fail("Failed Confirmation program displays User presets tab")
        
    clickTab(waitForObject(names.wdLeftPedalTreatmentLayout_tbLeftPedalPresets_TabWidget), "USER PRESETS")
    clickTab(waitForObject(names.wdRightPedalTreatmentLayout_tbRightPedalPresets_TabWidget), "USER PRESETS")
    mouseClick(waitForObjectItem(names.tabLeftUserPresets_leftUserPresetsView_PresetListView, "_1"), 339, 29, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.tabRightUserPresetsLayout_rightUserPresetsView_PresetListView, "_2"), 295, 28, Qt.NoModifier, Qt.LeftButton)

    if test.vp("selectionUserPresetsSoftTissue"):
        test.passes("Successful Confirmation program allows selection of presets for left and right pedals")
    else:
        test.fail("Failed Confirmation program allows selection of presets for left and right pedals")       

    clickButton(waitForObject(names.quickStartScreen_pbContinue_QPushButton))
    
    if test.vp("userPresetsLoaded"):
        test.passes("Successful Confirmation program navigates with presets loaded onto treatment screen")
    else:
        test.fail("Failed Confirmation program navigates with presets loaded onto treatment screen")

    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneQuickStart_QToolButton))
    
    if test.vp("userPresetsTabStone"):
        test.passes("Successful Confirmation program displays User presets tab")
    else:
        test.fail("Failed Confirmation program displays User presets tab")
        
    clickTab(waitForObject(names.wdLeftPedalTreatmentLayout_tbLeftPedalPresets_TabWidget), "USER PRESETS")
    clickTab(waitForObject(names.wdRightPedalTreatmentLayout_tbRightPedalPresets_TabWidget), "USER PRESETS")
    mouseClick(waitForObjectItem(names.tabLeftUserPresets_leftUserPresetsView_PresetListView, "_1"), 419, 32, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.tabRightUserPresetsLayout_rightUserPresetsView_PresetListView, "_2"), 191, 24, Qt.NoModifier, Qt.LeftButton)

    if test.vp("selectionUserPresetsStone"):
        test.passes("Successful Confirmation program allows selection of presets for left and right pedals")
    else:
        test.fail("Failed Confirmation program allows selection of presets for left and right pedals") 

    clickButton(waitForObject(names.quickStartScreen_pbContinue_QPushButton))

    if test.vp("userPresetsLoadedStone"):
        test.passes("Successful Confirmation program navigates with presets loaded onto treatment screen")
    else:
        test.fail("Failed Confirmation program navigates with presets loaded onto treatment screen")

    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))

    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton_4))
