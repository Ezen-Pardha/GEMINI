
# -*- coding: utf-8 -*-

import names
import croatian_localization as loc
import openpyxl
import re
import os


TESTCASE_DIR = os.path.dirname(os.path.abspath(__file__))

EXCEL_PATH = loc.EXCEL_PATH

SHEET_NAME = "Soft tissue"


def get_all_texts(obj):

    texts = []

    try:
        text = str(obj.text).strip()

        if text:
            if "<html>" in text.lower():
                text = re.sub(r"<[^>]+>", "", text)
                text = text.strip()

            if text:
                texts.append(text)

    except Exception:
        pass

    try:
        children = object.children(obj)

        for child in children:
            texts.extend(get_all_texts(child))

    except Exception:
        pass

    return texts


def main():

    # Check Excel file
    if not os.path.isfile(EXCEL_PATH):
        test.fail("Excel file not found: " + EXCEL_PATH)
        return

    workbook = None

    try:
        workbook = openpyxl.load_workbook(
            EXCEL_PATH,
            data_only=True,
            read_only=True
        )

        # Select worksheet
        if SHEET_NAME not in workbook.sheetnames:
            test.fail(
                "Excel sheet not found: " + SHEET_NAME +
                ". Available sheets: " + ", ".join(workbook.sheetnames)
            )
            return

        sheet = workbook[SHEET_NAME]

        # Login
        doubleClick(
            waitForObject(names.numpad_pushButton_8_NumpadButton),
            68, 52,
            Qt.NoModifier,
            Qt.LeftButton
        )

        doubleClick(
            waitForObject(names.numpad_pushButton_8_NumpadButton),
            116, 46,
            Qt.NoModifier,
            Qt.LeftButton
        )

        clickButton(
            waitForObject(names.mainFrame_okButton_QPushButton)
        )

        # Change language to Croatian
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

        clickButton(
            waitForObject(names.languagesFrame_pbCroatia_QPushButton)
        )

        clickButton(
            waitForObject(names.buttonsFrame_acceptButton_QPushButton)
        )

        clickButton(
            waitForObject(names.settingsScreen_pbBack_QPushButton)
        )

        # Open Soft Tissue Assistant
        clickButton(
            waitForObject(
                names.homeScreen_pbSoftTissueAssistant_QToolButton
            )
        )

        test.vp("Softtissue guidied")

        # Open Soft Tissue Procedures
        mouseClick(
            waitForObject(
                names.softTissueAssistantModeScreen_gbSoftTissueProcedures_QFrame
            ),
            90, 150,
            Qt.NoModifier,
            Qt.LeftButton
        )

        soft_tissue = waitForObject(
            names.softTissueAssistantModeScreen_SoftTissueAssistantModeScreen
        )
        loc.verify_screen(soft_tissue, "Soft Tissue Guided", globals())

    except Exception as e:
        test.fail("Localization validation error: " + str(e))

    finally:
        if workbook is not None:
            workbook.close()
