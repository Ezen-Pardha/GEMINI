# -*- coding: utf-8 -*-

from common import *

def main():
    navigate_service_mode()
    clickButton(waitForObject(names.demoModePanel_pbDemoModeOn_QToolButton))
    test.log("Verifying warning message when demo mode toggled")
    test.vp("Verifying demo mode toggle warning") 
    clickButton(waitForObject(names.buttonsFrame_rejectButton_QPushButton))
    mouseClick(waitForObject(names.systemConfigurationTab_rfidRegionLabel_QLabel), 146, 47, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.rfidRegionPanelFrame_rfidRegionComboBox_QComboBox), 250, 21, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.rfidRegionPanelFrame_rfidRegionComboBox_QComboBox, "India"), 78, 21, Qt.NoModifier, Qt.LeftButton)
    test.log("Verifying warning message RFID Region change")
    try:
        warning_dialog = findObject(names.o_WarningDialog)
    
        if warning_dialog and warning_dialog.visible:
            test.passes(
                "Warning popup displayed after system region change"
            )
        else:
            test.fail(
                "Warning popup was not displayed after system region change"
            )
    
    except LookupError:
        test.fail(
            "Warning popup was not displayed after system region change"
        )
        
    clickButton(waitForObject(names.rfidWritePowerNumberPicker_pbDecrement_QPushButton))
    clickButton(waitForObject(names.rfidReadPowerNumberPicker_pbIncrement_QPushButton))
    clickButton(waitForObject(names.fiberIdleTimeoutNumberPicker_pbIncrement_QPushButton))
    test.log("Verifying warning message RFID configuration changes")
    try:
        warning_dialog = findObject(names.o_WarningDialog)
    
        if warning_dialog and warning_dialog.visible:
            test.passes(
                "Warning popup displayed after RFID configuration changes"
            )
        else:
            test.fail(
                "Warning popup was not displayed after RFID configuration changes"
            )
    
    except LookupError:
        test.fail(
            "Warning popup was not displayed after RFID configuration changes"
        )
