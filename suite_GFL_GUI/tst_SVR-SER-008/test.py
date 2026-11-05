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
    power_label = waitForObject(names.rfidWritePowerNumberPicker_lbValue_QLabel)
    initial_text = str(power_label.text)
    initial_match = re.search(r'-?\d+', initial_text)

    if initial_match:
        initial_power = pybuiltins.int(initial_match.group(0))
        clickButton(waitForObject(names.rfidWritePowerNumberPicker_pbDecrement_QPushButton))
        decrement_text = str(power_label.text)
        decrement_match = re.search(r'-?\d+', decrement_text)
        if decrement_match:
            decrement_power = pybuiltins.int(decrement_match.group(0))
            if decrement_power < initial_power:
                test.passes("RFID Write Power decreased accordingly: {} -> {}".format(initial_power, decrement_power))
            else:
                test.fail(
                    "RFID Write Power did not decrease. "
                    "Initial: {}, Current: {}".format(
                        initial_power, decrement_power
                    )
                )
            clickButton(waitForObject(names.rfidWritePowerNumberPicker_pbIncrement_QPushButton))
            increment_text = str(power_label.text)
            increment_match = re.search(r'-?\d+', increment_text)
            if increment_match:
                increment_power = pybuiltins.int(increment_match.group(0))
                if increment_power > decrement_power:
                    test.passes(
                        "RFID Write Power increased accordingly: {} -> {}".format(
                            decrement_power, increment_power
                        )
                    )
                else:
                    test.fail(
                        "RFID Write Power did not increase. "
                        "Before increment: {}, Current: {}".format(
                            decrement_power, increment_power
                        )
                    )
            else:
                test.fail(
                    "Unable to read RFID Write Power after increment"
                )
        else:
            test.fail(
                "Unable to read RFID Write Power after decrement"
            )
    else:
        test.fail(
            "Unable to read initial RFID Write Power: {}".format(
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