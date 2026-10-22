
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
    if text is None:
        return ""

    text = str(text)
    text = re.sub(r"<br\s*/?>", " ", text, flags=re.IGNORECASE)
    text = re.sub(r"<[^>]+>", " ", text)
    text = text.replace("\xa0", " ")
    text = " ".join(text.split())
    text = re.sub(r"\s*<\s*", "<", text)
    text = re.sub(r"\s*>\s*", ">", text)

    return text.strip().casefold()


def get_object_text(obj):
    try:
        if not obj.visible:
            return ""
    except Exception:
        pass

    try:
        text = str(obj.text).strip()

        if text:
            text = re.sub(
                r"<br\s*/?>", " ", text, flags=re.IGNORECASE
            )
            text = re.sub(r"<[^>]+>", " ", text)
            return " ".join(text.split()).strip()
    except Exception:
        pass

    return ""


def get_screen_candidates(obj):
    candidates = []

    own_text = get_object_text(obj)

    if own_text:
        candidates.append(own_text)

    try:
        children = object.children(obj)
    except Exception:
        children = []

    child_texts = []

    for child in children:
        child_text = get_object_text(child)

        if child_text:
            child_texts.append(child_text)
            candidates.append(child_text)

    # Combine adjacent child texts to support split labels.
    for start in range(len(child_texts)):
        combined = ""

        for end in range(start, len(child_texts)):
            if combined:
                combined += " " + child_texts[end]
            else:
                combined = child_texts[end]

            candidates.append(combined)

    for child in children:
        candidates.extend(get_screen_candidates(child))

    return candidates


def main():

    # LOGIN

    sendEvent(
        "QMoveEvent",
        waitForObject(names.o_ScreenSwitcher),
        28, 208, 534, 218
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

    # CHANGE LANGUAGE TO Hungary

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
        waitForObject(names.languagesFrame_pbHungary_QPushButton)
    )

    clickButton(
        waitForObject(names.buttonsFrame_acceptButton_QPushButton)
    )

    clickButton(
        waitForObject(names.settingsScreen_pbBack_QPushButton)
    )

    # OPEN SOFT TISSUE QUICK START

    clickButton(
        waitForObject(names.homeScreen_pbSoftTissueQuickStart_QToolButton)
    )

    mouseClick(
        waitForObjectItem(
            names.tabLeftMainPresets_leftPresetsView_PresetListView,
            "_1", 44166
        ),
        467, 28, Qt.NoModifier, Qt.LeftButton
    )

    mouseClick(
        waitForObjectItem(
            names.tabRightMainPresets_rightPresetsView_PresetListView,
            "_1"
        ),
        121, 80, Qt.NoModifier, Qt.LeftButton
    )

    clickButton(
        waitForObject(names.quickStartScreen_pbContinue_QPushButton)
    )

    mouseClick(
        waitForObject(names.recommendedFiberWarningDialog_mainFrame_QFrame),
        539, 43, Qt.NoModifier, Qt.LeftButton
    )

    clickButton(
        waitForObject(names.mainFrame_okButton_QPushButton_2)
    )

    mouseClick(
        waitForObject(names.leftPedalWidget_wdPresetTabs_TabWidget),
        497, 44, Qt.NoModifier, Qt.LeftButton
    )

    mouseClick(
        waitForObject(names.rightPedalWidget_wdPresetTabs_TabWidget),
        98, 44, Qt.NoModifier, Qt.LeftButton
    )

    mouseClick(
        waitForObject(names.treatmentScreen_bottomBar_QFrame),
        890, 65, Qt.NoModifier, Qt.LeftButton
    )

    snooze(1)

    # LOAD EXCEL

    try:
        workbook = openpyxl.load_workbook(
            EXCEL_PATH,
            data_only=True,
            read_only=True
        )

        if "Treatment Modes" not in workbook.sheetnames:
            test.fail(
                "FAIL: Treatment Modes worksheet not found in Excel"
            )
            workbook.close()
            return

        sheet = workbook["Treatment Modes"]

    except Exception as error:
        test.fail("FAIL: Unable to load Excel: " + str(error))
        return

    # LOAD Hungary STRINGS FROM EXCEL
    # Column B = English
    # Column E = Hungary

    excel_strings = {}

    for row in sheet.iter_rows(min_row=2, values_only=True):

        if len(row) < 5:
            continue

        english = row[1]
        Hungary = row[12]

        if english is None or Hungary is None:
            continue

        english = str(english).strip()
        Hungary = str(Hungary).strip()

        normalized_Hungary = normalize(Hungary)

        if english and normalized_Hungary:
            excel_strings.setdefault(
                normalized_Hungary,
                {
                    "english": english,
                    "Hungary": Hungary
                }
            )

    workbook.close()

    # GET CURRENT TREATMENT SCREEN

    try:
        screen = waitForObject(
            names.treatmentScreen_bottomBar_QFrame
        )

        candidates = get_screen_candidates(screen)

        try:
            parent = object.parent(screen)
            candidates.extend(get_screen_candidates(parent))
        except Exception:
            pass

    except Exception as error:
        test.fail(
            "FAIL: Unable to collect Treatment screen strings: "
            + str(error)
        )
        return

    # INCLUDE RECORDED SCREEN OBJECTS

    recorded_objects = [
        names.leftPedalWidget_wdPresetTabs_TabWidget,
        names.rightPedalWidget_wdPresetTabs_TabWidget,
        names.treatmentScreen_bottomBar_QFrame
    ]

    for object_name in recorded_objects:
        try:
            obj = waitForObject(object_name)
            candidates.extend(get_screen_candidates(obj))
        except Exception:
            pass

    # NORMALIZE AND REMOVE DUPLICATES

    unique_candidates = {}

    for candidate in candidates:
        candidate = str(candidate).strip()
        normalized = normalize(candidate)

        if normalized:
            unique_candidates.setdefault(normalized, candidate)

    # MATCH SCREEN STRINGS AGAINST EXCEL

    matches = {}
    missing_strings = set()

    for normalized_candidate, original_candidate in (
        unique_candidates.items()
    ):

        # Ignore strings containing only numbers or symbols.

        if not re.search(r"[^\W\d_]", original_candidate, re.UNICODE):
            continue

        if normalized_candidate in excel_strings:

            data = excel_strings[normalized_candidate]

            matches[normalized_candidate] = data

        else:
            # Screen string is visible but absent from Hungary Excel.
            missing_strings.add(original_candidate)

    # REPORT MATCHED STRINGS

    pass_count = 0
    fail_count = 0

    for key in sorted(matches):

        data = matches[key]

        test.passes(
            "PASS: "
            + data["english"]
            + " -> "
            + data["Hungary"]
        )

        pass_count += 1

    # REPORT STRINGS MISSING FROM EXCEL

    for missing in sorted(missing_strings, key=str.casefold):

        test.fail(
            "FAIL: Visible screen string missing from Hungary Excel: "
            + missing
        )

        fail_count += 1

    # FINAL RESULT

    if pass_count > 0 and fail_count == 0:

        test.passes(
            "Hungary SOFT TISSUE QUICK START LOCALIZATION VALIDATION PASSED"
            + " | Matched: " + str(pass_count)
            + " | Missing from Excel: 0"
        )

    else:

        test.fail(
            "Hungary SOFT TISSUE QUICK START LOCALIZATION VALIDATION FAILED"
            + " | Matched: " + str(pass_count)
            + " | Missing from Excel: " + str(fail_count)
        )
