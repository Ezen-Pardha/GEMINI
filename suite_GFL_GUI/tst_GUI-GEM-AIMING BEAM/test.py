# -*- coding: utf-8 -*-
from common import *
import names

def main():
    enter_login_pin()

    clickButton(waitForObject(names.homeScreen_pbSoftTissueQuickStart_QToolButton))

    mouseClick(
        waitForObjectItem(
            names.tabLeftMainPresets_leftPresetsView_PresetListView, "_1"
        ),
        259, 56, Qt.NoModifier, Qt.LeftButton
    )

    clickTab(
        waitForObject(names.quickStartScreen_tbRightPedalTreatment_TabWidget),
        "SELECT RIGHT PEDAL TREATMENT"
    )

    clickTab(
        waitForObject(names.quickStartScreen_tbLeftPedalTreatment_TabWidget),
        "SELECT LEFT PEDAL TREATMENT"
    )

    mouseClick(
        waitForObjectItem(
            names.tabRightMainPresets_rightPresetsView_PresetListView, "_1"
        ),
        108, 66, Qt.NoModifier, Qt.LeftButton
    )

    clickButton(waitForObject(names.quickStartScreen_pbContinue_QPushButton))
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton_2))

    aiming_beam_button = waitForObject(
        names.bottomBar_aimingBeamButton_AimingBeamModeButton
    )

    test.verify(
        aiming_beam_button.visible,
        "Aiming Beam button is displayed on the Treatment screen."
    )

    clickButton(aiming_beam_button)

    clickButton(waitForObject(names.buttonsFrame_acceptButton_QPushButton_5))

    clickButton(
        waitForObject(names.bottomBar_aimingBeamButton_AimingBeamModeButton)
    )