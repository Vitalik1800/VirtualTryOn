"""
    Project: Virtual Try-On

    Stage: 2
    Substage: 2.2 - Configure Application Theme

    Descrption:
    Application colors, fonts and UI constants.
"""

# ===
# Stage 2.2
# Import Library
# ===

import customtkinter as ctk

BUTTON_WIDTH = 140
BUTTON_HEIGHT = 38
BUTTON_CORNER_RADIUS = 8

PADDING_LARGE = 20
PADDING = 10
PADDING_SMALL = 5

SIDEBAR_WIDTH = 300

# ===
# Stage 2.2
# Appearance
# ===

APPEARANCE_MODE = "System"
COLOR_THEME = "blue"

# ===
# Stage 2.2
# Window
# ===

WINDOW_TITLE = "Virtual Try-On"

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 750

MIN_WIDTH = 1000
MIN_HEIGHT = 650

# ===
# Stage 2.2
# Fonts
# ===

FONT_FAMILY = "Segoe UI"

TITLE_FONT = (FONT_FAMILY, 24, "bold")
HEADER_FONT = (FONT_FAMILY, 18, "bold")
TEXT_FONT = (FONT_FAMILY, 14)
BUTTON_FONT = (FONT_FAMILY, 14, "bold")
STATUS_FONT = (FONT_FAMILY, 12)

# ===
# Stage 2.2
# Colors
# ===

# Primary

PRIMARY_COLOR = "#2563EB"
PRIMARY_HOVER_COLOR = "#1D4ED8"

# Success

SUCCESS_COLOR = "#16A34A"
SUCCESS_HOVER_COLOR = "#15803D"

# Warning

WARNING_COLOR = "#F59E0B"
WARNING_HOVER_COLOR = "#D97706"

# Error

ERROR_COLOR = "#DC2626"
ERROR_HOVER_COLOR = "#B91C1C"

# Info

INFO_COLOR = "#0EA5E9"
INFO_HOVER_COLOR = "#0284C7"

# About

ABOUT_COLOR = "#7C3AED"
ABOUT_HOVER_COLOR = "#6D28D9"

# ===
# Stage 2.2
# Camera Preview
# ===

PREVIEW_WIDTH = 900
PREVIEW_HEIGHT = 600

PREVIEW_BORDER_WIDTH = 2
PREVIEW_CORNER_RADIUS = 10

# ===
# Stage 2.2
# Configure CustomTkinter
# ===

ctk.set_appearance_mode(APPEARANCE_MODE)
ctk.set_default_color_theme(COLOR_THEME)
