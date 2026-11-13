import os
import re
import names
import test
import common

import test


import test


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
    test.log("Starting Economy B and Frequency Test")

    runtime_path = os.path.expanduser(
        "~/Downloads/WORK/Gemini_GFL_2.5_Codebase_8May2026/"
        "build-gemini-Desktop-Debug"
    )

    common.configure_system_type(
        new_type="B",
        runtime_path=runtime_path
    )
    common.enter_login_pin()
    
    common.dismiss_fiber_verification_warning()
    
    common.verify_economyB_type()
    mouseClick(
        waitForObject(
            names.staticVersions_3_systemTypeVersion_QLabel
        ),
        57,
        17,
        Qt.NoModifier,
        Qt.LeftButton
    )
    
    clickButton(
        waitForObject(
            names.buttonsBar_backButton_QPushButton
        )
    )
    
    clickButton(
        waitForObject(
            names.buttonsBar_homeButton_QPushButton
        )
    )
    common.navigate_to_expert_screen()
    common.left_fragmentation_pulse()
    increment_frequency()    
    test.log("Economy B and Frequency Test Completed")
    