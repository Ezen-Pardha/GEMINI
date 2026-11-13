# -*- coding: utf-8 -*-
from common import *
import names

def main():
    enter_login_pin()

    clickButton(waitForObject(names.homeScreen_pbStoneQuickStart_QToolButton))

    mouseClick(
        waitForObjectItem(
            names.tabLeftMainPresets_leftPresetsView_PresetListView, "_1"
        ),
        252, 36, Qt.NoModifier, Qt.LeftButton
    )

    mouseClick(
        waitForObjectItem(
            names.tabRightMainPresets_rightPresetsView_PresetListView, "_1"
        ),
        150, 40, Qt.NoModifier, Qt.LeftButton
    )

    clickButton(waitForObject(names.quickStartScreen_pbContinue_QPushButton))

    # Confirm or acknowledge the preset selection if required
    # Verify the active profile in the top banner
    active_profile = waitForObject(names.topBar_buttonsBar_ButtonsBar_4)

    test.verify(
        active_profile.visible,
        "Active profile banner is displayed on the Treatment screen."
    )

    # Verify the Total Energy section is displayed
    total_energy = waitForObject(names.totalEnergyFrame_nameLabel_QLabel)

    test.verify(
        total_energy.visible,
        "Total Energy label is displayed on the Treatment screen."
    )