# -*- coding: utf-8 -*-

import names
from squish import *
from common import *


def main():

    navigate_service_mode()

    test.compare(
        waitForObjectExists(
            names.qt_tabwidget_tabbar_SYSTEM_CONFIGURATION_TabItem
        ).text,
        "SYSTEM CONFIGURATION"
    )

    clickTab(
        waitForObject(names.serviceScreenTabWidget_QTabWidget),
        "SOFTWARE UPDATE"
    )

    test.compare(
        waitForObjectExists(
            names.qt_tabwidget_tabbar_SOFTWARE_UPDATE_TabItem
        ).text,
        "SOFTWARE UPDATE"
    )

    application_version = str(
        waitForObjectExists(
            names.applicationUpdatePanel_VersionLabel_QLabel
        ).text
    ).strip()

    kernel_version = str(
        waitForObjectExists(
            names.staticVersions_2_kernelVersion_QLabel
        ).text
    ).strip()

    device_tree_version = str(
        waitForObjectExists(
            names.staticVersions_2_deviceTreeVersion_QLabel
        ).text
    ).strip()

    procedures_version = str(
        waitForObjectExists(
            names.proceduresUpdatePanel_VersionLabel_QLabel
        ).text
    ).strip()

    # Print Software Update values
    test.log("SOFTWARE UPDATE")
    test.log("Application Version: " + application_version)
    test.log("Kernel Version: " + kernel_version)
    test.log("Device Tree Version: " + device_tree_version)
    test.log("Procedures Version: " + procedures_version)

    clickTab(
        waitForObject(names.serviceScreenTabWidget_QTabWidget),
        "FIRMWARE UPDATE"
    )

    test.compare(
        waitForObjectExists(
            names.qt_tabwidget_tabbar_FIRMWARE_UPDATE_TabItem
        ).text,
        "FIRMWARE UPDATE"
    )

    rfid_version = str(
        waitForObjectExists(
            names.rfidUpdatePanel_VersionLabel_QLabel
        ).text
    ).strip()

    carrier_version = str(
        waitForObjectExists(
            names.staticVersions_carrierBoardVersion_QLabel
        ).text
    ).strip()

    rf_version = str(
        waitForObjectExists(
            names.wirelessRfUpdatePanel_VersionLabel_QLabel
        ).text
    ).strip()

    tx_version = str(
        waitForObjectExists(
            names.wirelessTxUpdatePanel_VersionLabel_QLabel
        ).text
    ).strip()

    # Print Firmware Update values
    test.log("===== FIRMWARE UPDATE =====")
    test.log("RFID Board Version: " + rfid_version)
    test.log("Carrier Board Version: " + carrier_version)
    test.log("Wireless RF Version: " + rf_version)
    test.log("Wireless TX Version: " + tx_version)

    test.log("SERVICE MODE VERSION SUMMARY")

    test.log("Application Version : " + application_version)
    test.log("Kernel Version      : " + kernel_version)
    test.log("Device Tree Version : " + device_tree_version)
    test.log("RFID Board Version  : " + rfid_version)
    test.log("Carrier Board       : " + carrier_version)
    test.log("Wireless RF Version : " + rf_version)
    test.log("Wireless TX Version : " + tx_version)
    test.log("Procedures Version  : " + procedures_version)

    test.passes(
        "PASS: Service mode version information was "
        "read successfully from the GUI"
    )
    
    
    
    
    
    
    