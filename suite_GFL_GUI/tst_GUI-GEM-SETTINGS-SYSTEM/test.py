# -*- coding: utf-8 -*-

from common import *
import names


def main():
    test.log("START: GUI-GEM-SETTINGS-SYSTEM")
    test.log("Preparing application and opening System Settings")

    enter_login_pin()
    navigate_to_settings()

    brightnessSlider = waitForObject(names.systemsettingframe_slBrightness_StatableSlider)
    volumeSlider = waitForObject(names.systemsettingframe_slVolume_StatableSlider)
    aimingBeamSlider = waitForObject(names.aimingbeamsettingframe_slAimingBeamDefaultLevel_StatableSlider)

    scrollTo(brightnessSlider, 100)
    sendEvent("QMouseEvent", brightnessSlider, QEvent.MouseButtonDblClick, 378, 19, Qt.LeftButton, 1, 0)
    openContextMenu(brightnessSlider, 378, 19, 1)
    scrollTo(brightnessSlider, 100)
    mouseDrag(brightnessSlider, 378, 19, 60, 7, 1, Qt.LeftButton)
    doubleClick(waitForObject(names.wdSystemSettingsLayout_100_QLabel), 47, 1, Qt.NoModifier, Qt.LeftButton)
    openContextMenu(waitForObject(names.wdSystemSettingsLayout_100_QLabel), 47, 1, 1)
    openContextMenu(waitForObject(names.wdSystemSettingsLayout_100_QLabel), 48, 2, 1)

    scrollTo(volumeSlider, 88)
    sendEvent("QMouseEvent", volumeSlider, QEvent.MouseButtonDblClick, 322, 15, Qt.LeftButton, 1, 0)
    openContextMenu(volumeSlider, 322, 15, 1)
    scrollTo(volumeSlider, 94)
    openContextMenu(volumeSlider, 370, 21, 1)
    scrollTo(volumeSlider, 100)
    openContextMenu(volumeSlider, 401, 25, 1)
    scrollTo(volumeSlider, 100)

    sendEvent("QMouseEvent", aimingBeamSlider, QEvent.MouseButtonDblClick, 358, 16, Qt.LeftButton, 1, 0)
    openContextMenu(aimingBeamSlider, 358, 16, 1)
    scrollTo(aimingBeamSlider, 10)
    mouseDrag(aimingBeamSlider, 358, 16, 53, -32, 1, Qt.LeftButton)

    test.log("STEP 1: Verify Settings screen")
    test.vp("System Settings Tab")

    test.log("GUI-SET-007: Decrease volume using buttons")
    clickButton(waitForObject(names.systemsettingframe_pbIncreaseVolume_QPushButton))
    clickButton(waitForObject(names.systemsettingframe_pbIncreaseVolume_QPushButton))
    test.vp("Decreases Volume using Button")

    test.log("GUI-SET-007: Increase volume using buttons")
    clickButton(waitForObject(names.systemsettingframe_pbIncreaseVolume_QPushButton_2))
    clickButton(waitForObject(names.systemsettingframe_pbIncreaseVolume_QPushButton_2))
    test.vp("Increases Volume using Button")

    test.log("GUI-SET-008: Decrease volume using slider")
    scrollTo(volumeSlider, 74)
    test.vp("Decreases Volume using Slider")

    test.log("GUI-SET-008: Increase volume using slider")
    scrollTo(volumeSlider, 100)
    test.vp("Increases Volume using Slider")

    test.log("GUI-SET-009: Set volume slider to minimum")
    scrollTo(volumeSlider, 25)
    volumeSlider = waitForObject(names.systemsettingframe_slVolume_StatableSlider)
    test.log("Minimum Volume Value: expected == 25, actual == " + str(volumeSlider.value))
    test.verify(volumeSlider.value == 25, "Minimum volume must equal 25")
    test.vp("Minimum Volume Value")

    test.log("GUI-SET-009: Set volume slider to maximum")
    scrollTo(volumeSlider, 100)
    volumeSlider = waitForObject(names.systemsettingframe_slVolume_StatableSlider)
    test.log("Maximum Volume Value: expected == 100, actual == " + str(volumeSlider.value))
    test.verify(volumeSlider.value == 100, "Maximum volume must equal 100")
    test.vp("Maximum Volume Value")

    test.log("GUI-SET-010: Decrease brightness using button")
    doubleClick(waitForObject(names.systemsettingframe_pbDecreaseBrightness_QPushButton), 34, 30, Qt.NoModifier, Qt.LeftButton)
    test.vp("Decreases Brightness using Button")

    test.log("GUI-SET-010: Increase brightness using button")
    doubleClick(waitForObject(names.systemsettingframe_pbIncreaseBrightness_QPushButton), 28, 24, Qt.NoModifier, Qt.LeftButton)
    test.vp("Increases Brightness using Button")

    test.log("GUI-SET-011: Decrease brightness using slider")
    sendEvent("QContextMenuEvent", brightnessSlider, QContextMenuEvent.Mouse, 376, 15, 3)
    openContextMenu(brightnessSlider, 279, 17, 1)
    scrollTo(brightnessSlider, 74)
    mouseDrag(brightnessSlider, 279, 17, -39, 7, 1, Qt.LeftButton)
    test.vp("Decreases Brightness using Slider")

    test.log("GUI-SET-011: Increase brightness using slider")
    scrollTo(brightnessSlider, 100)
    test.vp("Increases Brightness using Slider")

    test.log("GUI-SET-012: Set brightness slider to minimum")
    scrollTo(brightnessSlider, 25)
    brightnessSlider = waitForObject(names.systemsettingframe_slBrightness_StatableSlider)
    test.log("Minimum Brightness Value: expected == 25, actual == " + str(brightnessSlider.value))
    test.verify(brightnessSlider.value == 25, "Minimum brightness must equal 25")
    test.vp("Minimum Brightness Value")

    test.log("GUI-SET-012: Set brightness slider to maximum")
    scrollTo(brightnessSlider, 100)
    brightnessSlider = waitForObject(names.systemsettingframe_slBrightness_StatableSlider)
    test.log("Maximum Brightness Value: expected == 100, actual == " + str(brightnessSlider.value))
    test.verify(brightnessSlider.value == 100, "Maximum brightness must equal 100")
    test.vp("Maximum Brightness Value")

    return_home_from_settings()

    test.log("FINAL VALIDATION: GUI-SET-007 to GUI-SET-012 completed")
    test.log("GUI-GEM-SETTINGS-SYSTEM test execution finished")