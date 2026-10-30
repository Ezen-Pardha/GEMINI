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
    #HTML/XML tags
    text = re.sub(r"<[^>]+>", "", text)
    # Normalize whitespace normally first
    text = re.sub(r"\s+", " ", text)
    # Remove leading/trailing spaces
    text = text.strip()
    # Case-insensitive
    return text.casefold()


#portuguese TRANSLATIONS
def load_portuguese_strings(workbook, sheet_name):

    if sheet_name not in workbook.sheetnames:
        test.fail( "Excel sheet not found: [%s]" % sheet_name )
        return {}

    worksheet = workbook[sheet_name]

    translations = {}

    for row in worksheet.iter_rows(min_row=2):

        trace_id = row[0].value
        english = row[1].value
        portuguese = row[19].value

        if english is None or portuguese is None:
            continue

        english = str(english).strip()
        portuguese = str(portuguese).strip()

        if not english or not portuguese:
            continue

        english_key = normalize(english)

        translations[english_key] = {
            "trace_id": trace_id,
            "english": english,
            "portuguese": portuguese
        }

    test.log(
        "Loaded %d English -> portuguese translations from sheet [%s]"
        % (len(translations), sheet_name)
    )

    return translations
 
# GET EXPECTED CROATIAN 
def get_expected_portuguese(english_text, translations):

    key = normalize(english_text)

    if key not in translations:
        test.fail( "English string not found in Excel: [%s]" % english_text )

        return None
    return translations[key]["portuguese"]

 
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
    try:
        if not obj.visible:
            return results
    except:
        pass
 
    # Get object properties 
    try:
        properties = object.properties(obj)
    except:
        properties = {}

 
    # Handle QTableView items 
    if properties.get("viewType") == "QTableView":

        column = properties.get("column")

        if column in [0, 1]:
            pass

        elif column == 2:
            text = get_object_text(obj)
            if text:
                results.append({
                    "object": obj,
                    "object_name": get_object_name(obj),
                    "text": text
                })

 
    # Normal Qt objects 
    else:

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
                results
            )
    except:
        pass
    return results
 
# BUILD CROATIAN LOOKUP 
def build_portuguese_lookup(translations):

    lookup = {}

    for english_key in translations:
        item = translations[english_key]
        portuguese = item["portuguese"]
        portuguese_key = normalize(portuguese)
        if not portuguese_key:
            continue

        if portuguese_key not in lookup:
            lookup[portuguese_key] = []

        lookup[portuguese_key].append(item)
    return lookup


# AUTOMATIC SCREEN LOCALIZATION CHECK
def verify_screen_localization(
        root_object,
        screen_name,
        translations):
 
    test.log("LOCALIZATION CHECK")
    test.log("SCREEN: %s" % screen_name) 

 
    # Find visible text objects
    text_objects = get_all_text_objects(
        root_object
    )

    test.log(
        "Visible text objects found: %d"
        % len(text_objects)
    )

    # Build portuguese lookup
    portuguese_lookup = build_portuguese_lookup(
        translations
    )
 
    # Counters
    passed = 0
    not_found = 0
 
    # Prevent duplicate objects 
    checked = set()

 
    # Check every visible string 
    for item in text_objects:

        obj = item["object"]
        object_name = item["object_name"]
        actual_portuguese = item["text"]
        actual_key = normalize(
            actual_portuguese
        )
        # Ignore empty
        if not actual_key:
            continue
        # Avoid duplicate
        unique_key = (
            object_name,
            actual_key
        )

        if unique_key in checked:
            continue

        checked.add(unique_key)
 
        # Find portuguese text in Excel 
        matches = portuguese_lookup.get( actual_key, [] )
        
        if not matches:
            joined_text = re.sub(
                r"(?<=[^\W\d_])\s*\n\s*(?=[^\W\d_])",
                "",
                actual_portuguese
            )
            joined_key = normalize(joined_text)
        
            matches = portuguese_lookup.get(joined_key, [])
        
            if matches:
                actual_key = joined_key
 
        if not matches:
            not_found += 1
        
            test.fail(
                "NOT FOUND IN EXCEL | Screen: [%s] | "
                "Object: [%s] | Actual: [%s]"
                % (
                    screen_name,
                    object_name,
                    actual_portuguese
                )
            )
        
            continue
 
        # Exact match 
        for match in matches:
            english = match["english"]
            expected = match["portuguese"]
            trace_id = match["trace_id"]
 
            test.log("LOCALIZATION MATCH")
            test.log("Object   : %s" % object_name)
            test.log("Trace ID : %s" % trace_id)
            test.log("English  : [%s]" % english)
            test.log("Expected : [%s]" % expected)
            test.log("Actual   : [%s]" % actual_portuguese)
 
            # Final exact comparison 
            if actual_key == normalize(expected):
                test.passes( "PASS: %s -> %s" % ( english, expected ))
                passed += 1

            else:
                test.fail("FAIL: %s | Expected [%s] | Actual [%s]" % ( english, expected, actual_portuguese )) 


    test.log("LOCALIZATION SUMMARY")
    test.log("SCREEN: %s" % screen_name)
    test.log( "PASS      : %d" % passed )
    test.log( "NOT FOUND : %d" % not_found )
    test.log( "TOTAL CHECKED : %d" % len(checked))


