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

# TEXT NORMALIZATION
def normalize(text):

    if text is None:
        return ""

    text = str(text)
    # Remove HTML/XML tags
    text = re.sub(r"<[^>]+>", "", text)
    # Normalize whitespace
    text = re.sub(r"\s+", " ", text)
    # Remove leading/trailing spaces
    text = text.strip()
    # Case-insensitive
    return text.casefold()

# LOAD ENGLISH -> latvian TRANSLATIONS
def load_latvian_strings(workbook, sheet_name):

    if sheet_name not in workbook.sheetnames:
        test.fail(
            "Excel sheet not found: [%s]" % sheet_name
        )
        return {}

    worksheet = workbook[sheet_name]

    translations = {}

    for row in worksheet.iter_rows(min_row=2):

        trace_id = row[0].value
        english = row[1].value
        latvian = row[15].value

        if english is None or latvian is None:
            continue

        english = str(english).strip()
        latvian = str(latvian).strip()

        if not english or not latvian:
            continue

        english_key = normalize(english)

        translations[english_key] = {
            "trace_id": trace_id,
            "english": english,
            "latvian": latvian
        }

    test.log(
        "Loaded %d English -> latvian translations from sheet [%s]"
        % (len(translations), sheet_name)
    )

    return translations

# GET EXPECTED CROATIAN
def get_expected_latvian(english_text, translations):

    key = normalize(english_text)
    
    if key not in translations:
        test.fail("English string not found in Excel: [%s]" % english_text)
        return None

    return translations[key]["latvian"]

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

# GET ALL VISIBLE TEXT OBJECTS
def get_all_text_objects(obj, results=None):

    if results is None:
        results = []


    # Check visibility 
    # LOAD EXCEL

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

        for child in children:
            get_all_text_objects(
                child,
                results)
    except:
        pass

    return results

# BUILD CROATIAN LOOKUP
def build_latvian_lookup(translations):

    lookup = {}

    for english_key in translations:
        item = translations[english_key]
        latvian = item["latvian"]
        latvian_key = normalize(latvian)
        
        if not latvian_key:
            continue

        if latvian_key not in lookup:
            lookup[latvian_key] = []

        lookup[latvian_key].append(item)

    return lookup

# AUTOMATIC SCREEN LOCALIZATION CHECK
def verify_screen_localization(
        root_object,
        screen_name,
        translations):

    test.log("LOCALIZATION CHECK CALLED")
    test.log("SCREEN: %s" % screen_name)

    # Find visible text objects
    text_objects = get_all_text_objects(root_object)

    test.log("Visible text objects found: %d" % len(text_objects))
    
    # Build Croatian lookup
    latvian_lookup = build_latvian_lookup(translations)

    # Counters
    passed = 0
    not_found = 0
    
    # Prevent duplicate objects
    checked = set()

    # Check every visible string
    for item in text_objects:
        obj = item["object"]
        object_name = item["object_name"]
        actual_latvian = item["text"]

        actual_key = normalize(actual_latvian)

        # Ignore empty
        if not actual_key:
            continue

        # Avoid duplicate
        unique_key = (object_name, actual_key)

        if unique_key in checked:
            continue

        checked.add(unique_key) 
        
        # Find latvian text in Excel
        matches = latvian_lookup.get(actual_key, []) 
        
        # Not found         
        if not matches:
            not_found += 1
        
            test.fail(
                "NOT FOUND IN EXCEL | Screen: [%s] | "
                "Object: [%s] | Actual: [%s]"
                % (
                    screen_name,
                    object_name,
                    actual_latvian
                )
            )
        
            continue

        # Exact match 
        for match in matches:

            english = match["english"]
            expected = match["latvian"]
            trace_id = match["trace_id"] 
            test.log("LOCALIZATION MATCH")
            test.log("Object   : %s" % object_name)
            test.log("Trace ID : %s" % trace_id)
            test.log("English  : [%s]" % english)
            test.log("Expected : [%s]" % expected)
            test.log("Actual   : [%s]" % actual_latvian)
            
            # Final exact comparison
            if normalize(actual_latvian) == normalize(expected):
                test.passes("PASS: %s -> %s" % ( english, expected ))
                passed += 1

            else:
                test.fail("FAIL: %s | Expected [%s] | Actual [%s]" % ( english, expected, actual_latvian ))
   
    test.log("LOCALIZATION SUMMARY")
    test.log("SCREEN: %s" % screen_name)
    test.log("PASS      : %d" % passed)
    test.log("NOT FOUND : %d" % not_found)
    test.log("TOTAL CHECKED : %d" % len(checked))
    
    
