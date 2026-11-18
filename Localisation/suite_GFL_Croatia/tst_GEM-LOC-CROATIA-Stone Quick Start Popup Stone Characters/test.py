
# -*- coding: utf-8 -*-

import names
import openpyxl
import re
import unicodedata
import html
import os


def normalize(text):
    if text is None:
        return ""

    text = html.unescape(str(text))
    text = re.sub(r"<br\s*/?>", " ", text, flags=re.IGNORECASE)
    text = re.sub(r"<[^>]+>", " ", text)
    text = unicodedata.normalize("NFKC", text)

    text = text.replace("\xa0", " ")
    text = text.replace("\u2007", " ")
    text = text.replace("\u202f", " ")
    text = text.replace("\r", " ")
    text = text.replace("\n", " ")
    text = text.replace("\t", " ")

    text = text.replace("™", "")
    text = text.replace("®", "")
    text = text.replace("©", "")

    return " ".join(text.split()).strip().casefold()


def comparison_key(text):
    return re.sub(r"\s+", "", normalize(text))


def load_croatia_excel(excelpath):
    if not os.path.isfile(excelpath):
        test.fail("Excel file not found: " + excelpath)
        return None, {}

    workbook = openpyxl.load_workbook(
        excelpath,
        data_only=True,
        read_only=True
    )

    if "Treatment Modes" not in workbook.sheetnames:
        workbook.close()
        test.fail(
            "Worksheet 'Treatment Modes' does not exist in Excel file"
        )
        return None, {}

    sheet = workbook["Treatment Modes"]

    english_column = 2
    croatia_column = 4

    croatia_data = {}

    for row in sheet.iter_rows(
        min_col=english_column,
        max_col=croatia_column
    ):
        english_value = row[0].value
        croatia_value = row[croatia_column - english_column].value

        if english_value is None or croatia_value is None:
            continue

        english_key = comparison_key(english_value)
        translated_value = str(croatia_value).strip()

        if english_key and translated_value:
            croatia_data[english_key] = translated_value

    return workbook, croatia_data


def get_croatia_text(croatia_data, english_text):
    return croatia_data.get(
        comparison_key(english_text),
        ""
    )


def verify_text(croatia_data, object_name, english_text):
    try:
        obj = waitForObjectExists(object_name)
        actual_text = str(obj.text).strip()

    except Exception as e:
        test.fail(
            "Unable to read application object: "
            + str(object_name)
            + " | Error: "
            + str(e)
        )
        return False

    expected_text = get_croatia_text(
        croatia_data,
        english_text
    )

    if not expected_text:
        test.fail(
            "English text not found in Excel column B or croatia "
            "translation is empty in column C: "
            + str(english_text)
        )
        return False

    actual_normalized = comparison_key(actual_text)
    expected_normalized = comparison_key(expected_text)

    test.compare(
        actual_normalized,
        expected_normalized,
        "croatia text verification: "
        + str(english_text)
        
    )

    return actual_normalized == expected_normalized


def main():
    excelpath = (
        "/home/ezen/Test_Automation_Gemini/Localisation/"
        "suite_GFL_Bulgaria/"
        "tst_GEM-LOC-Bulgaria-PeakPower-SoftTissueCharacters/"
        "testdata/Gemini Split strings.xlsx"
    )

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
