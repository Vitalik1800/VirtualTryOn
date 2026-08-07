"""
Project: Virtual Try-On

Stage: 2
Substage: 2.8 - Application Settings

Description:
Application configuration and default parameters.
"""

from utils.resource_path import resource_path

# ===
# Stage 2.8
# Application
# ===

APP_NAME = "Virtual Try-On"
APP_VERSION = "1.0.0"

# ===
# Stage 2.8
# Camera
# ===

DEFAULT_CAMERA_INDEX = 0
CAMERA_WIDTH = 640
CAMERA_HEIGHT = 480
FPS_LIMIT = 40

# ===
# Stage 2.8
# Recording
# ===

ENABLE_AUTO_RECORDING = False
RECORDING_FPS = 30
RECORDING_FORMAT = "mp4"
RECORDINGS_DIRECTORY = "recordings"

# ===
# Stage 2.8
# Images
# ===

SCREENSHOTS_DIRECTORY = "screenshots"
OUTPUT_DIRECTORY = "output"

# ===
# Stage 2.8
# Assets
# ===

ASSETS_DIRECTORY = resource_path("assets")

ACCESSORIES_DIRECTORY = resource_path(
    "assets",
    "accessories"
)

GLASSES_DIRECTORY = resource_path(
    "assets",
    "accessories",
    "glasses"
)

HATS_DIRECTORY = resource_path(
    "assets",
    "accessories",
    "hats"
)

MASKS_DIRECTORY = resource_path(
    "assets",
    "accessories",
    "masks"
)

# ===
# Stage 2.8
# Default Values
# ===

DEFAULT_CATEGORY = "Glasses"
DEFAULT_ACCESSORY = None

# ===
# Stage 2.8
# Files
# ===

ICON_PATH = resource_path(
    "assets",
    "icons",
    "app.ico"
)

README_FILE = resource_path(
    "README.md"
)
