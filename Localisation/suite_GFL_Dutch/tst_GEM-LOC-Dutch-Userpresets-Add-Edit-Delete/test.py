
# -*- coding: utf-8 -*-

import names
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
# FIND DUTCH COLUMN
# ============================================================

def find_dutch_column(sheet):

    possible_headers = [
        "Dutch",
        "Nederlands",
        "Netherlands",
        "Dutch (Netherlands)",
        "Nederlands (Nederland)"
    ]

    for row in sheet.iter_rows(
        min_row=1,
        max_row=min(sheet.max_row, 10)
    ):

        for cell in row:

            if cell.value is None:
                continue

            value = str(cell.value).strip().casefold()

            for header in possible_headers:

                if value == header.casefold():

                    return cell.column

    # ========================================================
    # DUTCH COLUMN FALLBACK
    # ========================================================

    # Your current Excel log shows Dutch data is in column 7.
    return 7


# ============================================================
# VERIFY EXCEL STRING
# ============================================================

def verify_excel_string(
    object_name,
    sheet,
    row,
    dutch_column,
    description
):

    snooze(6)

    actual = str(
        waitForObjectExists(object_name).text
    )

    expected = get_excel_value(
        sheet,
        row,
        dutch_column
    )

    test.compare(
        actual,
        expected,
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
        "suite_GFL_Dutch/"
        "tst_GEM-LOC-Dutch-Userpresets-Add-Edit-Delete/"
        "testdata/Gemini Split strings.xlsx"
    )

    

    workbook = load_workbook(
        excelpath,
        read_only=True,
        data_only=True
    )

    sheet = workbook["Treatment Modes"]

    


    # ========================================================
    # FIND DUTCH COLUMN
    # ========================================================

    dutch_column = find_dutch_column(sheet)

    


    # ========================================================
    # LOGIN
    # ========================================================

    test.log("Entering login PIN")

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

    test.log("Opening Settings")

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
    # CHANGE LANGUAGE TO DUTCH
    # ========================================================

    

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


    # ========================================================
    # OPEN USER PRESETS
    # ========================================================

    test.log(
        "Opening User Presets - clicking Tab 3"
    )

    snooze(3)

    # ========================================================
    # CLICK TAB 3
    #
    # Qt tab index is zero-based:
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
    # CLICK USER PRESETS TAB
    #
    # After selecting Tab 3, click the User Presets tab.
    # This uses the tab index instead of Dutch text.
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

    test.log("Clicking Add Preset")

    clickButton(
        waitForObject(
            names.settingsScreen_addButton_QPushButton
        )
    )


    # ========================================================
    # 1. ADD PRESET OPERATION
    # ========================================================

    verify_excel_string(
        names.centralWidget_lbOperation_QLabel,
        sheet,
        67,
        dutch_column,
        "Add Preset Operation"
    )


    # ========================================================
    # 2. PRESET NAME
    # ========================================================

    verify_excel_string(
        names.centralWidget_pbName_QPushButton,
        sheet,
        50,
        dutch_column,
        "Preset Name"
    )


    # ========================================================
    # 3. AVERAGE POWER
    # ========================================================

    verify_excel_string(
        names.averagePowerWidget_nameLabel_QLabel,
        sheet,
        6,
        dutch_column,
        "Average Power"
    )


    # ========================================================
    # 4. AVERAGE POWER UNIT
    # ========================================================

    verify_excel_string(
        names.averagePowerWidget_unitsOfMeasureLabel_QLabel,
        sheet,
        7,
        dutch_column,
        "Average Power Unit"
    )


    # ========================================================
    # 5. PULSE ENERGY
    # ========================================================

    verify_excel_string(
        names.pulseEnergyWidget_nameLabel_QLabel,
        sheet,
        8,
        dutch_column,
        "Pulse Energy"
    )


    # ========================================================
    # 6. PULSE ENERGY UNIT
    # ========================================================

    mouseClick(
        waitForObject(
            names.centralWidget_frame_QFrame
        ),
        271,
        13,
        Qt.NoModifier,
        Qt.LeftButton
    )

    verify_excel_string(
        names.pulseEnergyWidget_unitsOfMeasureLabel_QLabel,
        sheet,
        9,
        dutch_column,
        "Pulse Energy Unit"
    )


    # ========================================================
    # 7. FREQUENCY
    # ========================================================

    verify_excel_string(
        names.frequencyWidget_nameLabel_QLabel,
        sheet,
        10,
        dutch_column,
        "Frequency"
    )


    # ========================================================
    # 8. FREQUENCY UNIT
    # ========================================================

    verify_excel_string(
        names.frequencyWidget_unitsOfMeasureLabel_QLabel,
        sheet,
        11,
        dutch_column,
        "Frequency Unit"
    )


    # ========================================================
    # 9. REGULAR PULSE
    # ========================================================

    test.compare(str(waitForObjectExists(names.modeButton_nameLabel_QLabel_3).text), "REGELMATIGE\nPULS")

    verify_excel_string(
        names.modeButton_nameLabel_QLabel_3,
        sheet,
        33,
        dutch_column,
        "Regular Pulse"
    )


    # ========================================================
    # 10. PEAK POWER
    # ========================================================

    verify_excel_string(
        names.peakPowerButton_nameLabel_QLabel_2,
        sheet,
        12,
        dutch_column,
        "Peak Power"
    )


    # ========================================================
    # 11. ADD BUTTON
    # ========================================================

    verify_excel_string(
        names.pulseModeWidget_saveButton_QPushButton,
        sheet,
        68,
        dutch_column,
        "Add Button"
    )


    # ========================================================
    # ENTER PRESET NAME
    # ========================================================

    mouseClick(
        waitForObject(
            names.pulseModeWidget_buttonsWidget_QWidget
        ),
        508,
        46,
        Qt.NoModifier,
        Qt.LeftButton
    )

    mouseClick(
        waitForObject(
            names.pulseModeWidget_buttonsWidget_QWidget
        ),
        411,
        1,
        Qt.NoModifier,
        Qt.LeftButton
    )

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
        dutch_column,
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
        actualEditName,
        "preset one",
        "Edit Preset Name"
    )


    # ========================================================
    # EDIT - AVERAGE POWER
    # ========================================================

    verify_excel_string(
        names.averagePowerWidget_nameLabel_QLabel,
        sheet,
        6,
        dutch_column,
        "Edit - Average Power"
    )


    # ========================================================
    # EDIT - AVERAGE POWER UNIT
    # ========================================================

    verify_excel_string(
        names.averagePowerWidget_unitsOfMeasureLabel_QLabel,
        sheet,
        7,
        dutch_column,
        "Edit - Average Power Unit"
    )


    # ========================================================
    # EDIT - PULSE ENERGY
    # ========================================================

    verify_excel_string(
        names.pulseEnergyWidget_nameLabel_QLabel,
        sheet,
        8,
        dutch_column,
        "Edit - Pulse Energy"
    )


    # ========================================================
    # EDIT - PULSE ENERGY UNIT
    # ========================================================

    verify_excel_string(
        names.pulseEnergyWidget_unitsOfMeasureLabel_QLabel,
        sheet,
        9,
        dutch_column,
        "Edit - Pulse Energy Unit"
    )


    # ========================================================
    # EDIT - FREQUENCY
    # ========================================================

    verify_excel_string(
        names.frequencyWidget_nameLabel_QLabel,
        sheet,
        10,
        dutch_column,
        "Edit - Frequency"
    )


    # ========================================================
    # EDIT - FREQUENCY UNIT
    # ========================================================

    verify_excel_string(
        names.frequencyWidget_unitsOfMeasureLabel_QLabel,
        sheet,
        11,
        dutch_column,
        "Edit - Frequency Unit"
    )


    # ========================================================
    # EDIT - REGULAR PULSE
    # ========================================================

    verify_excel_string(
        names.modeButton_nameLabel_QLabel_3,
        sheet,
        33,
        dutch_column,
        "Edit - Regular Pulse"
    )


    # ========================================================
    # EDIT - PEAK POWER
    # ========================================================

    verify_excel_string(
        names.peakPowerButton_nameLabel_QLabel_2,
        sheet,
        12,
        dutch_column,
        "Edit - Peak Power"
    )


    # ========================================================
    # UPDATE BUTTON
    # ========================================================

    verify_excel_string(
        names.pulseModeWidget_saveButton_QPushButton,
        sheet,
        69,
        dutch_column,
        "Update Button"
    )


    # ========================================================
    # SAVE EDITED PRESET
    # ========================================================

    mouseClick(
        waitForObject(
            names.pulseModeWidget_buttonsWidget_QWidget
        ),
        531,
        22,
        Qt.NoModifier,
        Qt.LeftButton
    )

    mouseClick(
        waitForObject(
            names.pulseModeWidget_buttonsWidget_QWidget
        ),
        509,
        30,
        Qt.NoModifier,
        Qt.LeftButton
    )

    clickButton(
        waitForObject(
            names.pulseModeWidget_saveButton_QPushButton
        )
    )


    # ========================================================
    # DELETE PRESET
    # ========================================================

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

    verify_excel_string(
        names.centralWidget_lbDialogTitle_QLabel,
        sheet,
        75,
        dutch_column,
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
        actualDeleteName,
        "preset one",
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
        actualInfo,
        expectedInfo,
        "Preset Information"
    )


    # ========================================================
    # CANCEL BUTTON
    # ========================================================

    verify_excel_string(
        names.buttonsFrame_rejectButton_QPushButton,
        sheet,
        73,
        dutch_column,
        "Cancel Button"
    )


    # ========================================================
    # DELETE BUTTON
    # ========================================================

    verify_excel_string(
        names.centralWidget_acceptButton_QPushButton,
        sheet,
        74,
        dutch_column,
        "Delete Button"
    )


    # ========================================================
    # CLOSE EXCEL
    # ========================================================

    workbook.close()

    test.log(
        "Dutch User Presets Add/Edit/Delete "
        "localization verification completed"
    )

