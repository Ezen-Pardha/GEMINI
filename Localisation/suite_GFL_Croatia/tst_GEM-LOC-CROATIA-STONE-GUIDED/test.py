# -*- coding: utf-8 -*-

import names
import openpyxl
import re


def normalize(text):

    text = str(text)

    # Remove HTML
    text = re.sub(
        r"<[^>]+>",
        "",
        text
    )

    # Normalize spaces
    text = " ".join(
        text.split()
    )

    # Normalize spaces around < and >
    text = re.sub(
        r"<\s+",
        "<",
        text
    )

    text = re.sub(
        r">\s+",
        ">",
        text
    )

    return text.strip().lower()


def get_text_lines(obj):

    lines = []

    # Ignore invisible objects
    try:
        if not obj.visible:
            return lines
    except:
        pass

    # Get object text
    try:

        text = str(obj.text).strip()

        if text:

            # Convert HTML breaks to newline
            text = re.sub(
                r"<br\s*/?>",
                "\n",
                text,
                flags=re.IGNORECASE
            )

            # Remove HTML tags
            text = re.sub(
                r"<[^>]+>",
                "",
                text
            )

            # Split lines
            for line in text.splitlines():

                line = " ".join(
                    line.split()
                ).strip()

                if line:
                    lines.append(line)

    except:
        pass

    # Get children
    try:

        children = object.children(obj)

        for child in children:

            lines.extend(
                get_text_lines(child)
            )

    except:
        pass

    return lines


def get_all_text_combinations(obj):

    result = []

    # Get lines from current object
    lines = get_text_lines(obj)

    

    for start in range(len(lines)):

        combined = ""

        for end in range(
            start,
            len(lines)
        ):

            if combined:

                combined += " " + lines[end]

            else:

                combined = lines[end]

            result.append(combined)


    try:

        children = object.children(obj)

        for child in children:

            result.extend(
                get_all_text_combinations(child)
            )

    except:
        pass

    return result


def main():
   
    # LOGIN

    sendEvent("QMoveEvent",waitForObject(names.o_ScreenSwitcher),0,168,590,178)

    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))

    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))

    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))

    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    snooze(2)

    clickButton(waitForObject(names.mainFrame_okButton_QPushButton))

    # CHANGE LANGUAGE TO CROATIAN
    clickButton(waitForObject(names.homeScreen_settingsButton_QPushButton))

    clickTab(waitForObject(names.settingsScreen_tbSystemInfo_TabWidget),"INFO")

    clickButton(waitForObject(names.gbSystemInformation_pbLanguageSettingsUpdate_QPushButton))

    clickButton(waitForObject(names.languagesFrame_pbCroatia_QPushButton))

    clickButton(waitForObject(names.buttonsFrame_acceptButton_QPushButton))

    clickButton(waitForObject(names.settingsScreen_pbBack_QPushButton))
    
  
    # OPEN STONE ASSISTANT
  
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
   
    # READ EXCEL

    excelpath = "/home/ntc/Test_Automation_Gemini/Localisation/suite_GFL_Croatia/tst_GEM-LOC-CROATIA-STONE-GUIDED/testdata/Gemini strings.xlsx"
    workbook = openpyxl.load_workbook(excelpath,data_only=True)

    sheet = workbook.active

    test.vp("Verify Stone Guided Screen")

  

    # STONE GUIDED SELECTION
   
    clickButton(waitForObject(names.locationFrame_kidneyPcnlLocationButton_QPushButton))
    clickButton(waitForObject(names.flowRateFrame_mediumFlowRateButton_QPushButton))
    clickButton(waitForObject(names.hardnessFrame_largeHardnessButton_QPushButton))
    snooze(1)
   
    # GET WHOLE STONE ASSISTANT SCREEN
    stone = waitForObject(names.stoneAssistantModeScreen_StoneAssistantModeScreen)
    # GET SCREEN STRINGS
    screen_candidates = (get_all_text_combinations(stone))
    # Remove duplicates
    screen_candidates = list(set(screen_candidates) )
    # READ CROATIAN FROM EXCEL
    excel_strings = {}


    for row in sheet.iter_rows(
        min_row=2,
        values_only=True
    ):

        if len(row) < 9:
            continue


        trace_id = row[0]
        english = row[1]
        croatian = row[8]


        if english is None:
            continue

        if croatian is None:
            continue


        english = str(
            english
        ).strip()

        croatian = str(
            croatian
        ).strip()


        if not english or not croatian:
            continue


        excel_strings[normalize(croatian)] = {
            "english": english,
            "croatian": croatian,
            "trace_id":
                "" if trace_id is None
                else str(trace_id).strip()
        }



    matches = []


    for candidate in screen_candidates:

        normalized_candidate = normalize(
            candidate
        )

        if not normalized_candidate:
            continue


        if normalized_candidate in excel_strings:

            data = excel_strings[
                normalized_candidate
            ]

            matches.append(
                (
                    len(normalized_candidate),
                    data["english"],
                    data["croatian"]
                )
            )



    unique_matches = {}

    for length, english, croatian in matches:

        key = normalize(croatian)

        # Keep the longest matching version
        if key not in unique_matches:

            unique_matches[key] = (length,english,croatian)


   
    # VALIDATION
    

    pass_count = 0


    for key in sorted(
        unique_matches,
        key=lambda x: unique_matches[x][0],
        reverse=True
    ):

        data = unique_matches[key]

        english = data[1]
        croatian = data[2]


        test.passes(
            english +
            " -> " +
            croatian
        )

        pass_count += 1


  
    # FINAL RESULT
  

    if pass_count > 0:

        test.passes(
            "CROATIAN LOCALIZATION VALIDATION PASSED"
        )

    else:

        test.fail(
            "NO CROATIAN STRINGS FOUND ON SCREEN"
        )
