# -*- coding: utf-8 -*-

import names
from common import *

def main():
<<<<<<< HEAD
    runtime_path = os.path.expanduser(
        "/home/ezen/Gemini_v1"
=======
    test.log("SVV TAG POP-PKP-001:Peak Power Selection Popup Low Button")
    enter_login_pin()
    verify_economy_type()
    runtime_path = os.path.expanduser(
        "/home/ezen/29October/latest Build (no Buttons bar)/build-gemini-Desktop-Debug/"
>>>>>>> afaf95eb9524d0398baf7cef49b0e422af595ff6
    )
 
    configure_system_type(
        new_type="B",
        runtime_path=runtime_path
    )
    test.log("Closing the currently running AUT")
    
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
    enter_login_pin()
    verify_economy_type()
    test.log("SVV TAG POP-PKP-001:Peak Power Selection Popup Low Button")
    clickButton(waitForObject(names.buttonsBar_backButton_QPushButton))
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton_8))
    clickButton(waitForObject(names.gbExpert_expertButton_QPushButton))
    test.passes("Manual treatment screen is verified") 
<<<<<<< HEAD
=======
    test.vp("peakPowerMode")
>>>>>>> afaf95eb9524d0398baf7cef49b0e422af595ff6
    test.vp("treatmentScreen")
    mouseClick(waitForObject(names.modeButton_nameLabel_QLabel, 126880), 54, 12, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_Square_QPushButton))
    mouseClick(waitForObject(names.peakPowerButton_nameLabel_QLabel_2, 455823), 59, 25, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_pw125_QPushButton_2, 149140))
    if test.imagePresent("lowPeakPower "):
        test.passes("Low Peak Power image is present and verified.")
    else:
        test.fail("Low Peak Power image is not present.")
    
    mouseClick(waitForObject(names.pulseModeWidget_buttonsWidget_QWidget), 474, 9, Qt.NoModifier, Qt.LeftButton)
    test.passes("Peak Power button is verified in the left pedal")
    test.imagePresent("RighPedalRegularPulse")
    test.passes("Right Pedal regular pulse button verified")
    test.imagePresent("rightPeakPower")
    test.passes("Right Pedal PeakPower button is verified")
<<<<<<< HEAD
=======
     
    test.log("SVV TAG POP-PKP-001:Peak Power Selection Popup Low Button")
>>>>>>> afaf95eb9524d0398baf7cef49b0e422af595ff6
    
    test.log("SVV TAG POP-PKP-002:Peak Power Selection Popup Medium Button")
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton_4))
    clickButton(waitForObject(names.gbExpert_expertButton_QPushButton))
    test.passes("Manual treatment screen is verified")   
    test.imagePresent("pulseModeButton")
    test.passes("Pulse Mode button is verified in the left pedal")
    mouseClick(waitForObject(names.peakPowerButton_nameLabel_QLabel_2, 181302), 41, 38, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_pw250_QPushButton_2))
    test.imagePresent("peakPowerMedium")
    test.passes("Medium Peak power button is verified ")
    test.imagePresent("rightRegularPulseMedium")
    test.passes("Right Regular pulse button is verified ")
    mouseClick(waitForObject(names.peakPowerButton_nameLabel_QLabel_3), 66, 38, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_pw250_QPushButton_2))
    test.imagePresent("rightpeakPowerMedium", { "occurrence": 2 })
    test.passes("Right peak power Medium button is verified ")
