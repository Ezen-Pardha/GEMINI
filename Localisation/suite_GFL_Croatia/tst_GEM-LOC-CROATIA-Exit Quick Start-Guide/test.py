# -*- coding: utf-8 -*-

import names
import openpyxl
import re


# =========================================================
# Excel Path
# =========================================================

EXCEL_PATH = "/home/ezen/Test_Automation_Katana/suite_Gemini_Localization_Croatia/tst_GEM-LOC-CROATIA-Exit Quick Start-Guide/testdata/Gemini strings.xlsx"


# =========================================================
# Normalize Text
# =========================================================

def normalize(text):

    if text is None:
        return ""

    text = str(text)

    # Remove HTML tags
    text = re.sub(r"<[^>]+>", " ", text)

    # Normalize spaces
    text = " ".join(text.split())

    # Normalize < and >
    text = re.sub(r"\s*<\s*", " < ", text)
    text = re.sub(r"\s*>\s*", " > ", text)

    return text.casefold()


# =========================================================
# Get All Visible Texts
# =========================================================

def get_all_texts(obj):

    texts = []

    try:
        if not obj.visible:
            return texts
    except:
        pass


    # -----------------------------------------------------
    # Get text property
    # -----------------------------------------------------

    try:

        value = str(obj.text).strip()

        if value:

            value = re.sub(
                r"<[^>]+>",
                " ",
                value
            )

            value = " ".join(
                value.split()
            )

            if value:
                texts.append(value)

    except:
        pass


    # -----------------------------------------------------
    # Get title property
    # -----------------------------------------------------

    try:

        value = str(obj.title).strip()

        if value:

            value = re.sub(
                r"<[^>]+>",
                " ",
                value
            )

            value = " ".join(
                value.split()
            )

            if value:
                texts.append(value)

    except:
        pass


    # -----------------------------------------------------
    # Get child objects
    # -----------------------------------------------------

    try:

        for child in object.children(obj):

            texts.extend(
                get_all_texts(child)
            )

    except:
        pass


    return texts


# =========================================================
# Load Croatian Strings from Excel
# =========================================================

def load_croatian_strings():

    

    


    workbook = openpyxl.load_workbook(
        EXCEL_PATH,
        data_only=True
    )

    sheet = workbook.active

    strings = []


    for row in sheet.iter_rows(
        min_row=2,
        values_only=True
    ):

        if len(row) < 9:
            continue


        # Column B = English
        english = row[1]

        # Column I = Croatian
        croatian = row[8]


        if english is None or croatian is None:
            continue


        english = str(
            english
        ).strip()

        croatian = str(
            croatian
        ).strip()


        if not english or not croatian:
            continue


        strings.append(
            {
                "english": english,
                "croatian": croatian,
                "normalized": normalize(croatian)
            }
        )


    


    return strings


# =========================================================
# Verify Screen / Popup Text Against Excel
# =========================================================

