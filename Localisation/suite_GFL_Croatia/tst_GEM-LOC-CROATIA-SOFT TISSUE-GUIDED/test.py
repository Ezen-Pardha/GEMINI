# -*- coding: utf-8 -*-

import names
import openpyxl
import re


def get_all_texts(obj):

    texts = []

    try:
        text = str(obj.text).strip()

        if text:

            if "<html>" in text:
                text = re.sub("<[^>]+>", "", text)
                text = text.strip()

            if text:
                texts.append(text)

    except:
        pass


    try:
        children = object.children(obj)

        for child in children:
            texts.extend(get_all_texts(child))

    except:
        pass


    return texts


def main():
    
    excelpath = "/home/ntc/suite_gemini_Localization_croatian/tst_GEM-LOC-CROATIA-SOFT TISSUE-GUIDED/testdata/Croatia Soft tissue guided.xlsx"

    workbook = openpyxl.load_workbook(excelpath)

    sheet = workbook.active

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



    clickButton(
        waitForObject(
            names.homeScreen_pbSoftTissueAssistant_QToolButton
        )
    )


    # Open Soft Tissue Procedures

    test.vp("Softtissue guidied")

   
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

    actual_texts = get_all_texts(soft_tissue)

    # Remove duplicate strings
    actual_texts = list(set(actual_texts))


    for text in actual_texts:

        for row in sheet.iter_rows(
            min_row=2,
            values_only=True
        ):

            if row[0] is None or row[1] is None:
                continue


            english = str(row[0]).strip()
            croatian = str(row[1]).strip()


            # Screen string matches Excel
            if croatian == text:

                test.passes(
                    english + " -> " + croatian
                )

                break





