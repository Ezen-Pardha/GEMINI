# -*- coding: utf-8 -*-

from common import *

def main():
    navigate_service_mode()
    clickTab(waitForObject(names.serviceScreenTabWidget_QTabWidget), "SOFTWARE UPDATE")
    test.vp("Verifying the software update tab")
    test.log("Confirming the program displays the System Checks tab")
