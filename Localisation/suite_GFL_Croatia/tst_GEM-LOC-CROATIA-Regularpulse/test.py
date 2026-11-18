# -*- coding: utf-8 -*-

import names
import re
import unicodedata
from openpyxl import load_workbook
import os

TESTCASE_DIR = os.path.dirname(os.path.abspath(__file__))
 
EXCEL_PATH = os.path.abspath(
    os.path.join( TESTCASE_DIR,
        "..",
        "shared",
        "testdata",
        "Gemini Split strings.xlsx"
    )
)



ENGLISH_COLUMN = 2
DUTCH_COLUMN = 4

workbook = None
sheet = None
dutch_strings = {}


def get_object_text(obj):
    for attribute in ("text", "title", "windowTitle", "accessibleName"):
        try:
            value = getattr(obj, attribute)
            if value is not None:
                value = str(value)
                if value.strip():
                    return value
        except Exception:
            pass
    return ""


def normalize_text(value):
    if value is None:
        return ""

    text = str(value)

    text = re.sub(r"<[^>]*>", " ", text)

    text = text.replace("\u00A0", " ")
    text = text.replace("\u2007", " ")
    text = text.replace("\u202F", " ")

    text = re.sub(r"[\r\n\t]+", " ", text)

    text = text.replace("™", "")
    text = text.replace("®", "")
    text = text.replace("©", "")

    try:
        text = unicodedata.normalize("NFKC", text)
    except Exception:
        pass

    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"\s+([.,;:!?])", r"\1", text)

    return text.strip().casefold()


def comparison_key(value):
    """
    Normalize the text and concatenate it by removing all whitespace.

    Examples:
        'GEMIDDELDE VERMOGEN' -> 'gemiddeldevermogen'
        'GEMIDDELDE\\nVERMOGEN' -> 'gemiddeldevermogen'
        'GEMIDDELDEVERMOGEN' -> 'gemiddeldevermogen'
    """
    return re.sub(r"\s+", "", normalize_text(value))


def load_dutch_strings():
    global workbook
    global sheet
    global dutch_strings

    try:
        workbook = load_workbook(
            EXCEL_PATH,
            read_only=True,
            data_only=True
        )
        sheet = workbook["Treatment Modes"]

        dutch_strings = {}

        for row in sheet.iter_rows(
            min_row=2,
            min_col=DUTCH_COLUMN,
            max_col=DUTCH_COLUMN
        ):
            value = row[0].value

            if value is None:
                continue

            key = comparison_key(value)

            if key and key not in dutch_strings:
                dutch_strings[key] = value

        return True

    except Exception as e:
        test.fail(
            "Failed to load Gemini Split strings Excel / Treatment Modes: "
            + str(e)
        )
        return False


def find_dutch_text(actual_text):
    if not actual_text:
        return None

    key = comparison_key(actual_text)

    if not key:
        return None

    return dutch_strings.get(key)


def verify_text(object_name, description):
    snooze(6)

    try:
        obj = waitForObject(object_name)
    except Exception as e:
        test.fail(
            description
            + " | Object not found: "
            + str(e)
        )
        return False

    actual_text = get_object_text(obj)

    if not actual_text:
        test.fail(
            description
            + " | UI text is empty"
        )
        return False

    expected_text = find_dutch_text(actual_text)

    if expected_text is None:
        test.fail(
            description
            + " | Dutch text not found in Excel: "
            + str(actual_text)
        )
        return False

    actual_key = comparison_key(actual_text)
    expected_key = comparison_key(expected_text)

    test.compare(
        actual_key,
        expected_key,
        description
    )

    return True


def verify_group(group_name):
    for object_name, description in verification_objects[group_name]:
        verify_text(object_name, description)


def verify_popup(group_name):
    verify_group(group_name)

    snooze(6)

    clickButton(
        waitForObject(
            names.centralWidget_OKButton_QPushButton
        )
    )


