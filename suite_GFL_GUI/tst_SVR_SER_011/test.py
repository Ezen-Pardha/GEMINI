# -*- coding: utf-8 -*-

from common import *

def main():
    navigate_service_mode()
    clickTab(waitForObject(names.serviceScreenTabWidget_QTabWidget), "SOFTWARE UPDATE")

    #test.compare(waitForObjectExists(names.qt_tabwidget_tabbar_SOFTWARE_UPDATE_TabItem).text, "SOFTWARE UPDATE")

    if test.compare(waitForObjectExists(names.qt_tabwidget_tabbar_SOFTWARE_UPDATE_TabItem).text, "SOFTWARE UPDATE"):

        test.passes("screen verified")
    else:

        test.fail("screen verification failed")
