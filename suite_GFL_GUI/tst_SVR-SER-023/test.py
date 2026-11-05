# -*- coding: utf-8 -*-

from common import *

def main():
    navigate_service_mode()
    clickButton(waitForObject(names.frameClearLogs_pbClearSystemLogs_QPushButton))
    clickButton(waitForObject(names.buttonsFrame_acceptButton_QPushButton))
    clickButton(waitForObject(names.centralWidget_okButton_QPushButton))
    clickButton(waitForObject(names.buttonsBar_backButton_QPushButton))
    clickTab(waitForObject(names.settingsScreen_tbSystemInfo_TabWidget), "LOGS")
    test.vp("Verifying logs tab")
    test.log("Confirming the logs are cleared")
