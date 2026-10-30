# -*- coding: utf-8 -*-

import names


def main():
    doubleClick(waitForObject(names.numpad_pushButton_8_NumpadButton), 61, 52, Qt.NoModifier, Qt.LeftButton)
    doubleClick(waitForObject(names.numpad_pushButton_8_NumpadButton), 61, 52, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton))
    clickButton(waitForObject(names.gbExpert_expertButton_QPushButton))
    clickButton(waitForObject(names.pulseModeWidget_saveButton_QPushButton))
    clickButton(waitForObject(names.pulseModeWidget_saveButton_QPushButton_3))
    clickButton(waitForObject(names.centralWidget_okButton_QPushButton_3))
    clickButton(waitForObject(names.centralWidget_pbName_QPushButton))
    mouseClick(waitForObject(names.keyboardPopup_lbText_QLabel_2), 78, 49, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_pbName_QPushButton))

    clickButton(waitForObject(names.centralWidget_pbName_QPushButton))
    mouseClick(waitForObject(names.keyboardPopup_lbText_QLabel), 29, 19, Qt.NoModifier, Qt.LeftButton)
    test.compare(str(waitForObjectExists(names.centralWidget_okButton_QPushButton_2).text), "OK")

    mouseClick(waitForObject(names.keyboardPopup_lbText_QLabel_2), 104, 21, Qt.NoModifier, Qt.LeftButton)
