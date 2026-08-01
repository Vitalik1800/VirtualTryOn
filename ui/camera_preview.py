"""
    Project: Virtual Try-On

    Stage: 2
    Substage: 2.6 - Create Camera Preview

    Description:
    Camera preview area.
"""

# ===
# Stage 2.6
# Import libraries
# ===

import customtkinter as ctk

from ui.theme import *

# ===
# Stage 2.6
# Camera Preview
# ===

class CameraPreview(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.configure_preview()
        self.create_widgets()

    # ===
    # Stage 2.6
    # Configure preview area
    # ===

    def configure_preview(self):

        self.configure(
            corner_radius=PREVIEW_CORNER_RADIUS,
            border_width=PREVIEW_BORDER_WIDTH
        )

    # ===
    # Stage 2.6
    # Create preview widgets
    # ===

    def create_widgets(self):

        self.preview_label = ctk.CTkLabel(
            self,
            text="Camera Preview",
            font=TITLE_FONT
        )

        self.preview_label.pack(
            expand=True
        )
