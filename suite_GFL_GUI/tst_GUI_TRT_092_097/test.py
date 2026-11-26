# -*- coding: utf-8 -*-

import names


def main():
    doubleClick(waitForObject(names.numpad_pushButton_8_NumpadButton), 82, 71, Qt.NoModifier, Qt.LeftButton)
    doubleClick(waitForObject(names.numpad_pushButton_8_NumpadButton), 82, 71, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton))

    clickButton(waitForObject(names.homeScreen_pbSoftTissueQuickStart_QToolButton))
    mouseClick(waitForObjectItem(names.tabLeftMainPresets_leftPresetsView_PresetListView, "_1"), 432, 47, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.tabRightMainPresets_nextPageButton_QPushButton))
    mouseClick(waitForObjectItem(names.tabRightMainPresets_rightPresetsView_PresetListView, "_1"), 319, 61, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.quickStartScreen_pbContinue_QPushButton))
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton_2))

    test.vp("treatmentScreenSoft01", "Successful display of Treatment Screen")

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 273, 24, 118, -5, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopupSoft", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    test.vp("treatmentScreenSoft01", "Successful display of program retain the last set of parameters in quick start mode")
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 183, 18, 70, -1, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopupSoft", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 271, 30, 74, 0, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopupSoft", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_4), 197, 24, 208, -1, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopupSoft", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_5), 73, 20, 130, -4, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopupSoft", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_4), 193, 27, 116, -1, 1, Qt.LeftButton)
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_5), 60, 24, 55, -5, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopupSoft", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 273, 29, 130, -5, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopupSoft", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    
    test.vp("manualModeSoft", "Successful display of program exits quick start mode to manual mode treatment screen.")

    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbSoftTissueAssistant_QToolButton))
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton_3))
    clickButton(waitForObject(names.homeScreen_pbSoftTissueQuickStart_QToolButton))
    mouseClick(waitForObjectItem(names.tabLeftMainPresets_leftPresetsView_PresetListView, "_2"), 443, 37, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.tabRightMainPresets_nextPageButton_QPushButton))
    mouseClick(waitForObjectItem(names.tabRightMainPresets_rightPresetsView_PresetListView, "_2"), 360, 62, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.quickStartScreen_pbContinue_QPushButton))
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton_2))

    test.vp("treatmentScreenSoft02", "Successful display of Treatment Screen")

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 278, 27, 126, -8, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopupSoft", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    test.vp("treatmentScreenSoft02", "Successful display of program retain the last set of parameters in quick start mode")
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 125, 23, 89, -1, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopupSoft", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 268, 34, 76, -7, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopupSoft", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_4), 128, 19, 127, 2, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopupSoft", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_5), 175, 28, 51, -1, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopupSoft", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_5), 179, 20, 113, -6, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopupSoft", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 275, 26, 131, 10, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopupSoft", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    
    test.vp("manualModeSoft", "Successful display of program exits quick start mode to manual mode treatment screen.")
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbSoftTissueQuickStart_QToolButton))
    mouseClick(waitForObjectItem(names.tabLeftMainPresets_leftPresetsView_PresetListView, "_3"), 524, 43, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.tabRightMainPresets_nextPageButton_QPushButton))
    mouseClick(waitForObjectItem(names.tabRightMainPresets_rightPresetsView_PresetListView, "_3"), 399, 67, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.quickStartScreen_pbContinue_QPushButton))
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton_2))

    test.vp("treatmentScreenSoft03", "Successful display of Treatment Screen")

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 333, 24, -255, -10, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopupSoft", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    test.vp("treatmentScreenSoft03", "Successful display of program retain the last set of parameters in quick start mode")
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 136, 28, 188, -3, 1, Qt.LeftButton)
    mouseClick(waitForObject(names.centralWidget_QFrame), 373, 518, Qt.NoModifier, Qt.LeftButton)
    test.vp("exitQuickStartPopupSoft", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 131, 20, 51, 0, 1, Qt.LeftButton)
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 229, 27, 165, 10, 1, Qt.LeftButton)
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 111, 26, -35, -1, 1, Qt.LeftButton)
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 76, 25, 107, -5, 1, Qt.LeftButton)
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 239, 23, -38, 2, 1, Qt.LeftButton)
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 188, 28, -111, -6, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopupSoft", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_4), 123, 32, 118, -13, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopupSoft", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_5), 78, 34, 103, -5, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopupSoft", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_4), 125, 24, 61, 5, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopupSoft", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 199, 20, -79, 1, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopupSoft", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    
    test.vp("manualModeSoft", "Successful display of program exits quick start mode to manual mode treatment screen.")
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbSoftTissueQuickStart_QToolButton))
    mouseClick(waitForObjectItem(names.tabLeftMainPresets_leftPresetsView_PresetListView, "_4"), 527, 49, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.tabRightMainPresets_nextPageButton_QPushButton))
    mouseClick(waitForObjectItem(names.tabRightMainPresets_rightPresetsView_PresetListView, "_3"), 445, 91, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.quickStartScreen_pbContinue_QPushButton))
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton_2))

    test.vp("treatmentScreenSoft04", "Successful display of Treatment Screen")

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_3), 342, 20, -247, -9, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopupSoft", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    test.vp("treatmentScreenSoft04", "Successful display of program retain the last set of parameters in quick start mode")     

    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbSoftTissueQuickStart_QToolButton))
    clickTab(waitForObject(names.wdLeftPedalTreatmentLayout_tbLeftPedalPresets_TabWidget), "USER PRESETS")
    clickTab(waitForObject(names.wdRightPedalTreatmentLayout_tbRightPedalPresets_TabWidget), "USER PRESETS")

    test.vp("noPresets", "Successful display of NO PRESETS in soft tissue Quick start")
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton_4))
    
    #Stone
    # clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneQuickStart_QToolButton))

    clickTab(waitForObject(names.wdLeftPedalTreatmentLayout_tbLeftPedalPresets_TabWidget), "USER PRESETS")
    clickTab(waitForObject(names.wdRightPedalTreatmentLayout_tbRightPedalPresets_TabWidget), "USER PRESETS")

    test.vp("noPresetsStone", "Successful display of NO PRESETS in stone Quick start")

    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton_4))
    clickButton(waitForObject(names.homeScreen_pbStoneQuickStart_QToolButton))
    mouseClick(waitForObjectItem(names.tabLeftMainPresets_leftPresetsView_PresetListView, "_1"), 473, 53, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.tabRightMainPresets_nextPageButton_QPushButton))
    mouseClick(waitForObjectItem(names.tabRightMainPresets_rightPresetsView_PresetListView, "_1"), 418, 46, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.quickStartScreen_pbContinue_QPushButton))
    
    test.vp("treatmentScreen01", "Successful display of Treatment Screen")

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 80, 23, 106, -9, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopup", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    test.vp("treatmentScreen01", "Successful display of program retain the last set of parameters in quick start mode")
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 181, 21, 158, -7, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopup", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 86, 24, 33, 1, 1, Qt.LeftButton)
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 119, 31, 106, -7, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopup", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_4), 162, 23, 215, -4, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopup", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_5), 120, 24, 225, -1, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopup", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_4), 171, 28, 128, -9, 1, Qt.LeftButton)
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_5), 78, 25, 112, -8, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopup", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 116, 32, 115, -4, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopup", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    
    test.vp("manualMode", "Successful display of program exits quick start mode to manual mode treatment screen.")

    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneQuickStart_QToolButton))
    clickButton(waitForObject(names.tabRightMainPresets_nextPageButton_QPushButton))
    mouseClick(waitForObjectItem(names.tabLeftMainPresets_leftPresetsView_PresetListView, "_2"), 579, 62, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.tabRightMainPresets_rightPresetsView_PresetListView, "_2"), 211, 60, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.quickStartScreen_pbContinue_QPushButton))

    test.vp("treatmentScreen02", "Successful display of Treatment Screen")

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 75, 30, 146, -13, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopup", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    test.vp("treatmentScreen02", "Successful display of program retain the last set of parameters in quick start mode")
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 135, 27, 222, -8, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopup", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 79, 22, 31, 3, 1, Qt.LeftButton)
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 114, 28, 115, -10, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopup", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_4), 158, 32, 221, -14, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopup", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_5), 100, 16, 169, -7, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopup", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_4), 171, 23, 131, -3, 1, Qt.LeftButton)
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_5), 68, 29, 124, -5, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopup", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 103, 22, 155, -8, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopup", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    
    test.vp("manualMode", "Successful display of program exits quick start mode to manual mode treatment screen.")
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneQuickStart_QToolButton))
    mouseClick(waitForObjectItem(names.tabLeftMainPresets_leftPresetsView_PresetListView, "_3"), 562, 68, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.tabRightMainPresets_nextPageButton_QPushButton))
    mouseClick(waitForObjectItem(names.tabRightMainPresets_rightPresetsView_PresetListView, "_3"), 401, 62, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.quickStartScreen_pbContinue_QPushButton))

    test.vp("treatmentScreen03", "Successful display of Treatment Screen")

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 119, 21, 159, 0, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopup", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    test.vp("treatmentScreen03", "Successful display of program retain the last set of parameters in quick start mode")
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 170, 17, 133, 6, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopup", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 132, 27, 84, 4, 1, Qt.LeftButton)
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 122, 26, 125, -7, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopup", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_4), 170, 32, 194, -9, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopup", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_5), 71, 28, 196, -3, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopup", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_4), 165, 26, 135, -2, 1, Qt.LeftButton)
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_5), 56, 26, 136, -4, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopup", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 231, 25, 107, -1, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopup", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    
    test.vp("manualMode", "Successful display of program exits quick start mode to manual mode treatment screen.")
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneQuickStart_QToolButton))
    mouseClick(waitForObjectItem(names.tabLeftMainPresets_leftPresetsView_PresetListView, "_4"), 511, 53, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.tabRightMainPresets_nextPageButton_QPushButton))
    mouseClick(waitForObjectItem(names.tabRightMainPresets_rightPresetsView_PresetListView, "_4"), 324, 49, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.quickStartScreen_pbContinue_QPushButton))

    test.vp("treatmentScreen04", "Successful display of Treatment Screen")

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 117, 24, 213, -6, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopup", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    test.vp("treatmentScreen04", "Successful display of program retain the last set of parameters in quick start mode")
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 143, 18, 167, -11, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopup", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 126, 17, 98, 8, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopup", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 129, 25, 97, 5, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopup", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 129, 22, 84, -2, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopup", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_4), 161, 31, 207, -2, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopup", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_5), 81, 21, 84, -11, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopup", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_4), 164, 32, 120, -6, 1, Qt.LeftButton)
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_5), 60, 25, 26, -7, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopup", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 131, 12, 231, 0, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopup", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    
    test.vp("manualMode", "Successful display of program exits quick start mode to manual mode treatment screen.")
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneQuickStart_QToolButton))
    clickButton(waitForObject(names.tabLeftMainPresets_nextPageButton_QPushButton))
    clickButton(waitForObject(names.tabRightMainPresets_nextPageButton_QPushButton))
    clickButton(waitForObject(names.tabLeftMainPresets_nextPageButton_QPushButton))
    clickButton(waitForObject(names.tabRightMainPresets_nextPageButton_QPushButton))
    mouseClick(waitForObjectItem(names.tabLeftMainPresets_leftPresetsView_PresetListView, "_1"), 568, 67, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.tabRightMainPresets_rightPresetsView_PresetListView, "_1"), 158, 62, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.quickStartScreen_pbContinue_QPushButton))
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton_2))

    test.vp("treatmentScreen05", "Successful display of Treatment Screen")

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 161, 20, 228, -4, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopup", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    test.vp("treatmentScreen05", "Successful display of program retain the last set of parameters in quick start mode")
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 52, 23, 191, -2, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopup", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 152, 26, 123, 3, 1, Qt.LeftButton)
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 45, 27, 41, -5, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopup", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 283, 25, 96, -3, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopup", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    
    test.vp("manualMode", "Successful display of program exits quick start mode to manual mode treatment screen.")
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneQuickStart_QToolButton))
    doubleClick(waitForObject(names.tabLeftMainPresets_nextPageButton_QPushButton), 80, 43, Qt.NoModifier, Qt.LeftButton)
    doubleClick(waitForObject(names.tabRightMainPresets_nextPageButton_QPushButton), 75, 37, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.tabLeftMainPresets_leftPresetsView_PresetListView, "_2"), 566, 67, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.tabRightMainPresets_rightPresetsView_PresetListView, "_2"), 175, 26, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.quickStartScreen_pbContinue_QPushButton))
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton_2))

    test.vp("treatmentScreen06", "Successful display of Treatment Screen")

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 79, 24, 182, -3, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopup", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    test.vp("treatmentScreen06", "Successful display of program retain the last set of parameters in quick start mode")
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 83, 12, 83, 5, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopup", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 83, 24, 33, 0, 1, Qt.LeftButton)
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 74, 29, 64, 3, 1, Qt.LeftButton)
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 110, 22, 11, 5, 1, Qt.LeftButton)
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 124, 22, 16, -1, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopup", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 113, 23, 121, 13, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopup", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    
    test.vp("manualMode", "Successful display of program exits quick start mode to manual mode treatment screen.")
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneQuickStart_QToolButton))
    doubleClick(waitForObject(names.tabLeftMainPresets_nextPageButton_QPushButton), 58, 34, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.tabLeftMainPresets_leftPresetsView_PresetListView, "_3"), 466, 69, Qt.NoModifier, Qt.LeftButton)
    doubleClick(waitForObject(names.tabRightMainPresets_nextPageButton_QPushButton), 33, 36, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.tabRightMainPresets_nextPageButton_QPushButton))
    mouseClick(waitForObjectItem(names.tabRightMainPresets_rightPresetsView_PresetListView, "_3"), 364, 73, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.quickStartScreen_pbContinue_QPushButton))
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton_2))

    test.vp("treatmentScreen07", "Successful display of Treatment Screen")

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 72, 20, 185, 0, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopup", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    test.vp("treatmentScreen07", "Successful display of program retain the last set of parameters in quick start mode")
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 74, 29, 95, 3, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopup", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 87, 36, 33, -10, 1, Qt.LeftButton)
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 42, 32, 87, 1, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopup", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 132, 24, 125, 3, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopup", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    
    test.vp("manualMode", "Successful display of program exits quick start mode to manual mode treatment screen.")
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneQuickStart_QToolButton))
    doubleClick(waitForObject(names.tabLeftMainPresets_nextPageButton_QPushButton), 48, 43, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.tabLeftMainPresets_nextPageButton_QPushButton))
    mouseClick(waitForObjectItem(names.tabLeftMainPresets_leftPresetsView_PresetListView, "_4"), 487, 49, Qt.NoModifier, Qt.LeftButton)
    doubleClick(waitForObject(names.tabRightMainPresets_nextPageButton_QPushButton), 45, 26, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.tabRightMainPresets_nextPageButton_QPushButton))
    mouseClick(waitForObjectItem(names.tabRightMainPresets_rightPresetsView_PresetListView, "_4"), 467, 54, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.quickStartScreen_pbContinue_QPushButton))
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton_2))

    test.vp("treatmentScreen08", "Successful display of Treatment Screen")

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 324, 27, 79, -3, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopup", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    test.vp("treatmentScreen08", "Successful display of program retain the last set of parameters in quick start mode")
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 129, 16, 171, 2, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopup", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 327, 28, 28, -4, 1, Qt.LeftButton)
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 109, 21, 123, -1, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopup", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 357, 28, 46, -1, 1, Qt.LeftButton)
    test.vp("exitQuickStartPopup", "Successful display of Exit QuickStart Popup")
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    
    test.vp("manualMode", "Successful display of program exits quick start mode to manual mode treatment screen.")
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
