import names
from squish import *
from common import *


def main():

    enter_login_pin()
    dismiss_fiber_verification_warning()

    # Select Fragmentation pulse mode
    clickButton(waitForObject(names.gbExpert_expertButton_QPushButton))

    mouseClick(waitForObject(names.modeButton_nameLabel_QLabel), 102, 32, Qt.NoModifier, Qt.LeftButton)

    clickButton(waitForObject(names.centralWidget_Fragmentation_QPushButton))
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))

    snooze(2)

    frequency = names.valueDrum_Cylinder_2
    increment = names.frequencyWidget_incrementButton_QPushButton
    decrement = names.frequencyWidget_decrementButton_QPushButton

    def get_frequency():
        return float(str(
            waitForObjectExists(frequency).displayedValue
        ).strip())

    def button_enabled(button):
        try:
            obj = findObject(button)
            return obj.visible and obj.enabled
        except LookupError:
            return False

    # ---------------------------------------------------------
    # Find minimum frequency
    # ---------------------------------------------------------

    actual = get_frequency()

    while button_enabled(decrement):

        previous = actual

        clickButton(waitForObject(decrement))
        snooze(0.5)

        actual = get_frequency()

        if actual >= previous:
            break

    minimum = get_frequency()

    # ---------------------------------------------------------
    # Find maximum frequency
    # ---------------------------------------------------------

    while button_enabled(increment):

        previous = actual

        clickButton(waitForObject(increment))
        snooze(0.5)

        actual = get_frequency()

        if actual <= previous:
            break

    maximum = get_frequency()

    # ---------------------------------------------------------
    # Verify frequency range
    # ---------------------------------------------------------

    test.log("Expected frequency range: 1 Hz - 40 Hz")
    test.log(
        "Actual frequency range: " +
        str(minimum) + " Hz - " + str(maximum) + " Hz"
    )

    if abs(minimum - 1.0) < 0.001 and abs(maximum - 40.0) < 0.001:

        test.passes(
            "PASS: Fragmentation pulse frequency range is "
            "1 Hz - 40 Hz"
        )

    else:

        test.fail(
            "FAIL: Fragmentation pulse frequency range is " +
            str(minimum) + " Hz - " + str(maximum) +
            " Hz. Expected: 1 Hz - 40 Hz"
        )

