# -*- coding: utf-8 -*-

import names
from common import *

def main():
    enter_login_pin()
    test.log("SVV TAG GUI-TRT-077: Stone Sense Button Enabled in STANDBY State")
    navigateto_Treatmentscreen_stone_QuickStart()
   
    try:
        obj = waitForObjectExists(
            names.stoneSenseFrame_pbStoneSense_QPushButton,
            5000
        )

        if obj.visible and obj.enabled:
            clickButton(obj)
            test.passes("StoneSense button is clickable and clicked")
        else:
            test.fail("StoneSense button is not visible or enabled")

    except Exception as e:
        
        test.fail("StoneSense button is not found or could not be clicked: " + str(e))
    
    clickButton(waitForObject(names.frame_pCancelButton_QPushButton))
    
    test.log("SVV TAG GUI-TRT-078: Stone Sense Button Disabled in READY State")
    
    clickButton(waitForObject(names.stateSwitch_readyButton_QPushButton))
    mouseClick(waitForObject(names.treatmentScreen_bottomBar_QFrame), 646, 0, Qt.NoModifier, Qt.LeftButton)
    try:
        obj = findObject(names.stoneSenseFrame_pbStoneSense_QPushButton)

        if obj.visible:
            test.fail("StoneSense button is visible in READY State")
        else:
            test.passes("StoneSense button is not visible in READY State as expected")

    except LookupError:
        test.passes("StoneSense button is not found in READY State as expected")
    
    
    

  
    
