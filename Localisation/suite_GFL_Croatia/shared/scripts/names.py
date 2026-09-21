# encoding: UTF-8

from objectmaphelper import *

o_ScreenSwitcher = {"type": "ScreenSwitcher", "unnamed": 1, "visible": 1}
loginScreen_LoginScreen = {"name": "LoginScreen", "type": "LoginScreen", "visible": 1, "window": o_ScreenSwitcher}
loginScreen_mainFrame_QFrame = {"container": loginScreen_LoginScreen, "name": "mainFrame", "type": "QFrame", "visible": 1}
mainFrame_gbPasscode_QGroupBox = {"container": loginScreen_mainFrame_QFrame, "name": "gbPasscode", "type": "QGroupBox", "visible": 1}
gbPasscode_inputFrame_PasscodeInputWidget = {"container": mainFrame_gbPasscode_QGroupBox, "name": "inputFrame", "type": "PasscodeInputWidget", "visible": 1}
inputFrame_numpad_Numpad = {"container": gbPasscode_inputFrame_PasscodeInputWidget, "name": "numpad", "type": "Numpad", "visible": 1}
numpad_pushButton_8_NumpadButton = {"container": inputFrame_numpad_Numpad, "name": "pushButton_8", "type": "NumpadButton", "visible": 1}
fiberVerificationWarningDialog_FiberVerificationWarningDialog = {"name": "FiberVerificationWarningDialog", "type": "FiberVerificationWarningDialog", "visible": 1}
fiberVerificationWarningDialog_mainFrame_QFrame = {"name": "mainFrame", "type": "QFrame", "visible": 1, "window": fiberVerificationWarningDialog_FiberVerificationWarningDialog}
mainFrame_okButton_QPushButton = {"container": fiberVerificationWarningDialog_mainFrame_QFrame, "name": "okButton", "type": "QPushButton", "visible": 1}
