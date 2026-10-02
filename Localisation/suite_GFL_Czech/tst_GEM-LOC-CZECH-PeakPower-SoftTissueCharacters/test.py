
# -*- coding: utf-8 -*-

import names
import openpyxl
import re


# ============================================================
# EXCEL CONFIGURATION
# ============================================================

EXCEL_FILE = ("/home/ezen/Test_Automation_Gemini/Localisation/suite_GFL_Czech/tst_GEM-LOC-CZECH-PeakPower-SoftTissueCharacters/testdata/Gemini strings.xlsx")

ENGLISH_COLUMN = 2      # Column B
CZECH_COLUMN = 13       # Column M


# ============================================================
# NORMALIZE TEXT
# ============================================================

def normalize_text(value):

    if value is None:
        return ""

    value = str(value)

    value = re.sub(
        r"<[^>]+>",
        "",
        value
    )

    value = re.sub(
        r"\s+",
        " ",
        value
    )

    return value.strip().casefold()


# ============================================================
# GET CZECH VALUES FROM COLUMN M
# ============================================================

def get_czech_values(sheet, english_text):

    expected_english = normalize_text(
        english_text
    )

    czech_values = []

    for row in range(2, sheet.max_row + 1):

        english_value = sheet.cell(
            row=row,
            column=ENGLISH_COLUMN
        ).value

        if english_value is None:
            continue

        if normalize_text(
            english_value
        ) == expected_english:

            czech_value = sheet.cell(
                row=row,
                column=CZECH_COLUMN
            ).value

            if czech_value is not None:

                czech_value = str(
                    czech_value
                ).strip()

                if czech_value:
                    czech_values.append(
                        czech_value
                    )

    return czech_values


# ============================================================
# VERIFY TEXT
# ============================================================

def verify_text(
        sheet,
        obj,
        english_text,
        description):

    snooze(6)

    actual_value = waitForObjectExists(
        obj
    ).text

    actual = (
        ""
        if actual_value is None
        else str(actual_value).strip()
    )

    czech_values = get_czech_values(
        sheet,
        english_text
    )

    if not czech_values:

        test.fail(
            "English string not found in Column B: "
            + english_text
        )

        return

    normalized_actual = normalize_text(
        actual
    )

    for expected in czech_values:

        if normalized_actual == normalize_text(
            expected
        ):

            test.compare(
                normalized_actual,
                normalize_text(expected),
                description
            )

            return

    test.fail(
        description
        + " | Expected: "
        + " / ".join(czech_values)
        + " | Actual: "
        + actual
    )


# ============================================================
# MAIN
# ============================================================

