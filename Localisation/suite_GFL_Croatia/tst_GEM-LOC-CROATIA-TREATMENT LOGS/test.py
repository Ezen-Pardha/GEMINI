# -*- coding: utf-8 -*-

import names
import croatian_localization as loc
import openpyxl
import re


EXCEL_PATH = loc.EXCEL_PATH


def normalize(text):
    return loc.normalize(text)


def get_all_texts(obj):

    texts = []

    try:
        if not obj.visible:
            return texts
    except:
        pass

    try:
        value = str(obj.text).strip()
        if value:
            value = re.sub(r"<[^>]+>", " ", value)
            value = " ".join(value.split())
            if value:
                texts.append(value)
    except:
        pass

    try:
        value = str(obj.title).strip()
        if value:
            value = re.sub(r"<[^>]+>", " ", value)
            value = " ".join(value.split())
            if value:
                texts.append(value)
    except:
        pass

    try:
        for child in object.children(obj):
            texts.extend(get_all_texts(child))
    except:
        pass

    return texts


def load_croatian_strings():
    return loc.translated_rows()


def verify_screen(root_object, screen_name):
    return loc.verify_screen(root_object, screen_name, globals())


def main():

    # LOGIN

    sendEvent("QMoveEvent", waitForObject(names.o_ScreenSwitcher), 16, 199, 599, 217)
    doubleClick(waitForObject(names.numpad_pushButton_8_NumpadButton), 85, 56, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton))

    # CHANGE LANGUAGE TO CROATIAN

    clickButton(waitForObject(names.homeScreen_settingsButton_QPushButton))
    clickTab(waitForObject(names.settingsScreen_tbSystemInfo_TabWidget), "INFO")
    clickButton(waitForObject(names.gbSystemInformation_pbLanguageSettingsUpdate_QPushButton))
    clickButton(waitForObject(names.languagesFrame_pbCroatia_QPushButton))
    clickButton(waitForObject(names.buttonsFrame_acceptButton_QPushButton))
    clickButton(waitForObject(names.settingsScreen_pbBack_QPushButton))
   

    # OPEN TREATMENT LOGS

    clickButton(waitForObject(names.homeScreen_logButton_QPushButton))

    test.vp("Verify Treatment Screen")



    # VERIFY TREATMENT LOGS

    logs_table = waitForObject(names.treatmentLogScreen_tvLogsTable_QTreeView)
    verify_screen(logs_table, "Treatment Logs")

    # CLICK TABLE

    mouseClick(waitForObject(names.treatmentLogScreen_tvLogsTable_QTreeView), 587, 68, Qt.NoModifier, Qt.LeftButton)

    # CLICK DATE HEADER

    mouseClick(waitForObject(names.treatmentLogScreen_tvLogsTable_QTreeView), 50, 25, Qt.NoModifier, Qt.LeftButton)
