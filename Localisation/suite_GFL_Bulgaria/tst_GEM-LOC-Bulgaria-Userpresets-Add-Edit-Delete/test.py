
# -*- coding: utf-8 -*-

import names
from openpyxl import load_workbook
import re


# ============================================================
# NORMALIZE TEXT
# ============================================================

def normalize(text):

    if text is None:
        return ""

    text = str(text)

    text = re.sub(
        r"<br\s*/?>",
        " ",
        text,
        flags=re.IGNORECASE
    )

    text = re.sub(
        r"<[^>]+>",
        " ",
        text
    )

    text = text.replace("\xa0", " ")

    text = " ".join(text.split())

    return text.strip().casefold()


# ============================================================
# LOAD BULGARIAN EXCEL DATA
#
# Sheet       : Treatment Modes
# English     : Column B
# Bulgarian   : Column C
# ============================================================

def load_bulgarian_excel(excelpath):

    workbook = load_workbook(
        excelpath,
        read_only=True,
        data_only=True
    )

    if "Treatment Modes" not in workbook.sheetnames:

        workbook.close()

        test.fail(
            "Worksheet 'Treatment Modes' does not exist "
            "in Excel file"
        )

        return None, {}

    sheet = workbook["Treatment Modes"]

    english_column = 2
    bulgarian_column = 3

    bulgarian_data = {}

    for row in sheet.iter_rows(
        min_col=english_column,
        max_col=bulgarian_column
    ):

        english_value = row[0].value
        bulgarian_value = row[1].value

        if english_value is None:
            continue

        english_key = normalize(
            english_value
        )

        if english_key == "":
            continue

        if bulgarian_value is None:
            bulgarian_value = ""

        bulgarian_data[english_key] = str(
            bulgarian_value
        )

    return workbook, bulgarian_data


# ============================================================
# GET BULGARIAN TRANSLATION
# ============================================================

def get_bulgarian_text(
    bulgarian_data,
    english_text
):

    key = normalize(
        english_text
    )

    if key not in bulgarian_data:

        # test.fail(
        #     "English text not found in Excel: "
        #     + str(english_text)
        # )

        return ""

    return bulgarian_data[key]


# ============================================================
# VERIFY APPLICATION STRING AGAINST EXCEL
# ============================================================

def verify_excel_string(
    object_name,
    bulgarian_data,
    english_text,
    description
):

    snooze(6)

    try:

        actual = str(
            waitForObjectExists(
                object_name
            ).text
        ).strip()

    except Exception as e:

        test.fail(
            "Unable to read application object: "
            + str(object_name)
            + " | Error: "
            + str(e)
        )

        return

    expected = get_bulgarian_text(
        bulgarian_data,
        english_text
    )

    actual_normalized = normalize(
        actual
    )

    expected_normalized = normalize(
        expected
    )

    test.compare(
        actual_normalized,
        expected_normalized,
        description
    )

    # if actual_normalized != expected_normalized:
    #
    #     test.fail(
    #         "Bulgarian text mismatch | "
    #         + description
    #         + " | Actual: "
    #         + actual
    #         + " | Expected: "
    #         + expected
    #     )


# ============================================================
# MAIN
# ============================================================

