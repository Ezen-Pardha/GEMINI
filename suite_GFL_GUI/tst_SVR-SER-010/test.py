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
    test.log("Confirming Fiber Idle Timeout dropdown is displayed")
    fiber_dropdown = object.exists({
        "type": "QComboBox",
        "name": "fiberIdleTimeoutComboBox",
        "visible": True
    })
    if fiber_dropdown:
        test.passes(
            "Fiber Idle Timeout dropdown is displayed"
        )
    else:
        test.fail(
            "FAIL: Fiber Idle Timeout dropdown is not displayed. "
            "The control provides increment and decrement buttons instead."
        )

    timeout_label = waitForObject(names.fiberIdleTimeoutNumberPicker_lbValue_QLabel)
    initial_text = str(timeout_label.text).strip()
    initial_match = re.search(r'\d+', initial_text)
    if initial_match:
        initial_timeout = pybuiltins.int(initial_match.group(0))
        test.log(
            "Initial Fiber Idle Timeout: {}".format(initial_text)
        )
        clickButton(waitForObject(names.fiberIdleTimeoutNumberPicker_pbIncrement_QPushButton))
        increment_text = str(timeout_label.text).strip()
        increment_match = re.search(r'\d+', increment_text)
        if increment_match:
            increment_timeout = pybuiltins.int(increment_match.group(0))
            if increment_timeout > initial_timeout:
                test.passes(
                    "Fiber Idle Timeout increased accordingly: {} -> {}".format(
                        initial_text, increment_text
                    )
                )
            else:
                test.fail(
                    "Fiber Idle Timeout did not increase. "
                    "Initial: {}, Current: {}".format(
                        initial_text, increment_text
                    )
                )
            clickButton(waitForObject(names.fiberIdleTimeoutNumberPicker_pbDecrement_QPushButton))
            decrement_text = str(timeout_label.text).strip()
            decrement_match = re.search(r'\d+', decrement_text)
            if decrement_match:
                decrement_timeout = pybuiltins.int(decrement_match.group(0))
                if decrement_timeout < increment_timeout:
                    test.passes(
                        "Fiber Idle Timeout decreased accordingly: {} -> {}".format(
                            increment_text, decrement_text
                        )
                    )
                else:
                    test.fail(
                        "Fiber Idle Timeout did not decrease. "
                        "Before decrement: {}, Current: {}".format(
                            increment_text, decrement_text
                        )
                    )
            else:
                test.fail(
                    "Unable to read Fiber Idle Timeout after decrement"
                )
        else:
            test.fail(
                "Unable to read Fiber Idle Timeout after increment"
            )
    else:
        test.fail(
            "Unable to read initial Fiber Idle Timeout: {}".format(
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
