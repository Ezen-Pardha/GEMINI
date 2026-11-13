# -*- coding: utf-8 -*-

import names

def handlePopup(timeout=1500, required=False):
    cancel_locator = {
        "container": names.centralWidget_QFrame,
        "name": "CancelButton",
        "type": "QPushButton",
        "visible": True
    }
    # Wait briefly for the optional popup to appear.
    found = waitFor( "object.exists(" + repr(cancel_locator) + ")", timeout)

    if not found:
        message = ( "Popup Cancel button did not appear within {} ms." .format(timeout))

        if required:
            test.fail(message)
            return False
        test.log(message + " Popup is optional for this action.")
        return False

    # Resolve the object only after confirming that it exists.
    try:
        cancel_button = waitForObject(cancel_locator, 1000)
        clickButton(cancel_button)
        test.log("Popup Cancel button clicked successfully.")
        return True

    except LookupError as error:
        test.fail( "Cancel button existed but could not be accessed: {}" .format(error))
        return False  
    

def main():
    doubleClick(waitForObject(names.numpad_pushButton_8_NumpadButton), 85, 57, Qt.NoModifier, Qt.LeftButton)
    doubleClick(waitForObject(names.numpad_pushButton_8_NumpadButton), 85, 57, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton))

    clickButton(waitForObject(names.homeScreen_pbSoftTissueAssistant_QToolButton))
    clickButton(waitForObject(names.gbSoftTissueProcedures_pbIncision_QPushButton))
    clickButton(waitForObject(names.softTissueAssistantModeScreen_pbContinue_QPushButton))

    test.vp("treatmentScreenSoft01","Successful display of the treatment screen")

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 194, 27, 195, -6, 1, Qt.LeftButton)
    test.vp("exitGuidedSoftTissue","Successful display of Exit Guided Mode Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    test.vp("treatmentScreenSoft01","Successful display of retaining last set of Parameters")
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 82, 29, 75, -3, 1, Qt.LeftButton)
    test.vp("exitGuidedSoftTissue","Successful display of Exit Guided Mode Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 75, 27, 50, -4, 1, Qt.LeftButton)
    test.vp("exitGuidedSoftTissue","Successful display of Exit Guided Mode Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    clickButton(waitForObject(names.treatmentCharacteristicsBar_pbEdit_QPushButton_2))
    clickButton(waitForObject(names.centralWidget_rejectButton_QPushButton))
    clickButton(waitForObject(names.gbSoftTissueProcedures_pbTumor_QPushButton))
    
    clickButton(waitForObject(names.softTissueAssistantModeScreen_pbContinue_QPushButton))

    test.vp("treatmentScreenSoft02","Successful display of the treatment screen")

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 199, 27, -163, -7, 1, Qt.LeftButton)
    test.vp("exitGuidedSoftTissue","Successful display of Exit Guided Mode Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    test.vp("treatmentScreenSoft02","Successful display of retaining last set of Parameters")
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 79, 19, 159, 4, 1, Qt.LeftButton)
    test.vp("exitGuidedSoftTissue","Successful display of Exit Guided Mode Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 74, 28, 47, -4, 1, Qt.LeftButton)
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 121, 24, 10, 0, 1, Qt.LeftButton)
    test.vp("exitGuidedSoftTissue","Successful display of Exit Guided Mode Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))

    clickButton(waitForObject(names.treatmentCharacteristicsBar_pbEdit_QPushButton_2))
    clickButton(waitForObject(names.centralWidget_rejectButton_QPushButton))
    clickButton(waitForObject(names.gbBphProcedures_pbEnucleation_QPushButton))
    clickButton(waitForObject(names.softTissueAssistantModeScreen_pbContinue_QPushButton))
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton_2))

    test.vp("treatmentScreenSoft03","Successful display of the treatment screen")

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 272, 25, -201, -15, 1, Qt.LeftButton)
    test.vp("exitGuidedSoftTissue","Successful display of Exit Guided Mode Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    test.vp("treatmentScreenSoft03","Successful display of retaining last set of Parameters")
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 173, 22, -75, 1, 1, Qt.LeftButton)
    test.vp("exitGuidedSoftTissue","Successful display of Exit Guided Mode Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 180, 32, -53, -11, 1, Qt.LeftButton)
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 266, 24, -61, -8, 1, Qt.LeftButton)
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 144, 28, -17, 0, 1, Qt.LeftButton)
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 204, 24, -9, -2, 1, Qt.LeftButton)
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 132, 26, -10, -6, 1, Qt.LeftButton)
    test.vp("exitGuidedSoftTissue","Successful display of Exit Guided Mode Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))

    clickButton(waitForObject(names.treatmentCharacteristicsBar_pbEdit_QPushButton_2))
    clickButton(waitForObject(names.centralWidget_rejectButton_QPushButton))
    clickButton(waitForObject(names.gbBphProcedures_pbEnucleationLow_ButtoWithCaptionAndSmallerSubCaption))
    clickButton(waitForObject(names.softTissueAssistantModeScreen_pbContinue_QPushButton))
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton_2))

    test.vp("treatmentScreenSoft04","Successful display of the treatment screen")

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 265, 27, -153, -5, 1, Qt.LeftButton)
    test.vp("exitGuidedSoftTissue","Successful display of Exit Guided Mode Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    test.vp("treatmentScreenSoft04","Successful display of retaining last set of Parameters")
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 176, 28, 85, -11, 1, Qt.LeftButton)
    test.vp("exitGuidedSoftTissue","Successful display of Exit Guided Mode Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 169, 25, -46, -8, 1, Qt.LeftButton)
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 265, 25, -70, -5, 1, Qt.LeftButton)
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 152, 28, -33, -9, 1, Qt.LeftButton)
    test.vp("exitGuidedSoftTissue","Successful display of Exit Guided Mode Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    clickButton(waitForObject(names.treatmentCharacteristicsBar_pbEdit_QPushButton_2))
    clickButton(waitForObject(names.centralWidget_rejectButton_QPushButton))
    clickButton(waitForObject(names.gbBphProcedures_pbVaporize_QPushButton))
    clickButton(waitForObject(names.softTissueAssistantModeScreen_pbContinue_QPushButton))

    test.vp("treatmentScreenSoft05","Successful display of the treatment screen")

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_3), 346, 23, -245, -8, 1, Qt.LeftButton)
    test.vp("exitGuidedSoftTissue","Successful display of Exit Guided Mode Popup")
    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    
    test.vp("treatmentScreenSoft05","Successful display of retaining last set of Parameters")
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    clickButton(waitForObject(names.locationFrame_kidneyPcnlLocationButton_QPushButton))
    clickButton(waitForObject(names.flowRateFrame_lowFlowRateButton_QPushButton))
    clickButton(waitForObject(names.hardnessFrame_smallHardnessButton_QPushButton))
    clickButton(waitForObject(names.stoneAssistantModeScreen_continueButton_QPushButton))
     
    test.vp("treatmentScreen01","Successful display of the treatment screen")

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 123, 21, 259, -18, 1, Qt.LeftButton)
    mouseClick(waitForObject(names.centralWidget_QFrame), 1126, 244, Qt.NoModifier, Qt.LeftButton)

    test.vp("exitpopup","Successful display of Exit Guided Mode Popup")
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
    
    test.vp("treatmentScreen01","Successful display of retaining last set of Parameters")
    
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 74, 20, 181, -20, 1, Qt.LeftButton)
    mouseClick(waitForObject(names.centralWidget_TitleLabel_QLabel), 811, 26, Qt.NoModifier, Qt.LeftButton)
     
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup")
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 57, 23, 140, 3, 1, Qt.LeftButton)
     
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup")
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return

    clickButton(waitForObject(names.treatmentCharacteristicsBar_pbEdit_QPushButton))
    clickButton(waitForObject(names.centralWidget_rejectButton_QPushButton))
    clickButton(waitForObject(names.hardnessFrame_mediumHardnessButton_QPushButton))
    clickButton(waitForObject(names.stoneAssistantModeScreen_continueButton_QPushButton))
     
    test.vp("treatmentScreen02","Successful display of the treatment screen")

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 158, 29, 205, 14, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
    
    test.vp("treatmentScreen02","Successful display of retaining last set of Parameters")
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 69, 22, 195, -7, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 62, 23, 137, 0, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    clickButton(waitForObject(names.treatmentCharacteristicsBar_pbEdit_QPushButton))
    clickButton(waitForObject(names.centralWidget_rejectButton_QPushButton))
    clickButton(waitForObject(names.hardnessFrame_largeHardnessButton_QPushButton))
    clickButton(waitForObject(names.stoneAssistantModeScreen_continueButton_QPushButton))

    test.vp("treatmentScreen03","Successful display of the treatment screen")

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 195, 24, 170, -22, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
    
    test.vp("treatmentScreen03","Successful display of retaining last set of Parameters") 
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 63, 24, 195, -4, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 74, 28, 111, 0, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    clickButton(waitForObject(names.treatmentCharacteristicsBar_pbEdit_QPushButton))
    mouseClick(waitForObject(names.centralWidget_QFrame), 159, 384, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_rejectButton_QPushButton))
    clickButton(waitForObject(names.hardnessFrame_unknownHardnessButton_QPushButton))
    clickButton(waitForObject(names.stoneAssistantModeScreen_continueButton_QPushButton))

    test.vp("treatmentScreen04","Successful display of the treatment screen")

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 171, 28, 183, -7, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
    
    test.vp("treatmentScreen04","Successful display of retaining last set of Parameters") 
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 72, 25, 212, -15, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 67, 27, 131, -11, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    clickButton(waitForObject(names.treatmentCharacteristicsBar_pbEdit_QPushButton))
    clickButton(waitForObject(names.centralWidget_rejectButton_QPushButton))
    clickButton(waitForObject(names.flowRateFrame_mediumFlowRateButton_QPushButton))
    clickButton(waitForObject(names.hardnessFrame_smallHardnessButton_QPushButton))
    clickButton(waitForObject(names.stoneAssistantModeScreen_continueButton_QPushButton))

    test.vp("treatmentScreen06","Successful display of the treatment screen")

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 120, 29, 246, -19, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
    
    test.vp("treatmentScreen06","Successful display of retaining last set of Parameters") 
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 89, 21, 196, -11, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return         
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 94, 31, 92, -8, 1, Qt.LeftButton)
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 191, 20, 10, 3, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return         
     
    clickButton(waitForObject(names.treatmentCharacteristicsBar_pbEdit_QPushButton))
    clickButton(waitForObject(names.centralWidget_rejectButton_QPushButton))
    clickButton(waitForObject(names.hardnessFrame_mediumHardnessButton_QPushButton))
    clickButton(waitForObject(names.stoneAssistantModeScreen_continueButton_QPushButton))

    test.vp("treatmentScreen07","Successful display of the treatment screen")

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 173, 31, 191, -14, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
    
    test.vp("treatmentScreen07","Successful display of retaining last set of Parameters")
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 109, 18, 178, 8, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
         
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 102, 32, 91, -10, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return         
     
    clickButton(waitForObject(names.treatmentCharacteristicsBar_pbEdit_QPushButton))
    clickButton(waitForObject(names.centralWidget_rejectButton_QPushButton))
    clickButton(waitForObject(names.hardnessFrame_largeHardnessButton_QPushButton))
    clickButton(waitForObject(names.stoneAssistantModeScreen_continueButton_QPushButton))

    test.vp("treatmentScreen08","Successful display of the treatment screen")

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 188, 25, 167, -18, 1, Qt.LeftButton)
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return   
    
    test.vp("treatmentScreen08","Successful display of retaining last set of Parameters")      
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 109, 29, 140, -11, 1, Qt.LeftButton)
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup")
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
        
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 97, 22, 106, -3, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup")
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 110, 10, 71, 0, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    clickButton(waitForObject(names.treatmentCharacteristicsBar_pbEdit_QPushButton))
    clickButton(waitForObject(names.centralWidget_rejectButton_QPushButton))
    clickButton(waitForObject(names.hardnessFrame_unknownHardnessButton_QPushButton))
    clickButton(waitForObject(names.stoneAssistantModeScreen_continueButton_QPushButton))

    test.vp("treatmentScreen09","Successful display of the treatment screen")

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 151, 15, 208, -11, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
    
    test.vp("treatmentScreen09","Successful display of retaining last set of Parameters")
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 96, 20, 149, -13, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 98, 17, 92, -5, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    clickButton(waitForObject(names.treatmentCharacteristicsBar_pbEdit_QPushButton))
    clickButton(waitForObject(names.centralWidget_rejectButton_QPushButton))
    clickButton(waitForObject(names.flowRateFrame_highFlowRateButton_QPushButton))
    clickButton(waitForObject(names.hardnessFrame_smallHardnessButton_QPushButton))
    clickButton(waitForObject(names.stoneAssistantModeScreen_continueButton_QPushButton))
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton_2))

    test.vp("treatmentScreen10","Successful display of the treatment screen")

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 130, 30, 244, -6, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
    
    test.vp("treatmentScreen10","Successful display of retaining last set of Parameters")
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 129, 24, 147, 3, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 131, 25, 59, -1, 1, Qt.LeftButton)
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 190, 24, 16, 0, 1, Qt.LeftButton)
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 132, 15, 98, -3, 1, Qt.LeftButton)
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 153, 12, 52, 10, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup")
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    clickButton(waitForObject(names.treatmentCharacteristicsBar_pbEdit_QPushButton))
    clickButton(waitForObject(names.centralWidget_rejectButton_QPushButton))
    clickButton(waitForObject(names.hardnessFrame_mediumHardnessButton_QPushButton))
    clickButton(waitForObject(names.stoneAssistantModeScreen_continueButton_QPushButton))
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton_2))     

    test.vp("treatmentScreen11","Successful display of the treatment screen")

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 155, 29, 209, -2, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup")
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
    
    test.vp("treatmentScreen11","Successful display of retaining last set of Parameters")
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 119, 14, 195, -3, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 127, 27, 62, 2, 1, Qt.LeftButton)
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 157, 14, 144, 7, 1, Qt.LeftButton)
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 134, 20, 59, 2, 1, Qt.LeftButton)
     
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup")
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    clickButton(waitForObject(names.treatmentCharacteristicsBar_pbEdit_QPushButton))
    clickButton(waitForObject(names.centralWidget_rejectButton_QPushButton))
    clickButton(waitForObject(names.hardnessFrame_largeHardnessButton_QPushButton))
    clickButton(waitForObject(names.stoneAssistantModeScreen_continueButton_QPushButton))
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton_2))

    test.vp("treatmentScreen12","Successful display of the treatment screen")

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 184, 22, 181, 0, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
    
    test.vp("treatmentScreen12","Successful display of retaining last set of Parameters")
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 140, 26, 155, -14, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 123, 27, 77, -4, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    clickButton(waitForObject(names.treatmentCharacteristicsBar_pbEdit_QPushButton))
    clickButton(waitForObject(names.centralWidget_rejectButton_QPushButton))
    clickButton(waitForObject(names.hardnessFrame_unknownHardnessButton_QPushButton))
    clickButton(waitForObject(names.stoneAssistantModeScreen_continueButton_QPushButton))
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton_2))

    test.vp("treatmentScreen13","Successful display of the treatment screen")

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 160, 22, 199, -10, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
    
    test.vp("treatmentScreen13","Successful display of retaining last set of Parameters")
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 136, 22, 141, -7, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 137, 21, 69, 0, 1, Qt.LeftButton)
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 158, 22, 114, -2, 1, Qt.LeftButton)
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 157, 26, 49, 5, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    clickButton(waitForObject(names.treatmentCharacteristicsBar_pbEdit_QPushButton))
    clickButton(waitForObject(names.centralWidget_rejectButton_QPushButton))
    clickButton(waitForObject(names.flowRateFrame_unknownFlowRateButton_QPushButton))
    clickButton(waitForObject(names.hardnessFrame_smallHardnessButton_QPushButton))
    clickButton(waitForObject(names.stoneAssistantModeScreen_continueButton_QPushButton))

    test.vp("treatmentScreen14","Successful display of the treatment screen")

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 137, 28, 227, -2, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
    
    test.vp("treatmentScreen14","Successful display of retaining last set of Parameters")
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 70, 23, 119, 0, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 72, 20, 208, -7, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    clickButton(waitForObject(names.treatmentCharacteristicsBar_pbEdit_QPushButton))
    clickButton(waitForObject(names.centralWidget_rejectButton_QPushButton))
    clickButton(waitForObject(names.hardnessFrame_mediumHardnessButton_QPushButton))
    clickButton(waitForObject(names.stoneAssistantModeScreen_continueButton_QPushButton))

    test.vp("treatmentScreen15","Successful display of the treatment screen")

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 162, 30, 209, -11, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
    
    test.vp("treatmentScreen15","Successful display of retaining last set of Parameters")
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 78, 24, 226, -14, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 69, 22, 126, -9, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    clickButton(waitForObject(names.treatmentCharacteristicsBar_pbEdit_QPushButton))
    clickButton(waitForObject(names.centralWidget_rejectButton_QPushButton))
    clickButton(waitForObject(names.hardnessFrame_largeHardnessButton_QPushButton))
    clickButton(waitForObject(names.stoneAssistantModeScreen_continueButton_QPushButton))

    test.vp("treatmentScreen16","Successful display of the treatment screen")

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 196, 21, 205, -5, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup")
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
    
    test.vp("treatmentScreen16","Successful display of retaining last set of Parameters")
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 76, 22, 207, 6, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup")
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 72, 25, 113, -4, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    clickButton(waitForObject(names.treatmentCharacteristicsBar_pbEdit_QPushButton))
    clickButton(waitForObject(names.centralWidget_rejectButton_QPushButton))
    clickButton(waitForObject(names.hardnessFrame_unknownHardnessButton_QPushButton))
    clickButton(waitForObject(names.stoneAssistantModeScreen_continueButton_QPushButton))

    test.vp("treatmentScreen17","Successful display of the treatment screen")

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 154, 25, 206, -3, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
    
    test.vp("treatmentScreen17","Successful display of retaining last set of Parameters")
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 72, 36, 236, -31, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 57, 24, 138, -11, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    clickButton(waitForObject(names.treatmentCharacteristicsBar_pbEdit_QPushButton))
    clickButton(waitForObject(names.centralWidget_rejectButton_QPushButton))
    clickButton(waitForObject(names.locationFrame_kidneyRirsLocationButton_QPushButton))
    clickButton(waitForObject(names.flowRateFrame_lowFlowRateButton_QPushButton))
    clickButton(waitForObject(names.hardnessFrame_smallHardnessButton_QPushButton))
    clickButton(waitForObject(names.stoneAssistantModeScreen_continueButton_QPushButton))

    test.vp("treatmentScreen18","Successful display of the treatment screen")

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 128, 20, 241, -18, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
    
    test.vp("treatmentScreen18","Successful display of retaining last set of Parameters")
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 72, 22, 207, -7, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup")
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 73, 22, 129, -8, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    clickButton(waitForObject(names.treatmentCharacteristicsBar_pbEdit_QPushButton))
    clickButton(waitForObject(names.centralWidget_rejectButton_QPushButton))
    clickButton(waitForObject(names.hardnessFrame_mediumHardnessButton_QPushButton))
    clickButton(waitForObject(names.stoneAssistantModeScreen_continueButton_QPushButton))

    test.vp("treatmentScreen19","Successful display of the treatment screen")

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 160, 19, 215, -1, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
    
    test.vp("treatmentScreen19","Successful display of retaining last set of Parameters")
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 58, 25, 151, -12, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup")
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 72, 25, 48, 5, 1, Qt.LeftButton)
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 162, 16, 99, 3, 1, Qt.LeftButton)
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 69, 31, 56, -6, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    clickButton(waitForObject(names.treatmentCharacteristicsBar_pbEdit_QPushButton))
    clickButton(waitForObject(names.centralWidget_rejectButton_QPushButton))
    clickButton(waitForObject(names.hardnessFrame_largeHardnessButton_QPushButton))
    clickButton(waitForObject(names.stoneAssistantModeScreen_continueButton_QPushButton))

    test.vp("treatmentScreen20","Successful display of the treatment screen")

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 199, 19, 155, -5, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup")
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return 
    
    test.vp("treatmentScreen20","Successful display of retaining last set of Parameters")
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 57, 18, 206, -16, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 59, 22, 131, -3, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup")
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    clickButton(waitForObject(names.treatmentCharacteristicsBar_pbEdit_QPushButton))
    clickButton(waitForObject(names.centralWidget_rejectButton_QPushButton))
    clickButton(waitForObject(names.hardnessFrame_unknownHardnessButton_QPushButton))
    clickButton(waitForObject(names.stoneAssistantModeScreen_continueButton_QPushButton))

    test.vp("treatmentScreen21","Successful display of the treatment screen")

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 165, 24, 212, 6, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup")
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return 
    
    test.vp("treatmentScreen21","Successful display of retaining last set of Parameters")        
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 70, 24, 198, -18, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup")
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 68, 30, 132, -17, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    clickButton(waitForObject(names.treatmentCharacteristicsBar_pbEdit_QPushButton))
    clickButton(waitForObject(names.centralWidget_rejectButton_QPushButton))
    clickButton(waitForObject(names.flowRateFrame_mediumFlowRateButton_QPushButton))
    clickButton(waitForObject(names.hardnessFrame_smallHardnessButton_QPushButton))
    clickButton(waitForObject(names.stoneAssistantModeScreen_continueButton_QPushButton))

    test.vp("treatmentScreen22","Successful display of the treatment screen")

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 125, 26, 248, 0, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
    
    test.vp("treatmentScreen22","Successful display of retaining last set of Parameters")
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 89, 17, 258, 2, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 94, 31, 112, -6, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    clickButton(waitForObject(names.treatmentCharacteristicsBar_pbEdit_QPushButton))
    clickButton(waitForObject(names.centralWidget_rejectButton_QPushButton))
    clickButton(waitForObject(names.hardnessFrame_mediumHardnessButton_QPushButton))
    clickButton(waitForObject(names.stoneAssistantModeScreen_continueButton_QPushButton))

    test.vp("treatmentScreen23","Successful display of the treatment screen")

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 163, 22, 227, 5, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
    
    test.vp("treatmentScreen23","Successful display of retaining last set of Parameters")
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 98, 28, 190, -9, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 106, 32, 96, -2, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    clickButton(waitForObject(names.treatmentCharacteristicsBar_pbEdit_QPushButton))
    clickButton(waitForObject(names.centralWidget_rejectButton_QPushButton))
    clickButton(waitForObject(names.hardnessFrame_largeHardnessButton_QPushButton))
    clickButton(waitForObject(names.stoneAssistantModeScreen_continueButton_QPushButton))     

    test.vp("treatmentScreen24","Successful display of the treatment screen")

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 189, 23, 176, -3, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup")
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
    
    test.vp("treatmentScreen24","Successful display of retaining last set of Parameters")
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 98, 26, 282, -5, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup")
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 258, 27, -54, 7, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup")
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    clickButton(waitForObject(names.treatmentCharacteristicsBar_pbEdit_QPushButton))
    clickButton(waitForObject(names.centralWidget_rejectButton_QPushButton))
    clickButton(waitForObject(names.hardnessFrame_unknownHardnessButton_QPushButton))
    clickButton(waitForObject(names.stoneAssistantModeScreen_continueButton_QPushButton))

    test.vp("treatmentScreen25","Successful display of the treatment screen")

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 169, 27, 224, -4, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
    
    test.vp("treatmentScreen25","Successful display of retaining last set of Parameters")
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 105, 23, 189, -15, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 89, 33, 117, -12, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    clickButton(waitForObject(names.treatmentCharacteristicsBar_pbEdit_QPushButton))
    clickButton(waitForObject(names.centralWidget_rejectButton_QPushButton))
    clickButton(waitForObject(names.flowRateFrame_unknownFlowRateButton_QPushButton))
    clickButton(waitForObject(names.hardnessFrame_smallHardnessButton_QPushButton))
    clickButton(waitForObject(names.stoneAssistantModeScreen_continueButton_QPushButton))

    test.vp("treatmentScreen26","Successful display of the treatment screen")

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 136, 22, 227, -20, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup")
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
    
    test.vp("treatmentScreen26","Successful display of retaining last set of Parameters")
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 70, 28, 228, -26, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 79, 19, 121, 1, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    clickButton(waitForObject(names.treatmentCharacteristicsBar_pbEdit_QPushButton))
    clickButton(waitForObject(names.centralWidget_rejectButton_QPushButton))
    clickButton(waitForObject(names.hardnessFrame_mediumHardnessButton_QPushButton))
    clickButton(waitForObject(names.stoneAssistantModeScreen_continueButton_QPushButton))

    test.vp("treatmentScreen27","Successful display of the treatment screen")

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 169, 14, 216, -1, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
    
    test.vp("treatmentScreen27","Successful display of retaining last set of Parameters")
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 85, 24, 166, -4, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 70, 28, 59, -5, 1, Qt.LeftButton)
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 168, 15, 105, -5, 1, Qt.LeftButton)
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 76, 31, 46, -3, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    clickButton(waitForObject(names.treatmentCharacteristicsBar_pbEdit_QPushButton))
    clickButton(waitForObject(names.centralWidget_rejectButton_QPushButton))
    clickButton(waitForObject(names.hardnessFrame_largeHardnessButton_QPushButton))
    clickButton(waitForObject(names.stoneAssistantModeScreen_continueButton_QPushButton))

    test.vp("treatmentScreen28","Successful display of the treatment screen")

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 203, 26, 193, -9, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
    
    test.vp("treatmentScreen28","Successful display of retaining last set of Parameters")
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 66, 30, 217, -19, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 68, 24, 127, -13, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    clickButton(waitForObject(names.treatmentCharacteristicsBar_pbEdit_QPushButton))
    clickButton(waitForObject(names.centralWidget_rejectButton_QPushButton))
    clickButton(waitForObject(names.hardnessFrame_unknownHardnessButton_QPushButton))
    clickButton(waitForObject(names.stoneAssistantModeScreen_continueButton_QPushButton))

    test.vp("treatmentScreen29","Successful display of the treatment screen")

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 165, 24, 195, -19, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup")
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
    
    test.vp("treatmentScreen29","Successful display of retaining last set of Parameters")
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 73, 32, 231, -6, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 70, 16, 134, -12, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    clickButton(waitForObject(names.treatmentCharacteristicsBar_pbEdit_QPushButton))
    clickButton(waitForObject(names.centralWidget_rejectButton_QPushButton))
    clickButton(waitForObject(names.locationFrame_ureterLocationButton_QPushButton))
    clickButton(waitForObject(names.flowRateFrame_lowFlowRateButton_QPushButton))
    clickButton(waitForObject(names.hardnessFrame_smallHardnessButton_QPushButton))
    clickButton(waitForObject(names.stoneAssistantModeScreen_continueButton_QPushButton, 201723))

    test.vp("treatmentScreen30","Successful display of the treatment screen")

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 131, 25, 237, -3, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
    
    test.vp("treatmentScreen30","Successful display of retaining last set of Parameters")
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 56, 31, 127, -10, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 54, 28, 41, 0, 1, Qt.LeftButton)
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 129, 23, 137, 2, 1, Qt.LeftButton)
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 62, 24, 32, 7, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup")     
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    clickButton(waitForObject(names.treatmentCharacteristicsBar_pbEdit_QPushButton))
    clickButton(waitForObject(names.centralWidget_rejectButton_QPushButton))
    clickButton(waitForObject(names.hardnessFrame_mediumHardnessButton_QPushButton))
    clickButton(waitForObject(names.stoneAssistantModeScreen_continueButton_QPushButton))

    test.vp("treatmentScreen31","Successful display of the treatment screen")

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 162, 22, 210, -14, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
    
    test.vp("treatmentScreen31","Successful display of retaining last set of Parameters")
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 53, 14, 43, 8, 1, Qt.LeftButton)
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 96, 22, 50, -6, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 154, 21, 135, -3, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 168, 26, 52, -6, 1, Qt.LeftButton)
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 83, 25, 6, -7, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    clickButton(waitForObject(names.treatmentCharacteristicsBar_pbEdit_QPushButton))
    clickButton(waitForObject(names.centralWidget_rejectButton_QPushButton))
    clickButton(waitForObject(names.hardnessFrame_largeHardnessButton_QPushButton))
    clickButton(waitForObject(names.stoneAssistantModeScreen_continueButton_QPushButton))

    test.vp("treatmentScreen32","Successful display of the treatment screen")

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 181, 30, 201, -13, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
    
    test.vp("treatmentScreen32","Successful display of retaining last set of Parameters")
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 52, 26, 149, -15, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 193, 26, 86, -7, 1, Qt.LeftButton)
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 51, 26, 38, 5, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    clickButton(waitForObject(names.treatmentCharacteristicsBar_pbEdit_QPushButton))
    clickButton(waitForObject(names.centralWidget_rejectButton_QPushButton))
    clickButton(waitForObject(names.hardnessFrame_unknownHardnessButton_QPushButton))
    clickButton(waitForObject(names.stoneAssistantModeScreen_continueButton_QPushButton))

    test.vp("treatmentScreen33","Successful display of the treatment screen")

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 155, 26, 202, -18, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
    
    test.vp("treatmentScreen33","Successful display of retaining last set of Parameters")
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 55, 16, 133, -8, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup")
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 158, 20, 121, -11, 1, Qt.LeftButton)
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 33, 20, 51, -8, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    clickButton(waitForObject(names.treatmentCharacteristicsBar_pbEdit_QPushButton))
    clickButton(waitForObject(names.centralWidget_rejectButton_QPushButton))
    clickButton(waitForObject(names.flowRateFrame_mediumFlowRateButton_QPushButton))
    clickButton(waitForObject(names.hardnessFrame_smallHardnessButton_QPushButton))
    clickButton(waitForObject(names.stoneAssistantModeScreen_continueButton_QPushButton))

    test.vp("treatmentScreen34","Successful display of the treatment screen")

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 132, 31, 238, -11, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
    
    test.vp("treatmentScreen34","Successful display of retaining last set of Parameters")
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 74, 23, 79, -1, 1, Qt.LeftButton)
     
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup")
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 116, 19, 126, 4, 1, Qt.LeftButton)
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 56, 25, 36, 11, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    clickButton(waitForObject(names.treatmentCharacteristicsBar_pbEdit_QPushButton))
    clickButton(waitForObject(names.centralWidget_rejectButton_QPushButton))
    clickButton(waitForObject(names.hardnessFrame_mediumHardnessButton_QPushButton))
    clickButton(waitForObject(names.stoneAssistantModeScreen_continueButton_QPushButton))

    test.vp("treatmentScreen35","Successful display of the treatment screen")

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 164, 26, 215, 12, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
    
    test.vp("treatmentScreen35","Successful display of retaining last set of Parameters")
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 82, 21, 88, -13, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 169, 26, 110, 1, 1, Qt.LeftButton)
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 50, 20, 37, 9, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    clickButton(waitForObject(names.treatmentCharacteristicsBar_pbEdit_QPushButton))
    clickButton(waitForObject(names.centralWidget_rejectButton_QPushButton))
    clickButton(waitForObject(names.hardnessFrame_largeHardnessButton_QPushButton))
    clickButton(waitForObject(names.stoneAssistantModeScreen_continueButton_QPushButton))

    test.vp("treatmentScreen36","Successful display of the treatment screen")

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 207, 22, 154, 0, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
    
    test.vp("treatmentScreen36","Successful display of retaining last set of Parameters")
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 71, 22, 70, -1, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 198, 23, 75, 7, 1, Qt.LeftButton)
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 57, 29, 31, 8, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    clickButton(waitForObject(names.treatmentCharacteristicsBar_pbEdit_QPushButton))
    clickButton(waitForObject(names.centralWidget_rejectButton_QPushButton))
    clickButton(waitForObject(names.hardnessFrame_unknownHardnessButton_QPushButton))
    clickButton(waitForObject(names.stoneAssistantModeScreen_continueButton_QPushButton))

    test.vp("treatmentScreen37","Successful display of the treatment screen")

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 154, 24, 191, 3, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
    
    test.vp("treatmentScreen37","Successful display of retaining last set of Parameters")
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 66, 22, 113, 0, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 165, 30, 98, -13, 1, Qt.LeftButton)
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 48, 21, 42, 9, 1, Qt.LeftButton)
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup")
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    clickButton(waitForObject(names.treatmentCharacteristicsBar_pbEdit_QPushButton))
    clickButton(waitForObject(names.centralWidget_rejectButton_QPushButton))
    clickButton(waitForObject(names.flowRateFrame_unknownFlowRateButton_QPushButton))
    clickButton(waitForObject(names.hardnessFrame_smallHardnessButton_QPushButton))
    clickButton(waitForObject(names.stoneAssistantModeScreen_continueButton_QPushButton))

    test.vp("treatmentScreen38","Successful display of the treatment screen")

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 131, 16, 232, 27, 1, Qt.LeftButton)
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
    
    test.vp("treatmentScreen38","Successful display of retaining last set of Parameters")
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 44, 18, 162, 19, 1, Qt.LeftButton)
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup")
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 126, 22, 122, 18, 1, Qt.LeftButton)
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 38, 14, 61, 5, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup")
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    clickButton(waitForObject(names.treatmentCharacteristicsBar_pbEdit_QPushButton))
    clickButton(waitForObject(names.centralWidget_rejectButton_QPushButton))
    mouseClick(waitForObject(names.stoneAssistantModeScreen_hardnessFrame_QFrame), 76, 168, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.hardnessFrame_mediumHardnessButton_QPushButton))
    clickButton(waitForObject(names.stoneAssistantModeScreen_continueButton_QPushButton))

    test.vp("treatmentScreen39","Successful display of the treatment screen")

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 163, 23, 190, 0, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
    
    test.vp("treatmentScreen39","Successful display of retaining last set of Parameters")
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 56, 27, 153, -4, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 152, 25, 142, 1, 1, Qt.LeftButton)
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 41, 17, 49, 1, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    clickButton(waitForObject(names.treatmentCharacteristicsBar_pbEdit_QPushButton))
    clickButton(waitForObject(names.centralWidget_rejectButton_QPushButton))
    clickButton(waitForObject(names.hardnessFrame_largeHardnessButton_QPushButton))
    clickButton(waitForObject(names.stoneAssistantModeScreen_continueButton_QPushButton))

    test.vp("treatmentScreen40","Successful display of the treatment screen")

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 191, 35, 173, -2, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
    
    test.vp("treatmentScreen40","Successful display of retaining last set of Parameters")
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 45, 21, 128, -12, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 60, 28, 30, 2, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    clickButton(waitForObject(names.treatmentCharacteristicsBar_pbEdit_QPushButton))
    clickButton(waitForObject(names.centralWidget_rejectButton_QPushButton))
    clickButton(waitForObject(names.hardnessFrame_unknownHardnessButton_QPushButton))
    clickButton(waitForObject(names.stoneAssistantModeScreen_continueButton_QPushButton))

    test.vp("treatmentScreen41","Successful display of the treatment screen")

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 152, 23, 206, -16, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
    
    test.vp("treatmentScreen41","Successful display of retaining last set of Parameters")
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 53, 24, 102, -6, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 49, 24, 41, 3, 1, Qt.LeftButton)
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 153, 30, 126, -17, 1, Qt.LeftButton)
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 49, 19, 43, 22, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    clickButton(waitForObject(names.treatmentCharacteristicsBar_pbEdit_QPushButton))
    clickButton(waitForObject(names.centralWidget_rejectButton_QPushButton))
    clickButton(waitForObject(names.locationFrame_bladderLocationButton_QPushButton))
    clickButton(waitForObject(names.flowRateFrame_highFlowRateButton_QPushButton))
    clickButton(waitForObject(names.hardnessFrame_smallHardnessButton_QPushButton))
    clickButton(waitForObject(names.stoneAssistantModeScreen_continueButton_QPushButton))

    test.vp("treatmentScreen42","Successful display of the treatment screen")

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 229, 30, 190, -1, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
    
    test.vp("treatmentScreen42","Successful display of retaining last set of Parameters")
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 126, 20, 231, -8, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 243, 24, 92, 3, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    clickButton(waitForObject(names.treatmentCharacteristicsBar_pbEdit_QPushButton))
    clickButton(waitForObject(names.centralWidget_rejectButton_QPushButton))
    clickButton(waitForObject(names.hardnessFrame_mediumHardnessButton_QPushButton))
    clickButton(waitForObject(names.stoneAssistantModeScreen_continueButton_QPushButton))

    test.vp("treatmentScreen43","Successful display of the treatment screen")

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 325, 30, 81, 7, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup")
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
    
    test.vp("treatmentScreen43","Successful display of retaining last set of Parameters")
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 142, 18, 233, -7, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 206, 25, 35, 0, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    clickButton(waitForObject(names.treatmentCharacteristicsBar_pbEdit_QPushButton))
    clickButton(waitForObject(names.centralWidget_rejectButton_QPushButton))
    clickButton(waitForObject(names.hardnessFrame_largeHardnessButton_QPushButton))
    clickButton(waitForObject(names.stoneAssistantModeScreen_continueButton_QPushButton))

    test.vp("treatmentScreen44","Successful display of the treatment screen")

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 340, 30, 68, 2, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup")
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
    
    test.vp("treatmentScreen44","Successful display of retaining last set of Parameters")
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 142, 24, 192, -10, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 137, 36, 90, -9, 1, Qt.LeftButton)
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    clickButton(waitForObject(names.treatmentCharacteristicsBar_pbEdit_QPushButton))
    clickButton(waitForObject(names.centralWidget_rejectButton_QPushButton))
    clickButton(waitForObject(names.hardnessFrame_unknownHardnessButton_QPushButton))
    clickButton(waitForObject(names.stoneAssistantModeScreen_continueButton_QPushButton))

    test.vp("treatmentScreen45","Successful display of the treatment screen")

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 329, 22, 73, 12, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup")
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
    
    test.vp("treatmentScreen45","Successful display of retaining last set of Parameters")
        
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 130, 30, 267, -3, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup")
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 187, 37, 52, -2, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup")
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    clickButton(waitForObject(names.treatmentCharacteristicsBar_pbEdit_QPushButton))
    clickButton(waitForObject(names.centralWidget_rejectButton_QPushButton))
    clickButton(waitForObject(names.flowRateFrame_unknownFlowRateButton_QPushButton))
    clickButton(waitForObject(names.hardnessFrame_smallHardnessButton_QPushButton))
    clickButton(waitForObject(names.stoneAssistantModeScreen_continueButton_QPushButton))
     
    test.vp("treatmentScreen46","Successful display of the treatment screen")

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 241, 22, 168, 3, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup")
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
    
    test.vp("treatmentScreen46","Successful display of retaining last set of Parameters")
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 128, 25, 196, -13, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 136, 21, 104, 16, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    clickButton(waitForObject(names.treatmentCharacteristicsBar_pbEdit_QPushButton))
    clickButton(waitForObject(names.centralWidget_rejectButton_QPushButton))
    clickButton(waitForObject(names.hardnessFrame_mediumHardnessButton_QPushButton))
    clickButton(waitForObject(names.stoneAssistantModeScreen_continueButton_QPushButton))

    test.vp("treatmentScreen47","Successful display of the treatment screen")

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 328, 12, 87, 0, 1, Qt.LeftButton)
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
    
    test.vp("treatmentScreen47","Successful display of retaining last set of Parameters")
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 137, 27, 198, -11, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    clickButton(waitForObject(names.treatmentCharacteristicsBar_pbEdit_QPushButton))
    clickButton(waitForObject(names.centralWidget_acceptButton_QPushButton))
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 123, 24, 115, -3, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup")
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    clickButton(waitForObject(names.treatmentCharacteristicsBar_pbEdit_QPushButton))
    clickButton(waitForObject(names.centralWidget_rejectButton_QPushButton))
    clickButton(waitForObject(names.hardnessFrame_largeHardnessButton_QPushButton))
    clickButton(waitForObject(names.stoneAssistantModeScreen_continueButton_QPushButton))
     
    test.vp("treatmentScreen48","Successful display of the treatment screen")

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 337, 20, 62, 5, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup")
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
    
    test.vp("treatmentScreen48","Successful display of retaining last set of Parameters")
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 134, 30, 194, -9, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup")
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 139, 30, 94, -11, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup") 
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    clickButton(waitForObject(names.treatmentCharacteristicsBar_pbEdit_QPushButton))
    clickButton(waitForObject(names.centralWidget_rejectButton_QPushButton))
    clickButton(waitForObject(names.hardnessFrame_unknownHardnessButton_QPushButton))
    clickButton(waitForObject(names.stoneAssistantModeScreen_continueButton_QPushButton))
     
    test.vp("treatmentScreen49","Successful display of the treatment screen")

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 327, 29, 72, 12, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup")
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
    
    test.vp("treatmentScreen49","Successful display of retaining last set of Parameters")
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 134, 20, 239, -7, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup")
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
     
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 194, 31, 44, -2, 1, Qt.LeftButton)
    
    test.vp("exitpopup","Successful display of Exit Guided Mode Popup")
    if not handlePopup(required=True):
        test.fail("Expected popup was not handled.")
        return
    
    clickButton(waitForObject(names.treatmentCharacteristicsBar_pbEdit_QPushButton))
    clickButton(waitForObject(names.centralWidget_rejectButton_QPushButton))
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton_2))
