
# -*- coding: utf-8 -*-

import names
import openpyxl
import re
import unicodedata


# ============================================================
# EXCEL CONFIGURATION
#
# Column B = English
# Column M = Czech
# ============================================================

EXCEL_PATH = (
    "/home/ezen/Test_Automation_Gemini/Localisation/"
    "suite_GFL_Czech/"
    "tst_GEM-LOC-CZECH-PeakPower-SoftTissueCharacters/"
    "testdata/Gemini strings.xlsx"
)

ENGLISH_COLUMN = 2
CZECH_COLUMN = 13


# ============================================================
# TEST DATA
# ============================================================

PRESET_NAME = "preset one"
PRESET_PARAMETER_VALUES = "6 J     3 Hz     18 W"


# ============================================================
# NORMALIZE LOCALIZATION TEXT
# ============================================================

def normalize_localization(text):

    if text is None:
        return ""

    text = str(text)

    # Remove HTML/XML tags
    text = re.sub(r"<[^>]+>", " ", text)

    # Normalize escaped line breaks
    text = text.replace("\\n", " ")

    # Normalize real line breaks
    text = text.replace("\n", " ")
    text = text.replace("\r", " ")

    # Normalize tabs
    text = text.replace("\t", " ")

    # Normalize special spaces
    text = text.replace("\u00A0", " ")
    text = text.replace("\u2007", " ")
    text = text.replace("\u202F", " ")

    # Remove trademark/copyright symbols
    text = text.replace("™", "")
    text = text.replace("®", "")
    text = text.replace("©", "")

    # Normalize Unicode
    try:
        text = unicodedata.normalize("NFKC", text)
    except Exception:
        pass

    # Remove whitespace differences
    text = re.sub(r"\s+", "", text)

    return text.casefold()


# ============================================================
# LOAD GEMINI STRINGS
# ============================================================

def load_gemini_strings():

    workbook = openpyxl.load_workbook(
        EXCEL_PATH,
        data_only=True
    )

    sheet = workbook.active

    excel_strings = []

    for row in sheet.iter_rows(
        min_row=2,
        max_col=CZECH_COLUMN
    ):

        english = row[ENGLISH_COLUMN - 1].value
        czech = row[CZECH_COLUMN - 1].value

        if english is not None and czech is not None:

            english_text = str(english).strip()
            czech_text = str(czech).strip()

            if english_text and czech_text:

                excel_strings.append(
                    {
                        "english": english_text,
                        "czech": czech_text
                    }
                )

    workbook.close()

    return excel_strings


# ============================================================
# VERIFY UI TEXT AGAINST CZECH EXCEL COLUMN M
# ============================================================

def verify_excel_text(
        object_name,
        excel_strings,
        description=""):

    # Wait before every verification
    snooze(6)

    actual_text = str(
        waitForObjectExists(object_name).text
    )

    actual_normalized = normalize_localization(
        actual_text
    )

    matches = []

    for item in excel_strings:

        excel_czech = item["czech"]

        excel_normalized = normalize_localization(
            excel_czech
        )

        if actual_normalized == excel_normalized:

            matches.append(item)

    if len(matches) == 0:

        test.fail(
            "{} | Czech text not found in Excel Column M | "
            "UI text: {}".format(
                description,
                actual_text
            )
        )

        return False

    match = matches[0]

    test.compare(
        actual_normalized,
        normalize_localization(
            match["czech"]
        ),
        "{} | English: {}".format(
            description,
            match["english"]
        )
    )

    return True


# ============================================================
# MAIN TEST
# ============================================================

