# -*- coding: utf-8 -*-

import names
import openpyxl
import re

# =========================================================

# Excel Configuration

# =========================================================

EXCEL_PATH = (
"/home/ezen/Test_Automation_Gemini/Localisation/"
"suite_GFL_Estonian/"
"tst_GEM-LOC-Estonian-PeakPower-SoftTissueCharacters/"
"testdata/Gemini Split strings.xlsx"
)

# Column B = English

# Column H = Estonian

ENGLISH_COLUMN = 2
ESTONIAN_COLUMN = 8

SHEET_NAME = "Soft tissue"

# =========================================================

# Normalize / Concatenate Text

# =========================================================

def normalize(text):


    if text is None:
        return ""
    
    text = str(text)
    
    # Remove HTML tags
    text = re.sub(
        r"<[^>]+>",
        "",
        text
    )
    
    # Remove all whitespace:
    # spaces
    # multiple spaces
    # new lines
    # tabs
    # carriage returns
    #
    # Example:
    #
    # KESKMINE VÕIMSUS
    # KESKMINE\nVÕIMSUS
    # KESKMINE   VÕIMSUS
    #
    # All become:
    #
    # KESKMINEVÕIMSUS
    
    text = re.sub(
        r"\s+",
        "",
        text
    )
    
    # Case-insensitive comparison
    return text.casefold()
    

# =========================================================

# Load Excel

# =========================================================

def load_excel():


    try:
    
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
    
            return None, None
    
        sheet = workbook[SHEET_NAME]
    
        return workbook, sheet
    
    except Exception as e:
    
        test.fail(
            "Unable to load Estonian localization Excel: "
            + str(e)
        )
    
        return None, None
    
    
# =========================================================

# Get Estonian Values From Excel

#

# English = Column B

# Estonian = Column H

#

# No hard-coded Excel row numbers

# =========================================================

def get_estonian_values(
sheet,
english_text
):


    expected_english = normalize(
        english_text
    )
    
    estonian_values = []
    
    for row in range(
        2,
        sheet.max_row + 1
    ):
    
        english_value = sheet.cell(
            row=row,
            column=ENGLISH_COLUMN
        ).value
    
        if english_value is None:
            continue
    
        # Compare concatenated English strings
        if normalize(
            english_value
        ) == expected_english:
    
            estonian_value = sheet.cell(
                row=row,
                column=ESTONIAN_COLUMN
            ).value
    
            if estonian_value is not None:
    
                estonian_value = str(
                    estonian_value
                ).strip()
    
                if estonian_value:
    
                    estonian_values.append(
                        estonian_value
                    )
    
    return estonian_values
    

# =========================================================

# Verify UI Text Against Excel

# =========================================================

def verify_text(
sheet,
object_name,
english_text,
description
):

    # Wait before verification
    snooze(6)
    
    try:
    
        obj = waitForObjectExists(
            object_name
        )
    
        actual_value = obj.text
    
        if actual_value is None:
            actual = ""
        else:
            actual = str(
                actual_value
            )
    
    except Exception as e:
    
        test.fail(
            description
            + " | Unable to read object: "
            + str(e)
        )
    
        return
    
    
# =====================================================
# Get Estonian translation from Excel
# =====================================================

    expected_values = get_estonian_values(
        sheet,
        english_text
    )


# =====================================================
# English string not found
# =====================================================

    if not expected_values:
    
        test.fail(
            description
            + " | English string not found in Column B: "
            + english_text
        )
    
        return


# =====================================================
# CONCATENATE UI STRING
# =====================================================

    actual_normalized = normalize(
        actual
    )


# =====================================================
# Compare concatenated UI string
# against concatenated Excel string
# =====================================================

    for expected in expected_values:
    
        expected_normalized = normalize(
            expected
        )
    
        if actual_normalized == expected_normalized:
    
            test.compare(
                actual_normalized,
                expected_normalized,
                description
            )
    
            return
    
    
# =====================================================
# Verification Failed
# =====================================================

    test.fail(
        description
        + " | Expected Estonian value from Column H: "
        + " / ".join(
            expected_values
        )
        + " | Actual: "
        + actual
    )


# =========================================================

# Get Visible centralWidget

# =========================================================

def get_central_widget():


    try:
    
        central_widget = findObject(
            {
                "name": "centralWidget",
                "type": "QFrame",
                "window": ":o_ScreenSwitcher"
            }
        )
    
        for i in range(20):
    
            try:
    
                if central_widget.visible:
                    return central_widget
    
            except:
                pass
    
            snooze(0.5)
    
        return None
    
    except Exception:
    
        return None
    

