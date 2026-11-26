# -*- coding: utf-8 -*-

import names
from common import *

def main():
    enter_login_pin()

    clickButton(waitForObject(names.gbExpert_expertButton_QPushButton))
    snooze(2)
    if test.compare(str(waitForObjectExists(names.centralWidget_titleLabel_QLabel).text), "Version Not Supported"):
        clickButton(waitForObject(names.centralWidget_okButton_QPushButton_4))
    snooze(2)
    mouseClick(waitForObject(names.peakPowerButton_nameLabel_QLabel), 39, 34, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_pw1000_QPushButton))
    mouseClick(waitForObject(names.peakPowerButton_nameLabel_QLabel_3), 17, 47, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_pw1000_QPushButton))
    test.imagePresent("Verified Maximum PeakPower Left and Right Side")
    test.passes("Verified Maximum PeakPower")
    

    
    
