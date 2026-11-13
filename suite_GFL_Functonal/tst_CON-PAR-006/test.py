# -*- coding: utf-8 -*-

import names
from common import * 

def main():
    enter_login_pin()

    clickButton(waitForObject(names.mainFrame_okButton_QPushButton))
    clickButton(waitForObject(names.gbExpert_expertButton_QPushButton))
    mouseClick(waitForObject(names.peakPowerButton_iconLabel_QLabel), 11, 20, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.buttonsFrame_rejectButton_QPushButton_2))
    test.fail("No peakpower values are avalible in build")

    
    
