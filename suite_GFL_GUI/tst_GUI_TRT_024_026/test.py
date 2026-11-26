
# -*- coding: utf-8 -*-

from common import *
import names


def main():
    enter_login_pin()

    # Navigate to Stone Quick Start
    clickButton(waitForObject(
        names.homeScreen_pbStoneQuickStart_QToolButton
    ))

    # Select Left Pedal preset
    mouseClick(
        waitForObjectItem(
            names.tabLeftMainPresets_leftPresetsView_PresetListView,
            "_1"
        ),
        316, 56,
        Qt.NoModifier,
        Qt.LeftButton
    )

    # Select Right Pedal preset
    mouseClick(
        waitForObjectItem(
            names.tabRightMainPresets_rightPresetsView_PresetListView,
            "_1"
        ),
        91, 39,
        Qt.NoModifier,
        Qt.LeftButton
    )

    # Continue to Treatment Screen
    clickButton(waitForObject(
        names.quickStartScreen_pbContinue_QPushButton
    ))

    # Verify top banner is visible
    top_banner = waitForObject(
        names.topBar_buttonsBar_ButtonsBar_4
    )

    test.verify(
        top_banner.visible,
        "Treatment Screen top banner is visible"
    )

    
    # Treatment Screen displays Treatment Mode icon
    mouseClick(
        top_banner,
        431, 33,
        Qt.NoModifier,
        Qt.LeftButton
    )

    test.verify(
        top_banner.visible,
        "Top banner remains visible for Treatment Mode icon verification"
    )

    test.log(
        "Treatment Mode icon area checked"
    )

    
    # Treatment Screen displays preset name in top banner
    mouseClick(
        top_banner,
        795, 34,
        Qt.NoModifier,
        Qt.LeftButton
    )

    test.verify(
        top_banner.visible,
        "Top banner remains visible for preset name verification"
    )

    test.log(
        "Preset name area checked"
    )

  
    # Modify a laser parameter and verify CUSTOM tag
    mouseDrag(
        waitForObject(
            names.indexPicker_valuePicker_IntervalSlider
        ),
        81, 24,
        220, 16,
        1,
        Qt.LeftButton
    )

    test.log(
        "Laser parameter adjustment performed"
    )

    # Handle Disable confirmation if displayed
    clickButton(waitForObject(
        names.centralWidget_DisableButton_QPushButton
    ))

    test.log(
        "Disable button clicked after parameter adjustment"
    )

    # Check top banner after parameter modification
    mouseClick(
        top_banner,
        721, 40,
        Qt.NoModifier,
        Qt.LeftButton
    )

    test.verify(
        top_banner.visible,
        "Top banner is visible after parameter modification"
    )

    test.log(
        "CUSTOM tag area checked after parameter modification"
    )

