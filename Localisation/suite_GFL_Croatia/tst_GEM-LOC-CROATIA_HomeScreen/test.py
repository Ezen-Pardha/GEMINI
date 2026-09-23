
# -*- coding: utf-8 -*-

import names
import openpyxl


def get_all_texts(obj):

    texts = []

    try:
        text = str(obj.text).strip()

        if text:
            texts.append(text)

    except:
        pass

    try:
        children = object.children(obj)

        for child in children:
            texts.extend(get_all_texts(child))

    except:
        pass

    return texts


def main():

    # Login
    doubleClick(
        waitForObject(names.numpad_pushButton_8_NumpadButton),
        68, 52,
        Qt.NoModifier,
        Qt.LeftButton
    )

    doubleClick(
        waitForObject(names.numpad_pushButton_8_NumpadButton),
        116, 46,
        Qt.NoModifier,
        Qt.LeftButton
    )

    clickButton(
        waitForObject(names.mainFrame_okButton_QPushButton)
    )


    # Change language to Croatian
    clickButton(
        waitForObject(names.homeScreen_settingsButton_QPushButton)
    )

    clickTab(
        waitForObject(names.settingsScreen_tbSystemInfo_TabWidget),
        "INFO"
    )

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

    clickButton(
        waitForObject(names.settingsScreen_pbBack_QPushButton)
    )

    test.vp("Verify Home Screen1")

    
   


    # Home screen
    mouseClick(
        waitForObject(names.homeScreen_HomeScreen),
        637, 179,
        Qt.NoModifier,
        Qt.LeftButton
    )

    mouseClick(
        waitForObject(names.homeScreen_gbExpert_QFrame),
        169, 60,
        Qt.NoModifier,
        Qt.LeftButton
    )

    mouseClick(
        waitForObject(names.topBar_buttonsBar_ButtonsBar),
        371, 25,
        Qt.NoModifier,
        Qt.LeftButton
    )


    # Read Excel
    excelpath = "/home/ntc/Test_Automation_Gemini/Localisation/suite_GFL_Croatia/tst_GEM-LOC-CROATIA_HomeScreen/testdata/coration home screen.xlsx"
    workbook = openpyxl.load_workbook(excelpath)
    sheet = workbook.active


    # Get all text from Home Screen
    home = waitForObject(names.homeScreen_HomeScreen)

    actual_texts = get_all_texts(home)


    # Verify English -> Croatian
    for row in sheet.iter_rows(min_row=2, values_only=True):

        if row[0] is None or row[1] is None:
            continue

        english = str(row[0]).strip()
        croatian = str(row[1]).strip()

        if croatian in actual_texts:

            test.passes(
                "PASS: " +
                english +
                " -> " +
                croatian
            )

        else:

            test.fail(
                "FAIL: " +
                english +
                " -> " +
                croatian
            )

