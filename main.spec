# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import (
    collect_data_files,
    collect_dynamic_libs,
    collect_submodules
)

# ==========================
# MediaPipe
# ==========================

mediapipe_datas = collect_data_files("mediapipe")
mediapipe_binaries = collect_dynamic_libs("mediapipe")
mediapipe_hidden = collect_submodules("mediapipe")

# ==========================
# OpenCV
# ==========================

opencv_datas = collect_data_files("cv2")
opencv_binaries = collect_dynamic_libs("cv2")

# ==========================
# Analysis
# ==========================

a = Analysis(
    ["main.py"],

    pathex=[],

    binaries=
        mediapipe_binaries
        +
        opencv_binaries,

    datas=[
        ("assets", "assets"),
    ]
    +
    mediapipe_datas
    +
    opencv_datas,

    hiddenimports=
        mediapipe_hidden,

    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],

    excludes=[
        "PyQt5",
        "PyQt6",
        "PySide2",
        "PySide6",
    ],

    noarchive=False,
    optimize=0,
)

# ==========================
# PYZ
# ==========================

pyz = PYZ(
    a.pure
)

# ==========================
# EXE
# ==========================

exe = EXE(

    pyz,

    a.scripts,

    [],

    exclude_binaries=True,

    name="Virtual Try-On",

    icon="assets/icons/app.ico",

    console=False,

    debug=False,

    bootloader_ignore_signals=False,

    strip=False,

    upx=True,

    disable_windowed_traceback=False,

    argv_emulation=False,

    target_arch=None,

    codesign_identity=None,

    entitlements_file=None,
)

# ==========================
# Collect
# ==========================

coll = COLLECT(

    exe,

    a.binaries,

    a.datas,

    strip=False,

    upx=True,

    upx_exclude=[],

    name="Virtual Try-On",
)