<<<<<<< HEAD
=======
   
    
>>>>>>> afaf95eb9524d0398baf7cef49b0e422af595ff6
    
    test.log("SVV TAG POP-PKP-003:Peak Power Selection Popup High Button")
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton_4))
    clickButton(waitForObject(names.gbExpert_expertButton_QPushButton))
    test.passes("Manual screen verified")
    mouseClick(waitForObject(names.modeButton_nameLabel_QLabel), 108, 44, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_Square_QPushButton))
    mouseClick(waitForObject(names.peakPowerButton_iconLabel_QLabel_2), 29, 41, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_pw500_QPushButton_2))
    test.imagePresent("regularPulsech")
    test.passes("Pulse button is verified")
    test.imagePresent("peakPowerHighB")
    test.passes("Peak power button is verified")
    mouseClick(waitForObject(names.modeButton_nameLabel_QLabel_2, 33130), 76, 28, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_Square_QPushButton))
    mouseClick(waitForObject(names.peakPowerButton_iconLabel_QLabel_3), 16, 42, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_pw500_QPushButton_2))
    test.imagePresent("regularPulsech")
    test.passes("Right pedal Pulse button is verified")
    
    """Peak Power Selection Popup High Button in Fragmentation pulse Mode"""
    test.log("Peak Power Selection Popup High Button in Fragmentation pulse Mode")
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton_4))
    clickButton(waitForObject(names.gbExpert_expertButton_QPushButton))
    test.passes("Manual screen verified")
    mouseClick(waitForObject(names.modeButton_nameLabel_QLabel), 89, 34, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_Fragmentation_QPushButton_2))
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton_2))

    try:
        peak_power_button = waitForObjectExists(names.peakPowerButton_iconLabel_QLabel_2, 3000)

        if object.exists(peak_power_button):
            mouseClick(peak_power_button, 35, 36, Qt.NoModifier, Qt.LeftButton)
            test.passes("Peak Power button is available and clicked successfully.")
        else:
            test.fail("Peak Power button is not available or not clickable. Continuing the script.")

    except Exception as e:
        test.fail("Peak Power button click failed. Reason: Fragmentation pulse mode selected")
   
    test.imagePresent("fragmentationPulseButton")
    test.passes("Left pedal Pulse button is verified")
    mouseClick(waitForObject(names.modeButton_nameLabel_QLabel_2), 37, 30, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_Fragmentation_QPushButton_2))
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton_2))
    test.imagePresent("fragmentationPulseButton")
    test.passes("Right pedal Pulse button is verified")
    
    """Peak Power Selection Popup High Button in Enucleation pulse Mode"""
    test.log("Peak Power Selection Popup High Button in Enucleation pulse Mode")
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton_4))
    clickButton(waitForObject(names.gbExpert_expertButton_QPushButton))
    test.passes("Manual screen verified")
    mouseClick(waitForObject(names.modeButton_nameLabel_QLabel), 89, 34, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_Enucleation_QPushButton_2))
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton_2))
    test.imagePresent("enucleationPulse")
    test.passes("Left pedal Pulse button is verified")
    try:
        peak_power_button = waitForObjectExists(names.peakPowerButton_iconLabel_QLabel_2, 3000)

        if object.exists(peak_power_button):
            mouseClick(peak_power_button, 35, 36, Qt.NoModifier, Qt.LeftButton)
            test.passes("Peak Power button is available and clicked successfully.")
        else:
            test.fail("Peak Power button is not available or not clickable. Continuing the script.")

    except Exception as e:
        test.fail("Peak Power button click failed. Reason: Enucleation pulse Mode" )
    
    mouseClick(waitForObject(names.modeButton_nameLabel_QLabel_2, 35629), 40, 16, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_Enucleation_QPushButton_2))
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton_2))
    test.imagePresent("enucleationPulse")
    test.passes("Right pedal Pulse button is verified")
    """Peak Power Selection Popup High Button in Minimal Carbonization pulse Mode"""
    test.log("Peak Power Selection Popup High Button in Minimal Carbonization pulse Mode")
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton_4))
    clickButton(waitForObject(names.gbExpert_expertButton_QPushButton))
    test.passes("Manual screen verified")
    mouseClick(waitForObject(names.modeButton_nameLabel_QLabel), 89, 34, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_Enucleation_QPushButton_2))
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton_2))
    mouseClick(waitForObject(names.modeButton_nameLabel_QLabel), 79, 21, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.cleaning_icon_QPushButton))
    clickButton(waitForObject(names.centralWidget_OKButton_QPushButton_2))
    clickButton(waitForObject(names.centralWidget_Cleaning_QPushButton_2))
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton_2))
    test.imagePresent("minimalCarbonizationPulseCL")
    test.passes("Left pedal Pulse button is verified")
    
    try:
        peak_power_button = waitForObjectExists(names.peakPowerButton_iconLabel_QLabel_2, 3000)

        if object.exists(peak_power_button):
            mouseClick(peak_power_button, 35, 36, Qt.NoModifier, Qt.LeftButton)
            test.passes("Peak Power button is available and clicked successfully.")
        else:
            test.fail("Peak Power button is not available or not clickable. Continuing the script.")

    except Exception as e:
        test.fail("Peak Power button click failed. Reason: Minimal Carbonization pulse Mode")
    
    mouseClick(waitForObject(names.treatmentScreen_bottomBar_QFrame), 1203, 1, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.modeButton_nameLabel_QLabel_2), 91, 50, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_Cleaning_QPushButton_2))
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton_2))
    test.imagePresent("minimalCarbonizationPulseCL")
    test.passes("Right pedal Pulse Mode button is verified")
   
    """Peak Power Selection Popup High Button in MRP Pulse Mode"""
    test.passes("Peak Power Selection Popup High Button in MRP pulse") 
    mouseClick(waitForObject(names.modeButton_nameLabel_QLabel), 100, 24, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_MRP_QPushButton_2))
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton_2))
    test.imagePresent("mrpPulsemodebutton")
    test.passes("Left Pedal MRP pulse mode button is verified")
    mouseClick(waitForObject(names.modeButton_nameLabel_QLabel_2), 38, 26, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_MRP_QPushButton_2))
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton_2))
   
    try:
        peak_power_button = waitForObjectExists(names.peakPowerButton_iconLabel_QLabel_2, 3000)

        if object.exists(peak_power_button):
            mouseClick(peak_power_button, 35, 36, Qt.NoModifier, Qt.LeftButton)
            test.passes("Peak Power button is available and clicked successfully.")
        else:
            test.fail("Peak Power button is not available or not clickable. Continuing the script.")

    except Exception as e:
        test.fail("Peak Power button click failed. Reason: MRP pulse Mode" )
    
    test.imagePresent("mrpPulsemodebutton")
    test.passes("Right Pedal MRP pulse mode button is verified")


    
    
