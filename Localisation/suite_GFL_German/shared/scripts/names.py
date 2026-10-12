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
o_MessageBoxAlert = {"type": "MessageBoxAlert", "unnamed": 1, "visible": 1}
centralWidget_QFrame = {"name": "centralWidget", "type": "QFrame", "visible": 1, "window": o_MessageBoxAlert}
centralWidget_okButton_QPushButton = {"container": centralWidget_QFrame, "name": "okButton", "type": "QPushButton", "visible": 1}
homeScreen_HomeScreen = {"name": "HomeScreen", "type": "HomeScreen", "visible": 1, "window": o_ScreenSwitcher}
homeScreen_settingsButton_QPushButton = {"container": homeScreen_HomeScreen, "name": "settingsButton", "type": "QPushButton", "visible": 1}
settingsScreen_SettingsScreen = {"name": "SettingsScreen", "type": "SettingsScreen", "visible": 1, "window": o_ScreenSwitcher}
settingsScreen_tbSystemInfo_TabWidget = {"container": settingsScreen_SettingsScreen, "name": "tbSystemInfo", "type": "TabWidget", "visible": 1}
settingsScreen_qt_tabwidget_stackedwidget_QStackedWidget = {"container": settingsScreen_SettingsScreen, "name": "qt_tabwidget_stackedwidget", "type": "QStackedWidget", "visible": 1}
qt_tabwidget_stackedwidget_wdSystemInfoLayout_QWidget = {"container": settingsScreen_qt_tabwidget_stackedwidget_QStackedWidget, "name": "wdSystemInfoLayout", "type": "QWidget", "visible": 1}
wdSystemInfoLayout_gbSystemInformation_QGroupBox = {"container": qt_tabwidget_stackedwidget_wdSystemInfoLayout_QWidget, "name": "gbSystemInformation", "type": "QGroupBox", "visible": 1}
gbSystemInformation_pbLanguageSettingsUpdate_QPushButton = {"container": wdSystemInfoLayout_gbSystemInformation_QGroupBox, "name": "pbLanguageSettingsUpdate", "type": "QPushButton", "visible": 1}
wdSystemInfoLayout_centralWidget_QFrame = {"container": qt_tabwidget_stackedwidget_wdSystemInfoLayout_QWidget, "name": "centralWidget", "type": "QFrame", "visible": 1}
centralWidget_languagesFrame_QFrame = {"container": wdSystemInfoLayout_centralWidget_QFrame, "name": "languagesFrame", "type": "QFrame", "visible": 1}
languagesFrame_pbLithuania_QPushButton = {"container": centralWidget_languagesFrame_QFrame, "name": "pbLithuania", "type": "QPushButton", "visible": 1}
centralWidget_buttonsFrame_QFrame = {"container": wdSystemInfoLayout_centralWidget_QFrame, "name": "buttonsFrame", "type": "QFrame", "visible": 1}
buttonsFrame_acceptButton_QPushButton = {"container": centralWidget_buttonsFrame_QFrame, "name": "acceptButton", "type": "QPushButton", "visible": 1}
gbSystemInformation_lbSystemInformation_QLabel = {"container": wdSystemInfoLayout_gbSystemInformation_QGroupBox, "name": "lbSystemInformation", "type": "QLabel", "visible": 1}
wdSystemInfoLayout_gbFiberInformation_QGroupBox = {"container": qt_tabwidget_stackedwidget_wdSystemInfoLayout_QWidget, "name": "gbFiberInformation", "type": "QGroupBox", "visible": 1}
gbFiberInformation_lbFiberInformation_QLabel = {"container": wdSystemInfoLayout_gbFiberInformation_QGroupBox, "name": "lbFiberInformation", "type": "QLabel", "visible": 1}
settingsScreen_tabBarSystemInfo_TabBar = {"container": settingsScreen_SettingsScreen, "name": "tabBarSystemInfo", "type": "TabBar", "visible": 1}
languagesFrame_pbLatvia_QPushButton = {"container": centralWidget_languagesFrame_QFrame, "name": "pbLatvia", "type": "QPushButton", "visible": 1}
settingsScreen_topBar_TopBar = {"container": settingsScreen_SettingsScreen, "name": "topBar", "type": "TopBar", "visible": 1}
topBar_buttonsBar_ButtonsBar = {"container": settingsScreen_topBar_TopBar, "name": "buttonsBar", "type": "ButtonsBar", "visible": 1}
loginScreen_header_TopBar = {"container": loginScreen_LoginScreen, "name": "header", "type": "TopBar", "visible": 1}
header_buttonsBar_ButtonsBar = {"container": loginScreen_header_TopBar, "name": "buttonsBar", "type": "ButtonsBar", "visible": 1}
languagesFrame_pbNorway_QPushButton = {"container": centralWidget_languagesFrame_QFrame, "name": "pbNorway", "type": "QPushButton", "visible": 1}
languagesFrame_pbPoland_QPushButton = {"container": centralWidget_languagesFrame_QFrame, "name": "pbPoland", "type": "QPushButton", "visible": 1}
languagesFrame_pbPortugese_QPushButton = {"container": centralWidget_languagesFrame_QFrame, "name": "pbPortugese", "type": "QPushButton", "visible": 1}
languagesFrame_pbRomania_QPushButton = {"container": centralWidget_languagesFrame_QFrame, "name": "pbRomania", "type": "QPushButton", "visible": 1}
languagesFrame_pbSlovakia_QPushButton = {"container": centralWidget_languagesFrame_QFrame, "name": "pbSlovakia", "type": "QPushButton", "visible": 1}
gbSystemInformation_lbFactoryProceduresVersionValue_QLabel = {"container": wdSystemInfoLayout_gbSystemInformation_QGroupBox, "name": "lbFactoryProceduresVersionValue", "type": "QLabel", "visible": 1}
languagesFrame_pbSlovenia_QPushButton = {"container": centralWidget_languagesFrame_QFrame, "name": "pbSlovenia", "type": "QPushButton", "visible": 1}
languagesFrame_pbSwedish_QPushButton = {"container": centralWidget_languagesFrame_QFrame, "name": "pbSwedish", "type": "QPushButton", "visible": 1}
languagesFrame_pbTurkey_QPushButton = {"container": centralWidget_languagesFrame_QFrame, "name": "pbTurkey", "type": "QPushButton", "visible": 1}
languagesFrame_pbFrance_QPushButton = {"container": centralWidget_languagesFrame_QFrame, "name": "pbFrance", "type": "QPushButton", "visible": 1}
languagesFrame_pbSpain_QPushButton = {"container": centralWidget_languagesFrame_QFrame, "name": "pbSpain", "type": "QPushButton", "visible": 1}
languagesFrame_pbEstonia_QPushButton = {"container": centralWidget_languagesFrame_QFrame, "name": "pbEstonia", "type": "QPushButton", "visible": 1}
languagesFrame_pbFinland_QPushButton = {"container": centralWidget_languagesFrame_QFrame, "name": "pbFinland", "type": "QPushButton", "visible": 1}
languagesFrame_pbGermany_QPushButton = {"container": centralWidget_languagesFrame_QFrame, "name": "pbGermany", "type": "QPushButton", "visible": 1}
languagesFrame_pbGreece_QPushButton = {"container": centralWidget_languagesFrame_QFrame, "name": "pbGreece", "type": "QPushButton", "visible": 1}
languagesFrame_pbHungary_QPushButton = {"container": centralWidget_languagesFrame_QFrame, "name": "pbHungary", "type": "QPushButton", "visible": 1}
languagesFrame_pbItaly_QPushButton = {"container": centralWidget_languagesFrame_QFrame, "name": "pbItaly", "type": "QPushButton", "visible": 1}
languagesFrame_pbJapan_QPushButton = {"container": centralWidget_languagesFrame_QFrame, "name": "pbJapan", "type": "QPushButton", "visible": 1}
