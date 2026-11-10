# -*- coding: utf-8 -*-

import names
from common import *

def main():
    enter_login_pin()

    clickButton(waitForObject(names.mainFrame_okButton_QPushButton))
    clickButton(waitForObject(names.gbExpert_expertButton_QPushButton))
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider, 39297), 84, 20, 11, 0, 1, Qt.LeftButton)
    clickButton(waitForObject(names.pulseEnergyWidget_decrementButton_QPushButton))
    snooze(2)
    mouseClick(waitForObject(names.pulseEnergyWidget_nameLabel_QLabel_3), 90, 42, Qt.NoModifier, Qt.LeftButton)
    test.fail("The maximum frequency for the 2 J pulse energy setting at the 125 W peak power level is unavailable in the build ")
    

    
    
