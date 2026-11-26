# -*- coding: utf-8 -*-

import re
import names

from squish import *
from common import *


def main():

    navigate_service_mode()

    test.vp("system_config_tab")

    def is_button_enabled(button):

        try:
            obj = findObject(button)

            return (
                obj.visible and
                obj.enabled
            )

        except LookupError:

            return False


    def click_available_button(
            increment_button,
            decrement_button):

        # Try increment first
        if is_button_enabled(increment_button):

            clickButton(
                waitForObject(increment_button)
            )

            snooze(0.5)

            return "increment"

        # If increment is disabled, try decrement
        elif is_button_enabled(decrement_button):

            clickButton(
                waitForObject(decrement_button)
            )

            snooze(0.5)

            return "decrement"

        return None

    increment = (
        names.fiberIdleTimeoutNumberPicker_pbIncrement_QPushButton
    )

    decrement = (
        names.fiberIdleTimeoutNumberPicker_pbDecrement_QPushButton
    )

    idle_time = (
        names.fiberIdleTimeoutNumberPicker_lbValue_QLabel
    )


    def get_idle_time():

        value = str(
            waitForObjectExists(idle_time).text
        )

        match = re.search(
            r"(\d+(?:\.\d+)?)",
            value
        )

        if not match:

            raise ValueError(
                "Unable to read fiber idle timeout value: " +
                value
            )

        return float(
            match.group(1)
        )


    # Read initial value
    initial_idle = get_idle_time()

    test.log(
        "Initial fiber idle timeout: " +
        str(initial_idle) +
        " hr"
    )


    # Change value
    idle_direction = click_available_button(
        increment,
        decrement
    )


    if idle_direction is None:

        test.fail(
            "FAIL: Fiber idle timeout cannot be changed. "
            "Both buttons are disabled. Current value: " +
            str(initial_idle) +
            " hr"
        )

    else:

        changed_idle = get_idle_time()

        test.log(
            "Fiber idle timeout after " +
            idle_direction +
            ": " +
            str(changed_idle) +
            " hr"
        )


        # Verify value changed
        if changed_idle != initial_idle:

            test.passes(
                "PASS: Fiber idle timeout changed from " +
                str(initial_idle) +
                " hr to " +
                str(changed_idle) +
                " hr"
            )

        else:

            test.fail(
                "FAIL: Fiber idle timeout did not change. "
                "Value remains " +
                str(initial_idle) +
                " hr"
            )


        if changed_idle > initial_idle:

            # Value was incremented
            if is_button_enabled(decrement):

                clickButton(
                    waitForObject(decrement)
                )

                snooze(0.5)

        elif changed_idle < initial_idle:

            # Value was decremented
            if is_button_enabled(increment):

                clickButton(
                    waitForObject(increment)
                )

                snooze(0.5)


        restored_idle = get_idle_time()

        test.log(
            "Fiber idle timeout restored to: " +
            str(restored_idle) +
            " hr"
        )


    rfid_region = (
        names.rfidRegionPanelFrame_rfidRegionComboBox_QComboBox
    )


    expected_regions = [

        "North America",
        "India",
        "Japan",
        "Peoples Republic of China",
        "European Union",
        "Korea",
        "New Zealand",
        "Malaysia",
        "Philippines",
        "Taiwan",
        "Russia",
        "Singapore",
        "Vietnam",
        "Thailand",
        "Argentina/Brazil",
        "Hong Kong",
        "Bangladesh",
        "Israel"

    ]


    # Current selected region
    before_region = str(
        waitForObject(rfid_region).currentText
    ).strip()


    test.log(
        "Current RFID region: " +
        before_region
    )


    # Open dropdown
    mouseClick(
        waitForObject(rfid_region),
        97,
        22,
        Qt.NoModifier,
        Qt.LeftButton
    )

    snooze(0.5)


    # Read dropdown values
    combo = waitForObject(rfid_region)

    actual_regions = []


    for index in range(combo.count):

        actual_regions.append(
            str(
                combo.itemText(index)
            )
        )


    test.log(
        "Expected RFID regions: " +
        str(expected_regions)
    )

    test.log(
        "Actual RFID regions: " +
        str(actual_regions)
    )


    # Compare available regions
    missing_regions = [

        region

        for region in expected_regions

        if region not in actual_regions

    ]


    unexpected_regions = [

        region

        for region in actual_regions

        if region not in expected_regions

    ]


    if not missing_regions and not unexpected_regions:

        test.passes(
            "PASS: All expected RFID regions are available"
        )

    else:

        test.fail(
            "FAIL: RFID Region list mismatch. " +
            "Missing: " +
            str(missing_regions) +
            ", Unexpected: " +
            str(unexpected_regions)
        )


    new_region = None


    for region in actual_regions:

        if region != before_region:

            new_region = region

            break


    if new_region:

        test.log(
            "Changing RFID Region: " +
            before_region +
            " -> " +
            new_region
        )


        mouseClick(
            waitForObjectItem(
                rfid_region,
                new_region
            ),
            80,
            14,
            Qt.NoModifier,
            Qt.LeftButton
        )

        snooze(0.5)


        after_region = str(
            waitForObject(rfid_region).currentText
        ).strip()


        test.log(
            "RFID Region after change: " +
            after_region
        )


        if after_region == new_region:

            test.passes(
                "PASS: RFID Region changed from " +
                before_region +
                " to " +
                after_region
            )

        else:

            test.fail(
                "FAIL: RFID Region change was not accepted. " +
                "Expected: " +
                new_region +
                ", Actual: " +
                after_region
            )

    else:

        test.fail(
            "FAIL: No alternate RFID Region available"
        )

    write_power = (
        names.rfidWritePowerNumberPicker_lbValue_QLabel
    )

    write_increment = (
        names.rfidWritePowerNumberPicker_pbIncrement_QPushButton
    )

    write_decrement = (
        names.rfidWritePowerNumberPicker_pbDecrement_QPushButton
    )


    def get_write_power():

        value = str(
            waitForObjectExists(write_power).text
        )

        match = re.search(
            r"(\d+(?:\.\d+)?)",
            value
        )

        if not match:

            raise ValueError(
                "Unable to read RFID write power: " +
                value
            )

        return float(
            match.group(1)
        )


    initial_write = get_write_power()


    test.log(
        "Initial RFID Write Power: " +
        str(initial_write) +
        " dB"
    )


    write_direction = click_available_button(
        write_increment,
        write_decrement
    )


    if write_direction is None:

        test.fail(
            "FAIL: RFID Write Power cannot be changed. "
            "Both buttons are disabled. Current value: " +
            str(initial_write) +
            " dB"
        )

        changed_write = initial_write

    else:

        changed_write = get_write_power()

        test.log(
            "RFID Write Power after " +
            write_direction +
            ": " +
            str(changed_write) +
            " dB"
        )


        if changed_write != initial_write:

            test.passes(
                "PASS: RFID Write Power changed from " +
                str(initial_write) +
                " dB to " +
                str(changed_write) +
                " dB"
            )

        else:

            test.fail(
                "FAIL: RFID Write Power did not change"
            )


        # Restore
        if changed_write > initial_write:

            if is_button_enabled(write_decrement):

                clickButton(
                    waitForObject(write_decrement)
                )

                snooze(0.5)

        elif changed_write < initial_write:

            if is_button_enabled(write_increment):

                clickButton(
                    waitForObject(write_increment)
                )

                snooze(0.5)


    restored_write = get_write_power()

    test.log(
        "RFID Write Power restored to: " +
        str(restored_write) +
        " dB"
    )


    read_power = (
        names.rfidReadPowerNumberPicker_lbValue_QLabel
    )

    read_increment = (
        names.rfidReadPowerNumberPicker_pbIncrement_QPushButton
    )

    read_decrement = (
        names.rfidReadPowerNumberPicker_pbDecrement_QPushButton
    )


    def get_read_power():

        value = str(
            waitForObjectExists(read_power).text
        )

        match = re.search(
            r"(\d+(?:\.\d+)?)",
            value
        )

        if not match:

            raise ValueError(
                "Unable to read RFID read power: " +
                value
            )

        return float(
            match.group(1)
        )


    initial_read = get_read_power()


    test.log(
        "Initial RFID Read Power: " +
        str(initial_read) +
        " dB"
    )


    read_direction = click_available_button(
        read_increment,
        read_decrement
    )


    if read_direction is None:

        test.fail(
            "FAIL: RFID Read Power cannot be changed. "
            "Both buttons are disabled. Current value: " +
            str(initial_read) +
            " dB"
        )

        changed_read = initial_read

    else:

        changed_read = get_read_power()

        test.log(
            "RFID Read Power after " +
            read_direction +
            ": " +
            str(changed_read) +
            " dB"
        )


        if changed_read != initial_read:

            test.passes(
                "PASS: RFID Read Power changed from " +
                str(initial_read) +
                " dB to " +
                str(changed_read) +
                " dB"
            )

        else:

            test.fail(
                "FAIL: RFID Read Power did not change"
            )


        # Restore
        if changed_read > initial_read:

            if is_button_enabled(read_decrement):

                clickButton(
                    waitForObject(read_decrement)
                )

                snooze(0.5)

        elif changed_read < initial_read:

            if is_button_enabled(read_increment):

                clickButton(
                    waitForObject(read_increment)
                )

                snooze(0.5)


    restored_read = get_read_power()

    test.log(
        "RFID Read Power restored to: " +
        str(restored_read) +
        " dB"
    )

    idle_ok = (
        restored_idle == initial_idle
    )

    write_ok = (
        restored_write == initial_write
    )

    read_ok = (
        restored_read == initial_read
    )


    if idle_ok:

        test.passes(
            "PASS: Fiber Idle Timeout setting restored correctly"
        )

    else:

        test.fail(
            "FAIL: Fiber Idle Timeout was not restored. " +
            "Initial: " +
            str(initial_idle) +
            ", Current: " +
            str(restored_idle)
        )


    if write_ok:

        test.passes(
            "PASS: RFID Write Power setting restored correctly"
        )

    else:

        test.fail(
            "FAIL: RFID Write Power was not restored. " +
            "Initial: " +
            str(initial_write) +
            ", Current: " +
            str(restored_write)
        )


    if read_ok:

        test.passes(
            "PASS: RFID Read Power setting restored correctly"
        )

    else:

        test.fail(
            "FAIL: RFID Read Power was not restored. " +
            "Initial: " +
            str(initial_read) +
            ", Current: " +
            str(restored_read)
        )
    
    
    
    
    