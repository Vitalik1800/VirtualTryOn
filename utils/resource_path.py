"""
Project: Virtual Try-On

Resource path utilities.
"""

import os
import sys


def resource_path(*paths):
    """
    Return absolute path to application resource.

    Works both in development mode and
    after building with PyInstaller.
    """

    if getattr(sys, "frozen", False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, *paths)
