

import names
from common import *


def verify_image(image_name, pass_message, fail_message):
    """Verify a saved Squish image and report a clear result."""
    if test.imagePresent(image_name):
        test.passes(pass_message)
        return True

    test.fail(fail_message)
    return False


def verify_text(object_name, expected_text, pass_message, fail_message):
    """Verify an object's text and report a clear result."""
    actual_text = str(waitForObjectExists(object_name).text)

    if test.compare(actual_text, expected_text):
        test.passes(pass_message)
        return True

    test.fail(f"{fail_message}. Actual text: {actual_text!r}")
    return False


def main():
    enter_login_pin()

    test.log("SVV TAG POP-SAV-001: Save preset popup left and right pedal")

    clickButton(waitForObject(names.gbExpert_expertButton_QPushButton))
    test.vp("Manual Treatment Screen")

    clickButton(waitForObject(names.pulseModeWidget_saveButton_QPushButton))
    test.log("Preset popup opened")

    mouseClick(
        waitForObject(names.progressFrame_valueProgress_QProgressBar_3),
        27, 6, Qt.NoModifier, Qt.LeftButton
    )
    mouseDrag(
        waitForObject(
            names.pulseModeWidget_averagePowerWidget_ParameterWithEnumerableValueWidget_3
        ),
        100, 106, 15, 0, 1, Qt.LeftButton
    )
    test.vp("Left Preset Popup")
    test.log("Left Preset Popup verification executed")

    mouseClick(
        waitForObject(names.backgroundShadowWidget_QWidget),
        713, 86, Qt.NoModifier, Qt.LeftButton
    )
    clickButton(waitForObject(names.centralWidget_pbClose_QPushButton))

    clickButton(waitForObject(names.pulseModeWidget_saveButton_QPushButton_2))
    test.vp("Right Preset Popup")
    clickButton(waitForObject(names.centralWidget_pbClose_QPushButton))
    test.log("Right Preset Popup verification executed")

    test.log(
        "SVV TAG POP-SAV-002: Save Preset Popup Displays Current Laser Parameters Upon Initialization"
    )

    mouseClick(
        waitForObject(names.topBar_buttonsBar_ButtonsBar_4),
        419, 60, Qt.NoModifier, Qt.LeftButton
    )
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton_4))
    clickButton(waitForObject(names.gbExpert_expertButton_QPushButton))
    clickButton(waitForObject(names.pulseModeWidget_saveButton_QPushButton))

    sendEvent("QMoveEvent", waitForObject(names.o_ScreenSwitcher), 0, -38, 1285, 256)

    mouseClick(
        waitForObject(
            names.pulseModeWidget_averagePowerWidget_ParameterWithEnumerableValueWidget_3,
            1358640
        ),
        106, 9, Qt.NoModifier, Qt.LeftButton
    )

    verify_text(
        names.averagePowerWidget_nameLabel_QLabel_3,
        "AVERAGE\nPOWER",
        "AVERAGE POWER label is verified",
        "AVERAGE POWER label verification failed"
    )
    verify_text(
        names.valueLabelBackgroundWithQuantityText_valueLabel_QLabel_5,
        "2",
        "Average Power value is verified",
        "Average Power value verification failed"
    )
    verify_text(
        names.averagePowerWidget_unitsOfMeasureLabel_QLabel_3,
        "W",
        "Average Power unit is verified",
        "Average Power unit verification failed"
    )
    verify_text(
        names.pulseEnergyWidget_nameLabel_QLabel_3,
        "PULSE\nENERGY",
        "PULSE ENERGY label is verified",
        "PULSE ENERGY label verification failed"
    )
    verify_image(
        "Pulse Energy",
        "Pulse Energy image is present",
        "Pulse Energy image is not present"
    )
    verify_text(
        names.pulseEnergyWidget_unitsOfMeasureLabel_QLabel_3,
        "J",
        "Pulse Energy unit is verified",
        "Pulse Energy unit verification failed"
    )
    verify_text(
        names.frequencyWidget_nameLabel_QLabel_3,
        "FREQUENCY",
        "FREQUENCY label is verified",
        "FREQUENCY label verification failed"
    )
    verify_text(
        names.frequencyWidget_unitsOfMeasureLabel_QLabel_3,
        "Hz",
        "Frequency unit is verified",
        "Frequency unit verification failed"
    )
    verify_image(
        "Frequency",
        "Frequency image is present",
        "Frequency image is not present"
    )

    clickButton(waitForObject(names.centralWidget_pbClose_QPushButton))

    test.log("SVV TAG POP-SAV-003: Save Preset Popup Pulse Energy Adjustment")
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton_4))
    clickButton(waitForObject(names.gbExpert_expertButton_QPushButton))
    clickButton(waitForObject(names.pulseModeWidget_saveButton_QPushButton))
    mouseDrag(
        waitForObject(names.indexPicker_valuePicker_IntervalSlider_8),
        88, 27, 114, 13, 1, Qt.LeftButton
    )
    test.vp("Pulse Energy Adjustment")

    test.log("SVV TAG POP-SAV-004: Save Preset Popup Frequency Adjustment")
    clickButton(waitForObject(names.centralWidget_pbClose_QPushButton))
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton_4))
    clickButton(waitForObject(names.gbExpert_expertButton_QPushButton))
    clickButton(waitForObject(names.pulseModeWidget_saveButton_QPushButton))
    mouseDrag(
        waitForObject(names.indexPicker_valuePicker_IntervalSlider_9),
        76, 22, 53, 10, 1, Qt.LeftButton
    )
    test.vp("Frequency Adjustment")
    test.log("Frequency Adjustment verified")

    test.log("SVV TAG POP-SAV-005: Save Preset Popup Peak Power Button")
    clickButton(waitForObject(names.centralWidget_pbClose_QPushButton))
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton_4))
    clickButton(waitForObject(names.gbExpert_expertButton_QPushButton))
    clickButton(waitForObject(names.pulseModeWidget_saveButton_QPushButton))

    mouseClick(
        waitForObject(names.peakPowerButton_iconLabel_QLabel),
        13, 21, Qt.NoModifier, Qt.LeftButton
    )
    clickButton(waitForObject(names.centralWidget_pw500_QPushButton))
    mouseClick(
        waitForObject(names.averagePowerWidget_progressFrame_QFrame_3),
        279, 25, Qt.NoModifier, Qt.LeftButton
    )
    mouseClick(
        waitForObject(names.peakPowerButton_iconLabel_QLabel),
        12, 18, Qt.NoModifier, Qt.LeftButton
    )
    clickButton(waitForObject(names.centralWidget_pw250_QPushButton))
    mouseClick(
        waitForObject(names.peakPowerButton_iconLabel_QLabel),
        24, 17, Qt.NoModifier, Qt.LeftButton
    )

    test.imagePresent("Peak Power")
    
    test.log("Peak Power adjustment verified")

    test.log("SVV TAG POP-SAV-006: Save Preset Popup Pulse Mode Button")
    clickButton(waitForObject(names.buttonsFrame_rejectButton_QPushButton_4))
    clickButton(waitForObject(names.centralWidget_pbClose_QPushButton))
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton_4))
    clickButton(waitForObject(names.gbExpert_expertButton_QPushButton))

    mouseClick(
        waitForObject(names.modeButton_nameLabel_QLabel),
        96, 43, Qt.NoModifier, Qt.LeftButton
    )
    test.log("Pulse Mode button selected")
    # test.vp("Pulse Mode Popup")

    test.imagePresent("Pulse Mode Popup")

    clickButton(waitForObject(names.centralWidget_MRP_QPushButton_2))
    test.vp("Pulse Mode Update Popup")
    test.log("Pulse Mode changed and verified")
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton_2))

    test.log("SVV TAG POP-SAV-007: Save Preset Popup Close Button")
    setWindowState(waitForObject(names.o_ScreenSwitcher), WindowState.Minimize)
    setWindowState(waitForObject(names.o_ScreenSwitcher), WindowState.Normal)
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton_4))
    clickButton(waitForObject(names.gbExpert_expertButton_QPushButton))
    clickButton(waitForObject(names.pulseModeWidget_saveButton_QPushButton, 45222))

    verify_image(
        "Close button",
        "Close/Cancel button image is available on the Preset screen",
        "Close/Cancel button image is not available on the Preset screen"
    )
    clickButton(waitForObject(names.centralWidget_pbClose_QPushButton))
    test.log("Close/Cancel button verification completed")

    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton_4))
    test.log("SVV TAG POP-SAV-008: Save Preset Popup Save Button")
    clickButton(waitForObject(names.gbExpert_expertButton_QPushButton))
    clickButton(waitForObject(names.pulseModeWidget_saveButton_QPushButton, 40615))
    verify_image(
        "Popup Save Button ",
        "Save button image is available on the Preset popup",
        "Save button image is not available on the Preset popup"
    )

    test.log("SVV TAG POP-SAV-009: Save Preset Popup Closes on Save Button")
    clickButton(waitForObject(names.centralWidget_pbClose_QPushButton))
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton_4))
    clickButton(waitForObject(names.gbExpert_expertButton_QPushButton))
    clickButton(waitForObject(names.pulseModeWidget_saveButton_QPushButton, 46063))
    clickButton(waitForObject(names.centralWidget_pbName_QPushButton))
    type(waitForObject(names.keyboardPopup_wdEdit_WdLineEdit), "Left")
    type(waitForObject(names.keyboardPopup_wdEdit_WdLineEdit), "<Backspace>")
    type(waitForObject(names.keyboardPopup_wdEdit_WdLineEdit), "Preset")
    test.log("Preset name entered")

    mouseClick(
        waitForObject(names.keyboardPopup_lbText_QLabel),
        131, 33, Qt.NoModifier, Qt.LeftButton
    )
    test.imagePresent("Save Preset")

    test.compare(str(waitForObjectExists(names.centralWidget_messageLabel_QLabel).text), "Preset with this name already exists\nPlease enter another name")
    
    clickButton(waitForObject(names.centralWidget_okButton_QPushButton_2))
    
    clickButton(waitForObject(names.pulseModeWidget_saveButton_QPushButton_3, 100456))
    
    test.log("Left preset name saved and verified")
    
    clickButton(waitForObject(names.centralWidget_softTissueButton_QPushButton))
    
    test.log("SVV TAG POP-SAV-010: Save Preset Popup Closes on Save Button")
    mouseClick(
        waitForObject(names.rightPedalWidget_wdPresetTabs_TabWidget),
        13, 56, Qt.NoModifier, Qt.LeftButton
    )
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton_4))
    clickButton(waitForObject(names.gbExpert_expertButton_QPushButton))
    mouseClick(
        waitForObject(names.leftPedalWidget_wdPresetTabs_TabWidget, 90840),
        479, 33, Qt.NoModifier, Qt.LeftButton
    )
    clickButton(waitForObject(names.pulseModeWidget_saveButton_QPushButton))
    test.log("Save Preset popup opened for left preset")
    clickButton(waitForObject(names.centralWidget_pbName_QPushButton))
    type(waitForObject(names.keyboardPopup_wdEdit_WdLineEdit), "leftpresetone")
    mouseClick(
        waitForObject(names.keyboardPopup_lbText_QLabel),
        99, 54, Qt.NoModifier, Qt.LeftButton
    )
    test.vp("Left preset save")
    clickButton(waitForObject(names.pulseModeWidget_saveButton_QPushButton_3))
    clickButton(waitForObject(names.centralWidget_softTissueButton_QPushButton))

    test.log("SVV TAG POP-SAV-011: Save Preset Popup Text Field Default")
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton_4))
    clickButton(waitForObject(names.gbExpert_expertButton_QPushButton))
    clickButton(waitForObject(names.pulseModeWidget_saveButton_QPushButton))

    verify_text(
        names.centralWidget_pbName_QPushButton,
        "Enter preset name",
        "Enter Preset Name field is verified in the Preset popup",
        "Enter Preset Name field verification failed in the Preset popup"
    )

    test.log("SVV TAG POP-SAV-012: Save Preset Popup Treatment Category Selection Required")
    clickButton(waitForObject(names.centralWidget_pbClose_QPushButton))
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton_4))
    clickButton(waitForObject(names.gbExpert_expertButton_QPushButton))
    clickButton(waitForObject(names.pulseModeWidget_saveButton_QPushButton, 81784))
    clickButton(waitForObject(names.centralWidget_pbName_QPushButton))
    type(waitForObject(names.keyboardPopup_wdEdit_WdLineEdit), "Preset one")
    mouseClick(
        waitForObject(names.keyboardPopup_lbText_QLabel),
        37, 22, Qt.NoModifier, Qt.LeftButton
    )

    # Note: This assertion checks the AVERAGE POWER label, not the selected
    # treatment category. Confirm the intended category object before changing it.
    verify_text(
        names.averagePowerWidget_nameLabel_QLabel_3,
        "AVERAGE\nPOWER",
        "AVERAGE POWER label is verified after preset name entry",
        "AVERAGE POWER label verification failed after preset name entry"
    )
    test.log("SVV TAG POP-SAV-013: Save Preset Popup Treatment Category Cancel Button")
    mouseClick(
        waitForObject(names.pulseModeWidget_buttonsWidget_QWidget_3),
        498, 24, Qt.NoModifier, Qt.LeftButton
    )
    clickButton(waitForObject(names.centralWidget_pbClose_QPushButton))
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton_4))
    clickButton(waitForObject(names.gbExpert_expertButton_QPushButton))
    clickButton(waitForObject(names.pulseModeWidget_saveButton_QPushButton))
    clickButton(waitForObject(names.centralWidget_pbName_QPushButton))
    type(waitForObject(names.keyboardPopup_wdEdit_WdLineEdit), "preset two")
    mouseClick(
        waitForObject(names.keyboardPopup_lbText_QLabel),
        135, 28, Qt.NoModifier, Qt.LeftButton
    )

    verify_image(
        "Close button",
        "Cancel button image is available on the Preset screen",
        "Cancel button image is not available on the Preset screen"
    )