def verify_screen(
    root_object,
    screen_name
):

    


    excel_strings = load_croatian_strings()


    screen_texts = get_all_texts(
        root_object
    )


    unique_texts = []


    for text in screen_texts:

        text = text.strip()

        if text and text not in unique_texts:

            unique_texts.append(
                text
            )


    if not unique_texts:

        test.fail(
            screen_name +
            ": No visible text found"
        )

        return


    verified = []


    for screen_text in unique_texts:

        screen_normalized = normalize(
            screen_text
        )


        matches = []


        for item in excel_strings:

            excel_normalized = item[
                "normalized"
            ]


            # -------------------------------------------------
            # Exact Match
            # -------------------------------------------------

            if screen_normalized == excel_normalized:

                matches.append(
                    item
                )


            # -------------------------------------------------
            # Partial Match
            # -------------------------------------------------

            elif (
                len(excel_normalized) >= 4
                and
                excel_normalized in screen_normalized
            ):

                matches.append(
                    item
                )


        # Longest match first
        matches.sort(
            key=lambda x: len(
                x["normalized"]
            ),
            reverse=True
        )


        for item in matches:

            croatian = item[
                "croatian"
            ]


            if croatian in verified:
                continue


            verified.append(
                croatian
            )


            test.log(
                "PASS: " +
                item["english"] +
                " -> " +
                item["croatian"]
            )

            

            test.passes(
                item["english"] +
                " -> " +
                item["croatian"]
            )


    if not verified:

        test.fail(
            screen_name +
            ": No matching Croatian text found in Excel"
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




        # -----------------------------------------------------
        # Wait for centralWidget to become visible
        # -----------------------------------------------------

        for i in range(20):

            try:

                if central_widget.visible:

                    

                    return central_widget


            except:

                pass


            

            snooze(0.5)


        

        return None


    except:

        test.log(
            "centralWidget could not be found"
        )

        return None


# =========================================================
# Main
# =========================================================

def main():

   


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
        55,
        69,
        Qt.NoModifier,
        Qt.LeftButton
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


   


    # =====================================================
    # CHANGE LANGUAGE TO CROATIA
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


    mouseClick(
        waitForObject(
            names.gbSystemInformation_widget_QWidget
        ),
        240,
        259,
        Qt.NoModifier,
        Qt.LeftButton
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
            names.buttonsBar_homeButton_QPushButton
        )
    )


    


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
        255,
        60,
        Qt.NoModifier,
        Qt.LeftButton
    )


    mouseClick(
        waitForObjectItem(
            names.tabRightMainPresets_rightPresetsView_PresetListView,
            "_1"
        ),
        129,
        45,
        Qt.NoModifier,
        Qt.LeftButton
    )


    clickButton(
        waitForObject(
            names.quickStartScreen_pbContinue_QPushButton
        )
    )


    # =====================================================
    # RECOMMENDED FIBER WARNING
    # =====================================================

   


    warning_label = waitForObject(
        names.mainFrame_messageLabel_QLabel
    )


    try:

        actual_warning_text = str(
            warning_label.text
        ).strip()


        


    except:

        test.log(
            "Unable to read warning label text"
        )


    # Excel-based verification
    verify_screen(
        warning_label,
        "Recommended Fiber Warning"
    )


    # Close warning popup
    clickButton(
        waitForObject(
            names.mainFrame_okButton_QPushButton_2
        )
    )


    # =====================================================
    # QUICK START POPUP
    # =====================================================

    


    mouseDrag(
        waitForObject(
            names.indexPicker_valuePicker_IntervalSlider
        ),
        275,
        32,
        150,
        7,
        1,
        Qt.LeftButton
    )


    # Give AUT time to display popup
    snooze(1)


    


    central_widget = get_central_widget()


    if central_widget is not None:


        


        mouseClick(
            central_widget,
            581,
            216,
            Qt.NoModifier,
            Qt.LeftButton
        )


        # Excel-based verification
        verify_screen(
            central_widget,
            "Quick Start Popup"
        )


        # Disable popup
        clickButton(
            waitForObject(
                names.centralWidget_DisableButton_QPushButton_2
            )
        )


    else:

        test.fail(
            "Quick Start centralWidget popup did not become visible"
        )


    # =====================================================
    # RETURN HOME
    # =====================================================

    clickButton(
        waitForObject(
            names.buttonsBar_homeButton_QPushButton_2
        )
    )


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
    # MOVE SLIDER
    # =====================================================

    

   
    # Click increment button
    max_clicks = 50

    for i in range(max_clicks):

        clickButton(
            waitForObject(
                names.pulseEnergyWidget_incrementButton_QPushButton
                )
            )

        

        try:
            central_widget = findObject({
                "name": "centralWidget",
                "type": "QFrame",
                "window": ":o_ScreenSwitcher"
                })

            if central_widget.visible:
                
                break

        except:
            pass

        snooze(0.2)

    else:
        test.fail(
            "Popup did not open after " + str(max_clicks) + " clicks"
            )

            


    # mouseDrag(
    #     waitForObject(
    #         names.indexPicker_valuePicker_IntervalSlider
    #     ),
    #     207,
    #     30,
    #     331,
    #     30,
    #     1,
    #     Qt.LeftButton
    # )


    # Give AUT time to display popup
    snooze(1)


    # =====================================================
    # SOFT TISSUE ASSISTANT POPUP 2
    #
    # POPUP 1 REMOVED
    # =====================================================

    test.log(
        "Checking Soft Tissue Assistant Popup 2"
    )


    central_widget = get_central_widget()


    if central_widget is not None:


        


        mouseClick(
            central_widget,
            429,
            483,
            Qt.NoModifier,
            Qt.LeftButton
        )


        # Excel-based verification
        verify_screen(
            central_widget,
            "Soft Tissue Assistant Popup 2"
        )


        # =================================================
        # POPUP 3
        # =================================================

        test.log(
            "Waiting for Popup 3"
        )


        snooze(1)


        central_widget = get_central_widget()


        if central_widget is not None:


            test.log(
                "Clicking Soft Tissue Assistant Popup 3"
            )


            mouseClick(
                central_widget,
                429,
                483,
                Qt.NoModifier,
                Qt.LeftButton
            )


            # Excel-based verification
            verify_screen(
                central_widget,
                "Soft Tissue Assistant Popup 3"
            )


            # =================================================
            # DISABLE POPUP
            # =================================================

            
            test.vp("VP1")
            
            clickButton(
                waitForObject(
                    names.centralWidget_DisableButton_QPushButton_2
                )
            )


        else:

            test.fail(
                "Soft Tissue Assistant Popup 3 did not become visible"
            )


    else:

        test.fail(
            "Soft Tissue Assistant Popup 2 did not become visible"
        )


    # =====================================================
    # RETURN HOME
    # =====================================================

    clickButton(
        waitForObject(
            names.buttonsBar_homeButton_QPushButton_2
        )
    )


    # =====================================================
    # TEST COMPLETED
    # =====================================================

    test.log(
        "=============================================="
    )

    test.log(
        "Croatian Localization Test Completed"
    )

    test.log(
        "=============================================="
    )
