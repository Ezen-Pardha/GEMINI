# -*- coding: utf-8 -*-

import names


def main():
    doubleClick(waitForObject(names.numpad_pushButton_8_NumpadButton), 60, 60, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton))    
    clickButton(waitForObject(names.homeScreen_pbStoneQuickStart_QToolButton))
    mouseClick(waitForObjectItem(names.tabLeftMainPresets_leftPresetsView_PresetListView, "_1"), 464, 33, Qt.NoModifier, Qt.LeftButton)

    if test.vp("treatmentOptions"):
        test.passes("Successful confirmation program displays the treatment options")
    else:
        test.fail("Failed confirmation program displays the treatment options")

    mouseClick(waitForObjectItem(names.tabRightMainPresets_rightPresetsView_PresetListView, "_1"), 195, 54, Qt.NoModifier, Qt.LeftButton)

    if test.vp("selectTreatmentOptions"):
        test.passes("Successful confirmation program allows selection of treatment options")
    else:
        test.fail("Failed confirmation program allows selection of treatment options")

    clickButton(waitForObject(names.quickStartScreen_pbContinue_QPushButton))    

    if test.vp("treatmentScreen"):
        test.passes("Successful confirmation program navigates to treatment screen")
    else:
        test.fail("Failed confirmation program navigates to treatment screen")

    if test.vp("averagePowerFillStone"):
        test.passes("Successful Confirmation of programs displaying fill range of Average Power")
    else:
        test.fail("Failed Confirmation of programs displaying fill range of Average Power")
    
    if test.vp("pulseEnergyFillStone"):
        test.passes("Successful Confirmation of programs displaying fill range of Pulse Energy")
    else:
        test.fail("Failed Confirmation of programs displaying fill range of Pulse Energy")
        
    if test.vp("frequencyFillStone"):
        test.passes("Successful Confirmation of programs displaying fill range of Frequency")
    else:
        test.fail("Failed Confirmation of programs displaying fill range of Frequency")    

    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton, 56313))
    clickButton(waitForObject(names.homeScreen_pbSoftTissueQuickStart_QToolButton))
    mouseClick(waitForObjectItem(names.tabLeftMainPresets_leftPresetsView_PresetListView, "_1"), 411, 56, Qt.NoModifier, Qt.LeftButton)

    if test.vp("treatmentOptionSoftTissue"):
        test.passes("Successful confirmation program displays the treatment options")
    else:
        test.fail("Failed confirmation program displays the treatment options")

    mouseClick(waitForObjectItem(names.tabRightMainPresets_rightPresetsView_PresetListView, "_2"), 208, 54, Qt.NoModifier, Qt.LeftButton)

    if test.vp("selectTreatmentScreenOptions"):
        test.passes("Successful confirmation program allows selection of treatment options")
    else:
        test.fail("Failed confirmation program allows selection of treatment options")

    clickButton(waitForObject(names.quickStartScreen_pbContinue_QPushButton))
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton_2))

    if test.vp("treatmetScreenSoftTissue"):
        test.passes("Successful confirmation program navigates to treatment screen")
    else:
        test.fail("Failed confirmation program navigates to treatment screen")    

    if test.vp("averagePowerFillSoftTissue"):
        test.passes("Successful Confirmation of programs displaying fill range of Average Power")
    else:
        test.fail("Failed Confirmation of programs displaying fill range of Average Power")
        
    if test.vp("frequencyFillSoftTissue"):
        test.passes("Successful Confirmation of programs displaying fill range of Frequency")
    else:
        test.fail("Failed Confirmation of programs displaying fill range of Frequency") 
    
    if test.vp("pulseEnergyFillSoftTissue"):
        test.passes("Successful Confirmation of programs displaying fill range of Pulse Energy")
    else:
        test.fail("Failed Confirmation of programs displaying fill range of Pulse Energy")

    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