def main():
    workbook = openpyxl.load_workbook(EXCEL_PATH, data_only=True)
    doubleClick(waitForObject(names.numpad_pushButton_8_NumpadButton), 58, 40, Qt.NoModifier, Qt.LeftButton)
    doubleClick(waitForObject(names.numpad_pushButton_8_NumpadButton), 58, 40, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_settingsButton_QPushButton))
    clickTab(waitForObject(names.settingsScreen_tbSystemInfo_TabWidget), "INFO")
    clickButton(waitForObject(names.gbSystemInformation_pbLanguageSettingsUpdate_QPushButton))

    clickButton(waitForObject(names.languagesFrame_pbLatvia_QPushButton))
    clickButton(waitForObject(names.buttonsFrame_acceptButton_QPushButton))
    clickButton(waitForObject(names.settingsScreen_pbBack_QPushButton))
    clickButton(waitForObject(names.homeScreen_settingsButton_QPushButton))
    
    translations = load_latvian_strings(workbook, "settings")
    
    mouseClick(waitForObject(names.topBar_buttonsBar_ButtonsBar_2), 1246, 15, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.topBar_buttonsBar_ButtonsBar_2), 654, 26, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.topBar_buttonsBar_ButtonsBar_2), 287, 36, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.topBar_buttonsBar_ButtonsBar_2), 112, 26, Qt.NoModifier, Qt.LeftButton)
#    clickTab(waitForObject(names.settingsScreen_tbSystemInfo_TabWidget))
    
    #system TAB-------------------------------
    verify_screen_localization(
    waitForObject(names.settingsScreen_SettingsScreen),
    "System Settings - SISTEMA",
    translations)
    
    mouseClick(waitForObject(names.systemsettingframe_label_QLabel), 104, 18, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.systemsettingframe_lbBrightnessName_QLabel), 311, 19, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.systemsettingframe_lbVolumeName_QLabel), 313, 23, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.aimingbeamsettingframe_label_2_QLabel), 222, 9, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.aimingbeamsettingframe_lbAimingBeamDefaultModeName_QLabel), 287, 25, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.aimingbeamsettingframe_lbAimingBeamDefaultLevelName_QLabel), 320, 28, Qt.NoModifier, Qt.LeftButton)

    test.vp("settingSystem_Latvian", "Successful GUI Verification")

    clickButton(waitForObject(names.aimingbeamsettingframe_pbAimingBeamOff_QPushButton))
    
    #aiming beam OFF---------------------------
    verify_screen_localization(
    waitForObject(names.settingsScreen_SettingsScreen),
    "System Settings - Aiming Beam OFF",
    translations)
    
    mouseClick(waitForObject(names.aimingbeamsettingframe_lbAimingBeamDefaultLevelName_QLabel), 264, 24, Qt.NoModifier, Qt.LeftButton)

    test.vp("settingSystem_AimingbeamOff_Latvian", "Successful GUI Verification")

    clickButton(waitForObject(names.aimingbeamsettingframe_pbAimingBeamOn_QPushButton))
    
    #aiming beam ON-----------------------------
    verify_screen_localization(
    waitForObject(names.settingsScreen_SettingsScreen),
    "System Settings - Aiming Beam ON",
    translations)
    
 #   clickTab(waitForObject(names.settingsScreen_tbSystemInfo_TabWidget), "SISTEMA")
    clickButton(waitForObject(names.settingsScreen_pbBack_QPushButton))





