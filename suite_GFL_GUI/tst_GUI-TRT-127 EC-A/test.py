# -*- coding: utf-8 -*-

import names


def main():
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton))
    clickButton(waitForObject(names.gbExpert_expertButton_QPushButton))
    mouseClick(waitForObject(names.peakPowerButton_nameLabel_QLabel_2), 37, 35, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_pw250_QPushButton_2))
    mouseClick(waitForObject(names.indexPicker_valuePicker_IntervalSlider), 272, 22, Qt.NoModifier, Qt.LeftButton)

    mouseClick(waitForObject(names.peakPowerButton_nameLabel_QLabel_3), 56, 34, Qt.NoModifier, Qt.LeftButton)
    test.imagePresent("Right PeakPower")

    mouseClick(waitForObject(names.peakPowerButton_iconLabel_QLabel_2), 20, 41, Qt.NoModifier, Qt.LeftButton)
    test.imagePresent("Select PeakPower")
    sendEvent("QMouseEvent", waitForObject(names.backgroundShadowWidget_QWidget), QEvent.MouseButtonPress, 1189, 165, Qt.LeftButton, 1, 0)
