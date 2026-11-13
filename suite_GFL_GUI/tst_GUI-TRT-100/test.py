# -*- coding: utf-8 -*-

import names


def main():
    doubleClick(waitForObject(names.numpad_pushButton_8_NumpadButton), 81, 73, Qt.NoModifier, Qt.LeftButton)
    doubleClick(waitForObject(names.numpad_pushButton_8_NumpadButton), 81, 73, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    clickButton(waitForObject(names.locationFrame_kidneyPcnlLocationButton_QPushButton))
    clickButton(waitForObject(names.flowRateFrame_lowFlowRateButton_QPushButton))
    clickButton(waitForObject(names.hardnessFrame_mediumHardnessButton_QPushButton))
    clickButton(waitForObject(names.stoneAssistantModeScreen_continueButton_QPushButton))
    clickButton(waitForObject(names.stoneSenseFrame_pbStoneSense_QPushButton))
    clickButton(waitForObject(names.calibrationPopupDialog_pbMiddleButton_QPushButton))
    clickButton(waitForObject(names.pCalibrationSuccessFrame_pOKButton_QPushButton))

    if test.vp("stoneSenseEnabled"):
        test.passes("Successful Confirmation program enables StoneSense")
    else:
        test.fail("Failed Confirmation program enables StoneSense")

    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 67, 31, 328, -14, 1, Qt.LeftButton)

    if test.vp("exitGuidedPopup"):
        test.fail("Failed Confirmation program displays the “frequency too High” popup when StoneSense is enabled, instead there is a EXIT GUIDED POPUP ")
    else:
        test.fail("Failed Confirmation program displays the “frequency too High” popup when StoneSense is enabled, instead there is a EXIT GUIDED POPUP ")

    clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneQuickStart_QToolButton))
    mouseClick(waitForObjectItem(names.tabLeftMainPresets_leftPresetsView_PresetListView, "_1"), 457, 70, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.tabRightMainPresets_rightPresetsView_PresetListView, "_1"), 157, 56, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.quickStartScreen_pbContinue_QPushButton))
    mouseDrag(waitForObject(names.indexPicker_valuePicker_IntervalSlider_2), 160, 25, 155, -9, 1, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
