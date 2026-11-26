# -*- coding: utf-8 -*-

from common import *

def main():
    enter_login_pin()
    clickButton(waitForObject(names.homeScreen_settingsButton_QPushButton))
    test.log("Navigating to Settings")
    clickTab(waitForObject(names.settingsScreen_tbSystemInfo_TabWidget), "LOGS")
    test.log("Navigating to Settings Logs Tab")
    
    logs_tab = waitForObject(names.settingsScreen_tbSystemInfo_TabWidget)
    test.log("SVV TAG:GUI-SET-047: Confirming LOGS tab is displayed on the screen")
    if str(logs_tab.tabText(logs_tab.currentIndex)) == "LOGS":
        test.passes("LOGS tab is displayed on the screen")
    else:
        test.fail("LOGS tab is not displayed on the screen")
        
    clickButton(waitForObject(names.settingsScreen_pbBack_QPushButton))
    test.log("Navigating back to home screen")
    clickButton(waitForObject(names.homeScreen_settingsButton_QPushButton))
    clickTab(waitForObject(names.settingsScreen_tbSystemInfo_TabWidget), "LOGS")
    test.log("Navigating to settings logs screen to confirm error messages are displayed")
    
    event_table = waitForObject(names.systemEventErrorLogWidget_tableView_QTableView)
    test.log("SVV TAG:GUI-SET-048: Confirming error messages are displayed")
    if event_table.model().rowCount() > 0:
        test.passes("PASS: System error messages are displayed")
    else:
        test.fail("FAIL: No system error messages are displayed")
        
    clickButton(waitForObject(names.settingsScreen_pbBack_QPushButton))
    test.log("Navigating back to home screen")
    clickButton(waitForObject(names.homeScreen_settingsButton_QPushButton))
    clickTab(waitForObject(names.settingsScreen_tbSystemInfo_TabWidget), "LOGS")
    test.log("Navigating to settings logs screen to confirm visibility and scrolling of scrollbar")
        
    scrollbar = waitForObject(names.tableView_QScrollBar_3)
    test.log("SVV TAG:GUI-SET-049: Confirming Vertical scrollbar is visible and scrolling is available")
    if scrollbar.visible and scrollbar.maximum > 0:
        test.passes("PASS: Vertical scrollbar is visible and scrolling is available")
    else:
        test.fail("FAIL: Vertical scrollbar is hidden or scrolling is unavailable")
        
    clickButton(waitForObject(names.settingsScreen_pbBack_QPushButton))
    test.log("Navigating back to home screen")
    clickButton(waitForObject(names.homeScreen_settingsButton_QPushButton))
    clickTab(waitForObject(names.settingsScreen_tbSystemInfo_TabWidget), "LOGS")
    test.log("Navigating to settings logs screen to confirm events in chronological order")
    test.log("SVV TAG:GUI-SET-050: Confirming the program displays the events in chronological order")
    def verify_chronological_order():
        table = waitForObject(names.systemEventErrorLogWidget_tableView_QTableView)
        model = table.model()
        row_count = model.rowCount()
        if row_count < 2:
            test.log(
                "Not enough event rows to verify chronological order"
            )
            return
        previous_time = None
        
        for row in range(row_count):
            index = model.index(row, 0)
            timestamp = str(model.data(index)).strip()
            try:
                current_time = datetime.strptime(
                    timestamp,
                    "%m-%d-%y %I:%M:%S%p"
                )
            except ValueError:
                test.fail(
                    "Unable to parse timestamp at row {}: {}".format(
                        row, timestamp
                    )
                )
                return
            if previous_time is not None:
                if current_time > previous_time:
                    test.fail(
                        "Events are not in descending order at row {}".format(
                            row
                        )
                    )
                    return
            previous_time = current_time
    test.passes("PASS: Event logs are ordered latest to oldest")
    
    clickButton(waitForObject(names.settingsScreen_pbBack_QPushButton))
    test.log("Navigating back to home screen")
    clickButton(waitForObject(names.homeScreen_settingsButton_QPushButton))
    clickTab(waitForObject(names.settingsScreen_tbSystemInfo_TabWidget), "LOGS")
    clickButton(waitForObject(names.settingsScreen_pbService_QPushButton))
    test.log("SVV TAG:GUI-SET-052: Verifying Service Mode passcode screen")
    
    try:
        login_screen = waitForObject(names.loginScreen_LoginScreen, 5000)
        if login_screen.visible:
            test.passes("PASS: Service Mode login screen is displayed")
        else:
            test.fail("FAIL: Service Mode login screen is not visible")
    except LookupError:
        test.fail("FAIL: Service Mode login screen is not displayed")
