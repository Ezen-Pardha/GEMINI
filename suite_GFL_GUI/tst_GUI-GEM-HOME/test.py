import test
from common import *


def main():
    test.log("========== START Home Page Test ==========")

    try:
        navigate_complete_recorded_flow()
        test.passes("PASS:  Home Page test completed successfully")

    except Exception as error:
        test.fail("FAIL: Stone Guided test failed - {}".format(error))
        raise