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


# LOAD ENGLISH -> estonia TRANSLATIONS
def load_estonia_strings(workbook, sheet_name):

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
        estonia = row[7].value

        if english is None or estonia is None:
            continue

        english = str(english).strip()
        estonia = str(estonia).strip()

        if not english or not estonia:
            continue

        english_key = normalize(english)

        translations[english_key] = {
            "trace_id": trace_id,
            "english": english,
            "estonia": estonia
        }

    test.log(
        "Loaded %d English -> estonia translations from sheet [%s]"
        % (len(translations), sheet_name)
    )

    return translations

 
# GET EXPECTED estoniaN  
def get_expected_estonia(english_text, translations):

    key = normalize(english_text)

    if key not in translations:
        test.fail(
            "English string not found in Excel: [%s]"
            % english_text
        )
        return None

    return translations[key]["estonia"]

 
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
                results
            )
    except:
        pass
    return results
 
# BUILD CROATIAN LOOKUP 
def build_estonia_lookup(translations):

    lookup = {}

    for english_key in translations:
        item = translations[english_key]
        estonia = item["estonia"]
        estonia_key = normalize(estonia)
        if not estonia_key:
            continue

        if estonia_key not in lookup:
            lookup[estonia_key] = []
        lookup[estonia_key].append(item)

    return lookup

 
# AUTOMATIC SCREEN LOCALIZATION CHECK 
def verify_screen_localization(
        root_object,
        screen_name,
        translations):

    test.log("LOCALIZATION CHECK")
    test.log("SCREEN: %s" % screen_name)
 
    # Find visible text objects 
    text_objects = get_all_text_objects( root_object )


    test.log(
        "Visible text objects found: %d"
        % len(text_objects)
    ) 
    # Build estonia lookup 
    estonia_lookup = build_estonia_lookup( translations )

 
    # Counters 
    passed = 0
    not_found = 0

 
    # Prevent duplicate objects
    checked = set()
 
    # Check every visible string 
    for item in text_objects:

        obj = item["object"]
        object_name = item["object_name"]
        actual_estonia = item["text"]
        actual_key = normalize( actual_estonia )

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
 
        # Find estonia text in Excel 
        matches = estonia_lookup.get( actual_key, [] ) 
        
        # Not found        
        if not matches:
            not_found += 1
        
            test.fail(
                "NOT FOUND IN EXCEL | Screen: [%s] | "
                "Object: [%s] | Actual: [%s]"
                % (
                    screen_name,
                    object_name,
                    actual_estonia
                )
            )
        
            continue
 
        # Exact match 
        for match in matches:

            english = match["english"]
            expected = match["estonia"]
            trace_id = match["trace_id"]
            
            test.log("LOCALIZATION MATCH")
            test.log("Object   : %s" % object_name)
            test.log("Trace ID : %s" % trace_id)
            test.log("English  : [%s]" % english)
            test.log("Expected : [%s]" % expected)
            test.log("Actual   : [%s]" % actual_estonia)
 
            # Final exact comparison 
            if normalize(actual_estonia) == normalize(expected):
                test.passes( "PASS: %s -> %s" % ( english, expected ))
                passed += 1

            else:
                test.fail( "FAIL: %s | Expected [%s] | Actual [%s]" % ( english, expected, actual_estonia  ))

  
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

