# # -*- coding: utf-8 -*-
#
# import names
#
#
# def main():
#     clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
#     clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
#     clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
#     clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
#     clickButton(waitForObject(names.mainFrame_okButton_QPushButton))
#     clickButton(waitForObject(names.homeScreen_settingsButton_QPushButton))
#     clickTab(waitForObject(names.settingsScreen_tbSystemInfo_TabWidget), "INFO")
#     clickButton(waitForObject(names.gbSystemInformation_pbLanguageSettingsUpdate_QPushButton))
#     clickButton(waitForObject(names.languagesFrame_pbCzech_QPushButton))
#     clickButton(waitForObject(names.buttonsFrame_acceptButton_QPushButton))
#     clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
#     clickButton(waitForObject(names.homeScreen_pbSoftTissueQuickStart_QToolButton))
#     mouseClick(waitForObjectItem(names.tabLeftMainPresets_leftPresetsView_PresetListView, "_1"), 238, 58, Qt.NoModifier, Qt.LeftButton)
#     mouseClick(waitForObjectItem(names.tabRightMainPresets_rightPresetsView_PresetListView, "_1"), 148, 32, Qt.NoModifier, Qt.LeftButton)
#     mouseClick(waitForObject(names.quickStartScreen_wdBottom_QWidget), 1167, 9, Qt.NoModifier, Qt.LeftButton)
#     sendEvent("QMoveEvent", waitForObject(names.o_ScreenSwitcher), 0, -51, 1286, 61)
#     clickButton(waitForObject(names.quickStartScreen_pbContinue_QPushButton))
#     clickButton(waitForObject(names.mainFrame_okButton_QPushButton_2))
#     clickButton(waitForObject(names.stateSwitch_readyButton_QPushButton))
#     test.compare(waitForObjectExists(names.eNUKLEACE_PROSTATY_VYSOK_ENERGIE_TabItem).text, "ENUKLEACE PROSTATY-(VYSOKÁ ENERGIE)")
#     test.compare(str(waitForObjectExists(names.averagePowerWidgetEmission_nameLabel_QLabel).text), "PRŮMĚRNÝ\nVÝKON")
#     test.compare(str(waitForObjectExists(names.frequencyWidgetEmission_nameLabel_QLabel).text), "FREKVENCE")
#     test.compare(str(waitForObjectExists(names.averagePowerWidgetEmission_unitsOfMeasureLabel_QLabel).text), "W")
#     test.compare(str(waitForObjectExists(names.pulseEnergyWidgetEmission_unitsOfMeasureLabel_QLabel).text), "J")
#     test.compare(str(waitForObjectExists(names.frequencyWidgetEmission_unitsOfMeasureLabel_QLabel).text), "Hz")
#     clickButton(waitForObject(names.stateSwitch_readyButton_QPushButton))
#     test.compare(str(waitForObjectExists(names.modeButtonEmission_nameLabel_QLabel).text), "BĚŽNÝ\nIMPULS")
#     test.compare(str(waitForObjectExists(names.peakPowerButtonEmission_nameLabel_QLabel).text), "ŠPIČKOVÝ\nVÝKON")
#     test.compare(str(waitForObjectExists(names.totalEnergyFrame_nameLabel_QLabel).text), "CELKOVÁ\nENERGIE")
#     test.compare(str(waitForObjectExists(names.totalTimeFrame_nameLabel_QLabel).text), "CELKOVÁ DOBA\nLASEROVÁNÍ")
#     test.compare(waitForObjectExists(names.eNUKLEACE_PROSTATY_VYSOK_ENERGIE_TabItem_2).text, "ENUKLEACE PROSTATY-(VYSOKÁ ENERGIE)")
#     test.compare(str(waitForObjectExists(names.averagePowerWidgetEmission_nameLabel_QLabel_2).text), "PRŮMĚRNÝ\nVÝKON")
#     clickButton(waitForObject(names.stateSwitch_readyButton_QPushButton))
#     test.compare(str(waitForObjectExists(names.pulseEnergyWidgetEmission_nameLabel_QLabel_2).text), "PULSNÍ\nENERGIE")
#     test.compare(str(waitForObjectExists(names.frequencyWidgetEmission_nameLabel_QLabel_2).text), "FREKVENCE")
#     test.compare(str(waitForObjectExists(names.averagePowerWidgetEmission_unitsOfMeasureLabel_QLabel_2).text), "W")
#     test.compare(str(waitForObjectExists(names.pulseEnergyWidgetEmission_unitsOfMeasureLabel_QLabel_2).text), "J")
#     test.compare(str(waitForObjectExists(names.frequencyWidgetEmission_unitsOfMeasureLabel_QLabel_2).text), "Hz")
#     test.compare(str(waitForObjectExists(names.peakPowerButtonEmission_nameLabel_QLabel_2).text), "ŠPIČKOVÝ\nVÝKON")
#     clickButton(waitForObject(names.stateSwitch_readyButton_QPushButton))
#     test.compare(str(waitForObjectExists(names.modeButtonEmission_nameLabel_QLabel_2).text), "BĚŽNÝ\nIMPULS")
#     test.compare(str(waitForObjectExists(names.fiberFrame_nameLabel_QLabel).text), "VLÁKNO")
#     test.compare(str(waitForObjectExists(names.fiberUsesFrame_nameLabel_QLabel).text), "ZBÝVAJÍCÍ\nPOUŽITÍ")
#     test.compare(str(waitForObjectExists(names.bottomBar_aimingBeamButton_AimingBeamModeButton).text), "Zaměřovací\npaprsek")
#     test.compare(str(waitForObjectExists(names.stateSwitch_standbyButton_QPushButton).text), "POHOTOVOSTNÍ REŽIM")
#     test.compare(str(waitForObjectExists(names.stateSwitch_readyButton_QPushButton).text), "PŘIPRAVENO")

