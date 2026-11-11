# -*- coding: utf-8 -*-

import names
from common import *

def main():
    enter_login_pin()

    clickButton(waitForObject(names.gbExpert_expertButton_QPushButton))
    mouseClick(waitForObject(names.peakPowerButton_iconLabel_QLabel_2), 7, 40, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_pw1000_QPushButton))
    mouseClick(waitForObject(names.peakPowerButton_nameLabel_QLabel_3), 17, 47, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_pw1000_QPushButton))
    test.imagePresent("Verified Maximum PeakPower Left and Right Side")
    test.passes("Verified Maximum PeakPower")
    

    
    