def verify_composite_localization(obj, translations, object_name=""):

    actual_text = get_raw_object_text(obj)

    if not actual_text:
        test.fail("Composite object has no text: %s" % object_name)
        return False

    test.log("")
    test.log("--------------------------------------------")
    test.log("COMPOSITE LOCALIZATION CHECK")
    test.log("Object : %s" % object_name)
    test.log("Actual : [%s]" % actual_text)
    test.log("--------------------------------------------")

    # Prepare translations, longest first
    candidates = []

    for english_key in translations:
        item = translations[english_key]
        expected = item["estonia"]

        if expected:
            candidates.append(item)

    candidates.sort(
        key=lambda item: len(str(item["estonia"])),
        reverse=True
    )

    remaining = actual_text.strip()

    while remaining:

        # Ignore separators between composite strings
        remaining = re.sub(r"^[\s,;]+", "", remaining)

        if not remaining:
            break

        found = False

        for item in candidates:

            expected = str(item["estonia"]).strip()

            if normalize(remaining).startswith(normalize(expected)):

                actual_part = remaining[:len(expected)]

                test.log("COMPOSITE PART MATCH")
                test.log("English  : [%s]" % item["english"])
                test.log("Expected : [%s]" % expected)
                test.log("Actual   : [%s]" % actual_part)
                test.log("Trace ID : %s" % item["trace_id"])

                remaining = remaining[len(expected):]

                found = True
                break

        if not found:

            test.log("COMPOSITE PART NOT FOUND")
            test.log("Remaining: [%s]" % remaining)

            test.fail(
                "FAIL: Composite localization -> [%s]"
                % actual_text
            )

            return False

    test.passes(
        "PASS: Complete composite localization -> [%s]"
        % actual_text
    )

    return True