# -*- coding: utf-8 -*-

import names
import openpyxl
from openpyxl import load_workbook


# ============================================================
# EXCEL FILE
# ============================================================

EXCEL_PATH = (
    "/home/ezen/Test_Automation_Gemini/Localisation/"
    "suite_GFL_Czech/"
    "tst_GEM-LOC-CZECH-Ready Screen/"
    "testdata/Ready Screen Czech.xlsx"
)


# ============================================================
# NORMALIZE TEXT
# ============================================================

def normalize_text(value):

    if value is None:
        return ""

    return " ".join(str(value).split())


# ============================================================
# GET EXPECTED TEXT FROM EXCEL
# ============================================================

def get_expected_text(sheet, excel_row):

    value = sheet.cell(
        row=excel_row,
        column=2
    ).value

    return normalize_text(value)


# ============================================================
# VERIFY OBJECT TEXT AGAINST EXCEL
# ============================================================

def verify_text(sheet, object_name, excel_row, description):

    # --------------------------------------------------------
    # Wait before every verification
    # --------------------------------------------------------

    snooze(2)

    test.log("======================================")
    test.log(
        "Starting verification: " +
        description
    )

    # --------------------------------------------------------
    # Get object from Object Map
    # --------------------------------------------------------

    obj = waitForObjectExists(
        getattr(names, object_name)
    )

    # --------------------------------------------------------
    # Get actual text
    # --------------------------------------------------------

    actual_text = normalize_text(
        obj.text
    )

    # --------------------------------------------------------
    # Get expected text from Excel
    # --------------------------------------------------------

    expected_text = get_expected_text(
        sheet,
        excel_row
    )

    # --------------------------------------------------------
    # Log values
    # --------------------------------------------------------

    test.log(
        "Excel Row : " +
        str(excel_row)
    )

    test.log(
        "Expected  : " +
        expected_text
    )

    test.log(
        "Actual    : " +
        actual_text
    )

    # --------------------------------------------------------
    # Compare
    # --------------------------------------------------------

    test.compare(
        actual_text,
        expected_text,
        description + " text verification"
    )

    test.log(
        "Completed : " +
        description
    )


# ============================================================
# MAIN
# ============================================================

