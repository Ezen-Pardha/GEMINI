
import names
from common import *

def main():

    enter_login_pin()

    clickButton(waitForObject(names.homeScreen_settingsButton_QPushButton))
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    clickButton(waitForObject(names.gbExpert_expertButton_QPushButton))

    # Select MRP pulse mode

    mouseClick(waitForObject(names.modeButton_nameLabel_QLabel), 114, 39, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.centralWidget_MRP_QPushButton))
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))

    expected_values = [
        0.2, 0.3, 0.4, 0.5, 0.6,
        0.7, 0.8, 0.9, 1.0, 1.1,
        1.2, 1.3, 1.4, 1.5, 1.6,
        1.7, 1.8, 1.9, 2.0, 2.5,
        3.0, 3.5, 4.0, 5.0, 6.0
    ]

    value_object = names.valueDrum_Cylinder
    increment_button = names.pulseEnergyWidget_incrementButton_QPushButton

    def read_pulse_energy():
        value = waitForObjectExists(value_object).displayedValue
        return float(str(value).strip())

    # Verify the initial setting
    actual_value = read_pulse_energy()

    if abs(actual_value - expected_values[0]) < 0.001:
        test.log(
            "PASS: Initial pulse energy verified: " +
            str(actual_value) + " J"
        )
    else:
        test.fail(
            "Initial pulse energy mismatch. Expected: 0.2 J, Actual: " +
            str(actual_value) + " J"
        )
        return

    # Verify each subsequent discrete setting
    for expected_value in expected_values[1:]:

        clickButton(waitForObject(increment_button))

        # Wait for the displayed value to update
        snooze(1)

        actual_value = read_pulse_energy()

        if abs(actual_value - expected_value) < 0.001:
            test.log(
                "PASS: Pulse energy setting verified: " +
                str(expected_value) + " J"
            )
            test.passes("Pulse Energy Value is: "+ str(actual_value) + " J")
        else:
            test.fail(
                "Pulse energy mismatch. Expected: " +
                str(expected_value) + " J, Actual: " +
                str(actual_value) + " J"
            )
            return

    test.passes(
        "All 25 discrete MRP pulse energy settings verified "
        "successfully from 0.2 J to 6.0 J."
    )
