import re
import names

from common import *
from squish import *


def main():

    navigate_service_mode()

    clickButton(
        waitForObject(names.demoModePanel_pbDemoModeOn_QToolButton)
    )

    test.log(
        "Verifying warning message when demo mode toggled"
    )

    mouseClick(
        waitForObject(names.centralWidget_lbDialogTitle_QLabel_2),
        127, 19,
        Qt.NoModifier,
        Qt.LeftButton
    )

    test.compare(
        str(
            waitForObjectExists(
                names.centralWidget_lbDialogTitle_QLabel_2
            ).text
        ),
        "Demo Mode"
    )

    test.vp("Verifying demo mode toggle warning")

    clickButton(
        waitForObject(names.buttonsFrame_rejectButton_QPushButton)
    )

    mouseClick(
        waitForObject(names.systemConfigurationTab_rfidRegionLabel_QLabel),
        146, 47,
        Qt.NoModifier,
        Qt.LeftButton
    )

    mouseClick(
        waitForObject(
            names.rfidRegionPanelFrame_rfidRegionComboBox_QComboBox
        ),
        250, 21,
        Qt.NoModifier,
        Qt.LeftButton
    )

    mouseClick(
        waitForObjectItem(
            names.rfidRegionPanelFrame_rfidRegionComboBox_QComboBox,
            "India"
        ),
        78, 21,
        Qt.NoModifier,
        Qt.LeftButton
    )

    test.log(
        "Verifying warning message RFID Region change"
    )

    test.fail(
        "Failure Expected: 'Warning Popup' is not available "
        "in the application after RFID region change"
    )

    def get_power_value(value_object):

        value = str(
            waitForObjectExists(value_object).text
        ).strip()

        match = re.search(
            r"(\d+(?:\.\d+)?)",
            value
        )

        if not match:
            raise ValueError(
                "Unable to read power value: " + value
            )

        return float(match.group(1))


    def button_enabled(button):

        try:
            obj = findObject(button)

            return (
                obj.visible and
                obj.enabled
            )

        except LookupError:

            return False

    write_power = names.rfidWritePowerNumberPicker_lbValue_QLabel
    write_increment = names.rfidWritePowerNumberPicker_pbIncrement_QPushButton
    write_decrement = names.rfidWritePowerNumberPicker_pbDecrement_QPushButton

    initial_write = get_power_value(write_power)

    test.log(
        "RFID Write Power - Initial: " +
        str(initial_write) + " dB"
    )


    # Increment
    if button_enabled(write_increment):

        clickButton(
            waitForObject(write_increment)
        )

        snooze(0.5)

        after_increment_write = get_power_value(
            write_power
        )

        test.log(
            "RFID Write Power - After Increment: " +
            str(after_increment_write) + " dB"
        )

        if after_increment_write > initial_write:

            test.passes(
                "PASS: RFID Write Power increased after increment"
            )

        else:

            test.fail(
                "FAIL: RFID Write Power did not increase after increment"
            )

    else:

        test.log(
            "RFID Write Power increment button is disabled"
        )

        after_increment_write = initial_write


    # Decrement
    if button_enabled(write_decrement):

        clickButton(
            waitForObject(write_decrement)
        )

        snooze(0.5)

        after_decrement_write = get_power_value(
            write_power
        )

        test.log(
            "RFID Write Power - After Decrement: " +
            str(after_decrement_write) + " dB"
        )

        if after_decrement_write < after_increment_write:

            test.passes(
                "PASS: RFID Write Power decreased after decrement"
            )

        else:

            test.fail(
                "FAIL: RFID Write Power did not decrease after decrement"
            )

    else:

        test.log(
            "RFID Write Power decrement button is disabled"
        )

    read_power = names.rfidReadPowerNumberPicker_lbValue_QLabel
    read_increment = names.rfidReadPowerNumberPicker_pbIncrement_QPushButton
    read_decrement = names.rfidReadPowerNumberPicker_pbDecrement_QPushButton

    initial_read = get_power_value(read_power)

    test.log(
        "RFID Read Power - Initial: " +
        str(initial_read) + " dB"
    )


    # Increment
    if button_enabled(read_increment):

        clickButton(
            waitForObject(read_increment)
        )

        snooze(0.5)

        after_increment_read = get_power_value(
            read_power
        )

        test.log(
            "RFID Read Power - After Increment: " +
            str(after_increment_read) + " dB"
        )

        if after_increment_read > initial_read:

            test.passes(
                "PASS: RFID Read Power increased after increment"
            )

        else:

            test.fail(
                "FAIL: RFID Read Power did not increase after increment"
            )

    else:

        test.log(
            "RFID Read Power increment button is disabled"
        )

        after_increment_read = initial_read


    # Decrement
    if button_enabled(read_decrement):

        clickButton(
            waitForObject(read_decrement)
        )

        snooze(0.5)

        after_decrement_read = get_power_value(
            read_power
        )

        test.log(
            "RFID Read Power - After Decrement: " +
            str(after_decrement_read) + " dB"
        )

        if after_decrement_read < after_increment_read:

            test.passes(
                "PASS: RFID Read Power decreased after decrement"
            )

        else:

            test.fail(
                "FAIL: RFID Read Power did not decrease after decrement"
            )

    else:

        test.log(
            "RFID Read Power decrement button is disabled"
        )

    test.log(
        "Verifying warning message RFID configuration changes"
    )

    test.fail(
        "Failure Expected: 'Warning Popup' is not available "
        "in the application after RFID configuration changes"
    )
