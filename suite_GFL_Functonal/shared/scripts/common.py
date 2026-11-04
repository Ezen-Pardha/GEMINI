from squish import *
import test
import names
import datetime
import subprocess
import os
import re

def capture_screenshot(description="screenshot", category="Images"):
    """Capture the active window and save it under Screenshots/Images."""

    category = category.strip()

    if category != "Images":
        raise ValueError("Category must be Images")

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    safe_description = "".join(
        c if c.isalnum() or c in "_-" else "_"
        for c in description
    )

    screenshot_root = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(
            os.path.abspath(__file__)
        ))),
        "Screenshots"
    )

    screenshot_dir = os.path.join(screenshot_root, category)
    os.makedirs(screenshot_dir, exist_ok=True)

    screenshot_path = os.path.join(
        screenshot_dir,
        "{}_{}.png".format(safe_description, timestamp)
    )

    try:
        subprocess.run(
            ["gnome-screenshot", "-w", "-f", screenshot_path],
            check=True,
            timeout=15
        )

        test.log("Screenshot saved: {}".format(screenshot_path))
        return screenshot_path

    except Exception as error:
        test.warning("Screenshot capture failed: {}".format(error))
        return None

def click_and_report(object_name, description, timeout=20000):
    """Wait for an object, click it, and report the result."""
    try:
        obj = waitForObject(object_name, timeout)
        clickButton(obj)

        test.passes("PASS: {}".format(description))
        return True

    except Exception as error:
        test.fail("FAIL: {} - {}".format(description, error))
        raise


def mouse_click_and_report(
        object_name, description, x, y, timeout=20000):
    """Perform a mouse click and report the result."""
    try:
        obj = waitForObject(object_name, timeout)

        mouseClick(
            obj,
            x, y,
            Qt.NoModifier,
            Qt.LeftButton
        )

        test.passes("PASS: {}".format(description))

    except Exception as error:
        test.fail("FAIL: {} - {}".format(description, error))
        raise


def double_click_and_report(
        object_name, description, x, y, timeout=20000):
    """Perform a double-click and report the result."""
    try:
        obj = waitForObject(object_name, timeout)

        doubleClick(
            obj,
            x, y,
            Qt.NoModifier,
            Qt.LeftButton
        )

        test.passes("PASS: {}".format(description))

    except Exception as error:
        test.fail("FAIL: {} - {}".format(description, error))
        raise


def mouse_drag_and_report(
        object_name,
        description,
        start_x, start_y,
        end_x, end_y,
        timeout=20000):
    """Perform a mouse drag and report the result."""
    try:
        obj = waitForObject(object_name, timeout)

        mouseDrag(
            obj,
            start_x, start_y,
            end_x, end_y,
            1,
            Qt.LeftButton
        )

        test.passes("PASS: {}".format(description))

    except Exception as error:
        test.fail("FAIL: {} - {}".format(description, error))
        raise

def enter_login_pin():
    """Enter PIN 8888."""
    test.log("Entering login PIN 8888")

    for index in range(4):
        click_and_report(
            names.numpad_pushButton_8_NumpadButton,
            "Enter PIN digit 8 ({} of 4)".format(index + 1)
        )


def dismiss_fiber_verification_warning():
    """Handle the fiber verification warning dialog."""

    mouse_drag_and_report(
        names.fiberVerificationWarningDialog_mainFrame_QFrame,
        "Handle fiber verification warning",
        570, 490,
        17, 88
    )

    click_and_report(
        names.mainFrame_okButton_QPushButton,
        "Confirm fiber verification warning"
    )


def navigate_to_expert_screen():
    """Navigate to the Expert screen."""

    click_and_report(
        names.gbExpert_expertButton_QPushButton,
        "Open Expert screen"
    )


