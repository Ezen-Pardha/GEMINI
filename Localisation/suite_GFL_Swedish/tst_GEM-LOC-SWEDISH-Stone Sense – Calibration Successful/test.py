# -*- coding: utf-8 -*-

import names
import openpyxl
import re
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

def normalize(text):

    if text is None:
        return ""

    text = str(text)
    #HTML tags.
    text = re.sub( r"<img\b(?=[^>]*stonesense)[^>]*>", " StoneSense ", text, flags=re.IGNORECASE )
    #HTML/XML tags.
    text = re.sub(r"<[^>]+>", "", text)
    # Normalize Unicode dash variants
    text = re.sub( r"(?<=\d)\s*[-\u2010\u2011\u2012\u2013\u2014\u2212]\s*(?=\d)", "-", text )
    #whitespace.
    text = re.sub(r"\s+", " ", text)
    # Remove spaces immediately before punctuation.
    text = re.sub(r"\s+([?!.,;:])", r"\1", text)
    # Remove leading/trailing spaces.
    text = text.strip()
    # Case-insensitive comparison.
    return text.casefold()

# LOAD ENGLISH -> swedish TRANSLATIONS
def load_swedish_strings(workbook, sheet_name):

    if sheet_name not in workbook.sheetnames:
        test.fail( "Excel sheet not found: [%s]" % sheet_name )
        return {}

    worksheet = workbook[sheet_name]

    translations = {}

    for row in worksheet.iter_rows(min_row=2):

        trace_id = row[0].value
        english = row[1].value
        swedish = row[24].value

        if english is None or swedish is None:
            continue

        english = str(english).strip()
        swedish = str(swedish).strip()

        if not english or not swedish:
            continue

        english_key = normalize(english)

        translations[english_key] = {
            "trace_id": trace_id,
            "english": english,
            "swedish": swedish
        }

    test.log( "Loaded %d English -> swedish translations from sheet [%s]" % (len(translations), sheet_name))

    return translations

# GET EXPECTED swedishN 
def get_expected_swedish(english_text, translations):

    key = normalize(english_text)

    if key not in translations:

        test.fail( "English string not found in Excel: [%s]" % english_text )

        return None

    return translations[key]["swedish"]

# GET TEXT FROM A QT OBJECT 
def get_object_text(obj):

    # Try .text 
    try:

        text = obj.text
        if text is not None:
            text = str(text).strip()
            if text:
                return text
    except:
        pass
 
    # Try .title 
    try:
        title = obj.title
        if title is not None:
            title = str(title).strip()
            if title:
                return title
    except:
        pass
    return ""

 
# GET OBJECT NAME 
def get_object_name(obj):

    try:
        name = obj.objectName
        if name:
            return str(name)
    except:
        pass
    return "UnnamedObject" 

#ALL VISIBLE TEXT OBJECTS 
def get_all_text_objects(obj, results=None):

    if results is None:
        results = []


    try:
        if not obj.visible:
            return results
    except:
        pass

 
    # Get object text 

    text = get_object_text(obj)
    if text: 
        results.append({
            "object": obj,
            "object_name": get_object_name(obj),
            "text": text
        }) 
        
    # Get children 
    try:
        children = object.children(obj)
        for child in children: get_all_text_objects( child, results )
    except:
        pass
    return results

 
# BUILD swedishN LOOKUP 
def build_swedish_lookup(translations):

    lookup = {}

    for english_key in translations:
        item = translations[english_key]
        swedish = item["swedish"]
        swedish_key = normalize(swedish)

        if not swedish_key:
            continue

        if swedish_key not in lookup:
            lookup[swedish_key] = []
        lookup[swedish_key].append(item)

    return lookup

 
