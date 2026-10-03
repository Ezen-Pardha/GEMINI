# -*- coding: utf-8 -*-

import names
import openpyxl
from openpyxl import load_workbook


def main():

    # ============================================================
    # EXCEL FILE
    # ============================================================

    excelpath = (
        "/home/ezen/Test_Automation_Gemini/Localisation/"
        "suite_GFL_Danish/"
        "tst_GEM-LOC-Danish-PeakPower-SoftTissueCharacters/"
        "testdata/Gemini Split strings.xlsx"
    )

    test.log("Loading Excel file...")

    workbook = load_workbook(
        excelpath,
        read_only=True,
        data_only=True
    )

    sheet = workbook["Treatment Modes"]

    test.log("Excel sheet loaded: Treatment Modes")


    # ============================================================
    # LOGIN
    # ============================================================

    test.log("Entering login PIN")

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


    # ============================================================
    # OPEN SETTINGS
    # ============================================================

    test.log("Opening Settings")

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


    # ============================================================
    # CHANGE LANGUAGE TO DANISH
    # ============================================================

    test.log("Selecting Danish language")

    clickButton(
        waitForObject(names.languagesFrame_pbDenmark_QPushButton)
    )

    clickButton(
        waitForObject(names.buttonsFrame_acceptButton_QPushButton)
    )


    # ============================================================
    # OPEN USER PRESETS
    # ============================================================

    test.log("Opening User Presets")

    clickTab(
        waitForObject(names.settingsScreen_tbSystemInfo_TabWidget),
        "TRÅDLØS FODKONTAKT"
    )

    clickTab(
        waitForObject(names.settingsScreen_tbSystemInfo_TabWidget),
        "FORUDINDSTILLI\nNGER FOR BRUGER"
    )

    sendEvent(
        "QMoveEvent",
        waitForObject(names.o_ScreenSwitcher),
        0,
        -66,
        1285,
        233
    )


    # ============================================================
    # ADD PRESET
    # ============================================================

    test.log("Clicking Add Preset")

    clickButton(
        waitForObject(names.settingsScreen_addButton_QPushButton)
    )


    # ============================================================
    # 1. ADD PRESET OPERATION
    # ============================================================

    actualText1 = str(
        waitForObjectExists(
            names.centralWidget_lbOperation_QLabel
        ).text
    )

    expectedText1 = str(
        sheet.cell(row=67, column=6).value
    )

    test.compare(
        actualText1,
        expectedText1,
        "Add Preset Operation"
    )


    # ============================================================
    # 2. PRESET NAME
    # ============================================================

    actualText2 = str(
        waitForObjectExists(
            names.centralWidget_pbName_QPushButton
        ).text
    )

    expectedText2 = str(
        sheet.cell(row=50, column=6).value
    )

    test.compare(
        actualText2,
        expectedText2,
        "Preset Name"
    )


    # ============================================================
    # 3. AVERAGE POWER
    # ============================================================

    actualText3 = str(
        waitForObjectExists(
            names.averagePowerWidget_nameLabel_QLabel
        ).text
    )

    expectedText3 = str(
        sheet.cell(row=6, column=6).value
    )

    test.compare(
        actualText3,
        expectedText3,
        "Average Power"
    )


    # ============================================================
    # 4. AVERAGE POWER UNIT
    # ============================================================

    actualText4 = str(
        waitForObjectExists(
            names.averagePowerWidget_unitsOfMeasureLabel_QLabel
        ).text
    )

    expectedText4 = str(
        sheet.cell(row=7, column=6).value
    )

    test.compare(
        actualText4,
        expectedText4,
        "Average Power Unit"
    )


    # ============================================================
    # 5. PULSE ENERGY
    # ============================================================

    actualText5 = str(
        waitForObjectExists(
            names.pulseEnergyWidget_nameLabel_QLabel
        ).text
    )

    expectedText5 = str(
        sheet.cell(row=8, column=6).value
    )

    test.compare(
        actualText5,
        expectedText5,
        "Pulse Energy"
    )


    # ============================================================
    # 6. PULSE ENERGY UNIT
    # ============================================================

    mouseClick(
        waitForObject(names.centralWidget_frame_QFrame),
        271,
        13,
        Qt.NoModifier,
        Qt.LeftButton
    )

    actualText6 = str(
        waitForObjectExists(
            names.pulseEnergyWidget_unitsOfMeasureLabel_QLabel
        ).text
    )

    expectedText6 = str(
        sheet.cell(row=9, column=6).value
    )

    test.compare(
        actualText6,
        expectedText6,
        "Pulse Energy Unit"
    )


    # ============================================================
    # 7. FREQUENCY
    # ============================================================

    actualText7 = str(
        waitForObjectExists(
            names.frequencyWidget_nameLabel_QLabel
        ).text
    )

    expectedText7 = str(
        sheet.cell(row=10, column=6).value
    )

    test.compare(
        actualText7,
        expectedText7,
        "Frequency"
    )


    # ============================================================
    # 8. FREQUENCY UNIT
    # ============================================================

    actualText8 = str(
        waitForObjectExists(
            names.frequencyWidget_unitsOfMeasureLabel_QLabel
        ).text
    )

    expectedText8 = str(
        sheet.cell(row=11, column=6).value
    )

    test.compare(
        actualText8,
        expectedText8,
        "Frequency Unit"
    )


    # ============================================================
    # 9. REGULAR PULSE
    # ============================================================

    actualText9 = str(
        waitForObjectExists(
            names.modeButton_nameLabel_QLabel_3
        ).text
    )

    expectedText9 = str(
        sheet.cell(row=33, column=6).value
    )

    test.compare(
        actualText9,
        expectedText9,
        "Regular Pulse"
    )


    # ============================================================
    # 10. PEAK POWER
    # ============================================================

    actualText10 = str(
        waitForObjectExists(
            names.peakPowerButton_nameLabel_QLabel_2
        ).text
    )

    expectedText10 = str(
        sheet.cell(row=12, column=6).value
    )

    test.compare(
        actualText10,
        expectedText10,
        "Peak Power"
    )


    # ============================================================
    # 11. ADD BUTTON
    # ============================================================

    actualText11 = str(
        waitForObjectExists(
            names.pulseModeWidget_saveButton_QPushButton
        ).text
    )

    expectedText11 = str(
        sheet.cell(row=68, column=6).value
    )

    test.compare(
        actualText11,
        expectedText11,
        "Add Button"
    )


    # ============================================================
    # ENTER PRESET NAME
    # ============================================================

    mouseClick(
        waitForObject(names.pulseModeWidget_buttonsWidget_QWidget),
        508,
        46,
        Qt.NoModifier,
        Qt.LeftButton
    )

    mouseClick(
        waitForObject(names.pulseModeWidget_buttonsWidget_QWidget),
        411,
        1,
        Qt.NoModifier,
        Qt.LeftButton
    )

    clickButton(
        waitForObject(names.centralWidget_pbName_QPushButton)
    )

    type(
        waitForObject(names.keyboardPopup_wdEdit_WdLineEdit),
        "preset one"
    )

    mouseClick(
        waitForObject(names.keyboardPopup_lbText_QLabel),
        77,
        26,
        Qt.NoModifier,
        Qt.LeftButton
    )

    clickButton(
        waitForObject(names.pulseModeWidget_saveButton_QPushButton)
    )


    # ============================================================
    # SELECT PRESET
    # ============================================================

    mouseClick(
        waitForObject(
            names.tabSettingsPresetsUserStonePresets_presetListView_PresetListView
        ),
        546,
        72,
        Qt.NoModifier,
        Qt.LeftButton
    )


    # ============================================================
    # EDIT PRESET
    # ============================================================

    clickButton(
        waitForObject(names.settingsScreen_editButton_QPushButton)
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


    # ============================================================
    # EDIT OPERATION
    # ============================================================

    actualEditOperation = str(
        waitForObjectExists(
            names.centralWidget_lbOperation_QLabel
        ).text
    )

    expectedEditOperation = str(
        sheet.cell(row=73, column=6).value
    )

    test.compare(
        actualEditOperation,
        expectedEditOperation,
        "Edit Preset Operation"
    )


    # ============================================================
    # EDIT PRESET NAME
    # ============================================================

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


    # ============================================================
    # EDIT - AVERAGE POWER
    # ============================================================

    actualEditAveragePower = str(
        waitForObjectExists(
            names.averagePowerWidget_nameLabel_QLabel
        ).text
    )

    expectedEditAveragePower = str(
        sheet.cell(row=6, column=6).value
    )

    test.compare(
        actualEditAveragePower,
        expectedEditAveragePower,
        "Edit - Average Power"
    )


    # ============================================================
    # EDIT - AVERAGE POWER UNIT
    # ============================================================

    actualEditAveragePowerUnit = str(
        waitForObjectExists(
            names.averagePowerWidget_unitsOfMeasureLabel_QLabel
        ).text
    )

    expectedEditAveragePowerUnit = str(
        sheet.cell(row=7, column=6).value
    )

    test.compare(
        actualEditAveragePowerUnit,
        expectedEditAveragePowerUnit,
        "Edit - Average Power Unit"
    )


    # ============================================================
    # EDIT - PULSE ENERGY
    # ============================================================

    actualEditPulseEnergy = str(
        waitForObjectExists(
            names.pulseEnergyWidget_nameLabel_QLabel
        ).text
    )

    expectedEditPulseEnergy = str(
        sheet.cell(row=8, column=6).value
    )

    test.compare(
        actualEditPulseEnergy,
        expectedEditPulseEnergy,
        "Edit - Pulse Energy"
    )


    # ============================================================
    # EDIT - PULSE ENERGY UNIT
    # ============================================================

    actualEditPulseEnergyUnit = str(
        waitForObjectExists(
            names.pulseEnergyWidget_unitsOfMeasureLabel_QLabel
        ).text
    )

    expectedEditPulseEnergyUnit = str(
        sheet.cell(row=9, column=6).value
    )

    test.compare(
        actualEditPulseEnergyUnit,
        expectedEditPulseEnergyUnit,
        "Edit - Pulse Energy Unit"
    )


    # ============================================================
    # EDIT - FREQUENCY
    # ============================================================

    actualEditFrequency = str(
        waitForObjectExists(
            names.frequencyWidget_nameLabel_QLabel
        ).text
    )

    expectedEditFrequency = str(
        sheet.cell(row=10, column=6).value
    )

    test.compare(
        actualEditFrequency,
        expectedEditFrequency,
        "Edit - Frequency"
    )


    # ============================================================
    # EDIT - FREQUENCY UNIT
    # ============================================================

    actualEditFrequencyUnit = str(
        waitForObjectExists(
            names.frequencyWidget_unitsOfMeasureLabel_QLabel
        ).text
    )

    expectedEditFrequencyUnit = str(
        sheet.cell(row=11, column=6).value
    )

    test.compare(
        actualEditFrequencyUnit,
        expectedEditFrequencyUnit,
        "Edit - Frequency Unit"
    )


    # ============================================================
    # EDIT - REGULAR PULSE
    # ============================================================

    actualEditRegularPulse = str(
        waitForObjectExists(
            names.modeButton_nameLabel_QLabel_3
        ).text
    )

    expectedEditRegularPulse = str(
        sheet.cell(row=33, column=6).value
    )

    test.compare(
        actualEditRegularPulse,
        expectedEditRegularPulse,
        "Edit - Regular Pulse"
    )


    # ============================================================
    # EDIT - PEAK POWER
    # ============================================================

    actualEditPeakPower = str(
        waitForObjectExists(
            names.peakPowerButton_nameLabel_QLabel_2
        ).text
    )

    expectedEditPeakPower = str(
        sheet.cell(row=12, column=6).value
    )

    test.compare(
        actualEditPeakPower,
        expectedEditPeakPower,
        "Edit - Peak Power"
    )


    # ============================================================
    # UPDATE BUTTON
    # ============================================================

    actualUpdateButton = str(
        waitForObjectExists(
            names.pulseModeWidget_saveButton_QPushButton
        ).text
    )

    expectedUpdateButton = str(
        sheet.cell(row=69, column=6).value
    )

    test.compare(
        actualUpdateButton,
        expectedUpdateButton,
        "Update Button"
    )


    # ============================================================
    # SAVE EDITED PRESET
    # ============================================================

    mouseClick(
        waitForObject(names.pulseModeWidget_buttonsWidget_QWidget),
        531,
        22,
        Qt.NoModifier,
        Qt.LeftButton
    )

    mouseClick(
        waitForObject(names.pulseModeWidget_buttonsWidget_QWidget),
        509,
        30,
        Qt.NoModifier,
        Qt.LeftButton
    )

    clickButton(
        waitForObject(names.pulseModeWidget_saveButton_QPushButton)
    )


    # ============================================================
    # DELETE PRESET
    # ============================================================

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


    # ============================================================
    # DELETE DIALOG TITLE
    # ============================================================

    actualDeleteTitle = str(
        waitForObjectExists(
            names.centralWidget_lbDialogTitle_QLabel
        ).text
    )

    expectedDeleteTitle = str(
        sheet.cell(row=74, column=6).value
    )

    test.compare(
        actualDeleteTitle,
        expectedDeleteTitle,
        "Delete Dialog Title"
    )


    # ============================================================
    # DELETE PRESET NAME
    # ============================================================

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


    # ============================================================
    # PRESET INFORMATION
    # ============================================================

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


    # ============================================================
    # CANCEL BUTTON
    # ============================================================

    actualCancel = str(
        waitForObjectExists(
            names.buttonsFrame_rejectButton_QPushButton
        ).text
    )

    expectedCancel = str(
        sheet.cell(row=71, column=6).value
    )

    test.compare(
        actualCancel,
        expectedCancel,
        "Cancel Button"
    )


    # ============================================================
    # DELETE BUTTON
    # ============================================================

    actualDelete = str(
        waitForObjectExists(
            names.centralWidget_acceptButton_QPushButton
        ).text
    )

    expectedDelete = str(
        sheet.cell(row=72, column=6).value
    )

    test.compare(
        actualDelete,
        expectedDelete,
        "Delete Button"
    )


    # ============================================================
    # CLOSE EXCEL
    # ============================================================

    workbook.close()

    test.log(
        "Danish Peak Power - Soft Tissue localization "
        "verification completed"
    )