def left_navigate_to_enucleation_disable():
    test.log("Selecting Mode")

    mouseClick(
        waitForObject(names.modeButton_nameLabel_QLabel),
        78, 37,
        Qt.NoModifier,
        Qt.LeftButton
    )

    test.log("Selecting Enucleation")

    clickButton(
        waitForObject(names.centralWidget_Enucleation_QPushButton)
    )

    test.log("Clicking Disable button")

    clickButton(
        waitForObject(names.centralWidget_DisableButton_QPushButton)
    )

    test.log("Enucleation Disable navigation completed")
    

    
def navigate_to_home_screen():
    """Navigate back to the Home Screen from Treatment Screen"""
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    "Home Screen"
    
def verify_economyB_type():
    test.log("Checking System Type")

    clickButton(
        waitForObject(names.homeScreen_settingsButton_QPushButton)
    )

    clickTab(
        waitForObject(names.settingsScreen_tbSystemInfo_TabWidget),
        "LOGS"
    )

    clickButton(
        waitForObject(names.settingsScreen_pbService_QPushButton)
    )

    for _ in range(5):
        clickButton(
            waitForObject(names.numpad_pushButton_9_NumpadButton)
        )

    system_type_label = waitForObject(
        names.staticVersions_3_systemTypeVersion_QLabel
    )

    actual_type = str(system_type_label.text).strip()

    test.log("Actual System Type: {}".format(actual_type))

    if actual_type.replace(" ", "").lower() == "economyb":
        test.passes("System Type is Economy B")
        return True

    message = "Incorrect Economy: Expected Economy B, found {}".format(
        actual_type
    )

    test.fail(message)

    try:
        QMessageBox.warning(
            None,
            "Incorrect Economy",
            message
        )
    except Exception:
        test.log("Unable to show QMessageBox; see failure log above")

    return False


def back_to_homescreen_from_servicemode():
    clickButton(waitForObject(names.buttonsBar_backButton_QPushButton))
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton_2))
    
    
def  left_Minimal_Carbonization ():
    mouseClick(
        waitForObject(names.modeButton_nameLabel_QLabel),
        35, 51, Qt.NoModifier, Qt.LeftButton
    )
    clickButton(
        waitForObject(names.centralWidget_Cleaning_QPushButton)
    )
    clickButton(
        waitForObject(names.centralWidget_DisableButton_QPushButton)
    )


def verify_economyC_type():
 
    test.log("Checking System Type")
 
    clickButton(
        waitForObject(names.homeScreen_settingsButton_QPushButton)
    )
 
    clickTab(
        waitForObject(names.settingsScreen_tbSystemInfo_TabWidget),
        "LOGS"
    )
 
    clickButton(
        waitForObject(names.settingsScreen_pbService_QPushButton)
    )
    snooze(2)
    test.compare(str(waitForObjectExists(names.centralWidget_titleLabel_QLabel).text), "Version Not Supported")    
    clickButton(waitForObject(names.centralWidget_okButton_QPushButton))
    for _ in range(4):
        clickButton(
            waitForObject(names.numpad_pushButton_9_NumpadButton)
        )
    system_type_label = waitForObject(
        names.staticVersions_3_systemTypeVersion_QLabel
    )
 
    actual_type = str(system_type_label.text).strip()
 
    test.log("Actual System Type: {}".format(actual_type))
 
    if actual_type.replace(" ", "").lower() == "economyc":
 
        test.passes("System Type is Economy C")
        return True
 
    message = "Incorrect Economy: Expected Economy C, found {}".format(
        actual_type
    )
 
    test.fail(message)
 
    try:
        QMessageBox.warning(
            None,
            "Incorrect Economy",
            message
        )
    except Exception:
        test.log("Unable to show QMessageBox; see failure log above")
 
    return False


def find_device_ini(runtime_path):
    """
    Validate and return the device.ini path provided by the test case.
    """
    file_path = runtime_path + "/bin/media/mmcblk1p1/factory/device.ini"
    
    ini_path = os.path.abspath(
        os.path.expanduser(file_path)
    )

    if not os.path.isfile(ini_path):
        raise FileNotFoundError(
            "Runtime device.ini not found: {}".format(ini_path)
        )

    test.log("Selected device.ini: {}".format(ini_path))
    return ini_path


