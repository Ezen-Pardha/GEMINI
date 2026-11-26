# -*- coding: utf-8 -*-

from common import *

def main():
    navigate_service_mode()
    test.log("Confirming the program displays System Serial number in System Configuration tab")
    serial_number_label = waitForObject(names.staticVersions_3_serialNumberLabel_QLabel)
    serial_number_value = waitForObject(names.staticVersions_3_serialNumberVersion_QLabel)
    if serial_number_label.isVisible() and serial_number_value.isVisible():
        serial_number = str(serial_number_value.text).strip()
        if serial_number:
            test.passes("Program displays the serial number: {}".format(serial_number))
        else:
            test.fail("Serial number value is empty")
    else:
        test.fail("Serial number label or value is not visible")
    
        
        
    