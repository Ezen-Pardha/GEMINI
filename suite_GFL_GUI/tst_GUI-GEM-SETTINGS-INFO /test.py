# -*- coding: utf-8 -*-

from common import *

def main():
    enter_login_pin()
    clickButton(waitForObject(names.homeScreen_settingsButton_QPushButton))
    test.log("Navigating to Settings Screen")
    clickTab(waitForObject(names.settingsScreen_tbSystemInfo_TabWidget), "INFO")
    test.log("navigating to Info tab")
    info_tab = waitForObject(names.settingsScreen_tbSystemInfo_TabWidget)
    if str(info_tab.tabText(info_tab.currentIndex)) == "INFO":
        test.passes("INFO tab is displayed on the screen")
    else:
        test.fail("INFO tab is not displayed on the screen")
    test.log("Navigating back from INFO tab")

    software_version_label = waitForObject(names.gbSystemInformation_lbSoftwareVersionName_QLabel)
    software_version_value = waitForObject(names.gbSystemInformation_lbSoftwareVersionValue_QLabel)
    test.log("SVV TAG:GUI-SET-018: Confirming the Software Version is displayed")
    version = str(software_version_value.text).strip()
    if software_version_label.visible and version:
        test.passes(
            "PASS: Software version is displayed: {}".format(version)
        )
    else:
        test.fail("FAIL: Software version is not displayed")
    
    factory_procedures_version_label = waitForObject(names.gbSystemInformation_lbFactoryProceduresVersionName_QLabel)
    factory_procedures_version_value = waitForObject(names.gbSystemInformation_lbFactoryProceduresVersionValue_QLabel)
    test.log("SVV TAG:GUI-SET-019: Confirming the Factory Procedures Version is displayed")
    version = str(factory_procedures_version_value.text).strip()
    if factory_procedures_version_label.visible and version:
        test.passes(
            "PASS: Factory Procedures version is displayed: {}".format(version)
        )
    else:
        test.fail("FAIL: Factory Procedures version is not displayed")
    
    system_serial_number_name_label = waitForObject(names.gbSystemInformation_lbSystemSerialNumberName_QLabel)
    system_serial_number_name_value = waitForObject(names.gbSystemInformation_lbSystemSerialNumberValue_QLabel)
    test.log("SVV TAG:GUI-SET-020: Confirming the System Serial Number Name is displayed")
    serial_number = str(system_serial_number_name_value.text).strip()
    if system_serial_number_name_label.visible and serial_number:
        test.passes(
            "PASS: System Serial Number Name is displayed: {}".format(serial_number)
        )
    else:
        test.fail("FAIL: System Serial Number Name is not displayed")
    
    language_settings_label = waitForObject(names.gbSystemInformation_lbLanguageSettingsName_QLabel)
    language_settings_value = waitForObject(names.gbSystemInformation_lbLanguageSettingsValue_QLabel)
    test.log("SVV TAG:GUI-SET-027: Confirming the Language Settings is displayed")
    language_value = str( language_settings_value.text).strip()
    if  language_settings_label.visible and language_value:
        test.passes(
            "PASS: Language Settings is displayed: {}".format(language_value)
        )
    else:
        test.fail("FAIL:Language Settings is not displayed")
    
        
