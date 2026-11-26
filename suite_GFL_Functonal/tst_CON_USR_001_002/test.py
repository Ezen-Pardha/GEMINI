# -*- coding: utf-8 -*-

import names

PRESET_CONFIGURATIONS = [
    ("frequency", "increment", 1),
    ("frequency", "decrement", 1),
    ("frequency", "increment", 1),
    ("frequency", "decrement", 1),
    ("frequency", "decrement", 2),
    ("frequency", "increment", 2),
    ("pulse", "decrement", 2),
    ("frequency", "decrement", 2),
    ("frequency", "decrement", 1),
    ("frequency", "increment", 2),
    ("frequency", "decrement", 3),
    ("frequency", "decrement", 1),
    ("frequency", "increment", 1),
    ("frequency", "increment", 1),
    ("pulse", "decrement", 1),
    ("frequency", "decrement", 1),
    ("pulse", "increment", 1),
    ("frequency", "increment", 1),
    ("pulse", "decrement", 1),
    ("frequency", "decrement", 1)
]

def create_20_presets():
    for index, config in enumerate(PRESET_CONFIGURATIONS, start=1):
        parameter, action, steps = config
        createUserPreset( index, parameter, action, steps)
    test.log("Completed creation of 20 presets for current user")

def get_user_profile_names(profiles_view):
    model = profiles_view.model()
    profile_names = []

    for row in range(model.rowCount()):
        for column in range(model.columnCount()):
            index = model.index(row, column)
            name = str(model.data(index, Qt.DisplayRole)).strip()

            if name and name != "None":
                profile_names.append(name)

    test.log("Profiles detected: {}".format(profile_names))
    return profile_names


def delete_all_user_profiles():

    clickButton(waitForObject(names.homeScreen_profilesButton_QPushButton))
    profiles_view = waitForObject(names.gbProfilesView_profilesView_ProfilesTreeView)
    deleted_profiles = []

    while True:

        # Read the current list on every iteration
        profile_names = get_user_profile_names(profiles_view)

        # Empty rows are ignored; no profiles is a valid condition
        if not profile_names:
            test.log("No existing user profiles found. Cleanup not required.")
            break

        profile_name = profile_names[0]
        test.log("Deleting user profile: %s" % profile_name)

        clickButton(waitForObject(names.buttonsFrame_deleteButton_QPushButton))

        mouseClick(waitForObjectItem(names.gbProfilesView_profilesView_ProfilesTreeView,profile_name ),
            379, 83, Qt.NoModifier, Qt.LeftButton )

        clickButton(waitForObject(names.buttonsFrame_acceptButton_QPushButton))

        # Wait for the selected profile to disappear
        if not waitFor( "profile_name not in get_user_profile_names(profiles_view)", 5000):
            test.fail( "Profile '%s' was not removed. Stopping cleanup." % profile_name)
            return False

        deleted_profiles.append(profile_name)
        test.log("Successfully deleted profile: %s" % profile_name)
    remaining_profiles = get_user_profile_names(profiles_view)

    test.verify( len(remaining_profiles) == 0, "All existing user profiles deleted")
    test.log( "Total user profiles deleted: %d" % len(deleted_profiles))
    clickButton(waitForObject( names.buttonsBar_homeButton_QPushButton_4))
    return len(remaining_profiles) == 0
    
def create_user_profile(profile_name):

    clickButton(waitForObject(names.homeScreen_profilesButton_QPushButton))
    clickButton(waitForObject(names.buttonsFrame_addButton_QPushButton))

    type(waitForObject(names.keyboardPopup_wdEdit_WdLineEdit), profile_name)
    mouseClick(waitForObject(names.keyboardPopup_lbText_QLabel), 156, 18,
        Qt.NoModifier, Qt.LeftButton)
    snooze(0.5)

    profiles_view = waitForObject(names.gbProfilesView_profilesView_ProfilesTreeView)

    if not waitFor("profile_name in get_user_profile_names(profiles_view)", 5000):
        test.fail("Profile creation failed: %s" % profile_name)
        return False
    test.log("User profile created: %s" % profile_name)

    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton_3))
    return True

def createUserPreset(preset_number, parameter, action, steps=1):
    # Select the parameter to modify
    if parameter == "pulse":
        if action == "increment":
            button = names.pulseEnergyWidget_incrementButton_QPushButton
        elif action == "decrement":
            button = names.pulseEnergyWidget_decrementButton_QPushButton_2
        else:
            raise ValueError("Invalid pulse action: {}".format(action))

    elif parameter == "frequency":
        if action == "increment":
            button = names.frequencyWidget_incrementButton_QPushButton
        elif action == "decrement":
            button = names.frequencyWidget_decrementButton_QPushButton_2
        else:
            raise ValueError("Invalid frequency action: {}".format(action))
    else:
        raise ValueError("Invalid parameter: {}".format(parameter))

    # Change the selected parameter
    for i in range(steps):
        clickButton(waitForObject(button))

    # Save preset
    clickButton(waitForObject(names.pulseModeWidget_saveButton_QPushButton_2))
    clickButton(waitForObject(names.centralWidget_pbName_QPushButton))

    preset_name = "mypreset_{}".format(preset_number)

    type(waitForObject(names.keyboardPopup_wdEdit_WdLineEdit), preset_name)

    mouseClick(waitForObject(names.keyboardPopup_lbText_QLabel), 171, 48,
        Qt.NoModifier,  Qt.LeftButton)

    clickButton(waitForObject(names.pulseModeWidget_saveButton_QPushButton))
    snooze(0.2)
    test.passes("Created user preset: {}".format(preset_name))
    
