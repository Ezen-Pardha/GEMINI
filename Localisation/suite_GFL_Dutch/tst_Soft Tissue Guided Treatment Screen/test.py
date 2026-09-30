# -*- coding: utf-8 -*-

import names
import openpyxl
import re


def normalize(text):
    text = str(text)
    text = re.sub(r"<br\s*/?>", " ", text, flags=re.IGNORECASE)
    text = re.sub(r"<[^>]+>", "", text)
    text = " ".join(text.split())
    text = re.sub(r"\s*<\s*", "<", text)
    text = re.sub(r"\s*>\s*", ">", text)
    return text.strip().lower()


def is_ignored(text):
    text = normalize(text)

    if not text or text == "aut":
        return True

    if re.match(r"^[\d\s.,:+\-/]+$", text):
        return True

    if re.match(r"^[\d\s.,:+\-/]+(w|j|hz|µm|mm|cm|s|min|%)$", text):
        return True

    return False


def get_object_text(obj):

    try:
        text = str(obj.text).strip()

        if text:
            text = re.sub(
                r"<br\s*/?>",
                " ",
                text,
                flags=re.IGNORECASE
            )
            text = re.sub(r"<[^>]+>", " ", text)
            text = " ".join(text.split())
            return text.strip()

    except:
        pass

    return ""


def get_screen_candidates(obj):

    candidates = []

    own_text = get_object_text(obj)

    if own_text and not is_ignored(own_text):
        candidates.append(own_text)

    try:
        children = object.children(obj)
    except:
        children = []

    child_texts = []

    for child in children:

        child_text = get_object_text(child)

        if child_text and not is_ignored(child_text):
            child_texts.append(child_text)
            candidates.append(child_text)

    # Create combinations only for matching against Excel.
    # They are NOT reported individually.
    for start in range(len(child_texts)):

        combined = ""

        for end in range(start, len(child_texts)):

            combined = (
                combined + " " + child_texts[end]
                if combined
                else child_texts[end]
            )

            if not is_ignored(combined):
                candidates.append(combined)

    for child in children:
        candidates.extend(get_screen_candidates(child))

    return candidates


def main():

    # LOGIN

    sendEvent(
        "QMoveEvent",
        waitForObject(names.o_ScreenSwitcher),
        34,
        185,
        582,
        201
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

    # CHANGE LANGUAGE TO DUTCH

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
            names.languagesFrame_pbDutch_QPushButton
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

    snooze(1)

    # OPEN SOFT TISSUE ASSISTANT

    clickButton(
        waitForObject(
            names.homeScreen_pbSoftTissueAssistant_QToolButton
        )
    )

    clickButton(
        waitForObject(
            names.gbSoftTissueProcedures_pbIncision_QPushButton
        )
    )

    clickButton(
        waitForObject(
            names.softTissueAssistantModeScreen_pbContinue_QPushButton
        )
    )

    # OPEN TREATMENT SCREEN

    mouseClick(
        waitForObject(
            names.leftPedalWidget_wdPresetTabs_TabWidget
        ),
        377,
        32,
        Qt.NoModifier,
        Qt.LeftButton
    )

    mouseClick(
        waitForObject(
            names.rightPedalWidget_wdPresetTabs_TabWidget
        ),
        267,
        35,
        Qt.NoModifier,
        Qt.LeftButton
    )

    mouseClick(
        waitForObject(
            names.valueFrame_valueLabel_QLabel
        ),
        172,
        1,
        Qt.NoModifier,
        Qt.LeftButton
    )

    mouseClick(
        waitForObject(
            names.treatmentScreen_bottomBar_QFrame
        ),
        894,
        47,
        Qt.NoModifier,
        Qt.LeftButton
    )

    snooze(1)

    # READ EXCEL

    excelpath = (
        "/home/ntc/Test_Automation_Gemini/Localisation/"
        "suite_GFL_Czech/tst_Home Screen/testdata/"
        "Gemini Split strings.xlsx"
    )

    workbook = openpyxl.load_workbook(
        excelpath,
        data_only=True
    )

    sheet = workbook["Treatment Modes"]

    # DUTCH = COLUMN G

    excel_strings = {}

    for row in sheet.iter_rows(
        min_row=2,
        values_only=True
    ):

        if len(row) < 7:
            continue

        trace_id = row[0]
        english = row[1]
        dutch = row[6]

        if english is None or dutch is None:
            continue

        english = str(english).strip()
        dutch = str(dutch).strip()

        if not english or not dutch:
            continue

        key = normalize(dutch)

        if key:
            excel_strings[key] = {
                "english": english,
                "dutch": dutch,
                "trace_id": (
                    ""
                    if trace_id is None
                    else str(trace_id).strip()
                )
            }

    # GET CURRENT TREATMENT SCREEN

    screen = waitForObject(
        names.treatmentScreen_bottomBar_QFrame
    )

    screen_candidates = get_screen_candidates(screen)

    # CHECK PARENT ALSO

    try:
        parent = object.parent(screen)
        screen_candidates.extend(
            get_screen_candidates(parent)
        )
    except:
        pass

    # REMOVE DUPLICATE SCREEN TEXTS

    unique_candidates = []
    seen = set()

    for candidate in screen_candidates:

        key = normalize(candidate)

        if not key:
            continue

        if key in seen:
            continue

        seen.add(key)
        unique_candidates.append(candidate)

    # SCREEN -> EXCEL MATCH

    matches = {}

    for candidate in unique_candidates:

        normalized_candidate = normalize(candidate)

        if normalized_candidate in excel_strings:

            data = excel_strings[normalized_candidate]

            matches[normalized_candidate] = (
                len(normalized_candidate),
                data["english"],
                data["dutch"]
            )

    # REMOVE SHORTER PARTIAL MATCHES

    final_matches = {}

    sorted_matches = sorted(
        matches.items(),
        key=lambda x: len(x[0]),
        reverse=True
    )

    for key, data in sorted_matches:

        partial_match = False

        for existing_key in final_matches:

            if key != existing_key and key in existing_key:
                partial_match = True
                break

        if not partial_match:
            final_matches[key] = data

    # RESULTS

    pass_count = 0

    for key in sorted(
        final_matches,
        key=lambda x: final_matches[x][0],
        reverse=True
    ):

        data = final_matches[key]

        test.passes(
            data[1] + " -> " + data[2]
        )

        pass_count += 1

    if pass_count > 0:

        test.passes(
            "DUTCH SOFT TISSUE TREATMENT "
            "LOCALIZATION VALIDATION PASSED"
        )

    else:

        test.fail(
            "NO DUTCH STRINGS FOUND ON SCREEN"
        )

    workbook.close()
    