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

    # Remove HTML/XML tags
    text = re.sub(r"<[^>]+>", "", text)
    # Normalize whitespace
    text = re.sub(r"\s+", " ", text)
    # Remove leading/trailing spaces
    text = text.strip()
    # Case-insensitive
    return text.casefold()

# LOAD ENGLISH -> Croatian TRANSLATIONS
def load_croatia_strings(workbook, sheet_name):

    if sheet_name not in workbook.sheetnames:
        test.fail( "Excel sheet not found: [%s]" % sheet_name )
        return {}

    worksheet = workbook[sheet_name]
    translations = {}
    for row in worksheet.iter_rows(min_row=2):

        trace_id = row[0].value
        english = row[1].value
        croatia = row[3].value

        if english is None or croatia is None:
            continue

        english = str(english).strip()
        croatia = str(croatia).strip()

        if not english or not croatia:
            continue

        english_key = normalize(english)

        translations[english_key] = {
            "trace_id": trace_id,
            "english": english,
            "croatia": croatia
        }

    test.log( "Loaded %d English -> croatia translations from sheet [%s]"  % (len(translations), sheet_name))
    return translations


def get_expected_croatia(english_text, translations):

    key = normalize(english_text)
    if key not in translations:

        test.fail( "English string not found in Excel: [%s]"  % english_text )
        return None
    return translations[key]["croatia"]


def get_object_text(obj):

    try:
        text = obj.text

        if text is not None:
            text = str(text).strip()
            if text:
                return text
    except:
        pass


    try:
        title = obj.title
        if title is not None:
            title = str(title).strip()

            if title:
                return title

    except:
        pass
    return ""

def get_object_name(obj):

    try:
        name = obj.objectName
        if name:
            return str(name)
    except:
        pass
    return "UnnamedObject"


def get_all_text_objects(obj, results=None):

    if results is None:
        results = []


    try:
        if not obj.visible:
            return results
    except:
        pass


    try:
        properties = object.properties(obj)
    except:
        properties = {}


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

    else:
        text = get_object_text(obj)
        if text:
            results.append({
                "object": obj,
                "object_name": get_object_name(obj),
                "text": text
            })


    try:
        children = object.children(obj)
        for child in children:

            get_all_text_objects(child, results)

    except:
        pass
    return results

 
def build_croatia_lookup(translations):

    lookup = {}
    for english_key in translations:
        item = translations[english_key]
        croatia = item["croatia"]
        croatia_key = normalize(croatia)
        if not croatia_key:
            continue
        if croatia_key not in lookup:
            lookup[croatia_key] = []
        lookup[croatia_key].append(item)
    return lookup


def verify_screen_localization(
        root_object,
        screen_name,
        translations):

    test.log("LOCALIZATION CHECK")
    test.log("SCREEN: %s" % screen_name)

    text_objects = get_all_text_objects( root_object )
    test.log( "Visible text objects found: %d" % len(text_objects))

    croatia_lookup = build_croatia_lookup(translations)

    passed = 0
    not_found = 0

    checked = set()

    for item in text_objects:
        obj = item["object"]
        object_name = item["object_name"]
        actual_croatia = item["text"]
        actual_key = normalize(actual_croatia)

        # Ignore empty
        if not actual_key:
            continue

        # Avoid duplicate
        unique_key = ( object_name, actual_key)

        if unique_key in checked:
            continue
        checked.add(unique_key)

        matches = croatia_lookup.get( actual_key, [])

        if not matches:
            test.log("NOT FOUND IN EXCEL")
            test.log("Object : %s" % object_name)
            test.log("Actual : [%s]" % actual_croatia)
            not_found += 1
            continue

        for match in matches:
            english = match["english"]
            expected = match["croatia"]
            trace_id = match["trace_id"]

            test.log("LOCALIZATION MATCH")
            test.log("Object   : %s" % object_name)
            test.log("Trace ID : %s" % trace_id)
            test.log("English  : [%s]" % english)
            test.log("Expected : [%s]" % expected)
            test.log("Actual   : [%s]" % actual_croatia)


            if normalize(actual_croatia) == normalize(expected):
                test.passes( "PASS: %s -> %s" % ( english, expected))
                passed += 1
            else:
                test.fail( "FAIL: %s | Expected [%s] | Actual [%s]" % (english, expected, actual_croatia))


    test.log("LOCALIZATION SUMMARY")
    test.log("SCREEN: %s" % screen_name)
    test.log( "PASS      : %d" % passed)
    test.log( "NOT FOUND : %d" % not_found)
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

    clickButton(waitForObject(names.languagesFrame_pbCroatia_QPushButton))
    clickButton(waitForObject(names.buttonsFrame_acceptButton_QPushButton))
    clickTab(waitForObject(names.settingsScreen_tbSystemInfo_TabWidget), "ZAPISNICI")
        
    mouseClick(waitForObject(names.topBar_buttonsBar_ButtonsBar_2), 1187, 9, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.topBar_buttonsBar_ButtonsBar_2), 683, 30, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.topBar_buttonsBar_ButtonsBar_2), 285, 27, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.topBar_buttonsBar_ButtonsBar_2), 116, 27, Qt.NoModifier, Qt.LeftButton)
    #clickTab(waitForObject(names.settingsScreen_tbSystemInfo_TabWidget), 4)
    clickTab(waitForObject(names.settingsScreen_tbSystemInfo_TabWidget), "ZAPISNICI")
    
    # Load Excel translations once

    test.vp("settingLogs_Croatia", "Successful GUI Verification")

    translations = load_croatia_strings(workbook,"settings")

    # Verify the REGISTROS screen immediately after entering it
    verify_screen_localization(
        waitForObject(names.settingsScreen_SettingsScreen),
        "System Settings - ZAPISNICI",
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
    
    workbook.close()
