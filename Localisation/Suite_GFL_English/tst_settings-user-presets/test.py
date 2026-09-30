# -*- coding: utf-8 -*-

import names
import openpyxl
import re


EXCEL_PATH = "/home/ntc/Test_Automation_Gemini/Localisation/Suite_GFL_English/tst_LoginScreen-Logoff/testdata/Gemini strings.xlsx"

verified_strings = set()


def normalize(text):

    if text is None:
        return ""

    text = str(text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = " ".join(text.split())
    text = re.sub(r"\s*<\s*", " < ", text)
    text = re.sub(r"\s*>\s*", " > ", text)

    return text.casefold().strip()


def is_number_or_numeric_value(text):

    text = str(text).strip()

    if not text:
        return True

    if re.fullmatch(r"\d+(\.\d+)?", text):
        return True

    if re.fullmatch(r"\d+(\.\d+)?\s*%", text):
        return True

    if re.fullmatch(
        r"\d+(\.\d+)?\s*(hz|w|j|microns?|mm|cm|sec|seconds?|min|minutes?)",
        text,
        re.IGNORECASE
    ):
        return True

    if re.fullmatch(
        r"\d{1,4}[/-]\d{1,2}[/-]\d{1,4}",
        text
    ):
        return True

    if re.fullmatch(
        r"\d+(\.\d+)?\s*[a-zA-Z]+\s*/\s*\d+(\.\d+)?\s*[a-zA-Z]+",
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


def load_english_strings():

    workbook = openpyxl.load_workbook(
        EXCEL_PATH,
        data_only=True
    )

    sheet = workbook.active

    strings = {}

    for row in sheet.iter_rows(
        min_row=2,
        values_only=True
    ):

        if len(row) < 1:
            continue

        english = row[0]

        if english is None:
            continue

        english = str(english).strip()

        if not english:
            continue

        key = normalize(english)

        if key not in strings:
            strings[key] = english

    workbook.close()

    return strings


def verify_screen(root_object, screen_name):

    global verified_strings

    excel_strings = load_english_strings()

    screen_texts = get_all_texts(root_object)

    unique_texts = {}

    for text in screen_texts:

        text = str(text).strip()

        if not text:
            continue

        normalized = normalize(text)

        if not normalized:
            continue

        if len(normalized) < 2:
            continue

        # Ignore numbers and numeric values
        if is_number_or_numeric_value(text):
            continue

        # AUT is the preset name manually entered by the test
        if normalized == "aut":
            continue

        if normalized not in unique_texts:
            unique_texts[normalized] = text


    for screen_normalized, actual_text in unique_texts.items():

        if screen_normalized in verified_strings:
            continue

        matches = []

        # Exact match
        if screen_normalized in excel_strings:

            matches.append(
                excel_strings[screen_normalized]
            )

        else:

            # Excel string contained inside UI text
            for excel_normalized, excel_original in excel_strings.items():

                if (
                    len(excel_normalized) >= 4
                    and excel_normalized in screen_normalized
                ):
                    matches.append(excel_original)

            # UI string contained inside Excel string
            if not matches:

                for excel_normalized, excel_original in excel_strings.items():

                    if (
                        len(screen_normalized) >= 4
                        and screen_normalized in excel_normalized
                    ):
                        matches.append(excel_original)


        if matches:

            matched = matches[0]
            key = normalize(matched)

            if key not in verified_strings:

                verified_strings.add(key)

                test.passes(matched)

        else:

            verified_strings.add(screen_normalized)

            test.fail(
                actual_text +
                " -> String not found in Excel"
            )


def main():

    # =========================================================
    # LOGIN
    # =========================================================

    sendEvent(
        "QMoveEvent",
        waitForObject(names.o_ScreenSwitcher),
        50,
        174,
        668,
        190
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

    verify_screen(
        waitForObject(names.o_ScreenSwitcher),
        "HOME"
    )


    # =========================================================
    # SETTINGS
    # =========================================================

    clickButton(
        waitForObject(names.homeScreen_settingsButton_QPushButton)
    )

    verify_screen(
        waitForObject(names.o_ScreenSwitcher),
        "SETTINGS"
    )


    # =========================================================
    # USER PRESETS
    # =========================================================

    clickTab(
        waitForObject(names.settingsScreen_tbSystemInfo_TabWidget),
        "USER\nPRESETS"
    )

    verify_screen(
        waitForObject(names.o_ScreenSwitcher),
        "USER PRESETS"
    )


    # =========================================================
    # ADD PRESET POPUP
    # =========================================================

    clickButton(
        waitForObject(names.settingsScreen_addButton_QPushButton)
    )

    # o_ScreenSwitcher is blocked by the Add Preset modal.
    # Verify using the actual Add Preset modal objects.

    verify_screen(
        waitForObject(names.centralWidget_lbOperation_QLabel),
        "ADD PRESET"
    )


    # =========================================================
    # PRESET NAME
    # =========================================================

    clickButton(
        waitForObject(names.centralWidget_pbName_QPushButton)
    )

    # Keyboard popup is active.
    # Do not use o_ScreenSwitcher here.


    clickButton(
        waitForObject(names.keyboardPopup_a_KeyButton)
    )

    clickButton(
        waitForObject(names.keyboardPopup_u_KeyButton)
    )

    clickButton(
        waitForObject(names.keyboardPopup_t_KeyButton)
    )


    # Verify keyboard text
    verify_screen(
        waitForObject(names.keyboardPopup_lbText_QLabel),
        "Keyboard"
    )


    mouseClick(
        waitForObject(names.keyboardPopup_lbText_QLabel),
        104,
        34,
        Qt.NoModifier,
        Qt.LeftButton
    )


    # =========================================================
    # SAVE PRESET
    # =========================================================

    clickButton(
        waitForObject(names.pulseModeWidget_saveButton_QPushButton)
    )

    verify_screen(
        waitForObject(names.o_ScreenSwitcher),
        "PRESET SAVED"
    )


    # =========================================================
    # EDIT PRESET
    # =========================================================

    clickButton(
        waitForObject(names.settingsScreen_editButton_QPushButton)
    )

    verify_screen(
        waitForObject(names.o_ScreenSwitcher),
        "EDIT PRESET"
    )


    # Select preset

    mouseClick(
        waitForObject(
            names.tabSettingsPresetsUserStonePresets_presetListView_PresetListView
        ),
        426,
        83,
        Qt.NoModifier,
        Qt.LeftButton
    )


    # Save/update

    clickButton(
        waitForObject(names.pulseModeWidget_saveButton_QPushButton)
    )

    verify_screen(
        waitForObject(names.o_ScreenSwitcher),
        "UPDATED PRESET"
    )


    # =========================================================
    # DELETE PRESET
    # =========================================================

    clickButton(
        waitForObject(names.settingsScreen_deletePresetButton_QPushButton)
    )


    # Select preset

    mouseClick(
        waitForObject(
            names.tabSettingsPresetsUserStonePresets_presetListView_PresetListView
        ),
        491,
        72,
        Qt.NoModifier,
        Qt.LeftButton
    )


    # =========================================================
    # DELETE CONFIRMATION POPUP
    # =========================================================

    # o_ScreenSwitcher is blocked by this popup.
    # Verify using the actual popup objects.

    verify_screen(
        waitForObject(names.centralWidget_lbDialogTitle_QLabel_2),
        "DELETE CONFIRMATION"
    )

    verify_screen(
        waitForObject(names.centralWidget_questionLabel_QLabel_2),
        "DELETE QUESTION"
    )


    # =========================================================
    # CONFIRM DELETE
    # =========================================================

    clickButton(
        waitForObject(names.buttonsFrame_acceptButton_QPushButton_2)
    )


    # =========================================================
    # FINAL USER PRESETS SCREEN
    # =========================================================

    verify_screen(
        waitForObject(names.o_ScreenSwitcher),
        "USER PRESETS FINAL"
    )