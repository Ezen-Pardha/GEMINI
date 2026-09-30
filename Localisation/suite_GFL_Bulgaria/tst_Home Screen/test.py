# -*- coding: utf-8 -*-

import names
import openpyxl


EXCEL_PATH = "/home/ntc/Test_Automation_Gemini/Localisation/suite_GFL_Czech/tst_Home Screen/testdata/Gemini Split strings.xlsx"


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

    # LOGIN

    sendEvent(
        "QMoveEvent",
        waitForObject(names.o_ScreenSwitcher),
        82, 182, 715, 202
    )

    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))

    clickButton(waitForObject(names.mainFrame_okButton_QPushButton))


    # CHANGE LANGUAGE TO BULGARIAN

    clickButton(waitForObject(names.homeScreen_settingsButton_QPushButton))

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
        waitForObject(
            names.languagesFrame_pbBulgaria_QPushButton
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


    # HOME SCREEN

    mouseClick(
        waitForObject(names.homeScreen_HomeScreen),
        66, 62,
        Qt.NoModifier,
        Qt.LeftButton
    )

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
        waitForObject(names.homeScreen_gbExpert_QFrame),
        86, 108,
        Qt.NoModifier,
        Qt.LeftButton
    )


    # READ EXCEL

    workbook = openpyxl.load_workbook(
        EXCEL_PATH,
        data_only=True
    )

    sheet = workbook["Home Screen"]


    # GET VISIBLE HOME SCREEN TEXT

    actual_texts = get_all_texts(home)

    actual_texts = set(
        text.strip()
        for text in actual_texts
        if text and text.strip()
    )


    # VERIFY ENGLISH -> BULGARIAN

    verified = set()

    pass_count = 0

    for row in sheet.iter_rows(
        min_row=2,
        values_only=True
    ):

        if len(row) < 3:
            continue

        english = row[1]
        bulgarian = row[2]

        if english is None or bulgarian is None:
            continue

        english = str(english).strip()
        bulgarian = str(bulgarian).strip()

        if not english or not bulgarian:
            continue

        if bulgarian in actual_texts:

            if bulgarian not in verified:

                verified.add(bulgarian)

                test.passes(
                    "PASS: " +
                    english +
                    " -> " +
                    bulgarian
                )

                pass_count += 1


    # FINAL RESULT

    if pass_count > 0:

        test.passes(
            "BULGARIAN HOME SCREEN LOCALIZATION VALIDATION PASSED"
        )

    else:

        test.fail(
            "NO BULGARIAN STRINGS FOUND ON HOME SCREEN"
        )

    workbook.close()