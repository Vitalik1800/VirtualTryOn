"""
    Project: Virtual Try-On

    Stage: 3
    Substage: 3.5 - Camera Preview

    Description:
    Video preview widget.
"""

# ===
# Stage 3.5
# Import libraries
# ===

import tkinter as tk

from ui.theme import *


# ===
# Stage 3.5
# Camera Preview
# ===

class CameraPreview(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.preview_label = None
        self.configure_preview()
        self.create_widgets()

    # ===
    # Stage 3.5
    # Configure preview area
    # ===

    def configure_preview(self):
        self.configure(
            corner_radius=PREVIEW_CORNER_RADIUS,
            border_width=PREVIEW_BORDER_WIDTH
        )

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    # ===
    # Stage 3.6
    # Create preview widgets
    # ===

    def create_widgets(self):
        self.preview_label = tk.Label(
            self,
            text="Camera Preview",
            font=TITLE_FONT
        )

        self.preview_label.grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
            sticky="nsew"
        )
