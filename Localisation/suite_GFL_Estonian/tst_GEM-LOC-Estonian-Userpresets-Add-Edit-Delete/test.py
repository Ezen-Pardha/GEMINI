
# -*- coding: utf-8 -*-

import names
import re
from openpyxl import load_workbook


# ============================================================
# EXCEL VALUE
# ============================================================

def get_excel_value(sheet, row, column):

    value = sheet.cell(
        row=row,
        column=column
    ).value

    if value is None:
        return ""

    return str(value)


# ============================================================
# NORMALIZE TEXT
# ============================================================

def normalize_text(text):

    if text is None:
        return ""

    text = str(text)

    # Replace HTML line breaks
    text = re.sub(
        r"<br\s*/?>",
        " ",
        text,
        flags=re.IGNORECASE
    )

    # Remove HTML tags
    text = re.sub(
        r"<[^>]+>",
        " ",
        text
    )

    # Replace line breaks and tabs with spaces
    text = re.sub(
        r"[\r\n\t]+",
        " ",
        text
    )

    # Replace non-breaking spaces
    text = text.replace(
        "\xa0",
        " "
    )

    # Remove multiple spaces
    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip().casefold()


# ============================================================
# FIND ESTONIAN COLUMN
# ============================================================

def find_estonian_column(sheet):

    possible_headers = [
        "Estonian",
        "Eesti",
        "Estonian (Estonia)",
        "Eesti (Eesti)"
    ]

    for row in sheet.iter_rows(
        min_row=1,
        max_row=min(sheet.max_row, 10)
    ):

        for cell in row:

            if cell.value is None:
                continue

            value = str(
                cell.value
            ).strip().casefold()

            for header in possible_headers:

                if value == header.casefold():

                    return cell.column

    # ========================================================
    # ESTONIAN COLUMN FALLBACK
    # ========================================================
    # Estonian translation is in Column H.
    return 8


# ============================================================
# VERIFY EXCEL STRING
# ============================================================

def verify_excel_string(
        object_name,
        sheet,
        row,
        estonian_column,
        description):

    snooze(6)

    actual = str(
        waitForObjectExists(
            object_name
        ).text
    )

    expected = get_excel_value(
        sheet,
        row,
        estonian_column
    )

    actual_normalized = normalize_text(
        actual
    )

    expected_normalized = normalize_text(
        expected
    )

    test.compare(
        actual_normalized,
        expected_normalized,
        description
    )


# ============================================================
# MAIN
# ============================================================

