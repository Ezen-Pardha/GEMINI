# -*- coding: utf-8 -*-

import names
import openpyxl
import re
import os

TESTCASE_DIR = os.path.dirname(os.path.abspath(__file__))

EXCEL_PATH = os.path.abspath(
    os.path.join(
        TESTCASE_DIR,
        "..",
        "shared",
        "testdata",
        "Gemini Split strings.xlsx"
    )
)




def normalize(text):
    text = str(text)
    text = re.sub(r"<br\s*/?>", " ", text, flags=re.IGNORECASE)
    text = re.sub(r"<[^>]+>", "", text)
    text = text.replace("\xa0", " ")
    text = " ".join(text.split())
    return text.strip().casefold()


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

            if value and value.lower() not in ("none", "null"):
                texts.append(value)
        except:
            pass

    try:
        for child in object.children(obj):
            texts.extend(get_all_texts(child))
    except:
        pass

    return texts


def ignore_text(text):
    text = normalize(text)

    if not text:
        return True

    # Ignore numeric-only values and standalone measurements
    if re.fullmatch(r"[\d\s.,:+\-/<>=%µμ]+", text):
        return True

    # Ignore symbol-only strings
    if re.fullmatch(r"[-_=.<>/%µμ:+]+", text):
        return True

    return False


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

    # CHANGE LANGUAGE TO Italy
    clickButton(waitForObject(names.homeScreen_settingsButton_QPushButton))
    clickTab(waitForObject(names.settingsScreen_tbSystemInfo_TabWidget), "INFO")
    clickButton(waitForObject(names.gbSystemInformation_pbLanguageSettingsUpdate_QPushButton))

    clickButton(waitForObject(names.languagesFrame_pbItaly_QPushButton))

    clickButton(waitForObject(names.buttonsFrame_acceptButton_QPushButton))
    clickButton(waitForObject(names.settingsScreen_pbBack_QPushButton))

    # HOME SCREEN
    home = waitForObject(names.homeScreen_HomeScreen)

    test.vp("Verified Home Screen")

    mouseClick(home, 643, 86, Qt.NoModifier, Qt.LeftButton)

    mouseClick(
        waitForObject(names.homeScreen_gbExpert_QFrame),
        86, 108,
        Qt.NoModifier,
        Qt.LeftButton
    )

    snooze(1)

    # LOAD HOME SCREEN EXCEL SHEET
    workbook = openpyxl.load_workbook(EXCEL_PATH, data_only=True)
    sheet = workbook["Home Screen"]

    # LOAD Italy STRINGS FROM EXCEL
    excel_strings = {}

    for row in sheet.iter_rows(min_row=2, values_only=True):

        if len(row) < 5:
            continue

        english = row[1]
        Italy = row[13]

        if english is None or Italy is None:
            continue

        english = str(english).strip()
        Italy = str(Italy).strip()

        if not english or not Italy:
            continue

        key = normalize(Italy)

        if key and key not in excel_strings:
            excel_strings[key] = {
                "english": english,
                "Italy": Italy
            }

    # GET STRINGS PRESENT ON SCREEN
    actual_texts = get_all_texts(home)

    # DEDUPLICATE SCREEN STRINGS
    screen_strings = {}

    for text in actual_texts:
        text = " ".join(str(text).split()).strip()

        if ignore_text(text):
            continue

        key = normalize(text)

        if key and key not in screen_strings:
            screen_strings[key] = text

    # VERIFY SCREEN STRINGS AGAINST EXCEL
    verified = set()
    pass_count = 0
    fail_count = 0

    for key in sorted(screen_strings):

        screen_text = screen_strings[key]

        if key in excel_strings:
            data = excel_strings[key]

            if key not in verified:
                test.passes(
                    "PASS: "
                    + data["english"]
                    + " -> "
                    + data["Italy"]
                )

                verified.add(key)
                pass_count += 1

        else:
            test.fail(
                "FAIL: Screen string not found in Italy Excel: "
                + screen_text
            )

            fail_count += 1

    # FINAL RESULT
    if fail_count > 0:
        test.fail(
            "Italy HOME SCREEN VALIDATION FAILED: "
            + str(fail_count)
            + " screen string(s) missing from Excel"
        )

    elif pass_count > 0:
        test.passes(
            "Italy HOME SCREEN VALIDATION PASSED: "
            + str(pass_count)
            + " unique screen string(s) verified"
        )

    else:
        test.fail("NO VALID STRINGS FOUND ON SCREEN")

    workbook.close()
