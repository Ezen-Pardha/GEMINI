# -*- coding: utf-8 -*-
from common import *

import names

def main():
    enter_login_pin()

    clickButton(waitForObject(names.homeScreen_logButton_QPushButton))

    test.vp("Verified Treatment Logs Screen")

    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton_9))
    clickButton(waitForObject(names.homeScreen_logButton_QPushButton))
    clickButton(waitForObject(names.treatmentLogScreen_pbBack_QPushButton))
    # test.vp("Verified Treatment Logs Screen")
    clickButton(waitForObject(names.homeScreen_logButton_QPushButton))
    mouseClick(waitForObject(names.dATE_HeaderViewItem), 11, 10, Qt.NoModifier, Qt.LeftButton)
    test.vp("Verified Treatment Logs Screen")
    mouseClick(waitForObject(names.topBar_buttonsBar_ButtonsBar_8), 147, 31, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.topBar_buttonsBar_ButtonsBar_8), 326, 34, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.treatmentLogScreen_activeUserProfile_QLabel), 78, 24, Qt.NoModifier, Qt.LeftButton)
    test.vp("Verified Treatment Logs Screen")
    mouseClick(waitForObject(names.treatmentLogScreen_lbProfileName_QLabel), 36, 22, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton_9))

  
