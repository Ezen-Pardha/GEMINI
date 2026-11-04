from common import *
import test
from common import *
import test



def left_verify_pulse_energy_range():
    test.log("Starting Pulse Energy range verification")

    expected_values = [2, 2.5, 3, 3.5, 4, 4.5, 5]

    increment_button = waitForObject(
        names.pulseEnergyWidget_incrementButton_QPushButton
    )

    cylinder = waitForObject(names.valueDrum_Cylinder)

    test.log("Cylinder internal value: {}".format(cylinder.value))

    for index, expected in enumerate(expected_values):
        test.log(
            "Checking Pulse Energy setting: {} J".format(expected)
        )
        test.passes(
            "Pulse Energy navigation checkpoint reached for {} J".format(
                expected
            )
        )

        if index < len(expected_values) - 1:
            clickButton(increment_button)
            snooze(0.3)

    test.log("Pulse Energy navigation completed")
    



def right_pulse_energy():
    test.log("Starting second Pulse Energy configuration")

    mode_label = waitForObject(
        names.modeButton_nameLabel_QLabel_2
    )

    mouseClick(
        mode_label,
        82, 39,
        Qt.NoModifier,
        Qt.LeftButton
    )
    clickButton(
        waitForObject(names.centralWidget_Enucleation_QPushButton)
    )

    clickButton(
        waitForObject(names.centralWidget_DisableButton_QPushButton)
    )

    for _ in range(6):
        clickButton(
            waitForObject(
                names.pulseEnergyWidget_incrementButton_QPushButton_2
            )
        )
        snooze(0.3)

    test.passes("Second Pulse Energy configuration completed")


  
def main():
    test.log("START: Expert Pulse Energy test")
    try:
        enter_login_pin()
        dismiss_fiber_verification_warning()
        navigate_to_expert_screen()
        left_navigate_to_enucleation_disable()
        left_verify_pulse_energy_range()
        right_pulse_energy()
        navigate_to_home_screen()
        
    except Exception as error:
        test.fail("Expert Pulse Energy test failed: {}".format(error))
        raise
