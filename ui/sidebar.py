"""
    Project: Virtual Try-On

    Stage: 2
    Substage: 2.5 - Create Sidebar

    Description:
    Left sidebar for accessory selection.
"""

# ===
# Stage 2.5
# Import libraries
# ===

import customtkinter as ctk

from ui.theme import *

# ===
# Stage 2.5
# Sidebar class
# ===

class Sidebar(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.configure_sidebar()
        self.create_widgets()

    # ===
    # Stage 2.5
    # Configure sidebar
    # ===

    def configure_sidebar(self):

        self.configure(
            width=260,
            corner_radius=0
        )

        self.grid_propagate(False)

    # ===
    # Stage 2.5
    # Create sidebar widgets
    # ===

    def create_widgets(self):

        # Sidebar title

        self.title_label = ctk.CTkLabel(
            self,
            text="Accessories",
            font=HEADER_FONT
        )

        self.title_label.pack(
            pady=(20, 10)
        )

        # Category selection

        self.category_menu = ctk.CTkOptionMenu(
            self,
            values=[
                "Glasses",
                "Hats",
                "Earrings",
                "Necklaces",
                "Watches"
            ],
            width=200
        )

        self.category_menu.pack(
            pady=(10, 20)
        )

        # Accessories label

        self.accessories_label = ctk.CTkLabel(
            self,
            text="Available Items",
            font=TEXT_FONT
        )

        self.accessories_label.pack()

        # Accessories list

        self.accessory_list = ctk.CTkTextbox(
            self,
            width=220,
            height=380
        )

        self.accessory_list.pack(
            pady=10
        )

        self.accessory_list.insert(
            "end",
            "- Aviator Glasses\n"
            "- Round Glasses\n"
            "- Baseball Cap\n"
            "- Earrings\n"
            "- Necklace\n"
            "- Smart Watch"
        )

        self.accessory_list.configure(
            state="disabled"
        )
