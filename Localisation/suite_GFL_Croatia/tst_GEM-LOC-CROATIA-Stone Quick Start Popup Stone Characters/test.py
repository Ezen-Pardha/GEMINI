
# -*- coding: utf-8 -*-

import names
import croatian_localization as loc
import openpyxl
import re
import unicodedata
import html
import os


def normalize(text):
    return loc.normalize(text)


def comparison_key(text):
    return re.sub(r"\s+", "", normalize(text))


def load_croatia_excel(excelpath):
    workbook = openpyxl.load_workbook(loc.EXCEL_PATH, data_only=True, read_only=True)
    return workbook, {}


def get_croatia_text(croatia_data, english_text):
    return croatia_data.get(
        comparison_key(english_text),
        ""
    )


def verify_text(croatia_data, object_name, english_text):
    return loc.verify_object(object_name, english_text,
        "Stone Characteristics: " + english_text, globals(), trace_id="TB" if english_text.upper() in ("LOW", "MEDIUM", "HIGH") else None)


def main():
    excelpath = loc.EXCEL_PATH

    workbook = None

    try:
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

        
        # clickButton(waitForObject(names.buttonsFrame_acceptButton_QPushButton))
        # clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
        # clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
        # clickButton(waitForObject(names.locationFrame_kidneyPcnlLocationButton_QPushButton))
        # clickButton(waitForObject(names.flowRateFrame_lowFlowRateButton_QPushButton))
        # clickButton(waitForObject(names.hardnessFrame_smallHardnessButton_QPushButton))
        # clickButton(waitForObject(names.stoneAssistantModeScreen_continueButton_QPushButton))
        # clickButton(waitForObject(names.treatmentCharacteristicsBar_pbEdit_QPushButton_2))
        # test.compare(str(waitForObjectExists(names.centralWidget_titleLabel_QLabel).text), "SVOJSTVA KAMENCA")
        # test.compare(str(waitForObjectExists(names.centralWidget_titleLabel_QLabel_2).text), "LOKACIJA")
        # test.compare(str(waitForObjectExists(names.centralWidget_valueLabel_QLabel).text), "BUBREG (PCNL)")
        # test.compare(str(waitForObjectExists(names.centralWidget_titleLabel_QLabel_3).text), "BRZINA PROTOKA")
        # test.compare(str(waitForObjectExists(names.centralWidget_titleLabel_QLabel_3).text), "BRZINA PROTOKA")
        # test.compare(str(waitForObjectExists(names.centralWidget_valueLabel_QLabel_2).text), "MALA")
        # test.compare(str(waitForObjectExists(names.centralWidget_titleLabel_QLabel_4).text), "TVRDOĆA")
        # test.compare(str(waitForObjectExists(names.centralWidget_descriptionLabel_QLabel).text), "Hounsfieldova ljestvica < 500")
        # test.compare(str(waitForObjectExists(names.centralWidget_valueLabel_QLabel_3).text), "Mekan")
        # test.compare(str(waitForObjectExists(names.centralWidget_rejectButton_QPushButton).text), "UREDI")
        # test.compare(str(waitForObjectExists(names.centralWidget_acceptButton_QPushButton).text), "U REDU")

        clickButton(waitForObject(names.languagesFrame_pbCroatia_QPushButton))

        clickButton(
            waitForObject(names.buttonsFrame_acceptButton_QPushButton)
        )

        clickButton(
            waitForObject(names.buttonsBar_homeButton_QPushButton)
        )

        clickButton(
            waitForObject(names.homeScreen_pbStoneAssistant_QToolButton)
        )

        clickButton(
            waitForObject(
                names.locationFrame_kidneyPcnlLocationButton_QPushButton
            )
        )

        clickButton(
            waitForObject(
                names.flowRateFrame_lowFlowRateButton_QPushButton
            )
        )

        clickButton(
            waitForObject(
                names.hardnessFrame_smallHardnessButton_QPushButton
            )
        )

        clickButton(
            waitForObject(
                names.stoneAssistantModeScreen_continueButton_QPushButton
            )
        )

        clickButton(
            waitForObject(
                names.treatmentCharacteristicsBar_pbEdit_QPushButton_2
            )
        )

        workbook, croatia_data = load_croatia_excel(excelpath)

        if workbook is None:
            return

        verify_text(
            croatia_data,
            names.centralWidget_titleLabel_QLabel,
            "STONE CHARACTERISTICS"
        )

        verify_text(
            croatia_data,
            names.centralWidget_titleLabel_QLabel_2,
            "LOCATION"
        )

        verify_text(
            croatia_data,
            names.centralWidget_valueLabel_QLabel,
            "KIDNEY (PCNL)"
        )

        verify_text(
            croatia_data,
            names.centralWidget_titleLabel_QLabel_3,
            "FLOW RATE"
        )

        verify_text(
            croatia_data,
            names.centralWidget_valueLabel_QLabel_2,
            "LOW"
        )

        verify_text(
            croatia_data,
            names.centralWidget_titleLabel_QLabel_4,
            "HARDNESS"
        )

        verify_text(
            croatia_data,
            names.centralWidget_descriptionLabel_QLabel,
            "Hounsfield Scale < 500"
        )

        verify_text(
            croatia_data,
            names.centralWidget_valueLabel_QLabel_3,
            "SOFT"
        )

        verify_text(
            croatia_data,
            names.centralWidget_rejectButton_QPushButton,
            "EDIT"
        )

        verify_text(
            croatia_data,
            names.centralWidget_acceptButton_QPushButton,
            "OK"
        )

    finally:
        if workbook is not None:
            workbook.close()