def update_system_type(new_type, runtime_path):
    """
    Update systemType to A, B, or C in the specified device.ini.
    """

    new_type = str(new_type).strip().upper()

    if new_type not in ("A", "B", "C"):
        raise ValueError(
            "Invalid system type '{}'. Use A, B, or C.".format(
                new_type
            )
        )

    ini_path = find_device_ini(runtime_path)

    with open(ini_path, "r") as file:
        content = file.read()

    pattern = r"(?m)^(\s*systemType\s*=\s*).*$"

    updated_content, count = re.subn(
        pattern,
        lambda match: match.group(1) + new_type,
        content
    )

    if count != 1:
        raise ValueError(
            "Expected exactly one systemType entry in '{}'; found {}."
            .format(ini_path, count)
        )

    with open(ini_path, "w") as file:
        file.write(updated_content)

    test.log(
        "Updated systemType to {} in {}".format(
            new_type, ini_path
        )
    )

    return ini_path


def configure_system_type(new_type, runtime_path):
    """
    Public helper called by Squish test cases.
    """

    test.log("Starting system type configuration")

    ini_path = update_system_type(new_type, runtime_path)

    test.log("System type configuration completed")
    return ini_path

  
def verify_economy_type():
    test.log("Checking System Type")
 
    clickButton(
        waitForObject(names.homeScreen_settingsButton_QPushButton)
    )
 
    clickTab(
        waitForObject(names.settingsScreen_tbSystemInfo_TabWidget),
        "LOGS"
    )
 
    clickButton(
        waitForObject(names.settingsScreen_pbService_QPushButton)
    )
 
    for _ in range(5):
        clickButton(
            waitForObject(names.numpad_pushButton_9_NumpadButton)
        )
    
    system_type_label = waitForObject(
        names.staticVersions_3_systemTypeVersion_QLabel
    )
 
    actual_type = str(system_type_label.text).strip()
 
    test.log("Actual System Type: {}".format(actual_type))
 
    if actual_type.replace(" ", "").lower() == "economyb":
        test.passes("System Type is Economy B")
        return True
 
    message = "Incorrect Economy: Expected Economy B, found {}".format(
        actual_type
    )
 
    test.fail(message)
 
    try:
        QMessageBox.warning(
            None,
            "Incorrect Economy",
            message
        )
    except Exception:
        test.log("Unable to show QMessageBox; see failure log above")
 
    return False

def verify_economyc_type():

    test.log("Checking System Type")

    clickButton(
        waitForObject(names.homeScreen_settingsButton_QPushButton)
    )

    clickTab(
        waitForObject(names.settingsScreen_tbSystemInfo_TabWidget),
        "LOGS"
    )

    clickButton(
        waitForObject(names.settingsScreen_pbService_QPushButton)
    )
    snooze(2)
    test.compare(str(waitForObjectExists(names.centralWidget_titleLabel_QLabel).text), "Version Not Supported")    
    clickButton(waitForObject(names.centralWidget_okButton_QPushButton))
    for _ in range(4):
        clickButton(
            waitForObject(names.numpad_pushButton_9_NumpadButton)
        )
    
    system_type_label = waitForObject(
        names.staticVersions_3_systemTypeVersion_QLabel
    )

    actual_type = str(system_type_label.text).strip()

    test.log("Actual System Type: {}".format(actual_type))

    if actual_type.replace(" ", "").lower() == "economyc":

        test.passes("System Type is Economy C")
        return True

    message = "Incorrect Economy: Expected Economy C, found {}".format(
        actual_type
    )

    test.fail(message)

    try:
        QMessageBox.warning(
            None,
            "Incorrect Economy",
            message
        )
    except Exception:
        test.log("Unable to show QMessageBox; see failure log above")

    return False