verification_objects = {
    "main": [
        (
            names.centralWidget_lbTitle_QLabel,
            "Mode Selection Title"
        ),
        (
            names.centralWidget_label_2_QLabel,
            "Standard Mode Label"
        ),
        (
            names.centralWidget_Square_QPushButton,
            "Standard Pulse Button"
        ),
        (
            names.centralWidget_CW_QPushButton,
            "Continuous Wave Button"
        ),
        (
            names.centralWidget_MRP_QPushButton,
            "MRP Button"
        ),
        (
            names.centralWidget_label_QLabel,
            "Expert Mode Label"
        ),
        (
            names.centralWidget_Fragmentation_QPushButton,
            "Fragmentation Pulse Button"
        ),
        (
            names.centralWidget_Cleaning_QPushButton,
            "Cleaning Pulse Button"
        ),
        (
            names.centralWidget_Enucleation_QPushButton,
            "Enucleation Pulse Button"
        ),
        (
            names.buttonsFrame_rejectButton_QPushButton,
            "Cancel Button"
        )
    ],

    "standard_pulse": [
        (
            names.centralWidget_TitleLabel_QLabel_2,
            "Standard Pulse Popup Title"
        ),
        (
            names.centralWidget_MessageLabel_QLabel_2,
            "Standard Pulse Popup Message"
        ),
        (
            names.centralWidget_OKButton_QPushButton,
            "Standard Pulse Popup OK Button"
        )
    ],

    "cw": [
        (
            names.centralWidget_TitleLabel_QLabel_2,
            "Continuous Wave Popup Title"
        ),
        (
            names.centralWidget_MessageLabel_QLabel_2,
            "Continuous Wave Popup Message"
        ),
        (
            names.centralWidget_OKButton_QPushButton,
            "Continuous Wave Popup OK Button"
        )
    ],

    "mrp": [
        (
            names.centralWidget_TitleLabel_QLabel_2,
            "MRP Popup Title"
        ),
        (
            names.centralWidget_MessageLabel_QLabel_2,
            "MRP Popup Message"
        ),
        (
            names.centralWidget_OKButton_QPushButton,
            "MRP Popup OK Button"
        )
    ],

    "fragmentation": [
        (
            names.centralWidget_TitleLabel_QLabel_2,
            "Fragmentation Popup Title"
        ),
        (
            names.centralWidget_MessageLabel_QLabel_2,
            "Fragmentation Popup Message"
        ),
        (
            names.centralWidget_OKButton_QPushButton,
            "Fragmentation Popup OK Button"
        )
    ],

    "cleaning": [
        (
            names.centralWidget_TitleLabel_QLabel_2,
            "Cleaning Popup Title"
        ),
        (
            names.centralWidget_MessageLabel_QLabel_2,
            "Cleaning Popup Message"
        ),
        (
            names.centralWidget_OKButton_QPushButton,
            "Cleaning Popup OK Button"
        )
    ],

    "enucleation": [
        (
            names.centralWidget_TitleLabel_QLabel_2,
            "Enucleation Popup Title"
        ),
        (
            names.centralWidget_MessageLabel_QLabel_2,
            "Enucleation Popup Message"
        ),
        (
            names.centralWidget_OKButton_QPushButton,
            "Enucleation Popup OK Button"
        )
    ]
 }


