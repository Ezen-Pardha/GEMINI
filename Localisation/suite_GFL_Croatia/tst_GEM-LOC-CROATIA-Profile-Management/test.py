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


# LOAD ENGLISH -> Croatia TRANSLATIONS
def load_croatia_strings(workbook, sheet_name):

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

    test.log(
        "Loaded %d English -> croatia translations from sheet [%s]"
        % (len(translations), sheet_name)
    )

    return translations

def get_expected_croatia(english_text, translations):

    key = normalize(english_text)
    if key not in translations:
        test.fail( "English string not found in Excel: [%s]" % english_text)

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


    croatia_lookup = build_croatia_lookup( translations)

    passed = 0
    not_found = 0

    checked = set()


    for item in text_objects:
        obj = item["object"]
        object_name = item["object_name"]
        actual_spanish = item["text"]

        actual_key = normalize( actual_spanish)

        # Ignore empty
        if not actual_key:
            continue

        # Avoid duplicate
        unique_key = ( object_name, actual_key)

        if unique_key in checked:
            continue

        checked.add(unique_key)
        matches = croatia_lookup.get( actual_key, [] )

        if not matches:
            test.log("NOT FOUND IN EXCEL")
            test.log("Object : %s" % object_name)
            test.log("Actual : [%s]" % actual_spanish)
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
            test.log("Actual   : [%s]" % actual_spanish)

            if normalize(actual_spanish) == normalize(expected):
                test.passes("PASS: %s -> %s" % (english, expected))
                passed += 1

            else:
                test.fail("FAIL: %s | Expected [%s] | Actual [%s]"  % ( english, expected, actual_croatia ))


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
    
    test.log("RAW COMPOSITE TEXT:")
    test.log(repr(actual_text))

    if not actual_text:
        test.fail("Composite object has no text: %s" % object_name)
        return False

    test.log("COMPOSITE LOCALIZATION CHECK")
    test.log("Object : %s" % object_name)
    test.log("Actual : [%s]" % actual_text)

    # Prepare translations, longest first
    candidates = []

    for english_key in translations:
        item = translations[english_key]
        expected = item["croatia"]

        if expected:
            candidates.append(item)

    candidates.sort(
        key=lambda item: len(str(item["croatia"])),
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
            expected = str(item["croatia"]).strip()
            
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

    clickButton(waitForObject(names.languagesFrame_pbCroatia_QPushButton))
    clickButton(waitForObject(names.buttonsFrame_acceptButton_QPushButton))
    clickButton(waitForObject(names.settingsScreen_pbBack_QPushButton))
    
    #extract Localised strings
    translations = load_croatia_strings(workbook,"Profile")
    
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

    test.vp("profileScreen", "Successful GUI verification")

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

    test.vp("profileScreen_Modify_Croatia", "Successful GUI verification")

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

    test.vp("profileScreen_Delete_Croatia", "Successful GUI verification")

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
    
    workbook.close()
