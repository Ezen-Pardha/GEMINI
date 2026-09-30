# -*- coding: utf-8 -*-

import names
import openpyxl


EXCEL_PATH = "/home/ntc/Test_Automation_Gemini/Localisation/suite_GFL_Czech/tst_Home Screen/testdata/Gemini Split strings.xlsx"

verified = set()


def get_all_texts(obj):

    texts = []

    try:
        if not obj.visible:
            return texts
    except:
        pass

    for attr in ("text", "title"):

        try:
            value = str(getattr(obj, attr)).strip()

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


def main():

    # Login
    sendEvent(
        "QMoveEvent",
        waitForObject(names.o_ScreenSwitcher),
        82, 182, 715, 202
    )

    clickButton(
        waitForObject(
            names.numpad_pushButton_8_NumpadButton
        )
    )

    clickButton(
        waitForObject(
            names.numpad_pushButton_8_NumpadButton
        )
    )

    clickButton(
        waitForObject(
            names.numpad_pushButton_8_NumpadButton
        )
    )

    clickButton(
        waitForObject(
            names.numpad_pushButton_8_NumpadButton
        )
    )

    clickButton(
        waitForObject(
            names.mainFrame_okButton_QPushButton
        )
    )


    # Change language to Czech
    clickButton(
        waitForObject(
            names.homeScreen_settingsButton_QPushButton
        )
    )

    clickTab(
        waitForObject(
            names.settingsScreen_tbSystemInfo_TabWidget
        ),
        "INFO"
    )

    clickButton(
        waitForObject(
            names.gbSystemInformation_pbLanguageSettingsUpdate_QPushButton
        )
    )

    clickButton(
        waitForObject(
            names.languagesFrame_pbCzech_QPushButton
        )
    )

    clickButton(
        waitForObject(
            names.buttonsFrame_acceptButton_QPushButton
        )
    )

    clickButton(
        waitForObject(
            names.settingsScreen_pbBack_QPushButton
        )
    )


    # Home Screen
    home = waitForObject(
        names.homeScreen_HomeScreen
    )

    mouseClick(
        home,
        643, 86,
        Qt.NoModifier,
        Qt.LeftButton
    )

    mouseClick(
        waitForObject(
            names.homeScreen_gbExpert_QFrame
        ),
        86, 108,
        Qt.NoModifier,
        Qt.LeftButton
    )


    # Read ONLY Home Screen sheet
    workbook = openpyxl.load_workbook(
        EXCEL_PATH,
        data_only=True
    )

    sheet = workbook["Home Screen"]


    # Get all visible Home Screen strings
    actual_texts = get_all_texts(home)


    # Remove duplicates
    actual_texts = set(
        text.strip()
        for text in actual_texts
        if text and text.strip()
    )


    # Verify English -> Czech
    for row in sheet.iter_rows(
        min_row=2,
        values_only=True
    ):

        english = row[1]
        czech = row[4]

        if english is None or czech is None:
            continue

        english = str(english).strip()
        czech = str(czech).strip()

        if not english or not czech:
            continue

        if czech in actual_texts:

            if czech not in verified:

                verified.add(czech)

                test.passes(
                    "PASS: " +
                    english +
                    " -> " +
                    czech
                )

        else:

            test.fail(
                "FAIL: " +
                english +
                " -> " +
                czech
            )

    workbook.close()