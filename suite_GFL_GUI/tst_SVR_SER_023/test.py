# -*- coding: utf-8 -*-

from common import *

def main():
    navigate_service_mode()
    clickButton(waitForObject(names.frameClearLogs_pbClearSystemLogs_QPushButton))
    clickButton(waitForObject(names.buttonsFrame_acceptButton_QPushButton))
    mouseClick(waitForObject(names.centralWidget_messageLabel_QLabel_2), 226, 27, Qt.NoModifier, Qt.LeftButton)
    
    label_obj = waitForObject(names.centralWidget_messageLabel_QLabel_2)
    label_txt = str(label_obj.text)
    test.log(label_txt)
    
    clickButton(waitForObject(names.centralWidget_okButton_QPushButton_5))
    clickButton(waitForObject(names.buttonsBar_backButton_QPushButton_4))
    clickTab(waitForObject(names.settingsScreen_tbSystemInfo_TabWidget), "LOGS")
    
    if test.vp("Verifying logs tab"):
        test.passes("All Logs have been cleared successfully")
    else:
        test.fail("Logs were not cleared successfully")
    