def main():

    # ========================================================
    # EXCEL FILE
    # ========================================================

    excelpath = (
        "/home/ezen/Test_Automation_Gemini/Localisation/"
        "suite_GFL_Estonian/"
        "tst_GEM-LOC-Estonian-Userpresets-Add-Edit-Delete/"
        "testdata/Gemini Split strings.xlsx"
    )

    # ========================================================
    # LOAD EXCEL
    # ========================================================

    workbook = load_workbook(
        excelpath,
        read_only=True,
        data_only=True
    )

    # ========================================================
    # EXCEL SHEET
    # ========================================================

    sheet = workbook["Treatment Modes"]

    # ========================================================
    # FIND ESTONIAN COLUMN
    # ========================================================

    estonian_column = find_estonian_column(
        sheet
    )

    # ========================================================
    # LOGIN
    # ========================================================

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

    # ========================================================
    # OPEN SETTINGS
    # ========================================================

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

    # ========================================================
    # CHANGE LANGUAGE TO ESTONIAN
    # ========================================================

    clickButton(
        waitForObject(
            names.languagesFrame_pbEstonia_QPushButton
        )
    )

    clickButton(
        waitForObject(
            names.buttonsFrame_acceptButton_QPushButton
        )
    )

    # ========================================================
    # OPEN USER PRESETS
    # ========================================================

    snooze(3)

    # ========================================================
    # SELECT TAB 3
    #
    # Tab 1 = index 0
    # Tab 2 = index 1
    # Tab 3 = index 2
    # ========================================================

    tabWidget = waitForObject(
        names.settingsScreen_tbSystemInfo_TabWidget
    )

    tabWidget.setCurrentIndex(2)

    snooze(3)

    # ========================================================
    # SELECT USER PRESETS TAB
    # ========================================================

    tabWidget.setCurrentIndex(2)

    snooze(3)

    sendEvent(
        "QMoveEvent",
        waitForObject(
            names.o_ScreenSwitcher
        ),
        0,
        -66,
        1285,
        233
    )

    # ========================================================
    # ADD PRESET
    # ========================================================

    # clickButton(waitForObject(names.settingsScreen_addButton_QPushButton))

    clickButton(
        waitForObject(
            names.settingsScreen_addButton_QPushButton
        )
    )

    # ========================================================
    # 1. ADD PRESET OPERATION
    # ========================================================
    
    # test.compare(str(waitForObjectExists(names.centralWidget_lbOperation_QLabel).text), "LISA EELSÄTE")
    # test.compare(str(waitForObjectExists(names.centralWidget_pbName_QPushButton).text), "Sisesta eelsätte nimi")
    # test.compare(str(waitForObjectExists(names.averagePowerWidget_nameLabel_QLabel_2).text), "KESKMINE\nVÕIMSUS")
    # test.compare(str(waitForObjectExists(names.averagePowerWidget_unitsOfMeasureLabel_QLabel_3).text), "W")
    # test.compare(str(waitForObjectExists(names.pulseEnergyWidget_nameLabel_QLabel).text), "IMPULSIENERGIA")
    # test.compare(str(waitForObjectExists(names.pulseEnergyWidget_unitsOfMeasureLabel_QLabel).text), "J")
    # test.compare(str(waitForObjectExists(names.frequencyWidget_nameLabel_QLabel).text), "SAGEDUS")
    # test.compare(str(waitForObjectExists(names.frequencyWidget_unitsOfMeasureLabel_QLabel).text), "Hz")
    # test.compare(str(waitForObjectExists(names.modeButton_nameLabel_QLabel_2).text), "REGULAARNE\nPULSS")
    # test.compare(str(waitForObjectExists(names.peakPowerButton_nameLabel_QLabel).text), "TIPUVÕIM\nSUS")
    # test.compare(str(waitForObjectExists(names.pulseModeWidget_saveButton_QPushButton).text), "LISA")

    verify_excel_string(
        names.centralWidget_lbOperation_QLabel,
        sheet,
        67,
        estonian_column,
        "Add Preset Operation"
    )

    # ========================================================
    # 2. PRESET NAME
    # ========================================================

    verify_excel_string(
        names.centralWidget_pbName_QPushButton,
        sheet,
        50,
        estonian_column,
        "Preset Name"
    )

    # ========================================================
    # 3. AVERAGE POWER
    # ========================================================

    verify_excel_string(
        names.averagePowerWidget_nameLabel_QLabel_2,
        sheet,
        6,
        estonian_column,
        "Average Power"
    )

    # ========================================================
    # 4. AVERAGE POWER UNIT
    # ========================================================

    verify_excel_string(
        names.averagePowerWidget_unitsOfMeasureLabel_QLabel_3,
        sheet,
        7,
        estonian_column,
        "Average Power Unit"
    )

    # ========================================================
    # 5. PULSE ENERGY
    # ========================================================

    verify_excel_string(
        names.pulseEnergyWidget_nameLabel_QLabel,
        sheet,
        8,
        estonian_column,
        "Pulse Energy"
    )

    # ========================================================
    # 6. PULSE ENERGY UNIT
    # ========================================================

    # mouseClick(
    #     waitForObject(
    #         names.centralWidget_frame_QFrame
    #     ),
    #     271,
    #     13,
    #     Qt.NoModifier,
    #     Qt.LeftButton
    # )

    verify_excel_string(
        names.pulseEnergyWidget_unitsOfMeasureLabel_QLabel,
        sheet,
        9,
        estonian_column,
        "Pulse Energy Unit"
    )

    # ========================================================
    # 7. FREQUENCY
    # ========================================================

    verify_excel_string(
        names.frequencyWidget_nameLabel_QLabel,
        sheet,
        10,
        estonian_column,
        "Frequency"
    )

    # ========================================================
    # 8. FREQUENCY UNIT
    # ========================================================

    verify_excel_string(
        names.frequencyWidget_unitsOfMeasureLabel_QLabel,
        sheet,
        11,
        estonian_column,
        "Frequency Unit"
    )

    # ========================================================
    # 9. REGULAR PULSE
    # ========================================================

    verify_excel_string(
        names.modeButton_nameLabel_QLabel_2,
        sheet,
        33,
        estonian_column,
        "Regular Pulse"
    )

    # ========================================================
    # 10. PEAK POWER
    # ========================================================

    verify_excel_string(
        names.peakPowerButton_nameLabel_QLabel,
        sheet,
        12,
        estonian_column,
        "Peak Power"
    )

    # ========================================================
    # 11. ADD BUTTON
    # ========================================================

    verify_excel_string(
        names.pulseModeWidget_saveButton_QPushButton,
        sheet,
        68,
        estonian_column,
        "Add Button"
    )

    # ========================================================
    # ENTER PRESET NAME
    # ========================================================

    clickButton(waitForObject(names.centralWidget_pbName_QPushButton))
   

    # mouseClick(
    #     waitForObject(
    #         names.pulseModeWidget_buttonsWidget_QWidget
    #     ),
    #     508,
    #     46,
    #     Qt.NoModifier,
    #     Qt.LeftButton
    # )
    #
    # mouseClick(
    #     waitForObject(
    #         names.pulseModeWidget_buttonsWidget_QWidget
    #     ),
    #     411,
    #     1,
    #     Qt.NoModifier,
    #     Qt.LeftButton
    # )

    clickButton(
        waitForObject(
            names.centralWidget_pbName_QPushButton
        )
    )

    type(
        waitForObject(
            names.keyboardPopup_wdEdit_WdLineEdit
        ),
        "preset one"
    )

    mouseClick(
        waitForObject(
            names.keyboardPopup_lbText_QLabel
        ),
        77,
        26,
        Qt.NoModifier,
        Qt.LeftButton
    )

    clickButton(
        waitForObject(
            names.pulseModeWidget_saveButton_QPushButton
        )
    )

    # ========================================================
    # SELECT PRESET
    # ========================================================

    clickButton(waitForObject(names.settingsScreen_editButton_QPushButton))
    # mouseClick(waitForObject(names.tabSettingsPresetsUserStonePresets_presetListView_PresetListView), 462, 61, Qt.NoModifier, Qt.LeftButton)

    mouseClick(
        waitForObject(
            names.tabSettingsPresetsUserStonePresets_presetListView_PresetListView
        ),
        546,
        72,
        Qt.NoModifier,
        Qt.LeftButton
    )

    # ========================================================
    # EDIT PRESET
    # ========================================================

    clickButton(
        waitForObject(
            names.settingsScreen_editButton_QPushButton
        )
    )

    mouseClick(
        waitForObject(
            names.tabSettingsPresetsUserStonePresets_presetListView_PresetListView
        ),
        494,
        66,
        Qt.NoModifier,
        Qt.LeftButton
    )

    # ========================================================
    # EDIT OPERATION
    # ========================================================

    verify_excel_string(
        names.centralWidget_lbOperation_QLabel,
        sheet,
        73,
        estonian_column,
        "Edit Preset Operation"
    )

    # ========================================================
    # EDIT PRESET NAME
    # ========================================================

    snooze(6)

    actualEditName = str(
        waitForObjectExists(
            names.centralWidget_pbName_QPushButton
        ).text
    )

    test.compare(
        normalize_text(actualEditName),
        normalize_text("preset one"),
        "Edit Preset Name"
    )

    # ========================================================
    # EDIT - AVERAGE POWER
    # ========================================================

    
    # test.compare(str(waitForObjectExists(names.centralWidget_lbOperation_QLabel).text), "<html><head></head><body><p><img src=\":/gui/themes/dark/icons/edit_profile_header_.png\"/><span style=\"font-size:12pt; font-weight:600;\">   REDIGEERI EELSÄTE</span></p></body></html>")
    # test.compare(str(waitForObjectExists(names.averagePowerWidget_nameLabel_QLabel_2).text), "KESKMINE\nVÕIMSUS")
    # test.compare(str(waitForObjectExists(names.averagePowerWidget_unitsOfMeasureLabel_QLabel_3).text), "W")
    # test.compare(str(waitForObjectExists(names.pulseEnergyWidget_nameLabel_QLabel).text), "IMPULSIENERGIA")
    # test.compare(str(waitForObjectExists(names.pulseEnergyWidget_unitsOfMeasureLabel_QLabel).text), "J")
    # test.compare(str(waitForObjectExists(names.frequencyWidget_nameLabel_QLabel).text), "SAGEDUS")
    # test.compare(str(waitForObjectExists(names.frequencyWidget_unitsOfMeasureLabel_QLabel).text), "Hz")
    # test.compare(str(waitForObjectExists(names.modeButton_nameLabel_QLabel_2).text), "REGULAARNE\nPULSS")
    # test.compare(str(waitForObjectExists(names.peakPowerButton_nameLabel_QLabel).text), "TIPUVÕIM\nSUS")
    # test.compare(str(waitForObjectExists(names.pulseModeWidget_saveButton_QPushButton).text), "VÄRSKEN\nDA")

    verify_excel_string(
        names.averagePowerWidget_nameLabel_QLabel_2,
        sheet,
        6,
        estonian_column,
        "Edit - Average Power"
    )

    # ========================================================
    # EDIT - AVERAGE POWER UNIT
    # ========================================================

    verify_excel_string(
        names.averagePowerWidget_unitsOfMeasureLabel_QLabel_3,
        sheet,
        7,
        estonian_column,
        "Edit - Average Power Unit"
    )

    # ========================================================
    # EDIT - PULSE ENERGY
    # ========================================================

    verify_excel_string(
        names.pulseEnergyWidget_nameLabel_QLabel,
        sheet,
        8,
        estonian_column,
        "Edit - Pulse Energy"
    )

    # ========================================================
    # EDIT - PULSE ENERGY UNIT
    # ========================================================

    verify_excel_string(
        names.pulseEnergyWidget_unitsOfMeasureLabel_QLabel,
        sheet,
        9,
        estonian_column,
        "Edit - Pulse Energy Unit"
    )

    # ========================================================
    # EDIT - FREQUENCY
    # ========================================================

    verify_excel_string(
        names.frequencyWidget_nameLabel_QLabel,
        sheet,
        10,
        estonian_column,
        "Edit - Frequency"
    )

    # ========================================================
    # EDIT - FREQUENCY UNIT
    # ========================================================

    verify_excel_string(
        names.frequencyWidget_unitsOfMeasureLabel_QLabel,
        sheet,
        11,
        estonian_column,
        "Edit - Frequency Unit"
    )

    # ========================================================
    # EDIT - REGULAR PULSE
    # ========================================================

    verify_excel_string(
        names.modeButton_nameLabel_QLabel_2,
        sheet,
        33,
        estonian_column,
        "Edit - Regular Pulse"
    )

    # ========================================================
    # EDIT - PEAK POWER
    # ========================================================

    verify_excel_string(
        names.peakPowerButton_nameLabel_QLabel,
        sheet,
        12,
        estonian_column,
        "Edit - Peak Power"
    )

    # ========================================================
    # UPDATE BUTTON
    # ========================================================

    verify_excel_string(
        names.pulseModeWidget_saveButton_QPushButton,
        sheet,
        69,
        estonian_column,
        "Update Button"
    )

    # ========================================================
    # SAVE EDITED PRESET
    # ========================================================

    # mouseClick(
    #     waitForObject(
    #         names.pulseModeWidget_buttonsWidget_QWidget
    #     ),
    #     531,
    #     22,
    #     Qt.NoModifier,
    #     Qt.LeftButton
    # )
    #
    # mouseClick(
    #     waitForObject(
    #         names.pulseModeWidget_buttonsWidget_QWidget
    #     ),
    #     509,
    #     30,
    #     Qt.NoModifier,
    #     Qt.LeftButton
    # )
    
    mouseClick(waitForObject(names.averagePowerWidget_unitsOfMeasureLabel_QLabel_3), 131, 49, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.pulseModeWidget_saveButton_QPushButton, 291175))
    #
    # clickButton(
    #     waitForObject(
    #         names.pulseModeWidget_saveButton_QPushButton
    #     )
    # )

    # ========================================================
    # DELETE PRESET
    # ========================================================

    # clickButton(waitForObject(names.settingsScreen_deletePresetButton_QPushButton))
    # mouseClick(waitForObject(names.tabSettingsPresetsUserStonePresets_presetListView_PresetListView), 527, 56, Qt.NoModifier, Qt.LeftButton)
    # clickButton(waitForObject(names.buttonsFrame_acceptButton_QPushButton_2))

    clickButton(
        waitForObject(
            names.settingsScreen_deletePresetButton_QPushButton
        )
    )

    mouseClick(
        waitForObject(
            names.tabSettingsPresetsUserStonePresets_presetListView_PresetListView
        ),
        553,
        80,
        Qt.NoModifier,
        Qt.LeftButton
    )

    # ========================================================
    # DELETE DIALOG TITLE
    # ========================================================

    # test.compare(str(waitForObjectExists(names.centralWidget_lbDialogTitle_QLabel).text), "Kas kustutada järgmine eelsäte?")
    # test.compare(str(waitForObjectExists(names.centralWidget_questionLabel_QLabel).text), "preset one")
    # test.compare(str(waitForObjectExists(names.infoFrame_extInfoLabel_QLabel).text), "6 J     3 Hz     18 W")
    # test.compare(str(waitForObjectExists(names.buttonsFrame_rejectButton_QPushButton).text), "TÜHISTA")
    # test.compare(str(waitForObjectExists(names.buttonsFrame_acceptButton_QPushButton_2).text), "KUSTUTA")

    verify_excel_string(
        names.centralWidget_lbDialogTitle_QLabel,
        sheet,
        75,
        estonian_column,
        "Delete Dialog Title"
    )

    # ========================================================
    # DELETE PRESET NAME
    # ========================================================

    snooze(6)

    actualDeleteName = str(
        waitForObjectExists(
            names.centralWidget_questionLabel_QLabel
        ).text
    )

    test.compare(
        normalize_text(actualDeleteName),
        normalize_text("preset one"),
        "Delete Preset Name"
    )

    # ========================================================
    # PRESET INFORMATION
    # ========================================================

    snooze(6)

    actualInfo = str(
        waitForObjectExists(
            names.infoFrame_extInfoLabel_QLabel
        ).text
    )

    expectedInfo = "6 J     3 Hz     18 W"

    test.compare(
        normalize_text(actualInfo),
        normalize_text(expectedInfo),
        "Preset Information"
    )

    # ========================================================
    # CANCEL BUTTON
    # ========================================================

    verify_excel_string(
        names.buttonsFrame_rejectButton_QPushButton,
        sheet,
        73,
        estonian_column,
        "Cancel Button"
    )

    # ========================================================
    # DELETE BUTTON
    # ========================================================

    verify_excel_string(
        names.buttonsFrame_acceptButton_QPushButton_2,
        sheet,
        74,
        estonian_column,
        "Delete Button"
    )

    # ========================================================
    # CLOSE EXCEL
    # ========================================================

    workbook.close()
