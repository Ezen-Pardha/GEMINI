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

    if re.fullmatch(r"[\d\s.,:+\-/<>=%µμ]+", text):
        return True

    if re.fullmatch(r"[-_=.<>/%µμ:+]+", text):
        return True

    return False


def main():

    sendEvent(
        "QMoveEvent",
        waitForObject(names.o_ScreenSwitcher),
        82, 182, 715, 202
    )
    snooze(2)

    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton))

    home = waitForObject(names.homeScreen_HomeScreen)

    

    snooze(1)

    workbook = openpyxl.load_workbook(EXCEL_PATH, data_only=True)
    sheet = workbook["Home Screen"]

    excel_strings = {}

    for row in sheet.iter_rows(min_row=2, values_only=True):

        if len(row) < 2:
            continue

        english = row[1]

        if english is None:
            continue

        english = str(english).strip()

        if not english:
            continue

        key = normalize(english)

        if key and key not in excel_strings:
            excel_strings[key] = {
                "english": english
            }

    actual_texts = get_all_texts(home)

    screen_strings = {}

    for text in actual_texts:
        text = " ".join(str(text).split()).strip()

        if ignore_text(text):
            continue

        key = normalize(text)

        if key and key not in screen_strings:
            screen_strings[key] = text

    verified = set()
    pass_count = 0
    fail_count = 0

    for key in sorted(screen_strings):

        screen_text = screen_strings[key]

        if key in excel_strings:
            data = excel_strings[key]

            if key not in verified:
                test.passes(
                    "PASS: English string verified: "
                    + data["english"]
                )

                verified.add(key)
                pass_count += 1

        else:
            test.fail(
                "FAIL: Screen string not found in English Excel: "
                + screen_text
            )

            fail_count += 1

    if fail_count > 0:
        test.fail(
            "English HOME SCREEN VALIDATION FAILED: "
            + str(fail_count)
            + " screen string(s) missing from Excel"
        )

    elif pass_count > 0:
        test.passes(
            "English HOME SCREEN VALIDATION PASSED: "
            + str(pass_count)
            + " unique screen string(s) verified"
        )

    else:
        test.fail("NO VALID STRINGS FOUND ON SCREEN")

    workbook.close()


main()