def main():

    # ========================================================
    # LOAD EXCEL
    # ========================================================

    test.log("======================================")
    test.log("LOADING CZECH EXCEL TEST DATA")
    test.log("======================================")

    test.log(
        "Excel Path: " +
        EXCEL_PATH
    )

    workbook = load_workbook(
        EXCEL_PATH
    )

    sheet = workbook["Sheet1"]

    test.log(
        "Excel file loaded successfully"
    )


    # ========================================================
    # LOGIN / NUMPAD
    # ========================================================

    test.log("======================================")
    test.log("STARTING LOGIN")
    test.log("======================================")

    for i in range(4):

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

    snooze(2)


    # ========================================================
    # OPEN SETTINGS
    # ========================================================

    test.log(
        "Opening Settings"
    )

    clickButton(
        waitForObject(
            names.homeScreen_settingsButton_QPushButton
        )
    )

    snooze(2)


    # ========================================================
    # OPEN SYSTEM INFORMATION
    # ========================================================

    test.log(
        "Opening System Information"
    )

    clickTab(
        waitForObject(
            names.settingsScreen_tbSystemInfo_TabWidget
        ),
        "INFO"
    )

    snooze(2)


    # ========================================================
    # LANGUAGE SETTINGS
    # ========================================================

    test.log(
        "Opening Language Settings"
    )

    clickButton(
        waitForObject(
            names.gbSystemInformation_pbLanguageSettingsUpdate_QPushButton
        )
    )

    snooze(2)

    test.log(
        "Selecting Czech language"
    )

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
    # RETURN TO HOME
    # ========================================================

    test.log(
        "Returning to Home"
    )

    clickButton(
        waitForObject(
            names.buttonsBar_homeButton_QPushButton
        )
    )

    snooze(2)


    # ========================================================
    # SOFT TISSUE QUICK START
    # ========================================================

    test.log(
        "Opening Soft Tissue Quick Start"
    )

    clickButton(
        waitForObject(
            names.homeScreen_pbSoftTissueQuickStart_QToolButton
        )
    )

    snooze(2)


    # ========================================================
    # SELECT LEFT TREATMENT
    # ========================================================

    test.log(
        "Selecting Left Treatment"
    )

    mouseClick(
        waitForObjectItem(
            names.tabLeftMainPresets_leftPresetsView_PresetListView,
            "_1"
        ),
        238,
        58,
        Qt.NoModifier,
        Qt.LeftButton
    )

    snooze(2)


    # ========================================================
    # SELECT RIGHT TREATMENT
    # ========================================================

    test.log(
        "Selecting Right Treatment"
    )

    mouseClick(
        waitForObjectItem(
            names.tabRightMainPresets_rightPresetsView_PresetListView,
            "_1"
        ),
        148,
        32,
        Qt.NoModifier,
        Qt.LeftButton
    )

    snooze(2)


    # ========================================================
    # QUICK START BOTTOM WIDGET
    # ========================================================

    test.log(
        "Adjusting Quick Start Screen"
    )

    mouseClick(
        waitForObject(
            names.quickStartScreen_wdBottom_QWidget
        ),
        1167,
        9,
        Qt.NoModifier,
        Qt.LeftButton
    )

    snooze(2)


    # ========================================================
    # MOVE SCREEN
    # ========================================================

    sendEvent(
        "QMoveEvent",
        waitForObject(
            names.o_ScreenSwitcher
        ),
        0,
        -51,
        1286,
        61
    )

    snooze(2)


    # ========================================================
    # CONTINUE
    # ========================================================

    test.log(
        "Clicking Continue"
    )

    clickButton(
        waitForObject(
            names.quickStartScreen_pbContinue_QPushButton
        )
    )

    snooze(2)


    # ========================================================
    # OK
    # ========================================================

    clickButton(
        waitForObject(
            names.mainFrame_okButton_QPushButton_2
        )
    )

    snooze(2)


    # ========================================================
    # READY STATE
    # ========================================================

    test.log(
        "Selecting Ready State"
    )

    clickButton(
        waitForObject(
            names.stateSwitch_readyButton_QPushButton
        )
    )

    snooze(2)


    # ========================================================
    # LEFT SIDE VERIFICATION
    # ========================================================

    test.log("======================================")
    test.log("STARTING LEFT SIDE VERIFICATION")
    test.log("======================================")


    # --------------------------------------------------------
    # LEFT TREATMENT NAME
    # Excel Row 2
    # --------------------------------------------------------

    verify_text(
        sheet,
        "eNUKLEACE_PROSTATY_VYSOK_ENERGIE_TabItem",
        2,
        "Left Treatment Name"
    )


    # --------------------------------------------------------
    # LEFT AVERAGE POWER
    # Excel Row 3
    # --------------------------------------------------------

    verify_text(
        sheet,
        "averagePowerWidgetEmission_nameLabel_QLabel",
        3,
        "Left Average Power"
    )


    # --------------------------------------------------------
    # LEFT PULSE ENERGY
    # Excel Row 4
    # --------------------------------------------------------

    verify_text(
        sheet,
        "pulseEnergyWidgetEmission_nameLabel_QLabel",
        4,
        "Left Pulse Energy"
    )


    # --------------------------------------------------------
    # LEFT FREQUENCY
    # Excel Row 5
    # --------------------------------------------------------

    verify_text(
        sheet,
        "frequencyWidgetEmission_nameLabel_QLabel",
        5,
        "Left Frequency"
    )


    # --------------------------------------------------------
    # LEFT PULSE MODE
    # Excel Row 6
    # --------------------------------------------------------

    verify_text(
        sheet,
        "modeButtonEmission_nameLabel_QLabel",
        6,
        "Left Pulse Mode"
    )


    # --------------------------------------------------------
    # LEFT PEAK POWER
    # Excel Row 7
    # --------------------------------------------------------

    verify_text(
        sheet,
        "peakPowerButtonEmission_nameLabel_QLabel",
        7,
        "Left Peak Power"
    )


    # --------------------------------------------------------
    # LEFT TOTAL ENERGY
    # Excel Row 8
    # --------------------------------------------------------

    verify_text(
        sheet,
        "totalEnergyFrame_nameLabel_QLabel",
        8,
        "Left Total Energy"
    )


    # --------------------------------------------------------
    # LEFT TOTAL TIME
    # Excel Row 9
    # --------------------------------------------------------

    verify_text(
        sheet,
        "totalTimeFrame_nameLabel_QLabel",
        9,
        "Left Total Time"
    )


    # --------------------------------------------------------
    # LEFT POWER UNIT
    # Excel Row 10
    # --------------------------------------------------------

    verify_text(
        sheet,
        "averagePowerWidgetEmission_unitsOfMeasureLabel_QLabel",
        10,
        "Left Power Unit"
    )


    # --------------------------------------------------------
    # LEFT ENERGY UNIT
    # Excel Row 11
    # --------------------------------------------------------

    verify_text(
        sheet,
        "pulseEnergyWidgetEmission_unitsOfMeasureLabel_QLabel",
        11,
        "Left Energy Unit"
    )


    # --------------------------------------------------------
    # LEFT FREQUENCY UNIT
    # Excel Row 12
    # --------------------------------------------------------

    verify_text(
        sheet,
        "frequencyWidgetEmission_unitsOfMeasureLabel_QLabel",
        12,
        "Left Frequency Unit"
    )


    # --------------------------------------------------------
    # LEFT FIBER
    # Excel Row 13
    # --------------------------------------------------------

    verify_text(
        sheet,
        "fiberFrame_nameLabel_QLabel",
        13,
        "Left Fiber"
    )


    # --------------------------------------------------------
    # LEFT FIBER VALUE
    # Excel Row 14
    # --------------------------------------------------------

    verify_text(
        sheet,
        "fiberUsesFrame_nameLabel_QLabel",
        14,
        "Left Remaining Uses"
    )


    # --------------------------------------------------------
    # LEFT AIMING BEAM
    # Excel Row 15
    # --------------------------------------------------------

    verify_text(
        sheet,
        "bottomBar_aimingBeamButton_AimingBeamModeButton",
        15,
        "Left Aiming Beam"
    )


    # --------------------------------------------------------
    # LEFT STANDBY
    # Excel Row 16
    # --------------------------------------------------------

    verify_text(
        sheet,
        "stateSwitch_standbyButton_QPushButton",
        16,
        "Left Standby"
    )


    # --------------------------------------------------------
    # LEFT READY
    # Excel Row 17
    # --------------------------------------------------------

    verify_text(
        sheet,
        "stateSwitch_readyButton_QPushButton",
        17,
        "Left Ready"
    )


    test.log("======================================")
    test.log("LEFT SIDE VERIFICATION COMPLETED")
    test.log("======================================")


    # ========================================================
    # RIGHT SIDE VERIFICATION
    # ========================================================

    test.log("======================================")
    test.log("STARTING RIGHT SIDE VERIFICATION")
    test.log("======================================")


    # --------------------------------------------------------
    # RIGHT TREATMENT NAME
    # Excel Row 2
    # --------------------------------------------------------

    verify_text(
        sheet,
        "eNUKLEACE_PROSTATY_VYSOK_ENERGIE_TabItem_2",
        2,
        "Right Treatment Name"
    )


    # --------------------------------------------------------
    # RIGHT AVERAGE POWER
    # Excel Row 3
    # --------------------------------------------------------

    verify_text(
        sheet,
        "averagePowerWidgetEmission_nameLabel_QLabel_2",
        3,
        "Right Average Power"
    )


    # --------------------------------------------------------
    # RIGHT PULSE ENERGY
    # Excel Row 4
    # --------------------------------------------------------

    verify_text(
        sheet,
        "pulseEnergyWidgetEmission_nameLabel_QLabel_2",
        4,
        "Right Pulse Energy"
    )


    # --------------------------------------------------------
    # RIGHT FREQUENCY
    # Excel Row 5
    # --------------------------------------------------------

    verify_text(
        sheet,
        "frequencyWidgetEmission_nameLabel_QLabel_2",
        5,
        "Right Frequency"
    )


    # --------------------------------------------------------
    # RIGHT PULSE MODE
    # Excel Row 6
    # --------------------------------------------------------

    verify_text(
        sheet,
        "modeButtonEmission_nameLabel_QLabel_2",
        6,
        "Right Pulse Mode"
    )


    # --------------------------------------------------------
    # RIGHT PEAK POWER
    # Excel Row 7
    # --------------------------------------------------------

    verify_text(
        sheet,
        "peakPowerButtonEmission_nameLabel_QLabel_2",
        7,
        "Right Peak Power"
    )


    # --------------------------------------------------------
    # RIGHT POWER UNIT
    # Excel Row 10
    # --------------------------------------------------------

    verify_text(
        sheet,
        "averagePowerWidgetEmission_unitsOfMeasureLabel_QLabel_2",
        10,
        "Right Power Unit"
    )


    # --------------------------------------------------------
    # RIGHT ENERGY UNIT
    # Excel Row 11
    # --------------------------------------------------------

    verify_text(
        sheet,
        "pulseEnergyWidgetEmission_unitsOfMeasureLabel_QLabel_2",
        11,
        "Right Energy Unit"
    )


    # --------------------------------------------------------
    # RIGHT FREQUENCY UNIT
    # Excel Row 12
    # --------------------------------------------------------

    verify_text(
        sheet,
        "frequencyWidgetEmission_unitsOfMeasureLabel_QLabel_2",
        12,
        "Right Frequency Unit"
    )


    test.log("======================================")
    test.log("RIGHT SIDE VERIFICATION COMPLETED")
    test.log("======================================")


    # ========================================================
    # FINAL READY BUTTON
    # ========================================================

    clickButton(
        waitForObject(
            names.stateSwitch_readyButton_QPushButton
        )
    )

    snooze(2)


    # ========================================================
    # TEST COMPLETED
    # ========================================================

    test.log("======================================")
    test.log(
        "ALL LOCALIZATION TEXT VERIFICATION COMPLETED"
    )
    test.log("======================================")

    test.log(
        "Test case completed successfully"
    )


    # ========================================================
    # READY SCREEN IMAGE VERIFICATION
    # ========================================================

    test.log("======================================")
    test.log(
        "STARTING READY SCREEN IMAGE VERIFICATION"
    )
    test.log("======================================")

    test.imagePresent("Ready screen header image")


    # test.log(
    #     "Ready screen image is present"
    # )

    clickButton(waitForObject(names.stateSwitch_readyButton_QPushButton))
    test.vp("Readyscreen")

    

    test.log(
        "Whole screen verification completed"
    )

    