# AUTOMATIC SCREEN LOCALIZATION CHECK 
def verify_screen_localization(
        root_object,
        screen_name,
        translations):
    
    test.log("LOCALIZATION CHECK")
    test.log("SCREEN: %s" % screen_name)
 
    # visible text objects 
    text_objects = get_all_text_objects( root_object ) 
    test.log( "Visible text objects found: %d" % len(text_objects) )
    
    # Build swedish lookup 
    swedish_lookup = build_swedish_lookup( translations ) 
    
    # Counters 
    passed = 0
    not_found = 0 
    
    # Prevent duplicate objects  
    checked = set()  
    
    for item in text_objects:
        obj = item["object"]
        object_name = item["object_name"]
        actual_swedish = item["text"]
        
        actual_key = normalize( actual_swedish )

        # Ignore empty
        if not actual_key:
            continue

        # Avoid duplicate
        unique_key = (  object_name, actual_key )

        if unique_key in checked:
            continue

        checked.add(unique_key) 
        
        # Find swedish text in Excel 
        matches = swedish_lookup.get( actual_key, [] ) 
        
        # Not found 
        if not matches:
            not_found += 1
        
            test.fail( "NOT FOUND IN EXCEL | Screen: [%s] | " "Object: [%s] | Actual: [%s]" % (
                    screen_name, object_name, actual_swedish
                )
            ) 
            continue


        # Exact match 
        for match in matches:

            english = match["english"]
            expected = match["swedish"]
            trace_id = match["trace_id"]
            
            test.log("LOCALIZATION MATCH")
            test.log("Object   : %s" % object_name)
            test.log("Trace ID : %s" % trace_id)
            test.log("English  : [%s]" % english)
            test.log("Expected : [%s]" % expected)
            test.log("Actual   : [%s]" % actual_swedish)
 
            # Final exact comparison  
            if normalize(actual_swedish) == normalize(expected):

                test.passes(  "PASS: %s -> %s"  % ( english, expected ))
                passed += 1

            else:
                test.fail( "FAIL: %s | Expected [%s] | Actual [%s]" % (  english, expected, actual_swedish ))


    # Summary 
    test.log("LOCALIZATION SUMMARY")
    test.log("SCREEN: %s" % screen_name)
    test.log("PASS      : %d" % passed)
    test.log("NOT FOUND : %d" % not_found)
    test.log("TOTAL CHECKED : %d" % len(checked))
    
def get_raw_object_text(obj):
    try:
        text = obj.text
        if text is not None:
            return str(text).strip()
    except:
        pass
    try:
        title = obj.title
        if title is not None:
            return str(title).strip()
    except:
        pass
    return ""

def verify_composite_localization(obj, translations, object_name="", ignore_dynamic_numbers = False):
    
    actual_text = get_raw_object_text(obj)
    
    if not actual_text:
        test.fail("Composite object has no text: %s" % object_name)
        return False

    test.log("COMPOSITE LOCALIZATION CHECK")
    test.log("Object : %s" % object_name)
    test.log("Actual : [%s]" % actual_text) 
    
    # Normalize the complete GUI text once.
    remaining = normalize(actual_text)
        
    if ignore_dynamic_numbers: 
        remaining = normalize(remaining) 
        
    candidates = []

    for english_key in translations:
        item = translations[english_key]
        expected = item.get("swedish", "")

        if expected and normalize(expected):
            candidates.append(item)

    candidates.sort(
        key=lambda item: len(normalize(item.get("swedish", ""))),
        reverse=True
    )

    while remaining:

        # Ignore separators between 2 strings
        remaining = re.sub(r"^[\s,;]+", "", remaining)

        if not remaining:
            break

        found = False
        for item in candidates:
            expected = normalize(item.get("swedish", ""))

            if not expected:
                continue 
            
            if re.search(r"(?<!\w)x(?!\w)", expected):
                parts = re.split(r"(?<!\w)x(?!\w)", expected)
            
                pattern = r"\d+".join( re.escape(part) for part in parts)
            
                match = re.match(pattern, remaining)
            
                if not match:
                    continue
            
                matched_length = match.end()            
            else:
                if not remaining.startswith(expected):
                    continue
            
                matched_length = len(expected)
            
            
            test.log("COMPOSITE PART MATCH")
            test.log("English  : [%s]" % item["english"])
            test.log("Expected : [%s]" % expected)
            test.log("Trace ID : %s" % item["trace_id"])
            
            # Remove the actual matched text 
            remaining = remaining[matched_length:]
            
            found = True
            break
        
        if not found:
            test.log("COMPOSITE PART NOT FOUND")
            test.log("Remaining: [%s]" % remaining)
            test.log("Candidate count: %d" % len(candidates))
        
            for item in candidates:
                expected = normalize(item.get("swedish", ""))
                test.log(
                    "Candidate swedishn: [%s] | Matches start: %s"
                    % (expected, remaining.startswith(expected) if expected else False)
                )
        
            test.fail(
                "FAIL: Composite localization -> [%s]" % actual_text
            )
            return False

    test.passes(
        "PASS: Complete composite localization -> [%s]"
        % actual_text
    )

    return True