def main():

    # ========================================================
    # LOAD EXCEL
    # ========================================================

    excel_strings = load_gemini_strings()


    # ========================================================
    # LOGIN / UNLOCK
    # ========================================================

    doubleClick(
        waitForObject(
            names.numpad_pushButton_8_NumpadButton
        ),
        91,
        78,
        Qt.NoModifier,
        Qt.LeftButton
    )

    doubleClick(
        waitForObject(
            names.numpad_pushButton_8_NumpadButton
        ),
        91,
        78,
        Qt.NoModifier,
        Qt.LeftButton
    )

    clickButton(
        waitForObject(
            names.mainFrame_okButton_QPushButton
        )
    )


    # ========================================================
    # OPEN SETTINGS
    # ========================================================

    clickButton(
        waitForObject(
            names.homeScreen_settingsButton_QPushButton
        )
    )


    # ========================================================
    # CHANGE LANGUAGE TO CZECH
    # ========================================================

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

    snooze(6)


    # ========================================================
    # HOME
    # ========================================================

    clickButton(
        waitForObject(
            names.buttonsBar_homeButton_QPushButton
        )
    )

    snooze(6)


    # ========================================================
    # OPEN SETTINGS AGAIN
    # ========================================================

    clickButton(
        waitForObject(
            names.homeScreen_settingsButton_QPushButton
        )
    )

    snooze(6)


    # ========================================================
    # OPEN USER PRESETS
    # ========================================================

    clickTab(
        waitForObject(
            names.settingsScreen_tbSystemInfo_TabWidget
        ),
        "PŘEDVOLBY\n UŽIVATELE"
    )

    snooze(6)


    # ========================================================
    # ADD PRESET
    # ========================================================

    clickButton(
        waitForObject(
            names.settingsScreen_addButton_QPushButton
        )
    )

    snooze(6)


    # ========================================================
    # ADD PRESET LOCALIZATION
    # ========================================================

    verify_excel_text(
        names.centralWidget_lbOperation_QLabel,
        excel_strings,
        "Add Preset Title"
    )

    verify_excel_text(
        names.centralWidget_pbName_QPushButton,
        excel_strings,
        "Preset Name Field"
    )

    verify_excel_text(
        names.averagePowerWidget_nameLabel_QLabel,
        excel_strings,
        "Average Power Label"
    )

    verify_excel_text(
        names.pulseEnergyWidget_nameLabel_QLabel,
        excel_strings,
        "Pulse Energy Label"
    )

    verify_excel_text(
        names.frequencyWidget_nameLabel_QLabel,
        excel_strings,
        "Frequency Label"
    )

    verify_excel_text(
        names.modeButton_nameLabel_QLabel_3,
        excel_strings,
        "Standard Pulse Label"
    )

    verify_excel_text(
        names.peakPowerButton_nameLabel_QLabel_2,
        excel_strings,
        "Peak Power Label"
    )

    verify_excel_text(
        names.pulseModeWidget_saveButton_QPushButton,
        excel_strings,
        "Add Button"
    )


    # ========================================================
    # UNITS
    # ========================================================

    snooze(6)

    test.compare(
        str(
            waitForObjectExists(
                names.averagePowerWidget_unitsOfMeasureLabel_QLabel
            ).text
        ),
        "W",
        "Average Power Unit"
    )

    snooze(6)

    test.compare(
        str(
            waitForObjectExists(
                names.pulseEnergyWidget_unitsOfMeasureLabel_QLabel
            ).text
        ),
        "J",
        "Pulse Energy Unit"
    )

    snooze(6)

    test.compare(
        str(
            waitForObjectExists(
                names.frequencyWidget_unitsOfMeasureLabel_QLabel
            ).text
        ),
        "Hz",
        "Frequency Unit"
    )


    # ========================================================
    # ENTER PRESET NAME
    # ========================================================

    clickButton(
        waitForObject(
            names.centralWidget_pbName_QPushButton
        )
    )

    clickButton(
        waitForObject(
            names.keyboardPopup_p_KeyButton
        )
    )

    clickButton(
        waitForObject(
            names.keyboardPopup_r_KeyButton
        )
    )

    clickButton(
        waitForObject(
            names.keyboardPopup_e_KeyButton
        )
    )

    clickButton(
        waitForObject(
            names.keyboardPopup_s_KeyButton
        )
    )

    clickButton(
        waitForObject(
            names.keyboardPopup_e_KeyButton
        )
    )

    clickButton(
        waitForObject(
            names.keyboardPopup_t_KeyButton
        )
    )

    clickButton(
        waitForObject(
            names.keyboardPopup_KeyButton_4
        )
    )

    clickButton(
        waitForObject(
            names.keyboardPopup_o_KeyButton
        )
    )

    clickButton(
        waitForObject(
            names.keyboardPopup_n_KeyButton
        )
    )

    clickButton(
        waitForObject(
            names.keyboardPopup_e_KeyButton
        )
    )

    mouseClick(
        waitForObject(
            names.keyboardPopup_lbText_QLabel
        ),
        66,
        23,
        Qt.NoModifier,
        Qt.LeftButton
    )

    snooze(3)


    # ========================================================
    # SAVE NEW PRESET
    # ========================================================

    clickButton(
        waitForObject(
            names.pulseModeWidget_saveButton_QPushButton
        )
    )

    snooze(6)


    # ========================================================
    # PRESET CATEGORY TABS
    # ========================================================

    verify_excel_text(
        names.tabBarPresetsForSettings_K_MEN_TabItem,
        excel_strings,
        "Stone Preset Tab"
    )

    verify_excel_text(
        names.tabBarPresetsForSettings_M_KK_TK_TabItem,
        excel_strings,
        "Soft Tissue Preset Tab"
    )


    # ========================================================
    # EDIT PRESET
    #
    # WORKING RECORDED FLOW:
    # 1. Click Edit
    # 2. Click preset in list at 406, 53
    # 3. Edit popup opens
    # ========================================================

    clickButton(
        waitForObject(
            names.settingsScreen_editButton_QPushButton
        )
    )

    snooze(3)

    mouseClick(
        waitForObject(
            names.tabSettingsPresetsUserStonePresets_presetListView_PresetListView
        ),
        406,
        53,
        Qt.NoModifier,
        Qt.LeftButton
    )

    snooze(6)


    # ========================================================
    # EDIT PRESET TITLE
    # ========================================================

    verify_excel_text(
        names.centralWidget_lbOperation_QLabel,
        excel_strings,
        "Edit Preset Title"
    )


    # ========================================================
    # PRESET NAME
    # ========================================================

    snooze(6)

    test.compare(
        str(
            waitForObjectExists(
                names.centralWidget_pbName_QPushButton
            ).text
        ),
        PRESET_NAME,
        "Preset Name"
    )


    # ========================================================
    # EDIT SCREEN LOCALIZATION
    # ========================================================

    verify_excel_text(
        names.averagePowerWidget_nameLabel_QLabel,
        excel_strings,
        "Average Power Label - Edit"
    )

    verify_excel_text(
        names.pulseEnergyWidget_nameLabel_QLabel,
        excel_strings,
        "Pulse Energy Label - Edit"
    )

    verify_excel_text(
        names.frequencyWidget_nameLabel_QLabel,
        excel_strings,
        "Frequency Label - Edit"
    )

    verify_excel_text(
        names.modeButton_nameLabel_QLabel_3,
        excel_strings,
        "Standard Pulse Label - Edit"
    )

    verify_excel_text(
        names.peakPowerButton_nameLabel_QLabel_2,
        excel_strings,
        "Peak Power Label - Edit"
    )

    verify_excel_text(
        names.pulseModeWidget_saveButton_QPushButton,
        excel_strings,
        "Update Button"
    )


    # ========================================================
    # EDIT SCREEN UNITS
    # ========================================================

    snooze(6)

    test.compare(
        str(
            waitForObjectExists(
                names.averagePowerWidget_unitsOfMeasureLabel_QLabel
            ).text
        ),
        "W",
        "Average Power Unit - Edit"
    )

    snooze(6)

    test.compare(
        str(
            waitForObjectExists(
                names.pulseEnergyWidget_unitsOfMeasureLabel_QLabel
            ).text
        ),
        "J",
        "Pulse Energy Unit - Edit"
    )

    snooze(6)

    test.compare(
        str(
            waitForObjectExists(
                names.frequencyWidget_unitsOfMeasureLabel_QLabel
            ).text
        ),
        "Hz",
        "Frequency Unit - Edit"
    )


    # ========================================================
    # UPDATE PRESET
    # ========================================================

    clickButton(
        waitForObject(
            names.pulseModeWidget_saveButton_QPushButton
        )
    )

    snooze(6)


    # ========================================================
    # DELETE PRESET
    #
    # Same working pattern:
    # Click Delete
    # Then select preset from list
    # ========================================================

    clickButton(
        waitForObject(
            names.settingsScreen_deletePresetButton_QPushButton
        )
    )

    snooze(3)

    mouseClick(
        waitForObject(
            names.tabSettingsPresetsUserStonePresets_presetListView_PresetListView
        ),
        494,
        79,
        Qt.NoModifier,
        Qt.LeftButton
    )

    snooze(6)


    # ========================================================
    # DELETE CONFIRMATION DIALOG
    # ========================================================

    verify_excel_text(
        names.centralWidget_lbDialogTitle_QLabel,
        excel_strings,
        "Delete Preset Dialog Title"
    )


    # ========================================================
    # PRESET NAME IN DELETE DIALOG
    # ========================================================

    snooze(6)

    test.compare(
        str(
            waitForObjectExists(
                names.centralWidget_questionLabel_QLabel
            ).text
        ),
        PRESET_NAME,
        "Preset Name in Delete Dialog"
    )


    # ========================================================
    # CANCEL BUTTON
    # ========================================================

    verify_excel_text(
        names.buttonsFrame_rejectButton_QPushButton,
        excel_strings,
        "Cancel Button"
    )


    # ========================================================
    # DELETE BUTTON
    # ========================================================

    verify_excel_text(
        names.centralWidget_acceptButton_QPushButton,
        excel_strings,
        "Delete Button"
    )


    # ========================================================
    # PRESET PARAMETER VALUES
    # ========================================================

    snooze(6)

    test.compare(
        str(
            waitForObjectExists(
                names.infoFrame_extInfoLabel_QLabel
            ).text
        ),
        PRESET_PARAMETER_VALUES,
        "Preset Parameter Values"
    )


    # ========================================================
    # CONFIRM DELETE
    # ========================================================

    clickButton(
        waitForObject(
            names.centralWidget_acceptButton_QPushButton
        )
    )

    snooze(6)


    # ========================================================
    # FINAL TAB VERIFICATION
    # ========================================================

    verify_excel_text(
        names.tabBarPresetsForSettings_K_MEN_TabItem,
        excel_strings,
        "Stone Tab"
    )

    verify_excel_text(
        names.tabBarPresetsForSettings_M_KK_TK_TabItem,
        excel_strings,
        "Soft Tissue Tab"
    )

    verify_excel_text(
        names.settingsScreen_pbBack_QPushButton,
        excel_strings,
        "Back Button"
    )
