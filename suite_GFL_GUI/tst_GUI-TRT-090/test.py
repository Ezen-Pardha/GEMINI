# -*- coding: utf-8 -*-

import names

def selectParameters(locationButton, flowButton, hardnessButton):
    clickButton(waitForObject(locationButton))
    clickButton(waitForObject(flowButton))
    clickButton(waitForObject(hardnessButton))
    clickButton(waitForObject(names.stoneAssistantModeScreen_continueButton_QPushButton))

def main():
    doubleClick(waitForObject(names.numpad_pushButton_8_NumpadButton), 65, 45, Qt.NoModifier, Qt.LeftButton)
    doubleClick(waitForObject(names.numpad_pushButton_8_NumpadButton), 65, 45, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton))    
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selectParameters(
        names.locationFrame_kidneyPcnlLocationButton_QPushButton,        
        names.flowRateFrame_lowFlowRateButton_QPushButton,        
        names.hardnessFrame_smallHardnessButton_QPushButton)
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 125, 24, 257, -7, 1, Qt.LeftButton)
    test.vp("exitGuidedPopup", "Successful display of Exit Guided Mode popup")
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))    

    test.vp("manualMode", "Successful display of program exits guided mode to manual mode treatment screen")

    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selectParameters(
        names.locationFrame_kidneyPcnlLocationButton_QPushButton,
        names.flowRateFrame_lowFlowRateButton_QPushButton,
        names.hardnessFrame_mediumHardnessButton_QPushButton)
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 156, 19, 236, 0, 1, Qt.LeftButton)
    test.vp("exitGuidedPopup", "Successful display of Exit Guided Mode popup")
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))    
    test.vp("manualMode", "Successful display of program exits guided mode to manual mode treatment screen")
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selectParameters(
        names.locationFrame_kidneyPcnlLocationButton_QPushButton,
        names.flowRateFrame_lowFlowRateButton_QPushButton,
        names.hardnessFrame_largeHardnessButton_QPushButton)   
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 199, 31, 170, 2, 1, Qt.LeftButton)
    test.vp("exitGuidedPopup", "Successful display of Exit Guided Mode popup")
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))   
    test.vp("manualMode", "Successful display of program exits guided mode to manual mode treatment screen")
     
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selectParameters(
        names.locationFrame_kidneyPcnlLocationButton_QPushButton,
        names.flowRateFrame_lowFlowRateButton_QPushButton,
        names.hardnessFrame_unknownHardnessButton_QPushButton)
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 167, 22, 231, 14, 1, Qt.LeftButton)
    test.vp("exitGuidedPopup", "Successful display of Exit Guided Mode popup")
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))    
    test.vp("manualMode", "Successful display of program exits guided mode to manual mode treatment screen")
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selectParameters(
        names.locationFrame_kidneyPcnlLocationButton_QPushButton,
        names.flowRateFrame_mediumFlowRateButton_QPushButton,
        names.hardnessFrame_smallHardnessButton_QPushButton
    )
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 135, 27, 268, -4, 1, Qt.LeftButton)
    test.vp("exitGuidedPopup", "Successful display of Exit Guided Mode popup")
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    test.vp("manualMode", "Successful display of program exits guided mode to manual mode treatment screen")
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selectParameters(
        names.locationFrame_kidneyPcnlLocationButton_QPushButton,
        names.flowRateFrame_mediumFlowRateButton_QPushButton,
        names.hardnessFrame_mediumHardnessButton_QPushButton
    )
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 159, 24, 226, -10, 1, Qt.LeftButton)
    test.vp("exitGuidedPopup", "Successful display of Exit Guided Mode popup")
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    test.vp("manualMode", "Successful display of program exits guided mode to manual mode treatment screen")
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selectParameters(
        names.locationFrame_kidneyPcnlLocationButton_QPushButton,
        names.flowRateFrame_mediumFlowRateButton_QPushButton,
        names.hardnessFrame_largeHardnessButton_QPushButton
    )
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 191, 22, 208, 10, 1, Qt.LeftButton)
    test.vp("exitGuidedPopup", "Successful display of Exit Guided Mode popup")
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    test.vp("manualMode", "Successful display of program exits guided mode to manual mode treatment screen")
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selectParameters(
        names.locationFrame_kidneyPcnlLocationButton_QPushButton,
        names.flowRateFrame_mediumFlowRateButton_QPushButton,
        names.hardnessFrame_unknownHardnessButton_QPushButton
    )
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 167, 23, 233, -2, 1, Qt.LeftButton)
    test.vp("exitGuidedPopup", "Successful display of Exit Guided Mode popup")
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    test.vp("manualMode", "Successful display of program exits guided mode to manual mode treatment screen")
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selectParameters(
        names.locationFrame_kidneyPcnlLocationButton_QPushButton,
        names.flowRateFrame_highFlowRateButton_QPushButton,
        names.hardnessFrame_smallHardnessButton_QPushButton
    )
    
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton_2))
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 122, 25, 263, -17, 1, Qt.LeftButton)
    test.vp("exitGuidedPopup", "Successful display of Exit Guided Mode popup")
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    test.vp("manualMode", "Successful display of program exits guided mode to manual mode treatment screen")
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selectParameters(
        names.locationFrame_kidneyPcnlLocationButton_QPushButton,
        names.flowRateFrame_highFlowRateButton_QPushButton,
        names.hardnessFrame_mediumHardnessButton_QPushButton
    )
    
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton_2))
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 169, 31, 208, 1, 1, Qt.LeftButton)
    test.vp("exitGuidedPopup", "Successful display of Exit Guided Mode popup")
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    test.vp("manualMode", "Successful display of program exits guided mode to manual mode treatment screen")

    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selectParameters(
        names.locationFrame_kidneyPcnlLocationButton_QPushButton,
        names.flowRateFrame_highFlowRateButton_QPushButton,
        names.hardnessFrame_largeHardnessButton_QPushButton
    )
    
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton_2))
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 204, 22, 166, -3, 1, Qt.LeftButton)
    test.vp("exitGuidedPopup", "Successful display of Exit Guided Mode popup")
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    test.vp("manualMode", "Successful display of program exits guided mode to manual mode treatment screen")

    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selectParameters(
        names.locationFrame_kidneyPcnlLocationButton_QPushButton,
        names.flowRateFrame_highFlowRateButton_QPushButton,
        names.hardnessFrame_unknownHardnessButton_QPushButton
    )
    
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton_2))
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 157, 13, 237, 7, 1, Qt.LeftButton)
    test.vp("exitGuidedPopup", "Successful display of Exit Guided Mode popup")
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    test.vp("manualMode", "Successful display of program exits guided mode to manual mode treatment screen")

    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selectParameters(
        names.locationFrame_kidneyPcnlLocationButton_QPushButton,
        names.flowRateFrame_unknownFlowRateButton_QPushButton,
        names.hardnessFrame_smallHardnessButton_QPushButton
    )
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 131, 28, 255, -4, 1, Qt.LeftButton)
    test.vp("exitGuidedPopup", "Successful display of Exit Guided Mode popup")
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    test.vp("manualMode", "Successful display of program exits guided mode to manual mode treatment screen")

    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selectParameters(
        names.locationFrame_kidneyPcnlLocationButton_QPushButton,
        names.flowRateFrame_unknownFlowRateButton_QPushButton,
        names.hardnessFrame_mediumHardnessButton_QPushButton
    )
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 165, 23, 216, 1, 1, Qt.LeftButton)
    test.vp("exitGuidedPopup", "Successful display of Exit Guided Mode popup")
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    test.vp("manualMode", "Successful display of program exits guided mode to manual mode treatment screen")

    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selectParameters(
        names.locationFrame_kidneyPcnlLocationButton_QPushButton,
        names.flowRateFrame_unknownFlowRateButton_QPushButton,
        names.hardnessFrame_largeHardnessButton_QPushButton
    )
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 186, 25, 211, 1, 1, Qt.LeftButton)
    test.vp("exitGuidedPopup", "Successful display of Exit Guided Mode popup")
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    test.vp("manualMode", "Successful display of program exits guided mode to manual mode treatment screen")

    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selectParameters(
        names.locationFrame_kidneyPcnlLocationButton_QPushButton,
        names.flowRateFrame_unknownFlowRateButton_QPushButton,
        names.hardnessFrame_unknownHardnessButton_QPushButton
    )
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 157, 32, 243, -8, 1, Qt.LeftButton)
    test.vp("exitGuidedPopup", "Successful display of Exit Guided Mode popup")
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    test.vp("manualMode", "Successful display of program exits guided mode to manual mode treatment screen")

    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selectParameters(
        names.locationFrame_kidneyRirsLocationButton_QPushButton,
        names.flowRateFrame_lowFlowRateButton_QPushButton,
        names.hardnessFrame_smallHardnessButton_QPushButton
    )
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 134, 28, 253, -12, 1, Qt.LeftButton)
    test.vp("exitGuidedPopup", "Successful display of Exit Guided Mode popup")
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    test.vp("manualMode", "Successful display of program exits guided mode to manual mode treatment screen")

    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selectParameters(
        names.locationFrame_kidneyRirsLocationButton_QPushButton,
        names.flowRateFrame_lowFlowRateButton_QPushButton,
        names.hardnessFrame_mediumHardnessButton_QPushButton
    )
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 162, 24, 214, -10, 1, Qt.LeftButton)
    test.vp("exitGuidedPopup", "Successful display of Exit Guided Mode popup")
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    test.vp("manualMode", "Successful display of program exits guided mode to manual mode treatment screen")

    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selectParameters(
        names.locationFrame_kidneyRirsLocationButton_QPushButton,
        names.flowRateFrame_lowFlowRateButton_QPushButton,
        names.hardnessFrame_largeHardnessButton_QPushButton
    )
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 204, 23, 197, -7, 1, Qt.LeftButton)
    test.vp("exitGuidedPopup", "Successful display of Exit Guided Mode popup")
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    test.vp("manualMode", "Successful display of program exits guided mode to manual mode treatment screen")

    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selectParameters(
        names.locationFrame_kidneyRirsLocationButton_QPushButton,
        names.flowRateFrame_lowFlowRateButton_QPushButton,
        names.hardnessFrame_unknownHardnessButton_QPushButton
    )
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 165, 22, 233, 2, 1, Qt.LeftButton)
    test.vp("exitGuidedPopup", "Successful display of Exit Guided Mode popup")
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    test.vp("manualMode", "Successful display of program exits guided mode to manual mode treatment screen")

    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selectParameters(
        names.locationFrame_kidneyRirsLocationButton_QPushButton,
        names.flowRateFrame_mediumFlowRateButton_QPushButton,
        names.hardnessFrame_smallHardnessButton_QPushButton
    )
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 127, 31, 279, -1, 1, Qt.LeftButton)
    test.vp("exitGuidedPopup", "Successful display of Exit Guided Mode popup")
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    test.vp("manualMode", "Successful display of program exits guided mode to manual mode treatment screen")

    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selectParameters(
        names.locationFrame_kidneyRirsLocationButton_QPushButton,
        names.flowRateFrame_mediumFlowRateButton_QPushButton,
        names.hardnessFrame_mediumHardnessButton_QPushButton
    )
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 151, 19, 249, 1, 1, Qt.LeftButton)
    test.vp("exitGuidedPopup", "Successful display of Exit Guided Mode popup")
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    test.vp("manualMode", "Successful display of program exits guided mode to manual mode treatment screen")

    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selectParameters(
        names.locationFrame_kidneyRirsLocationButton_QPushButton,
        names.flowRateFrame_mediumFlowRateButton_QPushButton,
        names.hardnessFrame_largeHardnessButton_QPushButton
    )
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 196, 24, 200, 4, 1, Qt.LeftButton)
    test.vp("exitGuidedPopup", "Successful display of Exit Guided Mode popup")
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    test.vp("manualMode", "Successful display of program exits guided mode to manual mode treatment screen")

    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selectParameters(
        names.locationFrame_kidneyRirsLocationButton_QPushButton,
        names.flowRateFrame_mediumFlowRateButton_QPushButton,
        names.hardnessFrame_unknownHardnessButton_QPushButton
    )
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 169, 29, 239, -22, 1, Qt.LeftButton)
    test.vp("exitGuidedPopup", "Successful display of Exit Guided Mode popup")
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    test.vp("manualMode", "Successful display of program exits guided mode to manual mode treatment screen")

    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selectParameters(
        names.locationFrame_kidneyRirsLocationButton_QPushButton,
        names.flowRateFrame_unknownFlowRateButton_QPushButton,
        names.hardnessFrame_smallHardnessButton_QPushButton
    )
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 132, 20, 265, 10, 1, Qt.LeftButton)
    test.vp("exitGuidedPopup", "Successful display of Exit Guided Mode popup")
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    test.vp("manualMode", "Successful display of program exits guided mode to manual mode treatment screen")

    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selectParameters(
        names.locationFrame_kidneyRirsLocationButton_QPushButton,
        names.flowRateFrame_unknownFlowRateButton_QPushButton,
        names.hardnessFrame_mediumHardnessButton_QPushButton
    )
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 149, 27, 244, -1, 1, Qt.LeftButton)
    test.vp("exitGuidedPopup", "Successful display of Exit Guided Mode popup")
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    test.vp("manualMode", "Successful display of program exits guided mode to manual mode treatment screen")

    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selectParameters(
        names.locationFrame_kidneyRirsLocationButton_QPushButton,
        names.flowRateFrame_unknownFlowRateButton_QPushButton,
        names.hardnessFrame_largeHardnessButton_QPushButton
    )
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 192, 29, 209, 4, 1, Qt.LeftButton)
    test.vp("exitGuidedPopup", "Successful display of Exit Guided Mode popup")
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    test.vp("manualMode", "Successful display of program exits guided mode to manual mode treatment screen")

    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selectParameters(
        names.locationFrame_kidneyRirsLocationButton_QPushButton,
        names.flowRateFrame_unknownFlowRateButton_QPushButton,
        names.hardnessFrame_unknownHardnessButton_QPushButton
    )
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 166, 18, 232, 6, 1, Qt.LeftButton)
    test.vp("exitGuidedPopup", "Successful display of Exit Guided Mode popup")
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    test.vp("manualMode", "Successful display of program exits guided mode to manual mode treatment screen")

    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selectParameters(
        names.locationFrame_ureterLocationButton_QPushButton,
        names.flowRateFrame_lowFlowRateButton_QPushButton,
        names.hardnessFrame_smallHardnessButton_QPushButton
    )
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 137, 27, 237, -3, 1, Qt.LeftButton)
    test.vp("exitGuidedPopup", "Successful display of Exit Guided Mode popup")
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    test.vp("manualMode", "Successful display of program exits guided mode to manual mode treatment screen")

    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selectParameters(
        names.locationFrame_ureterLocationButton_QPushButton,
        names.flowRateFrame_lowFlowRateButton_QPushButton,
        names.hardnessFrame_mediumHardnessButton_QPushButton
    )
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 156, 30, 249, -2, 1, Qt.LeftButton)
    test.vp("exitGuidedPopup", "Successful display of Exit Guided Mode popup")
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    test.vp("manualMode", "Successful display of program exits guided mode to manual mode treatment screen")

    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selectParameters(
        names.locationFrame_ureterLocationButton_QPushButton,
        names.flowRateFrame_lowFlowRateButton_QPushButton,
        names.hardnessFrame_largeHardnessButton_QPushButton
    )
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 184, 33, 219, -16, 1, Qt.LeftButton)
    test.vp("exitGuidedPopup", "Successful display of Exit Guided Mode popup")
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    test.vp("manualMode", "Successful display of program exits guided mode to manual mode treatment screen")

    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selectParameters(
        names.locationFrame_ureterLocationButton_QPushButton,
        names.flowRateFrame_lowFlowRateButton_QPushButton,
        names.hardnessFrame_unknownHardnessButton_QPushButton
    )
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 156, 26, 252, -2, 1, Qt.LeftButton)
    test.vp("exitGuidedPopup", "Successful display of Exit Guided Mode popup")
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    test.vp("manualMode", "Successful display of program exits guided mode to manual mode treatment screen")

    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selectParameters(
        names.locationFrame_ureterLocationButton_QPushButton,
        names.flowRateFrame_mediumFlowRateButton_QPushButton,
        names.hardnessFrame_smallHardnessButton_QPushButton
    )
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 124, 26, 279, 2, 1, Qt.LeftButton)
    test.vp("exitGuidedPopup", "Successful display of Exit Guided Mode popup")
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    test.vp("manualMode", "Successful display of program exits guided mode to manual mode treatment screen")

    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selectParameters(
        names.locationFrame_ureterLocationButton_QPushButton,
        names.flowRateFrame_mediumFlowRateButton_QPushButton,
        names.hardnessFrame_mediumHardnessButton_QPushButton
    )
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 157, 26, 240, -13, 1, Qt.LeftButton)
    test.vp("exitGuidedPopup", "Successful display of Exit Guided Mode popup")
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    test.vp("manualMode", "Successful display of program exits guided mode to manual mode treatment screen")

    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selectParameters(
        names.locationFrame_ureterLocationButton_QPushButton,
        names.flowRateFrame_mediumFlowRateButton_QPushButton,
        names.hardnessFrame_largeHardnessButton_QPushButton
    )
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 194, 29, 209, -2, 1, Qt.LeftButton)
    test.vp("exitGuidedPopup", "Successful display of Exit Guided Mode popup")
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    test.vp("manualMode", "Successful display of program exits guided mode to manual mode treatment screen")

    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selectParameters(
        names.locationFrame_ureterLocationButton_QPushButton,
        names.flowRateFrame_mediumFlowRateButton_QPushButton,
        names.hardnessFrame_unknownHardnessButton_QPushButton
    )
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 155, 26, 245, -12, 1, Qt.LeftButton)
    test.vp("exitGuidedPopup", "Successful display of Exit Guided Mode popup")
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    test.vp("manualMode", "Successful display of program exits guided mode to manual mode treatment screen")

    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selectParameters(
        names.locationFrame_ureterLocationButton_QPushButton,
        names.flowRateFrame_unknownFlowRateButton_QPushButton,
        names.hardnessFrame_smallHardnessButton_QPushButton
    )
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 137, 29, 263, -9, 1, Qt.LeftButton)
    test.vp("exitGuidedPopup", "Successful display of Exit Guided Mode popup")
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    test.vp("manualMode", "Successful display of program exits guided mode to manual mode treatment screen")

    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selectParameters(
        names.locationFrame_ureterLocationButton_QPushButton,
        names.flowRateFrame_unknownFlowRateButton_QPushButton,
        names.hardnessFrame_mediumHardnessButton_QPushButton
    )
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 157, 25, 253, -4, 1, Qt.LeftButton)
    test.vp("exitGuidedPopup", "Successful display of Exit Guided Mode popup")
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    test.vp("manualMode", "Successful display of program exits guided mode to manual mode treatment screen")

    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selectParameters(
        names.locationFrame_ureterLocationButton_QPushButton,
        names.flowRateFrame_unknownFlowRateButton_QPushButton,
        names.hardnessFrame_largeHardnessButton_QPushButton
    )
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 187, 35, 219, -12, 1, Qt.LeftButton)
    test.vp("exitGuidedPopup", "Successful display of Exit Guided Mode popup")
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    test.vp("manualMode", "Successful display of program exits guided mode to manual mode treatment screen")

    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selectParameters(
        names.locationFrame_ureterLocationButton_QPushButton,
        names.flowRateFrame_unknownFlowRateButton_QPushButton,
        names.hardnessFrame_unknownHardnessButton_QPushButton
    )
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 161, 32, 241, -5, 1, Qt.LeftButton)
    test.vp("exitGuidedPopup", "Successful display of Exit Guided Mode popup")
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    test.vp("manualMode", "Successful display of program exits guided mode to manual mode treatment screen")

    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selectParameters(
        names.locationFrame_bladderLocationButton_QPushButton,
        names.flowRateFrame_highFlowRateButton_QPushButton,
        names.hardnessFrame_smallHardnessButton_QPushButton
    )
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 243, 22, 157, -12, 1, Qt.LeftButton)
    test.vp("exitGuidedPopup", "Successful display of Exit Guided Mode popup")
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    test.vp("manualMode", "Successful display of program exits guided mode to manual mode treatment screen")

    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selectParameters(
        names.locationFrame_bladderLocationButton_QPushButton,
        names.flowRateFrame_highFlowRateButton_QPushButton,
        names.hardnessFrame_mediumHardnessButton_QPushButton
    )
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 327, 26, 76, -3, 1, Qt.LeftButton)
    test.vp("exitGuidedPopup", "Successful display of Exit Guided Mode popup")
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    test.vp("manualMode", "Successful display of program exits guided mode to manual mode treatment screen")

    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selectParameters(
        names.locationFrame_bladderLocationButton_QPushButton,
        names.flowRateFrame_highFlowRateButton_QPushButton,
        names.hardnessFrame_largeHardnessButton_QPushButton
    )
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 345, 27, 56, -4, 1, Qt.LeftButton)
    test.vp("exitGuidedPopup", "Successful display of Exit Guided Mode popup")
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    test.vp("manualMode", "Successful display of program exits guided mode to manual mode treatment screen")

    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selectParameters(
        names.locationFrame_bladderLocationButton_QPushButton,
        names.flowRateFrame_highFlowRateButton_QPushButton,
        names.hardnessFrame_unknownHardnessButton_QPushButton
    )
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 330, 27, 70, -9, 1, Qt.LeftButton)
    test.vp("exitGuidedPopup", "Successful display of Exit Guided Mode popup")
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    test.vp("manualMode", "Successful display of program exits guided mode to manual mode treatment screen")

    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selectParameters(
        names.locationFrame_bladderLocationButton_QPushButton,
        names.flowRateFrame_unknownFlowRateButton_QPushButton,
        names.hardnessFrame_smallHardnessButton_QPushButton
    )
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 243, 25, 158, -3, 1, Qt.LeftButton)
    test.vp("exitGuidedPopup", "Successful display of Exit Guided Mode popup")
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    test.vp("manualMode", "Successful display of program exits guided mode to manual mode treatment screen")

    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selectParameters(
        names.locationFrame_bladderLocationButton_QPushButton,
        names.flowRateFrame_unknownFlowRateButton_QPushButton,
        names.hardnessFrame_mediumHardnessButton_QPushButton
    )
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 325, 25, 80, 0, 1, Qt.LeftButton)
    test.vp("exitGuidedPopup", "Successful display of Exit Guided Mode popup")
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    test.vp("manualMode", "Successful display of program exits guided mode to manual mode treatment screen")

    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selectParameters(
        names.locationFrame_bladderLocationButton_QPushButton,
        names.flowRateFrame_unknownFlowRateButton_QPushButton,
        names.hardnessFrame_largeHardnessButton_QPushButton
    )
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 345, 27, 52, -3, 1, Qt.LeftButton)
    test.vp("exitGuidedPopup", "Successful display of Exit Guided Mode popup")
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    test.vp("manualMode", "Successful display of program exits guided mode to manual mode treatment screen")

    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    selectParameters(
        names.locationFrame_bladderLocationButton_QPushButton,
        names.flowRateFrame_unknownFlowRateButton_QPushButton,
        names.hardnessFrame_unknownHardnessButton_QPushButton
    )
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 326, 25, 73, 3, 1, Qt.LeftButton)
    test.vp("exitGuidedPopup", "Successful display of Exit Guided Mode popup")
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    test.vp("manualMode", "Successful display of program exits guided mode to manual mode treatment screen")

    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))  
    clickButton(waitForObject(names.homeScreen_pbSoftTissueAssistant_QToolButton))
    clickButton(waitForObject(names.gbSoftTissueProcedures_pbIncision_QPushButton))
    clickButton(waitForObject(names.softTissueAssistantModeScreen_pbContinue_QPushButton))
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 200, 26, 188, 7, 1, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    test.vp("manualMode_SoftTissue", "Successful display of program exits guided mode to manual mode treatment screen")
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbSoftTissueAssistant_QToolButton))
    clickButton(waitForObject(names.gbSoftTissueProcedures_pbTumor_QPushButton))
    clickButton(waitForObject(names.softTissueAssistantModeScreen_pbContinue_QPushButton))
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 190, 24, 217, 1, 1, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    test.vp("manualMode_SoftTissue", "Successful display of program exits guided mode to manual mode treatment screen")
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbSoftTissueAssistant_QToolButton))
    clickButton(waitForObject(names.gbBphProcedures_pbEnucleation_QPushButton))
    clickButton(waitForObject(names.softTissueAssistantModeScreen_pbContinue_QPushButton))
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton_2))
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 270, 21, 130, 7, 1, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    test.vp("manualMode_SoftTissue", "Successful display of program exits guided mode to manual mode treatment screen")
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbSoftTissueAssistant_QToolButton))
    clickButton(waitForObject(names.gbBphProcedures_pbEnucleationLow_ButtoWithCaptionAndSmallerSubCaption))
    clickButton(waitForObject(names.softTissueAssistantModeScreen_pbContinue_QPushButton))
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton_2))
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 275, 29, 130, -1, 1, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    test.vp("manualMode_SoftTissue", "Successful display of program exits guided mode to manual mode treatment screen")
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbSoftTissueAssistant_QToolButton))
    clickButton(waitForObject(names.gbBphProcedures_pbVaporize_QPushButton))
    clickButton(waitForObject(names.softTissueAssistantModeScreen_pbContinue_QPushButton))
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_3), 343, 27, -294, -11, 1, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    test.vp("manualMode_SoftTissue", "Successful display of program exits guided mode to manual mode treatment screen")
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    
    
  
    