def main():
    workbook = openpyxl.load_workbook(EXCEL_PATH, data_only=True)
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    clickButton(waitForObject(names.numpad_pushButton_8_NumpadButton))
    mouseClick(waitForObject(names.fiberVerificationWarningDialog_mainFrame_QFrame), 598, 550, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_settingsButton_QPushButton))
    clickTab(waitForObject(names.settingsScreen_tbSystemInfo_TabWidget), "INFO")
    clickButton(waitForObject(names.gbSystemInformation_pbLanguageSettingsUpdate_QPushButton))

    clickButton(waitForObject(names.languagesFrame_pbSwedish_QPushButton))
    clickButton(waitForObject(names.buttonsFrame_acceptButton_QPushButton))   
    clickButton(waitForObject(names.settingsScreen_pbBack_QPushButton))
    
    #extract Localised strings
    translations = load_swedish_strings(workbook, "Stone sense")
    
    clickButton(waitForObject(names.homeScreen_pbStoneAssistant_QToolButton))
    
    clickButton(waitForObject(names.locationFrame_kidneyPcnlLocationButton_QPushButton))    
    verify_screen_localization( waitForObject(names.locationFrame_kidneyPcnlLocationButton_QPushButton), "Location PCNL", translations )
    
    clickButton(waitForObject(names.flowRateFrame_mediumFlowRateButton_QPushButton))
    verify_screen_localization( waitForObject(names.flowRateFrame_mediumFlowRateButton_QPushButton), "flowrate", translations )
    
    clickButton(waitForObject(names.hardnessFrame_mediumHardnessButton_QPushButton))
    verify_composite_localization( waitForObject(names.hardnessFrame_mediumHardnessButton_QPushButton) , translations , "Hardness")
    
    clickButton(waitForObject(names.stoneAssistantModeScreen_continueButton_QPushButton))
    clickButton(waitForObject(names.stoneSenseFrame_pbStoneSense_QPushButton))
    
    mouseClick(waitForObject(names.calibrationPopupDialog_pStoneSenseTitleLabel_QLabel), 510, 5, Qt.NoModifier, Qt.LeftButton)    
    
    mouseClick(waitForObject(names.pMessageFrame_pInitiateCalibrationFrame_InitiateCalibrationDialog), 624, 7, Qt.NoModifier, Qt.LeftButton)

    test.vp("initiateCalibration_Swedish", "Successful GUI Verification")

    verify_screen_localization( waitForObject(names.pMessageFrame_pInitiateCalibrationFrame_InitiateCalibrationDialog), "message", translations )
    
    mouseClick(waitForObject(names.pInitiateCalibrationFrame_pCalibrationMessageLabel_QLabel), 401, 85, Qt.NoModifier, Qt.LeftButton)
    verify_screen_localization( waitForObject(names.pInitiateCalibrationFrame_pCalibrationMessageLabel_QLabel), "MessageLabel", translations )
    
    mouseClick(waitForObject(names.frame_emissionTextIcon_QLabel), 212, 110, Qt.NoModifier, Qt.LeftButton)    
    mouseClick(waitForObject(names.pInitiateCalibrationFrame_frame_QFrame), 998, 7, Qt.NoModifier, Qt.LeftButton)    
    verify_screen_localization( waitForObject(names.pInitiateCalibrationFrame_frame_QFrame), "calibrationFrame", translations )
    
    clickButton(waitForObject(names.calibrationPopupDialog_pbMiddleButton_QPushButton))
    mouseClick(waitForObject(names.pInitiateCalibrationFrame_pCalibrationMessageLabel_QLabel), 232, 128, Qt.NoModifier, Qt.LeftButton)

    test.vp("calibrationSuccessful_Swedish", "Successful GUI Verification")

    verify_composite_localization( waitForObject(names.pInitiateCalibrationFrame_pCalibrationMessageLabel_QLabel), translations, "messageLabel2nd step" )
    
    mouseClick(waitForObject(names.pMessageFrame_pInitiateCalibrationFrame_InitiateCalibrationDialog), 431, 7, Qt.NoModifier, Qt.LeftButton)    
    mouseClick(waitForObject(names.calibrationPopupDialog_pStoneSenseTitleLabel_QLabel), 339, 7, Qt.NoModifier, Qt.LeftButton)    
    mouseClick(waitForObject(names.pInitiateCalibrationFrame_pCalibrationMessageLabel_QLabel), 316, 335, Qt.NoModifier, Qt.LeftButton)    
    mouseClick(waitForObject(names.pProgressFrame_pTimerLabel_QLabel), 166, 37, Qt.NoModifier, Qt.LeftButton)
    verify_composite_localization( waitForObject(names.pProgressFrame_pTimerLabel_QLabel), translations,"Timer label", ignore_dynamic_numbers = True )
    
    mouseClick(waitForObject(names.pInitiateCalibrationFrame_pGraphicsView_QGraphicsView), 310, 402, Qt.NoModifier, Qt.LeftButton)
    
    mouseClick(waitForObject(names.frame_pStoneSenseTextLabel_QLabel), 345, 2, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.frame_pStoneSenseTextLabel_QLabel), 333, 116, Qt.NoModifier, Qt.LeftButton)
    verify_screen_localization( waitForObject(names.frame_pStoneSenseTextLabel_QLabel), "Stonesense Text", translations )
    
    mouseClick(waitForObject(names.frame_pAnimationLabel_QLabel), 225, 84, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.frame_pAnimationLabel_QLabel), 212, 165, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.frame_pStoneSenseTextLabel_QLabel), 271, 311, Qt.NoModifier, Qt.LeftButton)
    verify_screen_localization( waitForObject(names.frame_pStoneSenseTextLabel_QLabel), "Stonesense Text 2", translations )
    
    mouseClick(waitForObject(names.pCalibrationSuccessFrame_pEmissionLabel_QLabel), 511, 65, Qt.NoModifier, Qt.LeftButton)
    verify_screen_localization( waitForObject(names.pCalibrationSuccessFrame_pEmissionLabel_QLabel), "emission label", translations )
    
    clickButton(waitForObject(names.pCalibrationSuccessFrame_pOKButton_QPushButton))
    clickButton(waitForObject(names.stoneSenseFrame_pbStoneSense_QPushButton))
    mouseClick(waitForObject(names.centralWidget_QFrame_2), 721, 15, Qt.NoModifier, Qt.LeftButton)
    verify_screen_localization( waitForObject(names.centralWidget_QFrame_2), "central widget", translations )
    
    mouseClick(waitForObject(names.centralWidget_TitleLabel_QLabel), 569, 58, Qt.NoModifier, Qt.LeftButton)
    verify_screen_localization( waitForObject(names.centralWidget_QFrame_2), "title label", translations )
    
    mouseClick(waitForObject(names.centralWidget_MessageLabel_QLabel), 654, 126, Qt.NoModifier, Qt.LeftButton)
    verify_screen_localization( waitForObject(names.centralWidget_QFrame_2), "message label", translations )
    
    clickButton(waitForObject(names.centralWidget_DisableButton_QPushButton))
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton_2))
    
    
    
    
