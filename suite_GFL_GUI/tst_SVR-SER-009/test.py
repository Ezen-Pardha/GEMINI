# -*- coding: utf-8 -*-

from common import *
try:
    import builtins as pybuiltins
except ImportError:
    import __builtin__ as pybuiltins

def main():
    navigate_service_mode()
    clickTab(waitForObject(names.serviceScreenTabWidget_QTabWidget),"SYSTEM CONFIGURATION")
    test.log("Confirming System Configuration Tab is displayed")
    read_power_label = waitForObject(names.rfidReadPowerNumberPicker_lbValue_QLabel)
    initial_text = str(read_power_label.text)
    initial_match = re.search(r'-?\d+', initial_text)
    
    if initial_match:
        initial_read_power = pybuiltins.int(initial_match.group(0))
        clickButton(waitForObject(names.rfidReadPowerNumberPicker_pbIncrement_QPushButton))
        increment_text = str(read_power_label.text)
        increment_match = re.search(r'-?\d+', increment_text)
        if increment_match:
            increment_read_power = pybuiltins.int(increment_match.group(0))
            if increment_read_power > initial_read_power:
                test.passes("RFID Read Power increased accordingly: {} -> {}".format(initial_read_power, increment_read_power))
            else:
                test.fail(
                    "RFID Read Power did not increase. "
                    "Initial: {}, Current: {}".format(
                        initial_read_power, increment_read_power
                    )
                )
            clickButton(waitForObject(names.rfidReadPowerNumberPicker_pbDecrement_QPushButton))
            decrement_text = str(read_power_label.text)
            decrement_match = re.search(r'-?\d+', decrement_text)
            if decrement_match:
                decrement_read_power = pybuiltins.int(decrement_match.group(0))
                if decrement_read_power < increment_read_power:
                    test.passes(
                        "RFID Read Power decreased accordingly: {} -> {}".format(
                            increment_read_power, decrement_read_power
                        )
                    )
                else:
                    test.fail(
                        "RFID Read Power did not decrease. "
                        "Before decrement: {}, Current: {}".format(
                            increment_read_power, decrement_read_power
                        )
                    )
            else:
                test.fail(
                    "Unable to read RFID Read Power after decrement"
                )
        else:
            test.fail(
                "Unable to read RFID Read Power after increment"
            )
    else:
        test.fail(
            "Unable to read initial RFID Read Power: {}".format(
                initial_text
            )
        )
    
    test.log("Confirming update config button is displayed")
    try:
        update_config_button = waitForObject({
            "text": "update_config",
            "type": "QPushButton"
        })
    
        if update_config_button.visible:
            test.passes("Update Config button is displayed")
        else:
            test.fail("Update Config button is not visible")
    
    except LookupError:
        test.fail(
            "FAIL: Update Config button is not displayed. "
        )