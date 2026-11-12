
# -*- coding: utf-8 -*-

import names
import croatian_localization as loc
import openpyxl
import re
import os


TESTCASE_DIR = os.path.dirname(os.path.abspath(__file__))

EXCEL_PATH = loc.EXCEL_PATH

SHEET_NAME = "Treatment Logs"

VERIFIED_RESULTS = set()


def normalize(text):
    return loc.normalize(text)


def get_all_texts(obj):

    texts = []

    try:
        if not obj.visible:
            return texts
    except Exception:
        pass

    try:
        value = str(obj.text).strip()

        if value:
            value = re.sub(r"<[^>]+>", " ", value)
            value = " ".join(value.split())

            if value:
                texts.append(value)

    except Exception:
        pass

    try:
        value = str(obj.title).strip()

        if value:
            value = re.sub(r"<[^>]+>", " ", value)
            value = " ".join(value.split())

            if value:
                texts.append(value)

    except Exception:
        pass

    try:
        for child in object.children(obj):
            texts.extend(get_all_texts(child))
    except Exception:
        pass

    return texts


def load_croatian_strings():
    return loc.translated_rows()


def verify_screen(root_object, screen_name):
    return loc.verify_screen(root_object, screen_name, globals())


def main():

    # LOGIN

    sendEvent(
        "QMoveEvent",
        waitForObject(names.o_ScreenSwitcher),
        34,
        186,
        648,
        206
    )

    clickButton(
        waitForObject(names.numpad_pushButton_8_NumpadButton)
    )

    clickButton(
        waitForObject(names.numpad_pushButton_8_NumpadButton)
    )

    clickButton(
        waitForObject(names.numpad_pushButton_8_NumpadButton)
    )

    clickButton(
        waitForObject(names.numpad_pushButton_8_NumpadButton)
    )

    clickButton(
        waitForObject(names.mainFrame_okButton_QPushButton)
    )

    # OPEN SETTINGS

    clickButton(
        waitForObject(names.homeScreen_settingsButton_QPushButton)
    )

    # INFO TAB

    clickTab(
        waitForObject(names.settingsScreen_tbSystemInfo_TabWidget),
        "INFO"
    )

    # CHANGE LANGUAGE TO CROATIAN

    clickButton(
        waitForObject(
            names.gbSystemInformation_pbLanguageSettingsUpdate_QPushButton
        )
    )

    clickButton(
        waitForObject(names.languagesFrame_pbCroatia_QPushButton)
    )

    clickButton(
        waitForObject(names.buttonsFrame_acceptButton_QPushButton)
    )

    # OPEN LOGS

    clickTab(
        waitForObject(names.settingsScreen_tbSystemInfo_TabWidget),
        "ZAPISNICI"
    )

 

    # VERIFY LOGS SCREEN

    verify_screen(
        waitForObject(names.o_ScreenSwitcher),
        "Logs"
    )

    logs_view = waitForObject(names.systemEventErrorLogWidget_tableView_QTableView)
    loc.click_first_log_row(logs_view, globals())

    # VERIFY LOGS SCREEN AFTER ROW CLICK

    verify_screen(
        waitForObject(names.o_ScreenSwitcher),
        "Logs after row click"
    )