def main():

    workbook = None

    # ========================================================
    # EXCEL FILE
    # ========================================================

    excelpath = (
        "/home/ezen/Test_Automation_Gemini/Localisation/"
        "suite_GFL_Bulgaria/"
        "tst_GEM-LOC-Bulgaria-Userpresets-Add-Edit-Delete/"
        "testdata/Gemini Split strings.xlsx"
    )


    # ========================================================
    # LOAD EXCEL
    # ========================================================

    workbook, bulgarian_data = (
        load_bulgarian_excel(
            excelpath
        )
    )

    if workbook is None:
        return


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
    # CHANGE LANGUAGE TO BULGARIAN
    # ========================================================

    clickButton(
        waitForObject(
            names.languagesFrame_pbBulgaria_QPushButton
        )
    )

    clickButton(
        waitForObject(
            names.buttonsFrame_acceptButton_QPushButton
        )
    )

    snooze(6)


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
    # SELECT TAB 3 AGAIN
    # ========================================================

    tabWidget.setCurrentIndex(2)

    snooze(3)


    # ========================================================
    # SCREEN SWITCHER
    # ========================================================

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
        bulgarian_data,
        "ADD PRESET",
        "Add Preset Operation"
    )


    # ========================================================
    # 2. PRESET NAME
    # ========================================================

    verify_excel_string(
        names.centralWidget_pbName_QPushButton,
        bulgarian_data,
        "PRESET NAME",
        "Preset Name"
    )


    # ========================================================
    # 3. AVERAGE POWER
    # ========================================================

    verify_excel_string(
        names.averagePowerWidget_nameLabel_QLabel,
        bulgarian_data,
        "AVERAGE POWER",
        "Average Power"
    )


    # ========================================================
    # 4. AVERAGE POWER UNIT
    # ========================================================

    verify_excel_string(
        names.averagePowerWidget_unitsOfMeasureLabel_QLabel,
        bulgarian_data,
        "W",
        "Average Power Unit"
    )


    # ========================================================
    # 5. PULSE ENERGY
    # ========================================================

    verify_excel_string(
        names.pulseEnergyWidget_nameLabel_QLabel,
        bulgarian_data,
        "PULSE ENERGY",
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
        bulgarian_data,
        "J",
        "Pulse Energy Unit"
    )


    # ========================================================
    # 7. FREQUENCY
    # ========================================================

    verify_excel_string(
        names.frequencyWidget_nameLabel_QLabel,
        bulgarian_data,
        "FREQUENCY",
        "Frequency"
    )


    # ========================================================
    # 8. FREQUENCY UNIT
    # ========================================================

    verify_excel_string(
        names.frequencyWidget_unitsOfMeasureLabel_QLabel,
        bulgarian_data,
        "Hz",
        "Frequency Unit"
    )


    # ========================================================
    # 9. REGULAR PULSE
    # ========================================================

    verify_excel_string(
        names.modeButton_nameLabel_QLabel_3,
        bulgarian_data,
        "REGULAR PULSE",
        "Regular Pulse"
    )


    # ========================================================
    # 10. PEAK POWER
    # ========================================================

    verify_excel_string(
        names.peakPowerButton_nameLabel_QLabel_2,
        bulgarian_data,
        "PEAK POWER",
        "Peak Power"
    )


    # ========================================================
    # 11. ADD BUTTON
    # ========================================================

    verify_excel_string(
        names.pulseModeWidget_saveButton_QPushButton,
        bulgarian_data,
        "ADD",
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

    snooze(6)


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

    snooze(6)


    # ========================================================
    # EDIT OPERATION
    # ========================================================

    verify_excel_string(
        names.centralWidget_lbOperation_QLabel,
        bulgarian_data,
        "EDIT PRESET",
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
        bulgarian_data,
        "AVERAGE POWER",
        "Edit - Average Power"
    )


    # ========================================================
    # EDIT - AVERAGE POWER UNIT
    # ========================================================

    verify_excel_string(
        names.averagePowerWidget_unitsOfMeasureLabel_QLabel,
        bulgarian_data,
        "W",
        "Edit - Average Power Unit"
    )


    # ========================================================
    # EDIT - PULSE ENERGY
    # ========================================================

    verify_excel_string(
        names.pulseEnergyWidget_nameLabel_QLabel,
        bulgarian_data,
        "PULSE ENERGY",
        "Edit - Pulse Energy"
    )


    # ========================================================
    # EDIT - PULSE ENERGY UNIT
    # ========================================================

    verify_excel_string(
        names.pulseEnergyWidget_unitsOfMeasureLabel_QLabel,
        bulgarian_data,
        "J",
        "Edit - Pulse Energy Unit"
    )


    # ========================================================
    # EDIT - FREQUENCY
    # ========================================================

    verify_excel_string(
        names.frequencyWidget_nameLabel_QLabel,
        bulgarian_data,
        "FREQUENCY",
        "Edit - Frequency"
    )


    # ========================================================
    # EDIT - FREQUENCY UNIT
    # ========================================================

    verify_excel_string(
        names.frequencyWidget_unitsOfMeasureLabel_QLabel,
        bulgarian_data,
        "Hz",
        "Edit - Frequency Unit"
    )


    # ========================================================
    # EDIT - REGULAR PULSE
    # ========================================================

    verify_excel_string(
        names.modeButton_nameLabel_QLabel_3,
        bulgarian_data,
        "REGULAR PULSE",
        "Edit - Regular Pulse"
    )


    # ========================================================
    # EDIT - PEAK POWER
    # ========================================================

    verify_excel_string(
        names.peakPowerButton_nameLabel_QLabel_2,
        bulgarian_data,
        "PEAK POWER",
        "Edit - Peak Power"
    )


    # ========================================================
    # UPDATE BUTTON
    # ========================================================

    verify_excel_string(
        names.pulseModeWidget_saveButton_QPushButton,
        bulgarian_data,
        "UPDATE",
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

    snooze(6)


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

    snooze(6)


    # ========================================================
    # DELETE DIALOG TITLE
    # ========================================================

    verify_excel_string(
        names.centralWidget_lbDialogTitle_QLabel,
        bulgarian_data,
        "DELETE PRESET",
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
        bulgarian_data,
        "CANCEL",
        "Cancel Button"
    )


    # ========================================================
    # DELETE BUTTON
    # ========================================================

    verify_excel_string(
        names.centralWidget_acceptButton_QPushButton,
        bulgarian_data,
        "DELETE",
        "Delete Button"
    )


    # ========================================================
    # CLOSE EXCEL
    # ========================================================

    if workbook is not None:
        workbook.close()

