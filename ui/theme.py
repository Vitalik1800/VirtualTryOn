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

BUTTON_FONT = (
    "Segoe UI",
    14,
    "bold"
)

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

PRIMARY_COLOR = "#2563EB"
SECONDARY_COLOR = "#1E40AF"

SUCCESS_COLOR = "#16A34A"
WARNING_COLOR = "#F59E0B"
ERROR_COLOR = "#DC2626"

BACKGROUND_LIGHT = "#F5F5F5"
BACKGROUND_DARK = "#202020"

SIDEBAR_COLOR = "#2B2B2B"
FRAME_COLOR = "#303030"

TEXT_LIGHT = "#FFFFFF"
TEXT_DARK = "#1F2937"

HOVER_COLOR = "#1E88E5"
HOVER_COLOR_ERROR = "#B91C1C"

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
