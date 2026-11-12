
# -*- coding: utf-8 -*-

import names
import croatian_localization as loc
import openpyxl
import re
import os

TESTCASE_DIR = os.path.dirname(os.path.abspath(__file__))
 
EXCEL_PATH = loc.EXCEL_PATH



SHEET_NAME = "Treatment Modes"

# Column B = English
ENGLISH_COLUMN = 2

# Column D = Croatian
CROATIAN_COLUMN = 4




def normalize_text(value):

    if value is None:
        return ""

    value = str(value)

    # Remove HTML tags
    value = re.sub(r"<[^>]*>", "", value)

    # Replace line breaks with spaces
    value = value.replace("\n", " ")
    value = value.replace("\r", " ")

    # Normalize spaces
    value = " ".join(value.split())

    return value.strip().casefold()



def get_croatian_text(sheet, english_text):
    return loc.expected_text(english_text, "Treatment Modes")




def verify_text(sheet, object_name, english_text, description):
    return loc.verify_object(getattr(names, object_name), english_text, description,
                             globals(), "Treatment Modes")



def main():

  

   
    workbook = openpyxl.load_workbook(
        EXCEL_PATH,
        data_only=True,
        read_only=True
    )

    if SHEET_NAME not in workbook.sheetnames:

        test.fail(
            "Excel sheet not found: "
            + SHEET_NAME
        )

        workbook.close()
        return

    sheet = workbook[
        SHEET_NAME
    ]

    




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
            names.languagesFrame_pbCroatia_QPushButton
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


  

    clickButton(
        waitForObject(
            names.homeScreen_pbSoftTissueQuickStart_QToolButton
        )
    )




    mouseClick(
        waitForObjectItem(
            names.tabLeftMainPresets_leftPresetsView_PresetListView,
            "_1"
        ),
        289,
        45,
        Qt.NoModifier,
        Qt.LeftButton
    )




    mouseClick(
        waitForObjectItem(
            names.tabRightMainPresets_rightPresetsView_PresetListView,
            "_1"
        ),
        173,
        22,
        Qt.NoModifier,
        Qt.LeftButton
    )


    clickButton(
        waitForObject(
            names.quickStartScreen_pbContinue_QPushButton
        )
    )

    clickButton(
        waitForObject(
            names.mainFrame_okButton_QPushButton_2
        )
    )


    

    mouseClick(
        waitForObject(
            names.peakPowerButton_iconLabel_QLabel
        ),
        27,
        38,
        Qt.NoModifier,
        Qt.LeftButton
    )




    # test.compare(str(waitForObjectExists(names.centralWidget_lbTitle_QLabel).text), "ODABIR VRŠNE SNAGE")

    verify_text(
        sheet,
        "centralWidget_lbTitle_QLabel",
        "SELECT PEAK POWER",
        "Peak Power title"
    )

    verify_text(
        sheet,
        "centralWidget_pw500_QPushButton",
        "High",
        "High button"
    )

    verify_text(
        sheet,
        "centralWidget_pw250_QPushButton",
        "Medium",
        "Medium button"
    )

    verify_text(
        sheet,
        "centralWidget_pw125_QPushButton",
        "Low",
        "Low button"
    )

    verify_text(
        sheet,
        "buttonsFrame_rejectButton_QPushButton",
        "Cancel",
        "Cancel button"
    )


  

    clickButton(
        waitForObject(
            names.buttonsFrame_rejectButton_QPushButton
        )
    )

    clickButton(
        waitForObject(
            names.buttonsBar_homeButton_QPushButton_2
        )
    )


   
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


   

    clickButton(
        waitForObject(
            names.treatmentCharacteristicsBar_pbEdit_QPushButton
        )
    )

    mouseClick(
        waitForObject(
            names.centralWidget_QFrame
        ),
        495,
        191,
        Qt.NoModifier,
        Qt.LeftButton
    )

    mouseClick(
        waitForObject(
            names.centralWidget_titleLabel_QLabel
        ),
        0,
        24,
        Qt.NoModifier,
        Qt.LeftButton
    )


 

    verify_text(
        sheet,
        "centralWidget_titleLabel_QLabel",
        "Soft Tissue Characteristics",
        "Soft Tissue Characteristics title"
    )

    verify_text(
        sheet,
        "centralWidget_titleLabel_QLabel_2",
        "Procedure",
        "Procedure label"
    )

    verify_text(
        sheet,
        "centralWidget_valueLabel_QLabel",
        "Incision",
        "Procedure value"
    )

    verify_text(
        sheet,
        "centralWidget_rejectButton_QPushButton",
        "Edit",
        "Edit button"
    )

  

    verify_text(
        sheet,
        "centralWidget_acceptButton_QPushButton",
        "OK",
        "Accept button"
    )



    test.vp(
        "SoftTissueCharacters"
    )


  

    workbook.close()

    

