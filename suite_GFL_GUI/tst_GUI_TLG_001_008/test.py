# -*- coding: utf-8 -*-
from common import *

import names

def main():
    enter_login_pin()

    clickButton(waitForObject(names.homeScreen_logButton_QPushButton))
    test.vp("Verified Treatment Logs Screen")
    
    clickButton(waitForObject(names.treatmentLogScreen_pbBack_QPushButton))
    clickButton(waitForObject(names.homeScreen_logButton_QPushButton))
    #mouseClick(waitForObject(names.treatmentLogScreen_activeUserProfile_QLabel, 182236), 79, 22, Qt.NoModifier, Qt.LeftButton)
    
    label_obj = waitForObject(names.treatmentLogScreen_activeUserProfile_QLabel)
    profile = str(label_obj.text)
    test.log(profile)
    
    mouseClick(waitForObject(names.treatmentLogScreen_lbProfileName_QLabel), 30, 25, Qt.NoModifier, Qt.LeftButton)
    label_obj = waitForObject(names.treatmentLogScreen_lbProfileName_QLabel)
    profile_name = str(label_obj.text)
    test.log(profile_name)
    
    if profile_name == "Default":
        test.passes("Default profile is loaded")
    else:
        test.fail(profile_name + ": is loaded ")
    
    #test.breakpoint()
  