def main():

    # ========================================================
    # LOAD EXCEL
    # ========================================================

    try:

        workbook = openpyxl.load_workbook(
            EXCEL_FILE,
            data_only=True
        )

        if "Sheet1" in workbook.sheetnames:
            sheet = workbook["Sheet1"]
        else:
            sheet = workbook.active

    except Exception as e:

        test.fail(
            "Unable to load Gemini Strings Excel: "
            + str(e)
        )

        return


    # ========================================================
    # LOGIN
    # ========================================================

    snooze(2)

    waitForObject(
        names.numpad_pushButton_8_NumpadButton,
        30000
    )

    clickButton(
        waitForObject(
            names.numpad_pushButton_8_NumpadButton
        )
    )

    snooze(1)

    clickButton(
        waitForObject(
            names.numpad_pushButton_8_NumpadButton
        )
    )

    snooze(1)

    clickButton(
        waitForObject(
            names.numpad_pushButton_8_NumpadButton
        )
    )

    snooze(1)

    clickButton(
        waitForObject(
            names.numpad_pushButton_8_NumpadButton
        )
    )

    snooze(2)

    clickButton(
        waitForObject(
            names.mainFrame_okButton_QPushButton
        )
    )

    snooze(6)


    # ========================================================
    # SELECT CZECH LANGUAGE
    # ========================================================

    clickButton(
        waitForObject(
            names.homeScreen_settingsButton_QPushButton
        )
    )

    snooze(2)

    clickTab(
        waitForObject(
            names.settingsScreen_tbSystemInfo_TabWidget
        ),
        "INFO"
    )

    snooze(2)

    clickButton(
        waitForObject(
            names.gbSystemInformation_pbLanguageSettingsUpdate_QPushButton
        )
    )

    snooze(2)

    clickButton(
        waitForObject(
            names.languagesFrame_pbCzech_QPushButton
        )
    )

    snooze(2)

    clickButton(
        waitForObject(
            names.buttonsFrame_acceptButton_QPushButton
        )
    )

    snooze(2)


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
    # SOFT TISSUE QUICK START
    # ========================================================

    clickButton(
        waitForObject(
            names.homeScreen_pbSoftTissueQuickStart_QToolButton
        )
    )

    snooze(3)

    mouseClick(
        waitForObjectItem(
            names.tabLeftMainPresets_leftPresetsView_PresetListView,
            "_1"
        ),
        369,
        57,
        Qt.NoModifier,
        Qt.LeftButton
    )

    snooze(2)

    mouseClick(
        waitForObjectItem(
            names.tabRightMainPresets_rightPresetsView_PresetListView,
            "_1"
        ),
        206,
        54,
        Qt.NoModifier,
        Qt.LeftButton
    )

    snooze(2)

    clickButton(
        waitForObject(
            names.quickStartScreen_pbContinue_QPushButton
        )
    )

    snooze(3)

    clickButton(
        waitForObject(
            names.mainFrame_okButton_QPushButton_2
        )
    )

    snooze(6)


    # ========================================================
    # CANCEL MODE POPUP
    # ========================================================

    mouseClick(
        waitForObject(
            names.modeButton_nameLabel_QLabel
        ),
        77,
        33,
        Qt.NoModifier,
        Qt.LeftButton
    )

    snooze(3)

    clickButton(
        waitForObject(
            names.centralWidget_CancelButton_QPushButton_3
        )
    )

    snooze(3)


    # ========================================================
    # OPEN PEAK POWER
    # ========================================================

    mouseClick(
        waitForObject(
            names.peakPowerButton_nameLabel_QLabel
        ),
        46,
        29,
        Qt.NoModifier,
        Qt.LeftButton
    )

    snooze(2)


    # ========================================================
    # PEAK POWER VERIFICATION
    # ========================================================

    verify_text(
        sheet,
        names.centralWidget_lbTitle_QLabel,
        "SELECT PEAK POWER",
        "Peak Power Title"
    )

    verify_text(
        sheet,
        names.centralWidget_pw500_QPushButton,
        "500",
        "Peak Power High"
    )

    verify_text(
        sheet,
        names.centralWidget_pw250_QPushButton,
        "250",
        "Peak Power Medium"
    )

    verify_text(
        sheet,
        names.centralWidget_pw125_QPushButton,
        "125",
        "Peak Power Low"
    )

    verify_text(
        sheet,
        names.buttonsFrame_rejectButton_QPushButton,
        "CANCEL",
        "Peak Power Cancel"
    )


    # ========================================================
    # EXIT PEAK POWER
    # ========================================================

    clickButton(
        waitForObject(
            names.buttonsFrame_rejectButton_QPushButton
        )
    )

    snooze(3)

    clickButton(
        waitForObject(
            names.buttonsBar_homeButton_QPushButton_2
        )
    )

    snooze(6)


    # ========================================================
    # SOFT TISSUE ASSISTANT
    # ========================================================

    clickButton(
        waitForObject(
            names.homeScreen_pbSoftTissueAssistant_QToolButton
        )
    )

    snooze(3)

    clickButton(
        waitForObject(
            names.gbSoftTissueProcedures_pbIncision_QPushButton
        )
    )

    snooze(3)

    

    clickButton(
        waitForObject(
            names.softTissueAssistantModeScreen_pbContinue_QPushButton
        )
    )

    snooze(6)


    # ========================================================
    # TREATMENT CHARACTERISTICS
    # ========================================================

    clickButton(
        waitForObject(
            names.treatmentCharacteristicsBar_pbEdit_QPushButton
        )
    )

    snooze(6)


    # ========================================================
    # SOFT TISSUE CHARACTERISTICS VERIFICATION
    # ========================================================

    verify_text(
        sheet,
        names.centralWidget_titleLabel_QLabel,
        "SOFT TISSUE CHARACTERISTICS",
        "Soft Tissue Characteristics Title"
    )

    verify_text(
        sheet,
        names.centralWidget_titleLabel_QLabel_2,
        "PROCEDURE",
        "Procedure Label"
    )

    verify_text(
        sheet,
        names.centralWidget_valueLabel_QLabel,
        "INCISION",
        "Procedure Value"
    )

    verify_text(
        sheet,
        names.centralWidget_rejectButton_QPushButton,
        "EDIT",
        "Edit Button"
    )

    verify_text(
        sheet,
        names.centralWidget_acceptButton_QPushButton,
        "ACCEPT",
        "Accept Button"
    )


   


    # ========================================================
    # CLOSE EXCEL
    # ========================================================

    workbook.close()
