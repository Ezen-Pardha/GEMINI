# -*- coding: utf-8 -*-

from common import *

def main():
    enter_login_pin()
    clickButton(waitForObject(names.homeScreen_settingsButton_QPushButton))
    clickTab(waitForObject(names.settingsScreen_tbSystemInfo_TabWidget), "LOGS")
    test.log("Navigating to Logs tab")
    clickButton(waitForObject(names.settingsScreen_pbService_QPushButton))
    test.log("Navigating to Service Mode")
    for index in range(5):
        click_and_report(
            names.numpad_pushButton_9_NumpadButton,
            "Enter service PIN digit 9, press {} of 4".format(index + 1)
        )
    service_screen = waitForObject(
    names.serviceScreen_ServiceScreen
    )
    if service_screen.visible:
        test.passes("PASS: Service Mode is visible")
    else:
        test.fail("FAIL: Service Mode is not visible")

    clickTab(waitForObject(names.serviceScreenTabWidget_QTabWidget), "SYSTEM EVENT LOG")
    test.log("Navigating to System Event Log Tab")
    test.log("SVV TAG:GUI-SRV-026: Verifying System Event Log tab widget")
    try:
        event_log_tab = waitForObject(
            names.serviceScreenTabWidget_QTabWidget
        )

        if event_log_tab.isActiveWindow:
            test.passes(
                "PASS: System Event Log tab widget is active"
            )
        else:
            test.fail(
                "FAIL: System Event Log tab widget is not active"
            )

    except Exception as error:
        test.fail(
            "FAIL: Unable to verify System Event Log tab widget: "
            + str(error)
        )
        
    test.log("SVV TAG:GUI-SRV-027: Verifying System Event Log in table format")
    event_log_table = waitForObject({
        "name": "tableView",
        "type": "QTableView",
        "visible": True
    })
    if event_log_table.visible:
        test.passes("PASS: System Event Log table is visible")
    else:
        test.fail("FAIL: System Event Log table is not visible")
    
    test.log("SVV TAG:GUI-SRV-028: Verifying System Event Log horizantal and vertical scroll bars")
    vertical_scrollbar = waitForObject(names.tableView_QScrollBar_2)
    horizontal_scrollbar = waitForObject(names.tableView_QScrollBar)
    if vertical_scrollbar.visible and horizontal_scrollbar.visible:
        test.passes(
            "PASS: System Event Log provides horizontal and vertical scroll bars"
        )
    else:
        test.fail(
            "FAIL: One or both System Event Log scroll bars are not visible"
        )

    test.log("SVV TAG:GUI-SRV-029: Verifying Export Logs button is displayed")
    try:
        export_logs_button = waitForObject({
            "text": "Export Logs",
            "type": "QPushButton"
        })
        if export_logs_button.visible:
            test.passes("PASS: Export Logs button is displayed")
        else:
            test.fail("FAIL: Export Logs button is not displayed")

    except LookupError:
        test.fail("FAIL: Export Logs button is not provided")
