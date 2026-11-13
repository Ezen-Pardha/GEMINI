# -*- coding: utf-8 -*-
import os
import names

from squish import *
from common import *

def main():

    # Change Economy Type to C and restart AUT
    runtime_path = os.path.expanduser(
        "/home/ntc/Downloads/Gemini"
    )

    configure_system_type(
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

    test.passes("Bravo AUT restart command executed successfully")
    
    # Login and navigate to Dusting Pulse Mode
    enter_login_pin()
    dismiss_fiber_verification_warning()
    
    verify_economyc_type()
    back_to_homescreen_from_servicemode()
    
    clickButton(waitForObject(names.gbExpert_expertButton_QPushButton))

    mouseClick(waitForObject(names.modeButton_nameLabel_QLabel),108, 26,Qt.NoModifier,Qt.LeftButton)

    clickButton(waitForObject(names.centralWidget_Dusting_QPushButton))

    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))

    snooze(2)
    
    test.fail(" Peak power level value of 1000W is not available on the application's GUI")
    # test.vp("Peak_power_1000W")
    # test.passes("PASS: Dusting pulse peak power level verification completed")
    
    runtime_path = os.path.expanduser(
        "/home/ntc/Downloads/Gemini"
    )

    configure_system_type(
        new_type="B",
        runtime_path=runtime_path
    )
    

