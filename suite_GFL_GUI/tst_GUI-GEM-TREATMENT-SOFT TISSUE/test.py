# -*- coding: utf-8 -*-

import names
from common import *


def main():
    enter_login_pin()
    test.log("SVV TAG GUI-TRT-085: Soft Tissue-->Guided mode to display procedure selected in Top Banner")
    clickButton(waitForObject(names.homeScreen_pbSoftTissueAssistant_QToolButton))
    test.log("Soft tissue Guided Procedure screen Verified")
    clickButton(waitForObject(names.gbSoftTissueProcedures_pbIncision_QPushButton))
    test.log("Selected Soft tissue Procedure")
    clickButton(waitForObject(names.softTissueAssistantModeScreen_pbContinue_QPushButton))
    test.imagePresent("Procedure Edit")
    test.log("Treatment screen Procedure Edit button verified")
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton_4))
    
    test.log("SVV TAG GUI-TRT-086: Soft Tissue-->Guided mode to have procedure Edit Button in Top Banner")
     
    clickButton(waitForObject(names.homeScreen_pbSoftTissueAssistant_QToolButton))
    test.log("Soft tissue Guided Procedure screen Verified")
    clickButton(waitForObject(names.gbSoftTissueProcedures_pbIncision_QPushButton))
    test.log("Selected Soft tissue Procedure")
    clickButton(waitForObject(names.softTissueAssistantModeScreen_pbContinue_QPushButton))
    test.imagePresent("Procedure Edit")
    clickButton(waitForObject(names.treatmentCharacteristicsBar_pbEdit_QPushButton_2))
    title = str(waitForObjectExists(names.centralWidget_titleLabel_QLabel_2).text)
    
    if test.compare(title, "PROCEDURE"):
        test.passes("PROCEDURE Popup is verified successfully in Treatment screen")
    else:
        test.fail("PROCEDURE Popup verification failed. Actual text: " + title)
    
 