# =========================================================

# MAIN

# =========================================================

def main():

    workbook, sheet = load_excel()
    
    if workbook is None or sheet is None:
        return


# =====================================================
# LOGIN
# =====================================================

    clickButton(
        waitForObject(
            names.numpad_pushButton_8_NumpadButton
        )
    )
    
    doubleClick(
        waitForObject(
            names.numpad_pushButton_8_NumpadButton
        ),
        94,
        77,
        Qt.NoModifier,
        Qt.LeftButton
    )
    
    doubleClick(
        waitForObject(
            names.numpad_pushButton_8_NumpadButton
        ),
        94,
        77,
        Qt.NoModifier,
        Qt.LeftButton
    )
    
    clickButton(
        waitForObject(
            names.mainFrame_okButton_QPushButton
        )
    )
    
    
    # =====================================================
    # CHANGE LANGUAGE TO ESTONIAN
    # =====================================================
    
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
            names.languagesFrame_pbEstonia_QPushButton
        )
    )
    
    clickButton(
        waitForObject(
            names.buttonsFrame_acceptButton_QPushButton
        )
    )
    
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
    

    
    
    
    # =====================================================
    # SOFT TISSUE QUICK START
    # =====================================================
    
    

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
        377,
        65,
        Qt.NoModifier,
        Qt.LeftButton
    )
    
    mouseClick(
        waitForObjectItem(
            names.tabRightMainPresets_rightPresetsView_PresetListView,
            "_1"
        ),
        150,
        37,
        Qt.NoModifier,
        Qt.LeftButton
    )
    
    sendEvent(
        "QMoveEvent",
        waitForObject(
            names.o_ScreenSwitcher
        ),
        0,
        -50,
        1288,
        292
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
    
    
    # =====================================================
    # QUICK START EXIT POPUP
    # =====================================================
    
    mouseClick(
        waitForObject(
            names.modeButton_nameLabel_QLabel
        ),
        115,
        15,
        Qt.NoModifier,
        Qt.LeftButton
    )
    
    
    # =====================================================
    # QUICK START EXIT TITLE
    # =====================================================
    
    # test.compare(str(waitForObjectExists(names.centralWidget_TitleLabel_QLabel).text), "KAS VÄLJUDA KIIRKÄIVITUSE REŽIIMIST?")
    # test.compare(str(waitForObjectExists(names.centralWidget_MessageLabel_QLabel).text), "Kinnitage, et soovite kiirolekurežiimist väljuda.")
    # test.compare(str(waitForObjectExists(names.centralWidget_CancelButton_QPushButton).text), "TÜHISTA")
    # test.compare(str(waitForObjectExists(names.centralWidget_DisableButton_QPushButton).text), "CONFIRM")

    verify_text(
        sheet,
        names.centralWidget_TitleLabel_QLabel,
        "EXIT QUICK START MODE?",
        "Quick Start Exit Title"
    )
    
    
    # =====================================================
    # QUICK START EXIT MESSAGE
    # =====================================================
    
    verify_text(
        sheet,
        names.centralWidget_MessageLabel_QLabel,
        "Please confirm that you want to exit quick start mode.",
        "Quick Start Exit Message"
    )
    
    
    # =====================================================
    # QUICK START CANCEL
    # =====================================================
    
    verify_text(
        sheet,
        names.centralWidget_CancelButton_QPushButton,
        "CANCEL",
        "Quick Start Cancel Button"
    )
    
    
    # =====================================================
    # QUICK START CONFIRM
    # =====================================================
    
    verify_text(
        sheet,
        names.centralWidget_DisableButton_QPushButton,
        "CONFIRM",
        "Quick Start Confirm Button"
    )
    
    
    # =====================================================
    # CONFIRM EXIT
    # =====================================================

    # mouseClick(waitForObject(names.centralWidget_QFrame_2), 621, 166, Qt.NoModifier, Qt.LeftButton)
    # clickButton(waitForObject(names.centralWidget_CancelButton_QPushButton))
    #
    #
    # clickButton(waitForObject(names.gbSoftTissueProcedures_pbIncision_QPushButton))
    # clickButton(waitForObject(names.softTissueAssistantModeScreen_pbContinue_QPushButton))
    # clickButton(waitForObject(names.pulseEnergyWidget_incrementButton_QPushButton))
    # clickButton(waitForObject(names.pulseEnergyWidget_incrementButton_QPushButton))
    # clickButton(waitForObject(names.pulseEnergyWidget_incrementButton_QPushButton))
    # clickButton(waitForObject(names.pulseEnergyWidget_incrementButton_QPushButton))
    # clickButton(waitForObject(names.pulseEnergyWidget_incrementButton_QPushButton))
    # clickButton(waitForObject(names.pulseEnergyWidget_incrementButton_QPushButton))
    # clickButton(waitForObject(names.pulseEnergyWidget_incrementButton_QPushButton))
    # clickButton(waitForObject(names.pulseEnergyWidget_incrementButton_QPushButton))
    # clickButton(waitForObject(names.pulseEnergyWidget_incrementButton_QPushButton))
    # clickButton(waitForObject(names.pulseEnergyWidget_incrementButton_QPushButton))
    # clickButton(waitForObject(names.pulseEnergyWidget_incrementButton_QPushButton))
    # test.compare(str(waitForObjectExists(names.centralWidget_TitleLabel_QLabel).text), "KAS VÄLJUDA JUHENDATUD REŽIIMIST?")
    # test.compare(str(waitForObjectExists(names.centralWidget_MessageLabel_QLabel).text), "Kinnitage, et soovite juhendatud režiimist väljuda.")
    # test.compare(str(waitForObjectExists(names.centralWidget_CancelButton_QPushButton).text), "TÜHISTA")
    # test.compare(str(waitForObjectExists(names.centralWidget_DisableButton_QPushButton).text), "CONFIRM")

    # clickButton(
    #     waitForObject(
    #         names.centralWidget_DisableButton_QPushButton_2
    #     )
    # )
    #

    
    # =====================================================
    # RETURN HOME
    # =====================================================
    
    clickButton(
        waitForObject(
            names.centralWidget_CancelButton_QPushButton
        )
    )
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton_2))
    # =====================================================
    # SOFT TISSUE ASSISTANT
    # =====================================================
    
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
    
    
    # =====================================================
    # GUIDED MODE EXIT POPUP
    # =====================================================
    
    for i in range(30):

        clickButton(
            waitForObject(
                names.pulseEnergyWidget_incrementButton_QPushButton
            )
        )
    
        snooze(0.2)
    
        if i >= 15:
            try:
                waitForObjectExists(
                    names.somePopup_QDialog,
                    0.1
                )
                break
            except:
                pass
        
    # =====================================================
    # GUIDED MODE EXIT TITLE
    # =====================================================
    
    # test.compare(str(waitForObjectExists(names.centralWidget_TitleLabel_QLabel).text), "KAS VÄLJUDA JUHENDATUD REŽIIMIST?")
    # test.compare(str(waitForObjectExists(names.centralWidget_MessageLabel_QLabel).text), "Kinnitage, et soovite juhendatud režiimist väljuda.")
    # test.compare(str(waitForObjectExists(names.centralWidget_CancelButton_QPushButton).text), "TÜHISTA")
    # test.compare(str(waitForObjectExists(names.centralWidget_DisableButton_QPushButton).text), "CONFIRM")

    verify_text(
        sheet,
        names.centralWidget_TitleLabel_QLabel,
        "EXIT GUIDED MODE?",
        "Guided Mode Exit Title"
    )
    
    
    # =====================================================
    # GUIDED MODE EXIT MESSAGE
    # =====================================================
    
    verify_text(
        sheet,
        names.centralWidget_MessageLabel_QLabel,
        "Please confirm that you want to exit guided mode.",
        "Guided Mode Exit Message"
    )
    
    
    # =====================================================
    # GUIDED MODE CANCEL
    # =====================================================
    
    verify_text(
        sheet,
        names.centralWidget_CancelButton_QPushButton,
        "CANCEL",
        "Guided Mode Cancel Button"
    )
    
    
    # =====================================================
    # GUIDED MODE CONFIRM
    # =====================================================
    
    verify_text(
        sheet,
        names.centralWidget_DisableButton_QPushButton,
        "CONFIRM",
        "Guided Mode Confirm Button"
    )
    
    
    # =====================================================
    # CLOSE GUIDED MODE POPUP
    # =====================================================
    
    clickButton(
        waitForObject(
            names.centralWidget_DisableButton_QPushButton
        )
    )
    
    
    # =====================================================
    # CLOSE EXCEL
    # =====================================================
    
    workbook.close()
    
