# -*- coding: utf-8 -*-

import names
from common import *

def main():
    enter_login_pin()

    clickButton(waitForObject(names.gbExpert_expertButton_QPushButton))

    mouseClick(waitForObject(names.peakPowerButton_nameLabel_QLabel), 28, 38, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_pw250_QPushButton_2))
    mouseClick(waitForObject(names.peakPowerButton_nameLabel_QLabel), 47, 34, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_pw125_QPushButton_2))
    mouseClick(waitForObject(names.peakPowerButton_nameLabel_QLabel), 57, 33, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_pw500_QPushButton_2))
    mouseClick(waitForObject(names.peakPowerButton_nameLabel_QLabel_3), 34, 36, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_pw250_QPushButton_2))
    mouseClick(waitForObject(names.peakPowerButton_iconLabel_QLabel_3), 6, 55, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_pw125_QPushButton_2))
    mouseClick(waitForObject(names.peakPowerButton_nameLabel_QLabel_3), 8, 35, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_pw500_QPushButton_2))
    test.vp("Left_Max_Peakpower")
    test.vp("Right_Max_Peakpower")
