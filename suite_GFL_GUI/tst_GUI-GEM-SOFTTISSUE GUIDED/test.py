from common import *
import test


def main():
    test.log(
        "Starting Soft Tissue Assistant procedure navigation test"
    )
    try:
        navigate_soft_tissue_assistant()
        test.passes(
            "Soft Tissue Assistant navigation test completed"
        )
    except Exception as error:
        test.fail(
            "Soft Tissue Assistant navigation test failed: {}".format(
                error
            )
        )
        raise