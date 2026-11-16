import os
import re
import names
import test
import common

def increment_frequency():

    test.log("Incrementing Frequency and Clicking Display")

    # Increment 1
    clickButton(
        waitForObject(
            names.frequencyWidget_incrementButton_QPushButton
        )
    )

    mouseClick(
        waitForObject(
            names.valueLabelBackgroundWithQuantityText_valueLabel_QLabel
        ),
        134, 36,
        Qt.NoModifier,
        Qt.LeftButton
    )

    # Increment 2
    clickButton(
        waitForObject(
            names.frequencyWidget_incrementButton_QPushButton
        )
    )

    mouseClick(
        waitForObject(
            names.valueLabelBackgroundWithQuantityText_valueLabel_QLabel
        ),
        139, 45,
        Qt.NoModifier,
        Qt.LeftButton
    )

    # Increment 3
    clickButton(
        waitForObject(
            names.frequencyWidget_incrementButton_QPushButton
        )
    )

    mouseClick(
        waitForObject(
            names.valueLabelBackgroundWithQuantityText_valueLabel_QLabel
        ),
        138, 53,
        Qt.NoModifier,
        Qt.LeftButton
    )

    # Increment 4
    clickButton(
        waitForObject(
            names.frequencyWidget_incrementButton_QPushButton
        )
    )

    mouseClick(
        waitForObject(
            names.valueLabelBackgroundWithQuantityText_valueLabel_QLabel
        ),
        143, 58,
        Qt.NoModifier,
        Qt.LeftButton
    )

    # Increment 5
    clickButton(
        waitForObject(
            names.frequencyWidget_incrementButton_QPushButton
        )
    )

    mouseClick(
        waitForObject(
            names.valueLabelBackgroundWithQuantityText_valueLabel_QLabel
        ),
        114, 49,
        Qt.NoModifier,
        Qt.LeftButton
    )

    # Increment 6
    clickButton(
        waitForObject(
            names.frequencyWidget_incrementButton_QPushButton
        )
    )

    mouseClick(
        waitForObject(
            names.valueLabelBackgroundWithQuantityText_valueLabel_QLabel
        ),
        110, 42,
        Qt.NoModifier,
        Qt.LeftButton
    )

    # Increment 7
    clickButton(
        waitForObject(
            names.frequencyWidget_incrementButton_QPushButton
        )
    )

    mouseClick(
        waitForObject(
            names.valueLabelBackgroundWithQuantityText_valueLabel_QLabel
        ),
        132, 45,
        Qt.NoModifier,
        Qt.LeftButton
    )

    test.passes(
        "Frequency increment and display clicks completed"
    )

    
def main():
    test.log("Starting Economy C and Frequency Test")

    runtime_path = os.path.expanduser(
        "/home/ezen/Gemini_v1"
    )

    common.configure_system_type(
        new_type="C",
        runtime_path=runtime_path
    )
    
    try: 
        context = currentApplicationContext()
        context.detach()
        snooze(3)
        test.log("AUT context detached")
    except Exception as error:
        test.log("Error while closing AUT: " + str(error))

    startApplication(
        "bravo --disable-watchdog --watchdog-timeout=10 "
        "--disable-integrity-check "
        "--disable-fiber-use-check "
        "--disable-firmware-check "
        "--disable-ssm "
        "--disable-ports-check"
    )
    snooze(5)
    
    common.enter_login_pin()
    common.dismiss_fiber_verification_warning()
    common.verify_economyc_type()
    mouseClick(waitForObject(names.staticVersions_3_systemTypeVersion_QLabel), 57, 17, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.buttonsBar_backButton_QPushButton))
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    common.navigate_to_expert_screen()
    common.left_fragmentation_pulse()
    increment_frequency()    
    test.log("Economy C and Frequency Test Completed")
    runtime_path = os.path.expanduser(
        "/home/ezen/Gemini_v1"
    )
    common.configure_system_type(
        new_type="B",
        runtime_path=runtime_path
    )
    