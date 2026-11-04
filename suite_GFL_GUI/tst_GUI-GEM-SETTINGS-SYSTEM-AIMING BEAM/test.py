# -*- coding: utf-8 -*-

from common import *
import names


def main():
    test.log("START: GUI-GEM-SETTINGS-AIMING-BEAM")
    test.log("Preparing application and opening Aiming Beam Settings")

    enter_login_pin()
    navigate_to_settings()

    test.log("Opened Settings")
    test.log("STEP 1: Verify Aiming Beam Settings screen")
    test.vp("Aiming Beam Settings Tab")

    brightnessSlider = waitForObject(names.systemsettingframe_slBrightness_StatableSlider)
    volumeSlider = waitForObject(names.systemsettingframe_slVolume_StatableSlider)
    aimingBeamSlider = waitForObject(names.aimingbeamsettingframe_slAimingBeamDefaultLevel_StatableSlider)

    test.log("GUI-SET-013: Prepare brightness slider")
    scrollTo(brightnessSlider, 100)
    sendEvent("QMouseEvent", brightnessSlider, QEvent.MouseButtonDblClick, 378, 19, Qt.LeftButton, 1, 0)
    openContextMenu(brightnessSlider, 378, 19, 1)
    mouseDrag(brightnessSlider, 378, 19, 60, 7, 1, Qt.LeftButton)
    doubleClick(waitForObject(names.wdSystemSettingsLayout_100_QLabel), 47, 1, Qt.NoModifier, Qt.LeftButton)
    openContextMenu(waitForObject(names.wdSystemSettingsLayout_100_QLabel), 47, 1, 1)
    openContextMenu(waitForObject(names.wdSystemSettingsLayout_100_QLabel), 48, 2, 1)

    test.log("GUI-SET-013: Prepare volume slider")
    scrollTo(volumeSlider, 88)
    sendEvent("QMouseEvent", volumeSlider, QEvent.MouseButtonDblClick, 322, 15, Qt.LeftButton, 1, 0)
    openContextMenu(volumeSlider, 322, 15, 1)
    scrollTo(volumeSlider, 94)
    openContextMenu(volumeSlider, 370, 21, 1)
    scrollTo(volumeSlider, 100)
    openContextMenu(volumeSlider, 401, 25, 1)
    scrollTo(volumeSlider, 100)

    test.log("GUI-SET-013: Prepare aiming beam slider")
    sendEvent("QMouseEvent", aimingBeamSlider, QEvent.MouseButtonDblClick, 358, 16, Qt.LeftButton, 1, 0)
    openContextMenu(aimingBeamSlider, 358, 16, 1)
    mouseDrag(aimingBeamSlider, 358, 16, 53, -32, 1, Qt.LeftButton)

    test.log("GUI-SET-013: Decrease aiming beam intensity using button")
    clickButton(waitForObject(names.aimingbeamsettingframe_pbDecreaseAimingBeamDefaultLevel_QPushButton))
    clickButton(waitForObject(names.aimingbeamsettingframe_pbDecreaseAimingBeamDefaultLevel_QPushButton))
    test.log("Decreased aiming beam intensity using button")
    test.vp("Decreases Intensity Level using Button")

    test.log("GUI-SET-013: Increase aiming beam intensity using button")
    doubleClick(waitForObject(names.aimingbeamsettingframe_pbIncreaseAimingBeamDefaultLevel_QPushButton), 38, 33, Qt.NoModifier, Qt.LeftButton)
    test.log("Increased aiming beam intensity using button")
    test.vp("Increases Intensity Level using Button")

    test.log("GUI-SET-014: Adjust aiming beam intensity using slider")
    sendEvent("QMouseEvent", aimingBeamSlider, QEvent.MouseButtonDblClick, 360, 14, Qt.LeftButton, 1, 0)
    mouseDrag(aimingBeamSlider, 360, 14, -74, 16, 1, Qt.LeftButton)
    openContextMenu(aimingBeamSlider, 278, 30, 1)
    mouseDrag(aimingBeamSlider, 278, 30, -321, -16, 1, Qt.LeftButton)
    test.log("Adjusted aiming beam intensity using slider")
    test.vp("Minimum Intensity Level using Slider")

    test.log("GUI-SET-014: Set aiming beam intensity to minimum")
    scrollTo(aimingBeamSlider, 1)
    sendEvent("QMouseEvent", aimingBeamSlider, QEvent.MouseButtonDblClick, 32, 15, Qt.LeftButton, 1, 0)
    openContextMenu(aimingBeamSlider, 32, 15, 1)
    test.log("Set aiming beam intensity to minimum")
    test.vp("Minimum Intensity Level using Slider")

    test.log("GUI-SET-014: Set aiming beam intensity to maximum")
    scrollTo(aimingBeamSlider, 10)
    openContextMenu(aimingBeamSlider, 448, -1, 1)
    test.log("Set aiming beam intensity to maximum")
    test.vp("Maximum Intensity Level using Slider")

    test.log("GUI-SET-015: Disable aiming beam")
    clickButton(waitForObject(names.aimingbeamsettingframe_pbAimingBeamOff_QPushButton))
    test.log("Selected Aiming Beam Disabled mode")
    test.vp("Aiming Beam Disabled Mode")

    test.log("GUI-SET-015: Enable aiming beam")
    clickButton(waitForObject(names.aimingbeamsettingframe_pbAimingBeamOn_QPushButton))
    test.log("Selected Aiming Beam On mode")

    return_home_from_settings()

    test.log("FINAL VALIDATION: GUI-SET-013 to GUI-SET-015 completed")
    test.log("Aiming Beam Settings test execution finished")