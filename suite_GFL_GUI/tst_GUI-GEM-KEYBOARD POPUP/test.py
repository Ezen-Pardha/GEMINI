
# -*- coding: utf-8 -*-

from common import *
import names


def open_keyboard_popup():
    clickButton(waitForObject(names.centralWidget_pbName_QPushButton))
    snooze(1)

    test.verify(
        waitForObjectExists(
            names.keyboardPopup_wdEdit_WdLineEdit
        ).visible,
        "Keyboard popup is displayed"
    )


def click_keyboard_ok():
    mouseClick(
        waitForObject(names.keyboardPopup_lbText_QLabel),
        76, 32,
        Qt.NoModifier,
        Qt.LeftButton
    )
    snooze(1)


def click_keyboard_cancel():
    mouseClick(
        waitForObject(names.keyboardPopup_lbText_QLabel_2),
        76, 28,
        Qt.NoModifier,
        Qt.LeftButton
    )
    snooze(1)


def main():

    test.log("STEP 1: Enter login PIN")
    enter_login_pin()
    snooze(2)

    test.log("STEP 2: Open Expert screen")
    clickButton(
        waitForObject(names.gbExpert_expertButton_QPushButton)
    )
    snooze(2)

    test.verify(
        waitForObjectExists(
            names.pulseModeWidget_saveButton_QPushButton
        ).visible,
        "Expert screen is displayed"
    )

    test.log("STEP 3: Open Save Preset popup")
    clickButton(
        waitForObject(names.pulseModeWidget_saveButton_QPushButton)
    )
    snooze(1)

    test.log("STEP 4: Open keyboard popup")
    open_keyboard_popup()

    test.log("STEP 5: Verify keyboard OK and CANCEL labels")

    test.compare(
        str(waitForObjectExists(
            names.keyboardPopup_lbText_QLabel
        ).text),
        "OK",
        "Keyboard OK label is displayed"
    )

    test.compare(
        str(waitForObjectExists(
            names.keyboardPopup_lbText_QLabel_2
        ).text),
        "CANCEL",
        "Keyboard CANCEL label is displayed"
    )

    test.log("PASS: Keyboard OK and CANCEL labels verified")

    test.log("STEP 6: Verify keyboard text field")

    edit_field = waitForObjectExists(
        names.keyboardPopup_wdEdit_WdLineEdit
    )

    test.verify(
        edit_field.visible,
        "Keyboard text field is visible"
    )

    test.log("STEP 7: Verify CANCEL action")

    click_keyboard_cancel()

    test.verify(
        not object.exists(names.keyboardPopup_wdEdit_WdLineEdit),
        "Keyboard popup is closed after clicking CANCEL"
    )

    test.log("PASS: Keyboard CANCEL action verified")

    test.log("STEP 8: Reopen keyboard popup")

    open_keyboard_popup()

    test.log("STEP 9: Verify alphabet key")

    text_before_alpha = str(
        waitForObjectExists(
            names.keyboardPopup_wdEdit_WdLineEdit
        ).text
    )

    clickButton(
        waitForObject(names.keyboardPopup_a_KeyButton)
    )
    snooze(1)

    text_after_alpha = str(
        waitForObjectExists(
            names.keyboardPopup_wdEdit_WdLineEdit
        ).text
    )

    test.verify(
        text_after_alpha != text_before_alpha,
        "Alphabet key enters a character"
    )

    test.log("PASS: Alphabet key verified")

    test.log("STEP 10: Verify Caps Lock / uppercase keys")

    # Exact key objects from your recording
    clickButton(
        waitForObject(names.keyboardPopup_a_KeyButton_2)
    )
    snooze(1)

    clickButton(
        waitForObject(names.keyboardPopup_A_KeyButton_2)
    )
    snooze(1)

    test.log("Caps Lock / uppercase keys clicked")

    test.log("STEP 11: Verify numeric keyboard toggle")

    text_before_numeric = str(
        waitForObjectExists(
            names.keyboardPopup_wdEdit_WdLineEdit
        ).text
    )

    clickButton(
        waitForObject(names.keyboardPopup_123_KeyButton)
    )
    snooze(1)

    test.verify(
        waitForObjectExists(
            names.keyboardPopup_1_KeyButton
        ).visible,
        "Numeric keyboard is displayed after selecting 123"
    )

    test.log("PASS: Numeric keyboard toggle verified")

    test.log("STEP 12: Verify numeric key entry")

    clickButton(
        waitForObject(names.keyboardPopup_1_KeyButton)
    )
    snooze(1)

    text_after_numeric = str(
        waitForObjectExists(
            names.keyboardPopup_wdEdit_WdLineEdit
        ).text
    )

    test.verify(
        text_after_numeric != text_before_numeric,
        "Numeric key enters a character"
    )

    test.log("PASS: Numeric key entry verified")

    test.log("STEP 13: Verify alphabet keyboard toggle")

    clickButton(
        waitForObject(names.keyboardPopup_ABC_KeyButton)
    )
    snooze(1)

    test.verify(
        waitForObjectExists(
            names.keyboardPopup_a_KeyButton
        ).visible,
        "Alphabet keyboard is displayed after selecting ABC"
    )

    test.log("PASS: Alphabet keyboard toggle verified")

    test.log("STEP 14: Verify backspace")

    text_before_backspace = str(
        waitForObjectExists(
            names.keyboardPopup_wdEdit_WdLineEdit
        ).text
    )

    clickButton(
        waitForObject(names.keyboardPopup_KeyButton_2)
    )
    snooze(1)

    text_after_backspace = str(
        waitForObjectExists(
            names.keyboardPopup_wdEdit_WdLineEdit
        ).text
    )

    test.verify(
        len(text_after_backspace) < len(text_before_backspace),
        "Backspace removes a character"
    )

    test.log("PASS: Backspace verified")

    test.log("STEP 15: Verify keyboard OK label")

    test.compare(
        str(waitForObjectExists(
            names.keyboardPopup_lbText_QLabel
        ).text),
        "OK",
        "Keyboard OK label is displayed"
    )

    test.log("STEP 16: Click keyboard OK")

    click_keyboard_ok()

    test.verify(
        not object.exists(names.keyboardPopup_wdEdit_WdLineEdit),
        "Keyboard popup is closed after clicking OK"
    )

    test.log("PASS: Keyboard OK action verified")

    test.log("Keyboard popup test completed")
