# -*- coding: utf-8 -*-

import names
from common import *

def main():
    enter_login_pin()

    clickButton(waitForObject(names.gbExpert_expertButton_QPushButton))
    mouseClick(waitForObject(names.peakPowerButton_nameLabel_QLabel_2), 70, 30, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_pw500_QPushButton_2))
    mouseClick(waitForObject(names.peakPowerButton_iconLabel_QLabel_3), 6, 32, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_pw500_QPushButton_2))
    test.imagePresent("imageVerified Maximum Peak Power On Left and Right Side")
    test.passes("Verified Maximum PeakPower")
    

    

  

    
    
    
    
