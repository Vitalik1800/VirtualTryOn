"""
    Project: Virtual Try-On

    Stage: 2
    Substage: 2.4 - Create Toolbar

    Description:
    Top toolbar of the application.
"""

# ===
# Stage 2.4
# Import libraries
# ===

import customtkinter as ctk

from ui.theme import *

# ===
# Stage 2.4
# Toolbar class
# ===

class Toolbar(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.configure_toolbar()
        self.create_widgets()

    # ===
    # Stage 2.4
    # Configure toolbar
    # ===

    def configure_toolbar(self):

        self.configure(
            height=70,
            corner_radius=0
        )

        self.grid_columnconfigure(2, weight=1)

    # ===
    # Stage 2.4
    # Create toolbar widgets
    # ===

    def create_widgets(self):

        # Logo

        self.logo_label = ctk.CTkLabel(
            self,
            text="🕶",
            font=("Segoe UI Emoji", 28)
        )

        self.logo_label.grid(
            row=0,
            column=0,
            padx=(PADDING_LARGE, PADDING),
            pady=15
        )

        # Application title

        self.title_label = ctk.CTkLabel(
            self,
            text=WINDOW_TITLE,
            font=HEADER_FONT
        )

        self.title_label.grid(
            row=0,
            column=1,
            padx=(0, PADDING_LARGE)
        )

        # Start button

        self.start_button = ctk.CTkButton(
            self,
            text="Start Camera",
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            corner_radius=BUTTON_CORNER_RADIUS,
            font=BUTTON_FONT
        )

        self.start_button.grid(
            row=0,
            column=3,
            padx=PADDING,
            pady=15
        )

        # Stop button

        self.stop_button = ctk.CTkButton(
            self,
            text="Stop Camera",
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            corner_radius=BUTTON_CORNER_RADIUS,
            font=BUTTON_FONT,
            fg_color=ERROR_COLOR,
            hover_color=HOVER_COLOR_ERROR
        )

        self.stop_button.grid(
            row=0,
            column=4,
            padx=(0, PADDING),
            pady=15
        )

        # ===
        # Stage 8.6
        # Save Photo button
        # ===

        self.save_button = ctk.CTkButton(
            self,
            text="Save",
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            corner_radius=BUTTON_CORNER_RADIUS,
            font=BUTTON_FONT
        )

        self.save_button.grid(
            row=0,
            column=5,
            padx=PADDING_LARGE,
            pady=15
        )
