from common import *
import common
import names
import test


def verify_pulse_energy_range():

    expected_minimum = 4
    expected_maximum = 8

    test.log("START: Pulse Energy range verification")
    current_value = 4
    displayed_maximum = 6

    test.log("Expected minimum: {} J".format(expected_minimum))
    test.log("Expected maximum: {} J".format(expected_maximum))
    test.log("Displayed minimum: {} J".format(current_value))
    test.log("Displayed maximum: {} J".format(displayed_maximum))

    if displayed_maximum != expected_maximum:
        test.fail(
            "Pulse Energy maximum mismatch. Expected: {} J, "
            "Displayed: {} J".format(
                expected_maximum, displayed_maximum
            )
        )
        return

    test.passes(
        "Pulse Energy range verified: {} J to {} J".format(
            expected_minimum, expected_maximum
        )
    )
    
def right_Minimal_Carbonization():

    mouseClick(
        waitForObject(names.modeButton_nameLabel_QLabel_2),
        15, 28, Qt.NoModifier, Qt.LeftButton
    )
    mouseClick(
        waitForObject(names.centralWidget_mainWidget_QWidget),
        198, 484, Qt.NoModifier, Qt.LeftButton
    )

    clickButton(
        waitForObject(names.centralWidget_Cleaning_QPushButton)
    )

    clickButton(
        waitForObject(names.centralWidget_DisableButton_QPushButton)
    )

    mouseClick(
        waitForObject(names.valueDrum_Cylinder_2),
        153, 46, Qt.NoModifier, Qt.LeftButton
    )

    clickButton(
        waitForObject(
            names.pulseEnergyWidget_incrementButton_QPushButton_2
        )
    )
    mouseClick(
        waitForObject(names.valueDrum_Cylinder_2),
        92, 43, Qt.NoModifier, Qt.LeftButton
    )



def main():
    common.enter_login_pin()
    common.dismiss_fiber_verification_warning()
    common.navigate_to_expert_screen()
    common.left_Minimal_Carbonization()
    verify_pulse_energy_range()
    right_Minimal_Carbonization
    common.navigate_to_home_screen()
