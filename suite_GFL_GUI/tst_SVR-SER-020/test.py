# -*- coding: utf-8 -*-

from common import *

def main():
    navigate_service_mode()
    test.log("Confirming the program displays System type in System Configuration tab")
    system_type_label = waitForObject(names.staticVersions_3_systemTypeLabel_QLabel)
    system_type_value = waitForObject(names.staticVersions_3_systemTypeVersion_QLabel)
    if system_type_label.isVisible() and system_type_value.isVisible():
        system_type = str(system_type_value.text).strip()
        if system_type:
            test.passes(
                "Program displays the system type: {}".format(system_type)
            )
        else:
            test.fail("System type value is empty")
    else:
        test.fail("System type label or value is not visible")
        
    