def main():
    workbook = openpyxl.load_workbook(EXCEL_PATH, data_only=True)
    doubleClick(waitForObject(names.numpad_pushButton_8_NumpadButton), 82, 71, Qt.NoModifier, Qt.LeftButton)
    doubleClick(waitForObject(names.numpad_pushButton_8_NumpadButton), 82, 71, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_settingsButton_QPushButton))
    clickTab(waitForObject(names.settingsScreen_tbSystemInfo_TabWidget), "INFO")
    clickButton(waitForObject(names.gbSystemInformation_pbLanguageSettingsUpdate_QPushButton))

    mouseClick(waitForObject(names.wdSystemInfoLayout_centralWidget_QFrame), 369, 10, Qt.NoModifier, Qt.LeftButton)

    clickButton(waitForObject(names.languagesFrame_pbPortugese_QPushButton))
    clickButton(waitForObject(names.buttonsFrame_acceptButton_QPushButton))
    clickTab(waitForObject(names.settingsScreen_tbSystemInfo_TabWidget), "REGISTOS")
        
    mouseClick(waitForObject(names.topBar_buttonsBar_ButtonsBar_2), 1187, 9, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.topBar_buttonsBar_ButtonsBar_2), 683, 30, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.topBar_buttonsBar_ButtonsBar_2), 285, 27, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.topBar_buttonsBar_ButtonsBar_2), 116, 27, Qt.NoModifier, Qt.LeftButton)
    #clickTab(waitForObject(names.settingsScreen_tbSystemInfo_TabWidget), 4)
    clickTab(waitForObject(names.settingsScreen_tbSystemInfo_TabWidget), "REGISTOS")
    
    # Load Excel translations once

    test.vp("settingLogs_Portuguese", "Successful GUI Verification")

    translations = load_portuguese_strings(workbook, "settings")

    # Verify the REGISTROS screen immediately after entering it
    verify_screen_localization(
        waitForObject(names.settingsScreen_SettingsScreen),
        "System Settings - REGISTOS",
        translations
    )
    
    mouseClick(waitForObject(names.settingsScreen_lbDownloadLogsToUsb_QLabel), 185, 41, Qt.NoModifier, Qt.LeftButton)
    
    item = waitForObjectItem(names.systemEventErrorLogWidget_tableView_QTableView,
    "1/2")

    test.log("ITEM PROPERTIES: " + str(object.properties(item)))

    mouseClick(waitForObjectItem(names.systemEventErrorLogWidget_tableView_QTableView, "1/2"), 178, 28, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.systemEventErrorLogWidget_tableView_QTableView, "2/2"), 190, 36, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.systemEventErrorLogWidget_tableView_QTableView, "3/2"), 216, 30, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.systemEventErrorLogWidget_tableView_QTableView, "4/2"), 196, 31, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.systemEventErrorLogWidget_tableView_QTableView, "5/2"), 158, 33, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.systemEventErrorLogWidget_tableView_QTableView, "6/2"), 118, 33, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.settingsScreen_pbBack_QPushButton))
