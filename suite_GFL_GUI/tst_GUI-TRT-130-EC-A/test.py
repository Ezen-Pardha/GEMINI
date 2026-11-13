# -*- coding: utf-8 -*-

import names
from common import *

def main():
    enter_login_pin()

    clickButton(waitForObject(names.gbExpert_expertButton_QPushButton))
    mouseClick(waitForObject(names.peakPowerButton_iconLabel_QLabel_2), 11, 33, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_pw500_QPushButton_2))
    mouseClick(waitForObject(names.peakPowerButton_nameLabel_QLabel_3), 61, 26, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_pw500_QPushButton_2))
    mouseClick(waitForObject(names.peakPowerButton_iconLabel_QLabel_3), 11, 31, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_rejectButton_QPushButton))
    test.imagePresent("Verified maximum peakpuwer on Righ and Left side")

    
    
    
    