def delete_all_user_presets():

    preset_view = waitForObject( names.tabSettingsPresetsUserStonePresets_presetListView_PresetListView)

    deleted_count = 0

    while preset_view.presetCount > 0:
        count_before = preset_view.presetCount

        clickButton(waitForObject(names.settingsScreen_deletePresetButton_QPushButton))

        mouseClick( waitForObjectItem(names.tabSettingsPresetsUserStonePresets_presetListView_PresetListView, "_1" ),
            475, 45, Qt.NoModifier, Qt.LeftButton)

        clickButton(waitForObject(names.buttonsFrame_acceptButton_QPushButton))

        # Wait until the model reflects the deletion
        waitFor("preset_view.presetCount < count_before", 5000)

        deleted_count += 1

        test.log("Deleted preset %d; remaining: %d" %
                 (deleted_count, preset_view.presetCount))

    test.verify(
        preset_view.presetCount == 0,
        "All user presets deleted"
    )
    
def find_profile_on_current_page(profiles_view, profile_name):

    model = profiles_view.model()
    for row in range(model.rowCount()):
        for column in range(model.columnCount()):

            index = model.index(row, column)
            name = str(model.data(index, Qt.DisplayRole)).strip()
            if name == profile_name:
                return index
    return None

def select_user_profile(profile_name):

    clickButton(waitForObject(names.homeScreen_profilesButton_QPushButton))
    profiles_view = waitForObject(names.gbProfilesView_profilesView_ProfilesTreeView)

    target_index = None

    # Maximum 3 pages for 20 profiles (8 profiles per page)
    for page_number in range(1, 4):
        snooze(0.3)

        test.log("Searching for {} on profile page {}".format(profile_name, page_number))

        target_index = find_profile_on_current_page(profiles_view, profile_name)

        if target_index is not None:
            break

        # Replace with the actual Next Page object from Object Spy
        clickButton(waitForObject(names.scrollFrame_nextPageButton_QPushButton))

    if target_index is None:
        test.fail("Profile {} not found on any page".format(profile_name))
        return False

    rect = profiles_view.visualRect(target_index)
    center = rect.center()

    mouseClick(profiles_view, center.x, center.y, Qt.NoModifier,Qt.LeftButton)

    clickButton(waitForObject(names.buttonsFrame_continueButton_QPushButton))
    snooze(0.3)
    test.passes("Selected user profile: {}".format(profile_name))
    return True
    
def open_quick_start():

    clickButton(waitForObject(names.homeScreen_pbStoneQuickStart_QToolButton))
    mouseClick(waitForObjectItem(names.tabLeftMainPresets_leftPresetsView_PresetListView, "_1" ),
        567, 69, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.tabRightMainPresets_rightPresetsView_PresetListView, "_1"),
        108, 43, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.quickStartScreen_pbContinue_QPushButton))
    snooze(0.5)
    
def verify_21st_preset_limit():

    test.log("Attempting to save the 21st preset for USER20")

    # Change a parameter to make this a genuine save attempt
    clickButton(waitForObject(names.frequencyWidget_incrementButton_QPushButton))

    # Start the save operation

    clickButton(waitForObject(names.pulseModeWidget_saveButton_QPushButton_2))
    if test.vp("maximumPresetsPopup", "Successful"):
        test.passes("Successful Confirmation of Program reporting error message of maximum user Preset")
    else:
        test.fail("Failed reporting error message of maximum user Preset")
    clickButton(waitForObject(names.centralWidget_okButton_QPushButton))

def main():
    doubleClick(waitForObject(names.numpad_pushButton_8_NumpadButton), 40, 59, Qt.NoModifier, Qt.LeftButton)
    doubleClick(waitForObject(names.numpad_pushButton_8_NumpadButton), 40, 59, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton))
    
    # clickButton(waitForObject(names.scrollFrame_nextPageButton_QPushButton))
    # clickButton(waitForObject(names.scrollFrame_backPageButton_QPushButton))
    
    #deletion of user profiles
    delete_all_user_profiles()

    for user_number in range(1, 21):

        profile_name = "USER{}".format(user_number)
        test.log("STARTING {}".format(profile_name))
        
        if not create_user_profile(profile_name):
            test.fail("Stopping: could not create {}".format(profile_name))
            break

        if not select_user_profile(profile_name):
            test.fail("Stopping: could not select {}".format(profile_name))
            break

        open_quick_start()
        create_20_presets()
        test.log("COMPLETED {}".format(profile_name))
        
        if user_number == 20:
            verify_21st_preset_limit()
        clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton_5))
    test.log("Completed creation of 20 users with 20 presets each")
    
    clickButton(waitForObject(names.buttonsBar_homeButton_QPushButton_5))
