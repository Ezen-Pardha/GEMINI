# -*- coding: utf-8 -*-

from common import *
import names


def main():
    test.log("START: GUI-TRT-105 and GUI-TRT-106 - Treatment Screen Pulse Mode Tests")
    test.log("Preparing application and opening Treatment screen")

    enter_login_pin()

    test.log("GUI-TRT-105: Selecting Manual mode")
    clickButton(waitForObject(names.gbExpert_expertButton_QPushButton))

    test.log("Opening Pulse Mode selection")
    sendEvent("QMouseEvent", waitForObject(names.pulseModeWidget_frequencyWidget_ParameterSettingsWidget_2), QEvent.MouseButtonDblClick, 622, 138, Qt.LeftButton, 1, 0)
    sendEvent("QMouseEvent", waitForObject(names.pulseModeWidget_frequencyWidget_ParameterSettingsWidget_2), QEvent.MouseButtonRelease, 622, 138, Qt.LeftButton, 0, 0)

    test.log("GUI-TRT-105: Verifying Regular and Continuous Wave pulse information popups")

    test.log("Verifying Regular Pulse information popup")
    mouseClick(waitForObject(names.modeButton_nameLabel_QLabel), 84, 38, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.square_icon_QPushButton))
    test.vp("regularPulsePopupInfo")
    test.log("Regular Pulse information popup verification completed")

    test.log("Closing Regular Pulse popup and opening Continuous Wave information")
    clickButton(waitForObject(names.centralWidget_OKButton_QPushButton_3))
    clickButton(waitForObject(names.cW_icon_QPushButton))
    test.vp("continuousWavePopupInfo")
    test.log("Continuous Wave information popup verification completed")

    test.log("GUI-TRT-105: Regular and Continuous Wave popup verification completed")
    test.log("GUI-TRT-105: Starting Advanced Pulse Mode popup information verification")

    test.log("Closing Continuous Wave popup and opening Minimal Retropulsion Pulse information")
    clickButton(waitForObject(names.centralWidget_OKButton_QPushButton_3))
    clickButton(waitForObject(names.mRP_icon_QPushButton))
    test.vp("minimalRetropulsionPulsePopupInfo")
    test.log("Minimal Retropulsion Pulse information popup verification completed")

    test.log("Closing Minimal Retropulsion Pulse popup and opening Fragmentation Pulse information")
    clickButton(waitForObject(names.centralWidget_OKButton_QPushButton_3))
    clickButton(waitForObject(names.fragmentation_icon_QPushButton))
    test.vp("fragmentationPulsePopupInfo")
    test.log("Fragmentation Pulse information popup verification completed")

    test.log("Closing Fragmentation Pulse popup and opening Minimal Carbonization Pulse information")
    clickButton(waitForObject(names.centralWidget_OKButton_QPushButton_3))
    clickButton(waitForObject(names.cleaning_icon_QPushButton))
    test.vp("minimalCarbonizationPulsePopupInfo")
    test.log("Minimal Carbonization Pulse information popup verification completed")

    test.log("Closing Minimal Carbonization Pulse popup and opening Enucleation Pulse information")
    clickButton(waitForObject(names.centralWidget_OKButton_QPushButton_3))
    clickButton(waitForObject(names.enucleation_icon_QPushButton))
    test.vp("enucleationPulsePopupInfo")
    test.log("Enucleation Pulse information popup verification completed")

    test.log("GUI-TRT-105: Advanced Pulse Mode popup information verification completed")

    test.log("Closing Enucleation Pulse popup")
    clickButton(waitForObject(names.centralWidget_OKButton_QPushButton_3))
    clickButton(waitForObject(names.buttonsFrame_rejectButton_QPushButton_5))

    sendEvent("QMouseEvent", waitForObject(names.bottomBar_lbPedalStatusIcon_QLabel), QEvent.MouseButtonDblClick, 35, 32, Qt.LeftButton, 1, 0)
    sendEvent("QMouseEvent", waitForObject(names.bottomBar_lbPedalStatusIcon_QLabel), QEvent.MouseButtonRelease, 35, 32, Qt.LeftButton, 0, 0)

    test.log("Returning to Home screen")
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton_4))

    test.log("GUI-TRT-105: Treatment Screen Pulse Mode Popup Info test execution completed")

    test.log("GUI-TRT-106: Starting Advanced Pulse Mode selection and Peach Colour Highlight verification")

    test.log("Selecting Manual mode")
    clickButton(waitForObject(names.gbExpert_expertButton_QPushButton))

    test.log("Opening Pulse Mode selection")
    mouseClick(waitForObject(names.modeButton_nameLabel_QLabel), 93, 28, Qt.NoModifier, Qt.LeftButton)

    test.log("Selecting Minimal Retropulsion advanced pulse mode")
    clickButton(waitForObject(names.centralWidget_MRP_QPushButton_2))
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton_2))
    test.vp("minimalRetropulsionPulsePeachColour")
    test.log("Minimal Retropulsion Pulse peach colour highlight verification completed")

    test.log("Selecting Fragmentation advanced pulse mode")
    mouseClick(waitForObject(names.modeButton_nameLabel_QLabel), 78, 23, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_Fragmentation_QPushButton_2))
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton_2))
    test.vp("fragmentationPulsePeachColour")
    test.log("Fragmentation Pulse peach colour highlight verification completed")

    test.log("Selecting Minimal Carbonization advanced pulse mode")
    mouseClick(waitForObject(names.modeButton_nameLabel_QLabel), 83, 46, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_Cleaning_QPushButton_2))
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton_2))
    test.vp("minimalCarbonizationPulsePeachColour")
    test.log("Minimal Carbonization Pulse peach colour highlight verification completed")

    test.log("Selecting Enucleation advanced pulse mode")
    mouseClick(waitForObject(names.modeButton_nameLabel_QLabel), 96, 34, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_Enucleation_QPushButton_2))
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton_2))
    test.vp("enucleationPulsePeachColour")
    test.log("Enucleation Pulse peach colour highlight verification completed")

    test.log("GUI-TRT-106: Advanced Pulse Mode peach colour highlight verification completed")

    test.log("Returning to Home screen")
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton_4))

    test.log("GUI-TRT-105: Treatment Screen Pulse Mode Popup Info test execution completed")
    test.log("GUI-TRT-106: Treatment Screen Advanced Pulse Mode Peach Colour Highlight test execution completed")
    test.log("END: GUI-TRT-105 and GUI-TRT-106")