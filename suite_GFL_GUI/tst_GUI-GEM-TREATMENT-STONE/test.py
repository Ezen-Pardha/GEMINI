# -*- coding: utf-8 -*-

import names
from common import *

def main():
    
    enter_login_pin()
    
    test.log("SVV TAG GUI-TRT-083: Stone Characteristics in Top Banner")
    
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    test.log("Guided modes Treatment screen verified")
    clickButton(waitForObject(names.locationFrame_kidneyPcnlLocationButton_QPushButton))
    clickButton(waitForObject(names.flowRateFrame_lowFlowRateButton_QPushButton))
    clickButton(waitForObject(names.hardnessFrame_smallHardnessButton_QPushButton))
    test.log("Guided modes Location, FlowRate, Hardness is selected")
    clickButton(waitForObject(names.stoneAssistantModeScreen_continueButton_QPushButton))
    mouseClick(waitForObject(names.topBar_buttonsBar_ButtonsBar_4), 619, 41, Qt.NoModifier, Qt.LeftButton)
    test.log("Guided Treatment Screen is verified")
    clickButton(waitForObject(names.treatmentCharacteristicsBar_pbEdit_QPushButton))
    test.compare(str(waitForObjectExists(names.centralWidget_titleLabel_QLabel).text), "STONE CHARACTERISTICS")
    if object.exists(names.centralWidget_titleLabel_QLabel):
        popup = waitForObject(names.centralWidget_titleLabel_QLabel)

        if str(popup.text).strip() == "STONE CHARACTERISTICS":
            test.passes("Stone Characteristics popup is present and text is verified")
        else:
            test.fail("Popup is present, but the text does not match")
    else:
        test.log("Stone Characteristics popup is not present")
    clickButton(waitForObject(names.centralWidget_acceptButton_QPushButton))
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton_4))
    
     
    test.log("SVV TAG GUI-TRT-084: EDIT Stone Characteristics in Top Banner")
    
    
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    test.log("Guided modes Treatment screen verified")
    clickButton(waitForObject(names.locationFrame_kidneyPcnlLocationButton_QPushButton))
    clickButton(waitForObject(names.flowRateFrame_lowFlowRateButton_QPushButton))
    clickButton(waitForObject(names.hardnessFrame_smallHardnessButton_QPushButton))
    test.log("Guided modes Location, FlowRate, Hardness is selected")
    clickButton(waitForObject(names.stoneAssistantModeScreen_continueButton_QPushButton))
    mouseClick(waitForObject(names.topBar_buttonsBar_ButtonsBar_4), 619, 41, Qt.NoModifier, Qt.LeftButton)
    test.log("Guided Treatment Screen is verified")
    clickButton(waitForObject(names.treatmentCharacteristicsBar_pbEdit_QPushButton))
    test.compare(str(waitForObjectExists(names.centralWidget_titleLabel_QLabel).text), "STONE CHARACTERISTICS")
    if object.exists(names.centralWidget_titleLabel_QLabel):
        popup = waitForObject(names.centralWidget_titleLabel_QLabel)

        if str(popup.text).strip() == "STONE CHARACTERISTICS":
            test.passes("Stone Characteristics popup is present and text is verified")
        else:
            test.fail("Popup is present, but the text does not match")
    else: 
        test.log("Stone Characteristics popup is not present")
    mouseClick(waitForObject(names.centralWidget_QFrame_3), 564, 26, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_rejectButton_QPushButton))
    clickButton(waitForObject(names.hardnessFrame_mediumHardnessButton_QPushButton))
    clickButton(waitForObject(names.stoneAssistantModeScreen_continueButton_QPushButton))
    test.log("Stone Characteristics Edited the hardness and continued")
    
