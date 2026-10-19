from common import *
import test
import names

SOFT_TISSUE_PRESETS = [
    "Soft Tissue 1",
    "Soft Tissue 2",
    "Soft Tissue 3",
    "Soft Tissue 4",
    "Soft Tissue 5",
    "Soft Tissue 6",
]

STONE_PRESETS = [
    "Stone 1",
    "Stone 2",
    "Stone 3",
    "Stone 4",
    "Stone 5",
    "Stone 6",
]


def test_create_soft_tissue_presets():
    test.log("========== CREATE SOFT TISSUE PRESETS ==========")

    navigate_to_preset_category("SOFT TISSUE")

    create_six_presets(
        "SOFT TISSUE",
        SOFT_TISSUE_PRESETS,

    #     sendEvent("QMoveEvent", waitForObject(names.o_ScreenSwitcher), 0, 130, 754, 154)
    # clickButton(waitForObject(names.settingsScreen_addButton_QPushButton))

        names.settingsScreen_addButton_QPushButton,
        names.keyboardPopup_wdEdit_WdLineEdit,
        names.pulseModeWidget_saveButton_QPushButton,
    )

    if not verify_six_presets("SOFT TISSUE"):
        raise AssertionError("Soft Tissue preset verification failed")


def test_create_stone_presets():
    test.log("========== CREATE STONE PRESETS ==========")

    navigate_to_preset_category("STONE")

    create_six_presets(
        "STONE",
        STONE_PRESETS,
        names.settingsScreen_addButton_QPushButton,
        names.keyboardPopup_wdEdit_WdLineEdit,
        names.pulseModeWidget_saveButton_QPushButton,
    )

    if not verify_six_presets("STONE"):
        raise AssertionError("Stone preset verification failed")


def test_edit_soft_tissue_preset():
    test.log("========== EDIT SOFT TISSUE PRESET ==========")

    edit_preset(
        "SOFT TISSUE",
        "Soft Tissue 1",
        "Soft Tissue Edited",
    )


def test_edit_stone_preset():
    test.log("========== EDIT STONE PRESET ==========")

    edit_preset(
        "STONE",
        "Stone 1",
        "Stone Edited",
    )


def test_delete_soft_tissue_preset():
    test.log("========== DELETE SOFT TISSUE PRESET ==========")

    delete_preset("SOFT TISSUE", "Soft Tissue Edited")


def test_delete_stone_preset():
    test.log("========== DELETE STONE PRESET ==========")

    delete_preset("STONE", "Stone Edited")


def test_verify_both_categories():
    test.log("========== VERIFY FINAL PRESET COUNTS ==========")

    navigate_to_preset_category("SOFT TISSUE")

    if not verify_six_presets("SOFT TISSUE"):
        raise AssertionError(
            "Soft Tissue does not contain exactly six presets"
        )

    navigate_to_preset_category("STONE")

    if not verify_six_presets("STONE"):
        raise AssertionError(
            "Stone does not contain exactly six presets"
        )

    test.passes("Both categories contain exactly six presets")


def main():
    test.log("==============================================")
    test.log("STARTING PRESET CREATE / EDIT / DELETE TEST")
    test.log("==============================================")

    enter_login_pin()

    test_create_soft_tissue_presets()
    test_create_stone_presets()

    test_edit_soft_tissue_preset()
    test_edit_stone_preset()

    test_delete_soft_tissue_preset()
    test_delete_stone_preset()

    test_verify_both_categories()

    test.passes(
        "Preset create, edit, delete and verification tests completed"
    )

