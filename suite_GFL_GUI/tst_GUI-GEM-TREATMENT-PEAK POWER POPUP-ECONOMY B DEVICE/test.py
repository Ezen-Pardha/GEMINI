# -*- coding: utf-8 -*-

import names
from common import *

def main():
    test.log("SVV TAG POP-PKP-001:Peak Power Selection Popup Low Button")
    enter_login_pin()
    verify_economy_type()
    clickButton(waitForObject(names.buttonsBar_backButton_QPushButton))
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton_8))
    clickButton(waitForObject(names.gbExpert_expertButton_QPushButton))
    test.passes("Manual treatment screen is verified") 
    test.vp("peakPowerMode")
    mouseClick(waitForObject(names.modeButton_nameLabel_QLabel, 126880), 54, 12, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_Square_QPushButton))
    mouseClick(waitForObject(names.peakPowerButton_nameLabel_QLabel_2, 455823), 59, 25, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_pw125_QPushButton_2, 149140))
    if test.imagePresent("lowPeakPower "):
        test.passes("Low Peak Power image is present and verified.")
    else:
        test.fail("Low Peak Power image is not present.")
    
    mouseClick(waitForObject(names.pulseModeWidget_buttonsWidget_QWidget), 474, 9, Qt.NoModifier, Qt.LeftButton)
    test.passes("Peak Power button is verified in the left pedal")
    test.imagePresent("RighPedalRegularPulse")
    test.passes("Right Pedal regular pulse button verified")
    test.imagePresent("rightPeakPower")
    test.passes("Right Pedal PeakPower button is verified")
     
    test.log("SVV TAG POP-PKP-001:Peak Power Selection Popup Low Button")
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton_4))
    clickButton(waitForObject(names.gbExpert_expertButton_QPushButton))
    test.passes("Manual treatment screen is verified")   
    test.imagePresent("pulseModeButton")
    test.passes("Pulse Mode button is verified in the left pedal")
    mouseClick(waitForObject(names.peakPowerButton_nameLabel_QLabel_2, 181302), 41, 38, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_pw250_QPushButton_2))
    test.imagePresent("peakPowerMedium")
    test.passes("Medium Peak power button is verified ")
    test.imagePresent("rightRegularPulseMedium")
    test.passes("Right Regular pulse button is verified ")
    mouseClick(waitForObject(names.peakPowerButton_nameLabel_QLabel_3), 66, 38, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_pw250_QPushButton_2))
    test.imagePresent("rightpeakPowerMedium", { "occurrence": 2 })
    test.passes("Right peak power Medium button is verified ")
   
    
    
    
