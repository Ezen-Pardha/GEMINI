# -*- coding: utf-8 -*-
import os
import re
import names
import test
import common

def verify_pulse_energy_display():
    test.log("Verifying Pulse Energy Display Values")

    mouseClick(
        waitForObject(names.valueDrum_Cylinder),
        189, 56, Qt.NoModifier, Qt.LeftButton
    )
    clickButton(waitForObject(names.pulseEnergyWidget_incrementButton_QPushButton))

    mouseClick(
        waitForObject(names.valueDrum_Cylinder),
        107, 36, Qt.NoModifier, Qt.LeftButton
    )
    clickButton(waitForObject(names.pulseEnergyWidget_incrementButton_QPushButton))

    mouseClick(
        waitForObject(names.valueDrum_Cylinder),
        155, 35, Qt.NoModifier, Qt.LeftButton
    )
    clickButton(waitForObject(names.pulseEnergyWidget_incrementButton_QPushButton))

    mouseClick(
        waitForObject(names.valueDrum_Cylinder),
        142, 30, Qt.NoModifier, Qt.LeftButton
    )
    clickButton(waitForObject(names.pulseEnergyWidget_incrementButton_QPushButton))

    mouseClick(
        waitForObject(names.valueDrum_Cylinder),
        146, 34, Qt.NoModifier, Qt.LeftButton
    )
    clickButton(waitForObject(names.pulseEnergyWidget_incrementButton_QPushButton))

    mouseClick(
        waitForObject(names.valueDrum_Cylinder),
        178, 28, Qt.NoModifier, Qt.LeftButton
    )
    clickButton(waitForObject(names.pulseEnergyWidget_incrementButton_QPushButton))

    mouseClick(
        waitForObject(names.valueDrum_Cylinder),
        122, 31, Qt.NoModifier, Qt.LeftButton
    )
    clickButton(waitForObject(names.pulseEnergyWidget_incrementButton_QPushButton))

    mouseClick(
        waitForObject(names.valueDrum_Cylinder),
        162, 30, Qt.NoModifier, Qt.LeftButton
    )
    clickButton(waitForObject(names.pulseEnergyWidget_incrementButton_QPushButton))

    mouseClick(
        waitForObject(names.valueDrum_Cylinder),
        157, 37, Qt.NoModifier, Qt.LeftButton
    )
    clickButton(waitForObject(names.pulseEnergyWidget_incrementButton_QPushButton))

    mouseClick(
        waitForObject(names.valueDrum_Cylinder),
        150, 45, Qt.NoModifier, Qt.LeftButton
    )
    clickButton(waitForObject(names.pulseEnergyWidget_incrementButton_QPushButton))

    mouseClick(
        waitForObject(names.valueDrum_Cylinder),
        125, 48, Qt.NoModifier, Qt.LeftButton
    )
    clickButton(waitForObject(names.pulseEnergyWidget_incrementButton_QPushButton))

    mouseClick(
        waitForObject(names.valueDrum_Cylinder),
        151, 43, Qt.NoModifier, Qt.LeftButton
    )
    clickButton(waitForObject(names.pulseEnergyWidget_incrementButton_QPushButton))

    mouseClick(
        waitForObject(names.valueDrum_Cylinder),
        148, 30, Qt.NoModifier, Qt.LeftButton
    )

    test.log("Pulse Energy click sequence completed")
def main():
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
    common.left_dusting_pulse()
    verify_pulse_energy_display()
    runtime_path = os.path.expanduser(
        "/home/ezen/Gemini_v1"
    )
    common.configure_system_type(
        new_type="B",
        runtime_path=runtime_path
    )