def main():
    global workbook

    if not load_dutch_strings():
        return

    doubleClick(
        waitForObject(
            names.numpad_pushButton_8_NumpadButton
        ),
        91,
        77,
        Qt.NoModifier,
        Qt.LeftButton
    )

    snooze(6)

    clickButton(
        waitForObject(
            names.numpad_pushButton_8_NumpadButton
        )
    )

    snooze(6)

    clickButton(
        waitForObject(
            names.numpad_pushButton_8_NumpadButton
        )
    )

    snooze(6)

    clickButton(
        waitForObject(
            names.mainFrame_okButton_QPushButton
        )
    )

    snooze(6)

    clickButton(
        waitForObject(
            names.homeScreen_settingsButton_QPushButton
        )
    )

    snooze(6)

    clickTab(
        waitForObject(
            names.settingsScreen_tbSystemInfo_TabWidget
        ),
        "INFO"
    )

    snooze(6)

    clickButton(
        waitForObject(
            names.gbSystemInformation_pbLanguageSettingsUpdate_QPushButton
        )
    )

    snooze(6)

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

    snooze(6)

    clickButton(
        waitForObject(
            names.buttonsBar_homeButton_QPushButton
        )
    )

    snooze(6)

    clickButton(
        waitForObject(
            names.gbExpert_expertButton_QPushButton
        )
    )

    snooze(6)

    # mouseClick(waitForObject(names.modeButton_nameLabel_QLabel), 41, 30, Qt.NoModifier, Qt.LeftButton)
    # test.compare(str(waitForObjectExists(names.centralWidget_lbTitle_QLabel).text), "ODABIR NAČINA")
    # test.compare(str(waitForObjectExists(names.centralWidget_label_2_QLabel).text), "STANDARDNO")
    # test.compare(str(waitForObjectExists(names.centralWidget_Square_QPushButton).text), "STANDARDNI\nIMPULS")
    # test.compare(str(waitForObjectExists(names.centralWidget_CW_QPushButton).text), "KONTINUIRANI\nVAL\n(CW)")
    # test.compare(str(waitForObjectExists(names.centralWidget_label_QLabel).text), "NAPREDNO")
    # test.compare(str(waitForObjectExists(names.centralWidget_MRP_QPushButton).text), "IMPULS\nS\nMINIMALNOM\nRETROPULZIJOM™")
    # test.compare(str(waitForObjectExists(names.centralWidget_Fragmentation_QPushButton).text), "IMPULS\nZA\nFRAGMENTACIJU™")
    # test.compare(str(waitForObjectExists(names.centralWidget_Cleaning_QPushButton).text), "IMPULS\nS\nMINIMALNOM\nKARBONIZACIJOM™")
    # test.compare(str(waitForObjectExists(names.centralWidget_Enucleation_QPushButton).text), "IMPULS\nZA\nENUKLEACIJU™")
    # mouseClick(waitForObject(names.centralWidget_label_2_QLabel), 60, 51, Qt.NoModifier, Qt.LeftButton)
    # clickButton(waitForObject(names.square_icon_QPushButton))
    # test.compare(str(waitForObjectExists(names.centralWidget_TitleLabel_QLabel_2).text), "STANDARDNI IMPULS")
    # test.compare(str(waitForObjectExists(names.centralWidget_MessageLabel_QLabel_2).text), "Standardni oblik impulsa, kao impuls ravnog vrha, koji se upotrebljava za litotripsiju i postupke na mekom tkivu.")
    # test.compare(str(waitForObjectExists(names.centralWidget_OKButton_QPushButton).text), "U REDU")
    # mouseClick(waitForObject(names.centralWidget_TitleLabel_QLabel_2), 1019, 137, Qt.NoModifier, Qt.LeftButton)
    # clickButton(waitForObject(names.centralWidget_OKButton_QPushButton))
    # clickButton(waitForObject(names.cW_icon_QPushButton))
    # test.compare(str(waitForObjectExists(names.centralWidget_TitleLabel_QLabel_2).text), "KONTINUIRANI VAL (CW)")
    # test.compare(str(waitForObjectExists(names.centralWidget_MessageLabel_QLabel_2).text), "Stalna i neprekidna snaga lasera za postupke na mekom tkivu, kao što su vaporizacija i koagulacija tkiva.")
    # test.compare(str(waitForObjectExists(names.centralWidget_MessageLabel_QLabel_2).text), "Stalna i neprekidna snaga lasera za postupke na mekom tkivu, kao što su vaporizacija i koagulacija tkiva.")
    # test.compare(str(waitForObjectExists(names.centralWidget_OKButton_QPushButton).text), "U REDU")
    # clickButton(waitForObject(names.centralWidget_OKButton_QPushButton))
    # clickButton(waitForObject(names.mRP_icon_QPushButton))
    # test.compare(str(waitForObjectExists(names.centralWidget_TitleLabel_QLabel_2).text), "IMPULS S MINIMALNOM RETROPULZIJOM™")
    # test.compare(str(waitForObjectExists(names.centralWidget_MessageLabel_QLabel_2).text), "Poseban oblik impulsa, optimiziran za smanjenje retropulzije tijekom litotripsije.")
    # test.compare(str(waitForObjectExists(names.centralWidget_OKButton_QPushButton).text), "U REDU")
    # clickButton(waitForObject(names.centralWidget_OKButton_QPushButton))
    # clickButton(waitForObject(names.mRP_icon_QPushButton))
    # test.compare(str(waitForObjectExists(names.centralWidget_TitleLabel_QLabel_2).text), "IMPULS S MINIMALNOM RETROPULZIJOM™")
    # test.compare(str(waitForObjectExists(names.centralWidget_MessageLabel_QLabel_2).text), "Poseban oblik impulsa, optimiziran za smanjenje retropulzije tijekom litotripsije.")
    # test.compare(str(waitForObjectExists(names.centralWidget_OKButton_QPushButton).text), "U REDU")
    # clickButton(waitForObject(names.centralWidget_OKButton_QPushButton))
    # clickButton(waitForObject(names.fragmentation_icon_QPushButton))
    # test.compare(str(waitForObjectExists(names.centralWidget_TitleLabel_QLabel_2).text), "IMPULS ZA FRAGMENTACIJU™")
    # test.compare(str(waitForObjectExists(names.centralWidget_MessageLabel_QLabel_2).text), "Poseban oblik impulsa, optimiziran za ablaciju kamena u velike fragmente.")
    # test.compare(str(waitForObjectExists(names.centralWidget_OKButton_QPushButton).text), "U REDU")
    # clickButton(waitForObject(names.centralWidget_OKButton_QPushButton))
    # clickButton(waitForObject(names.cleaning_icon_QPushButton))
    # test.compare(str(waitForObjectExists(names.centralWidget_TitleLabel_QLabel_2).text), "IMPULS S MINIMALNOM KARBONIZACIJOM™")
    # test.compare(str(waitForObjectExists(names.centralWidget_MessageLabel_QLabel_2).text), "Poseban oblik impulsa za rezanje i izrezivanje mekog tkiva uz minimalnu karbonizaciju tkiva.")
    # test.compare(str(waitForObjectExists(names.centralWidget_OKButton_QPushButton).text), "U REDU")
    # clickButton(waitForObject(names.centralWidget_OKButton_QPushButton))
    # clickButton(waitForObject(names.enucleation_icon_QPushButton))
    # test.compare(str(waitForObjectExists(names.centralWidget_TitleLabel_QLabel_2).text), "IMPULS ZA ENUKLEACIJU™")
    # test.compare(str(waitForObjectExists(names.centralWidget_MessageLabel_QLabel_2).text), "Poseban oblik impulsa, osmišljen za postupak enukleacije kako bi se maksimiziralo termo-mehaničko odvajanje adenomskog tkiva i kapsule uz istodoban snažan učinak hemostaze.")
    # test.compare(str(waitForObjectExists(names.centralWidget_OKButton_QPushButton).text), "U REDU")
    # clickButton(waitForObject(names.centralWidget_OKButton_QPushButton))

    mouseClick(
        waitForObject(
            names.modeButton_nameLabel_QLabel
        ),
        73,
        25,
        Qt.NoModifier,
        Qt.LeftButton
    )

    verify_group("main")

    snooze(6)

    clickButton(
        waitForObject(
            names.square_icon_QPushButton
        )
    )

    verify_popup("standard_pulse")

    snooze(6)

    clickButton(
        waitForObject(
            names.cW_icon_QPushButton
        )
    )

    verify_popup("cw")

    snooze(6)

    clickButton(
        waitForObject(
            names.mRP_icon_QPushButton
        )
    )

    verify_popup("mrp")

    snooze(6)

    clickButton(
        waitForObject(
            names.fragmentation_icon_QPushButton
        )
    )

    verify_popup("fragmentation")

    snooze(6)

    clickButton(
        waitForObject(
            names.cleaning_icon_QPushButton
        )
    )

    verify_popup("cleaning")

    snooze(6)

    clickButton(
        waitForObject(
            names.enucleation_icon_QPushButton
        )
    )

    verify_popup("enucleation")

    snooze(6)

    # test.vp("RegularPulse")

    clickButton(
        waitForObject(
            names.buttonsFrame_rejectButton_QPushButton
        )
    )

    snooze(6)

    try:
        workbook.close()
    except Exception:
        pass
