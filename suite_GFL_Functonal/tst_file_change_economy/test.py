import os
import common
import test
def main():
    """Change the path of the to the File Build Path Where You Had Downloaded"""
    
    runtime_path = os.path.expanduser(
        "~/home/ntc/gemini0ct28/"
        "build-gemini-Desktop-Debug"
    )
    
    common.configure_system_type(
        new_type="B",
        runtime_path=runtime_path
    )