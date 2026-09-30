# -*- coding: utf-8 -*-

import names
import openpyxl
import re


EXCEL_PATH = "/home/ntc/Test_Automation_Gemini/Localisation/suite_GFL_Czech/tst_Home Screen/testdata/Gemini Split strings.xlsx"


def normalize(text):
    text = str(text)
    text = re.sub(r"<br\s*/?>", " ", text, flags=re.IGNORECASE)
    text = re.sub(r"<[^>]+>", "", text)
    text = text.replace("\xa0", " ")
    text = " ".join(text.split())
    return text.strip().lower()


def is_ignored_text(text):

    text = normalize(text)

    if not text:
        return True

    if text == "aut":
        return True

    if re.match(r"^[\d\s.,:%/+\-]+$", text):
        return True

    if re.match(r"^[\d\s.,:%/+\-]+[a-zµ°]+$", text):
        return True

    if re.match(
        r"^[\d\s.,:%/+\-]+[a-zµ°]+\s*/\s*[\d\s.,:%/+\-]+[a-zµ°]+$",
        text
    ):
        return True

    return False


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

                value = re.sub(
                    r"<br\s*/?>",
                    " ",
                    value,
                    flags=re.IGNORECASE
                )

                value = re.sub(r"<[^>]+>", "", value)
                value = " ".join(value.split())

                if value and not is_ignored_text(value):
                    texts.append(value)

        except:
            pass

    try:

        for child in object.children(obj):
            texts.extend(get_all_texts(child))

    except:
        pass

    return texts


def get_all_text_combinations(obj):

    result = []

    lines = get_all_texts(obj)

    for start in range(len(lines)):

        combined = ""

        for end in range(start, len(lines)):

            if combined:
                combined += " " + lines[end]
            else:
                combined = lines[end]

            if not is_ignored_text(combined):
                result.append(combined)

    try:

        for child in object.children(obj):
            result.extend(get_all_text_combinations(child))

    except:
        pass

    return result


def get_screen_candidates(obj):

    candidates = set()

    texts = get_all_texts(obj)
    combinations = get_all_text_combinations(obj)

    for text in texts + combinations:

        key = normalize(text)

        if key and not is_ignored_text(key):
            candidates.add(key)

    return candidates


def main():

    # =========================================================
    # LOGIN
    # =========================================================

    sendEvent(
        "QMoveEvent",
        waitForObject(names.o_ScreenSwitcher),
        82,
        182,
        715,
        202
    )

    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton))

    # =========================================================
    # OPEN HOME SCREEN
    # =========================================================

    home = waitForObject(names.homeScreen_HomeScreen)

    mouseClick(
        home,
        643,
        86,
        Qt.NoModifier,
        Qt.LeftButton
    )

    mouseClick(
        waitForObject(names.homeScreen_gbExpert_QFrame),
        86,
        108,
        Qt.NoModifier,
        Qt.LeftButton
    )

    snooze(1)

    # =========================================================
    # READ EXCEL
    # =========================================================

    workbook = openpyxl.load_workbook(
        EXCEL_PATH,
        data_only=True
    )

    sheet = workbook["Home Screen"]

    # =========================================================
    # CREATE EXCEL MAPPING
    #
    # English = Column B
    # Danish  = Column F
    # =========================================================

    excel_rows = {}

    for row in sheet.iter_rows(
        min_row=2,
        values_only=True
    ):

        if len(row) < 6:
            continue

        english = row[1]
        danish = row[5]

        if english is None:
            continue

        english = str(english).strip()

        if not english:
            continue

        english_key = normalize(english)

        if english_key not in excel_rows:

            excel_rows[english_key] = {
                "english": english,
                "danish": None
            }

        if danish is not None:

            danish = str(danish).strip()

            if danish:
                excel_rows[english_key]["danish"] = danish

    # =========================================================
    # CHANGE LANGUAGE TO DANISH
    # =========================================================

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
            names.languagesFrame_pbDenmark_QPushButton
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

    # =========================================================
    # OPEN SAME HOME SCREEN STATE IN DANISH
    # =========================================================

    home = waitForObject(names.homeScreen_HomeScreen)

    mouseClick(
        home,
        643,
        86,
        Qt.NoModifier,
        Qt.LeftButton
    )

    mouseClick(
        waitForObject(names.homeScreen_gbExpert_QFrame),
        86,
        108,
        Qt.NoModifier,
        Qt.LeftButton
    )

    snooze(1)

    # =========================================================
    # CAPTURE DANISH HOME SCREEN
    # =========================================================

    danish_candidates = get_screen_candidates(home)

    # =========================================================
    # VALIDATE EXCEL DANISH STRINGS AGAINST SCREEN
    # =========================================================

    pass_count = 0
    fail_count = 0
    verified = set()

    for english_key, data in excel_rows.items():

        english = data["english"]
        danish = data["danish"]

        # -----------------------------------------------------
        # DANISH TRANSLATION MISSING IN EXCEL
        # -----------------------------------------------------

        if danish is None or not danish.strip():

            result_key = english_key + "|MISSING_EXCEL"

            if result_key not in verified:

                test.fail(
                    "FAIL: " +
                    english +
                    " -> Danish translation is missing in Excel"
                )

                verified.add(result_key)
                fail_count += 1

            continue

        # -----------------------------------------------------
        # CHECK DANISH STRING ON SCREEN
        # -----------------------------------------------------

        danish_key = normalize(danish)

        result_key = english_key + "|" + danish_key

        if result_key in verified:
            continue

        if danish_key in danish_candidates:

            test.passes(
                "PASS: " +
                english +
                " -> " +
                danish
            )

            verified.add(result_key)
            pass_count += 1

        else:

            test.fail(
                "FAIL: " +
                english +
                " -> " +
                danish +
                " | String is missing on screen"
            )

            verified.add(result_key)
            fail_count += 1

    # =========================================================
    # FINAL RESULT
    # =========================================================

    if fail_count > 0:

        test.fail(
            "DANISH HOME SCREEN LOCALIZATION VALIDATION FAILED"
        )

    elif pass_count > 0:

        test.passes(
            "DANISH HOME SCREEN LOCALIZATION VALIDATION PASSED"
        )

    else:

        test.fail(
            "NO EXCEL STRINGS FOUND FOR VALIDATION"
        )

    workbook.close()