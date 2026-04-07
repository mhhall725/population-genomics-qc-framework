import os
import sys

def check_lab_setup():
    print("--- Nuclear Clean Workstation Test ---")
    print(f"Python Version: {sys.version}")
    
    # Check if our professional folders exist
    expected_folders = ['data', 'scripts', 'results', 'notebooks']
    for folder in expected_folders:
        if os.path.exists(folder):
            print(f"✅ Folder '{folder}' is present.")
        else:
            print(f"❌ Folder '{folder}' is missing!")

    print("\nStatus: Ready for v9 Genomic Data.")

if __name__ == "__main__":
    check_lab_setup()
    