def main():
    workbook = openpyxl.load_workbook(EXCEL_PATH, data_only=True)
    doubleClick(waitForObject(names.numpad_pushButton_8_NumpadButton), 64, 73, Qt.NoModifier, Qt.LeftButton)
    doubleClick(waitForObject(names.numpad_pushButton_8_NumpadButton), 64, 73, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_settingsButton_QPushButton))
    clickTab(waitForObject(names.settingsScreen_tbSystemInfo_TabWidget), "INFO")
    clickButton(waitForObject(names.gbSystemInformation_pbLanguageSettingsUpdate_QPushButton))

    clickButton(waitForObject(names.languagesFrame_pbEstonia_QPushButton))
    clickButton(waitForObject(names.buttonsFrame_acceptButton_QPushButton))
    clickButton(waitForObject(names.settingsScreen_pbBack_QPushButton))
    
    #extract Localised strings
    translations = load_estonia_strings(workbook, "Profile")
    
    clickButton(waitForObject(names.homeScreen_profilesButton_QPushButton))
    mouseClick(waitForObject(names.topBar_buttonsBar_ButtonsBar), 1185, 12, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.topBar_buttonsBar_ButtonsBar), 671, 21, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.topBar_buttonsBar_ButtonsBar), 114, 21, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.topBar_buttonsBar_ButtonsBar), 244, 30, Qt.NoModifier, Qt.LeftButton)
    
    #evaluate Topbar
    verify_screen_localization(
        waitForObject(
            names.profilesScreen_ProfilesScreen
        ),
        "Profiles Screen - TopBar",
        translations
    )
    
    test.vp("profileScreen_Estonian", "Successful GUI Verification")

    mouseClick(waitForObject(names.profilesScreen_selectUserLabel_QLabel), 600, 16, Qt.NoModifier, Qt.LeftButton)
    
    #evaluate Default user button
    verify_screen_localization(
        waitForObject(names.profilesScreen_selectUserLabel_QLabel),
        "Select Profile to ADD Label",
        translations
    )
    
    clickButton(waitForObject(names.gbProfilesView_defaultUserButton_QPushButton))
    
    #evaluate Default user button
    verify_screen_localization(
        waitForObject(names.profilesScreen_ProfilesScreen),
        "Profiles Screen - Default User",
        translations
    )
    
    clickButton(waitForObject(names.buttonsFrame_addButton_QPushButton))
    
    #verify ADD keyboard
    verify_screen_localization(
        waitForObject(names.keyboardPopup_KeyboardPopup),
        "Keyboard Popup",
        translations
    )
    
    mouseClick(waitForObject(names.keyboardPopup_KeyboardPopup), 986, 37, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.keyboardPopup_wdEdit_WdLineEdit), "user")
    mouseClick(waitForObject(names.keyboardPopup_lbText_QLabel), 50, 28, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.keyboardPopup_centralWidget_QFrame), 629, 28, Qt.NoModifier, Qt.LeftButton)
    
    #verify ADD keyboard
    verify_screen_localization(
        waitForObject(names.keyboardPopup_centralWidget_QFrame),
        "Profile name already exists Popup",
        translations
    )
    
    mouseClick(waitForObject(names.centralWidget_messageLabel_QLabel), 440, 42, Qt.NoModifier, Qt.LeftButton)
    
    verify_composite_localization(
        waitForObject(names.centralWidget_messageLabel_QLabel),
        translations,
        "Already Exists"
    )
    
    clickButton(waitForObject(names.centralWidget_okButton_QPushButton_2))
    mouseClick(waitForObject(names.keyboardPopup_lbText_QLabel_2), 142, 28, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.buttonsFrame_editButton_QPushButton))

    test.vp("profileScreen_Modify_Estonian", "Successful GUI Verification")

    mouseClick(waitForObject(names.profilesScreen_selectUserLabel_QLabel), 696, 8, Qt.NoModifier, Qt.LeftButton)
    
    verify_screen_localization(
        waitForObject(names.profilesScreen_selectUserLabel_QLabel),
        "select Profile to MODIFY Label",
        translations
    )
    
    mouseClick(waitForObjectItem(names.gbProfilesView_profilesView_ProfilesTreeView, "user"), 191, 38, Qt.NoModifier, Qt.LeftButton)
    
    #verify MODIFY keyboard
    verify_screen_localization(
        waitForObject(names.keyboardPopup_KeyboardPopup),
        "Keyboard Popup",
        translations
    )
    
    mouseClick(waitForObject(names.keyboardPopup_KeyboardPopup), 959, 12, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.keyboardPopup_lbText_QLabel), 83, 18, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.keyboardPopup_centralWidget_QFrame), 648, 19, Qt.NoModifier, Qt.LeftButton)    
    mouseClick(waitForObject(names.centralWidget_messageLabel_QLabel), 373, 35, Qt.NoModifier, Qt.LeftButton)
    
    #verify exists popup    
    verify_composite_localization(
        waitForObject(names.centralWidget_messageLabel_QLabel),
        translations,
        "Same name entered popup"
    )
    
    clickButton(waitForObject(names.centralWidget_okButton_QPushButton_2))
    mouseClick(waitForObject(names.keyboardPopup_lbText_QLabel_2), 147, 37, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.buttonsFrame_cancelButton_QPushButton))
    clickButton(waitForObject(names.buttonsFrame_deleteButton_QPushButton))

    test.vp("profileScreen_Delete_Estonian", "Successful GUI Verification")

    mouseClick(waitForObject(names.profilesScreen_selectUserLabel_QLabel), 763, 13, Qt.NoModifier, Qt.LeftButton)
    
    verify_screen_localization(
        waitForObject(names.profilesScreen_selectUserLabel_QLabel),
        "select Profile to DELETE Label",
        translations
    )
    
    mouseClick(waitForObjectItem(names.gbProfilesView_profilesView_ProfilesTreeView, "user"), 191, 50, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.profilesScreen_centralWidget_QFrame), 1057, 16, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.centralWidget_lbDialogTitle_QLabel), 348, 20, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.centralWidget_questionLabel_QLabel), 531, 17, Qt.NoModifier, Qt.LeftButton)
    
    #verify DELETE Popup
    verify_screen_localization(
        waitForObject(names.profilesScreen_centralWidget_QFrame),
        "delete popup text ",
        translations
    )
    
    clickButton(waitForObject(names.buttonsFrame_rejectButton_QPushButton))
    clickButton(waitForObject(names.buttonsFrame_cancelButton_QPushButton))
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton))
