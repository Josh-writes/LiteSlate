"""Build script for creating a standalone LiteSlate .exe using PyInstaller."""

import subprocess
import sys

def build():
    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--onefile",
        "--windowed",
        "--name", "LiteSlate",
        # Uncomment and set the path to an icon file if you have one:
        # "--icon", "assets/icon.ico",
        "liteslate.py",
    ]

    print("Building LiteSlate executable...")
    subprocess.run(cmd, check=True)
    print("Build complete! Executable is in the dist/ folder.")

if __name__ == "__main__":
    build()
