# -*- coding: utf-8 -*-

import names


def main():
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    mouseClick(waitForObject(names.fiberVerificationWarningDialog_mainFrame_QFrame), 607, 544, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton))
    clickButton(waitForObject(names.gbExpert_expertButton_QPushButton))
    mouseClick(waitForObject(names.peakPowerButton_iconLabel_QLabel_2), 22, 20, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_pw125_QPushButton_2))

    mouseClick(waitForObject(names.peakPowerButton_iconLabel_QLabel_2), 14, 39, Qt.NoModifier, Qt.LeftButton)
    test.imagePresent("Left PeakPower")
    clickButton(waitForObject(names.centralWidget_rejectButton_QPushButton))
    mouseClick(waitForObject(names.peakPowerButton_iconLabel_QLabel_3), 21, 33, Qt.NoModifier, Qt.LeftButton)
    test.imagePresent("RPeakPower")

    mouseClick(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 313, 30, Qt.NoModifier, Qt.LeftButton)
