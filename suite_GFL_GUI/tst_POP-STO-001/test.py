# -*- coding: utf-8 -*-

import names
from squish import *


def main():
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    if test.vp("stoneGuidedModeCharacteristicsScreen"):
        test.passes("Successful confirmation program displays the stone guided mode characteristics screen.")
    else:
        test.fail("Failed confirmation program displays the stone guided mode characteristics screen.")

    clickButton(waitForObject(names.locationFrame_kidneyPcnlLocationButton_QPushButton))
    clickButton(waitForObject(names.flowRateFrame_lowFlowRateButton_QPushButton))
    clickButton(waitForObject(names.hardnessFrame_smallHardnessButton_QPushButton))

    if test.vp("stoneGuided_Characteristics"):
        test.passes("Successful Confirmation program allows selection of location, flow rate and hardness.")
    else:
        test.fail("Failed Confirmation program allows selection of location, flow rate and hardness.")

    clickButton(waitForObject(names.stoneAssistantModeScreen_continueButton_QPushButton))    

    if test.vp("stoneGuided_Treatmentscreen"):
        test.passes("Successful Confirmation program navigates to treatment screen.")
    else:
        test.fail("Failed Confirmation program navigates to treatment screen.")

    clickButton(waitForObject(names.treatmentCharacteristicsBar_pbEdit_QPushButton))
    
    if test.vp("stoneCharacteristicPopup"):
        test.passes("Successful Confirmation program displays the stone characteristics popup. ")
    else:
        test.fail("Failed Confirmation program displays the stone characteristics popup. ")

    clickButton(waitForObject(names.centralWidget_rejectButton_QPushButton))
    
    if test.vp("StoneCharacteristicsScreen"):
        test.passes("Successful Confirmation program displays the stone characteristics screen")
    else:
        test.fail("Failed Confirmation program displays the stone characteristics screen")

    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton_2))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    if test.vp("stoneGuidedModeCharacteristicsScreen"):
        test.passes("Successful confirmation program displays the stone guided mode characteristics screen.")
    else:
        test.fail("Failed confirmation program displays the stone guided mode characteristics screen.")
        
    clickButton(waitForObject(names.locationFrame_kidneyPcnlLocationButton_QPushButton))
    clickButton(waitForObject(names.flowRateFrame_lowFlowRateButton_QPushButton))
    clickButton(waitForObject(names.hardnessFrame_smallHardnessButton_QPushButton))
    
    if test.vp("stoneGuided_Characteristics"):
        test.passes("Successful Confirmation program allows selection of location, flow rate and hardness.")
    else:
        test.fail("Failed Confirmation program allows selection of location, flow rate and hardness.")
        
    clickButton(waitForObject(names.stoneAssistantModeScreen_continueButton_QPushButton))
    
    if test.vp("stoneGuided_Treatmentscreen"):
        test.passes("Successful Confirmation program navigates to treatment screen.")
    else:
        test.fail("Failed Confirmation program navigates to treatment screen.")
        
    clickButton(waitForObject(names.treatmentCharacteristicsBar_pbEdit_QPushButton))
    
    if test.vp("stoneCharacteristicPopup"):
        test.passes("Successful Confirmation program displays the stone characteristics popup. ")
    else:
        test.fail("Failed Confirmation program displays the stone characteristics popup. ")
        
    clickButton(waitForObject(names.centralWidget_acceptButton_QPushButton))
    
    if test.vp("stoneGuided_Treatmentscreen"):
        test.passes("Successful Confirmation program closes popup.")
    else:
        test.fail("Failed Confirmation program closes popup.")
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    if test.vp("stoneGuidedModeCharacteristicsScreen"):
        test.passes("Successful confirmation program displays the stone guided mode characteristics screen.")
    else:
        test.fail("Failed confirmation program displays the stone guided mode characteristics screen.")
        
    clickButton(waitForObject(names.locationFrame_kidneyPcnlLocationButton_QPushButton))
    clickButton(waitForObject(names.flowRateFrame_lowFlowRateButton_QPushButton))
    clickButton(waitForObject(names.hardnessFrame_smallHardnessButton_QPushButton))
    
    if test.vp("stoneGuided_Characteristics"):
        test.passes("Successful Confirmation program allows selection of location, flow rate and hardness.")
    else:
        test.fail("Failed Confirmation program allows selection of location, flow rate and hardness.")
        
    clickButton(waitForObject(names.stoneAssistantModeScreen_continueButton_QPushButton))
    
    if test.vp("stoneGuided_Treatmentscreen"):
        test.passes("Successful Confirmation program closes popup.")
    else:
        test.fail("Failed Confirmation program closes popup.")
        
    clickButton(waitForObject(names.treatmentCharacteristicsBar_pbEdit_QPushButton))
    
    if test.vp("locationWidget"):
        test.passes("Successful Confirmation program displays location in the stone characteristics popup.")
    else:
        test.fail("Failed Confirmation program displays location in the stone characteristics popup.")
        
    if test.vp("flowRateWidget"):
        test.passes("Successful Confirmation program displays the flow rate in the stone characteristics popup.")
    else:
        test.fail("Failed Confirmation program displays the flow rate in the stone characteristics popup.")
        
    if test.vp("hardnessWidget"):
        test.passes("Successful Confirmation program displays the hardness in the stone characteristics popup.")
    else:
        test.fail("Failed Confirmation program program displays the hardness in the stone characteristics popup.")        

    clickButton(waitForObject(names.centralWidget_acceptButton_QPushButton, 32050))
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
