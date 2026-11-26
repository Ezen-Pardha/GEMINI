# -*- coding: utf-8 -*-

import names


def main():
    doubleClick(waitForObject(names.numpad_pushButton_8_NumpadButton), 88, 51, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    clickButton(waitForObject(names.locationFrame_kidneyPcnlLocationButton_QPushButton))

    if test.vp("treatmentOptionsStone"):
        test.passes("Successful confirmation program displays the treatment options")
    else:
        test.fail("Failed confirmation program displays the treatment options")

    clickButton(waitForObject(names.flowRateFrame_mediumFlowRateButton_QPushButton))
    clickButton(waitForObject(names.hardnessFrame_largeHardnessButton_QPushButton))

    if test.vp("selectTreatmentOptionsStone"):
        test.passes("Successful confirmation program allows selection of treatment options")
    else:
        test.fail("Failed confirmation program allows selection of treatment options")

    clickButton(waitForObject(names.stoneAssistantModeScreen_continueButton_QPushButton))
    if test.vp("treatmentScreenStone"):
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
    
    if test.vp("frequnecyFillStone"):
        test.passes("Successful Confirmation of programs displaying fill range of Frequency")
    else:
        test.fail("Failed Confirmation of programs displaying fill range of Frequency")   

    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbSoftTissueAssistant_QToolButton))

    if test.vp("treatmentOptionsSoftTissue"):
        test.passes("Successful confirmation program displays the treatment options")
    else:
        test.fail("Failed confirmation program displays the treatment options")

    clickButton(waitForObject(names.gbSoftTissueProcedures_pbIncision_QPushButton))

    if test.vp("selectTreatmentOptionsSoftTissue"):
        test.passes("Successful confirmation program allows selection of treatment options")
    else:
        test.fail("Failed confirmation program allows selection of treatment options")

    clickButton(waitForObject(names.softTissueAssistantModeScreen_pbContinue_QPushButton))

    if test.vp("treatmentScreenSoftTissue"):
        test.passes("Successful confirmation program navigates to treatment screen")
    else:
        test.fail("Failed confirmation program navigates to treatment screen")
        
    if test.vp("averagePowerFillSoftTissue"):
        test.passes("Successful Confirmation of programs displaying fill range of Average Power")
    else:
        test.fail("Failed Confirmation of programs displaying fill range of Average Power")
        
    if test.vp("pulseEnergyFillSoftTissue"):
        test.passes("Successful Confirmation of programs displaying fill range of Pulse Energy")
    else:
        test.fail("Failed Confirmation of programs displaying fill range of Pulse Energy")
        
    if test.vp("frequencyFillSoftTissue"):
        test.passes("Successful Confirmation of programs displaying fill range of Frequency")
    else:
        test.fail("Failed Confirmation of programs displaying fill range of Frequency")

    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
