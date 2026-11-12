
# -*- coding: utf-8 -*-

from common import *
import names


def main():

    enter_login_pin()

    clickButton(waitForObject(names.mainFrame_okButton_QPushButton))

    # Verify Home screen
    try:
        waitForObjectExists(names.homeScreen_HomeScreen)
        test.passes("PASS: Home screen is displayed after login.")
    except Exception as error:
        test.fail("FAIL: Home screen not found: " + str(error))
        return

    # Recorded navigation
    mouseClick(
        waitForObject(names.homeScreen_HomeScreen),
        639, 182, Qt.NoModifier, Qt.LeftButton
    )

    mouseClick(
        waitForObject(names.homeScreen_HomeScreen),
        269, 476, Qt.NoModifier, Qt.LeftButton
    )

    mouseClick(
        waitForObject(names.homeScreen_gbExpert_QFrame),
        1068, 94, Qt.NoModifier, Qt.LeftButton
    )

    clickButton(waitForObject(names.gbExpert_expertButton_QPushButton))

    mouseClick(
        waitForObject(names.leftPedalWidget_wdPresetTabs_TabWidget),
        509, 30, Qt.NoModifier, Qt.LeftButton
    )

    mouseClick(
        waitForObject(names.rightPedalWidget_wdPresetTabs_TabWidget),
        266, 20, Qt.NoModifier, Qt.LeftButton
    )

    mouseClick(
        waitForObject(names.modeButton_nameLabel_QLabel, 90195),
        88, 31, Qt.NoModifier, Qt.LeftButton
    )

    mouseClick(
        waitForObject(names.centralWidget_label_2_QLabel),
        286, 34, Qt.NoModifier, Qt.LeftButton
    )

    sendEvent(
        "QMouseEvent",
        waitForObject(names.backgroundShadowWidget_QWidget),
        QEvent.MouseButtonPress,
        688, 322, Qt.LeftButton, 1, 0
    )

    mouseClick(
        waitForObject(names.totalTimeFrame_nameLabel_QLabel),
        174, 36, Qt.NoModifier, Qt.LeftButton
    )

    mouseClick(
        waitForObject(names.modeButton_nameLabel_QLabel),
        67, 34, Qt.NoModifier, Qt.LeftButton
    )

    sendEvent(
        "QMouseEvent",
        waitForObject(names.backgroundShadowWidget_QWidget),
        QEvent.MouseButtonPress,
        803, 452, Qt.LeftButton, 1, 0
    )

    mouseDrag(
        waitForObject(names.indexPicker_valuePicker_IntervalSlider, 85743),
        87, 19, -86, -14, 1, Qt.LeftButton
    )

    clickButton(waitForObject(names.buttonsFrame_rejectButton_QPushButton))
    clickButton(waitForObject(names.buttonsFrame_rejectButton_QPushButton_2))

    mouseClick(
        waitForObject(names.valueDrum_Cylinder),
        50, 18, Qt.NoModifier, Qt.LeftButton
    )

    mouseClick(
        waitForObject(names.pulseEnergyWidget_nameLabel_QLabel),
        102, 31, Qt.NoModifier, Qt.LeftButton
    )

    # Pulse energy verification
    expected_values = [
        0.2, 0.3, 0.4, 0.5, 0.6,
        0.7, 0.8, 0.9, 1.0, 1.1,
        1.2, 1.3, 1.4, 1.5, 1.6,
        1.7, 1.8, 1.9, 2.0, 2.5,
        3.0, 3.5, 4.0, 5.0, 6.0
    ]

    value_object = names.valueDrum_Cylinder
    increment_button = names.pulseEnergyWidget_incrementButton_QPushButton

    def read_value():
        obj = waitForObjectExists(value_object)
        return float(str(obj.displayedValue).strip())

    try:
        actual_value = read_value()
    except Exception as error:
        test.fail("FAIL: Unable to read initial pulse energy: " + str(error))
        return

    if abs(actual_value - expected_values[0]) >= 0.001:
        test.fail(
            "FAIL: Expected 0.2 J, actual "
            + str(actual_value) + " J"
        )
        return

    test.passes(
        "PASS: Expected 0.2 J, actual "
        + str(actual_value) + " J"
    )

    for expected_value in expected_values[1:]:

        previous_value = read_value()

        try:
            button = waitForObject(increment_button)

            # Click the center area of the increment button
            mouseClick(
                button, 10, 10,
                Qt.NoModifier, Qt.LeftButton
            )

            # Wait until the displayed value changes
            changed = waitFor(
                lambda: abs(read_value() - previous_value) >= 0.001,
                3000
            )

            if not changed:
                actual_value = read_value()
                test.fail(
                    "FAIL: Value did not change after increment. "
                    "Previous: " + str(previous_value) + " J, "
                    "Actual: " + str(actual_value) + " J"
                )
                return

            actual_value = read_value()

        except Exception as error:
            test.fail(
                "FAIL: Error checking expected "
                + str(expected_value) + " J: " + str(error)
            )
            return

        if abs(actual_value - expected_value) < 0.001:
            test.passes(
                "PASS: Expected " + str(expected_value)
                + " J, actual " + str(actual_value) + " J"
            )
        else:
            test.fail(
                "FAIL: Expected " + str(expected_value)
                + " J, actual " + str(actual_value) + " J"
            )
            return

    test.passes(
        "PASS: All 25 pulse energy values verified successfully."
    )
