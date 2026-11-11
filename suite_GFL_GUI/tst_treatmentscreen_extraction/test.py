# -*- coding: utf-8 -*-

import names

def inspectQtObject(object_name, obj):
    test.log("Inspecting object: " + object_name)

    for prop_name in ("value", "currentValue", "text"):
        try:
            value = getattr(obj, prop_name)
            test.log("{} = {}".format(prop_name, value))
        except Exception as error:
            test.log("{} unavailable: {}".format(prop_name, error))

    try:
        meta_object = obj.metaObject()

        for index in range(meta_object.propertyCount()):
            prop = meta_object.property(index)
            name = str(prop.name())

            if name in ("value", "currentValue", "text"):
                test.log(
                    "Qt property {} = {}".format(
                        name, prop.read(obj)
                    )
                )
    except Exception as error:
        test.log("Meta-object inspection unavailable: {}".format(error))


def inspectPulseEnergy():
    cylinder = waitForObject(names.valueDrum_Cylinder)

    pulse_energy = str(cylinder.displayedValue).strip()

    test.log("Pulse Energy: {}".format(pulse_energy))

    return pulse_energy

def inspectFrequency():
    cylinder = waitForObject(names.valueDrum_Cylinder_2)

    frequency = str(cylinder.displayedValue).strip()

    test.log("Frequency: {}".format(frequency))

    return frequency


def main():
    doubleClick(waitForObject(names.numpad_pushButton_8_NumpadButton), 77, 67, Qt.NoModifier, Qt.LeftButton)
    doubleClick(waitForObject(names.numpad_pushButton_8_NumpadButton), 77, 67, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.mainFrame_okButton_QPushButton))
    clickButton(waitForObject(names.homeScreen_pbStoneQuickStart_QToolButton))
    mouseClick(waitForObjectItem(names.tabLeftMainPresets_leftPresetsView_PresetListView, "_1"), 561, 57, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.tabRightMainPresets_rightPresetsView_PresetListView, "_1"), 183, 33, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.quickStartScreen_pbContinue_QPushButton))
    
    mouseClick(waitForObject(names.valueDrum_Cylinder), 172, 19, Qt.NoModifier, Qt.LeftButton)   
    mouseClick(waitForObject(names.valueDrum_Cylinder), 28, 35, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.valueDrum_Cylinder), 239, 37, Qt.NoModifier, Qt.LeftButton)
    
    pulse_energy = waitForObject(names.valueDrum_Cylinder)
    inspectQtObject("Pulse energy candidate", pulse_energy)
    
    pulse_energy = inspectPulseEnergy()
    test.log("Actual selected Pulse Energy = {}".format(pulse_energy))
    
    mouseClick(waitForObject(names.valueDrum_Cylinder_2), 132, 39, Qt.NoModifier, Qt.LeftButton)
    frequency = inspectFrequency()
    test.log("Actual selected Frequency = {}".format(frequency))
    mouseClick(waitForObject(names.valueDrum_Cylinder_2), 28, 39, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.valueDrum_Cylinder_2), 232, 34, Qt.NoModifier, Qt.LeftButton)
