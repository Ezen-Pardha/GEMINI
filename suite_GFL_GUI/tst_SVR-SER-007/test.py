# -*- coding: utf-8 -*-

from common import *

def main():
    navigate_service_mode()
    clickTab(waitForObject(names.serviceScreenTabWidget_QTabWidget),"SYSTEM CONFIGURATION")
    test.log("Confirming System Configuration Tab is displayed")
    test.log("Selecting the RFID region dropdown")
    mouseClick(waitForObject(names.systemConfigurationTab_rfidRegionLabel_QLabel),205, 75,Qt.NoModifier,Qt.LeftButton)
    region_combo = waitForObject(names.rfidRegionPanelFrame_rfidRegionComboBox_QComboBox)
    mouseClick(region_combo,243, 17,Qt.NoModifier,Qt.LeftButton)
    test.log("Displaying all RFID regions which are available")
    region_count = region_combo.count
    regions = []
    for index in range(region_count):
        region_name = str(region_combo.itemText(index)).strip()
        regions.append(region_name)

    if region_count > 0:
        test.passes(
            "RFID region dropdown displays {} available regions: {}".format(
                region_count, ", ".join(regions)
            )
        )
    else:
        test.fail(
            "RFID region dropdown does not display any available regions"
        )
    mouseClick(waitForObjectItem(names.rfidRegionPanelFrame_rfidRegionComboBox_QComboBox,"Japan"),97, 7,Qt.NoModifier,Qt.LeftButton)
    test.log("Confirming the program selects the RFID region")
    selected_region = str(region_combo.currentText).strip()
    if selected_region == "Japan":
        test.passes(
            "Program selected the RFID region: {}".format(selected_region)
        )
    else:
        test.fail(
            "RFID region selection failed. Expected: Japan, Actual: {}".format(
                selected_region
            )
        )
