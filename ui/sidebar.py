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

import os
import tkinter as tk

from ui.theme import *


# ===
# Stage 2.5
# Sidebar class
# ===

class Sidebar(ctk.CTkFrame):

    def __init__(
        self,
        master,
        category_callback,
        selection_callback
    ):
        super().__init__(master)

        self.title_label = None
        self.category_menu = None
        self.accessories_label = None
        self.accessory_list = None

        self.callback = category_callback
        self.selection_callback = selection_callback

        self.configure_sidebar()
        self.create_widgets()

    # ===
    # Stage 2.5
    # Configure sidebar
    # ===

    def configure_sidebar(self):

        self.configure(
            width=SIDEBAR_WIDTH,
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
            pady=(PADDING_LARGE, PADDING)
        )

        # Category selection

        self.category_menu = ctk.CTkOptionMenu(
            self,
            values=[
                "Glasses",
                "Hats",
                "Masks"
            ],
            width=SIDEBAR_WIDTH,
            command=self.callback
        )

        self.category_menu.pack(
            pady=(PADDING, PADDING_LARGE)
        )

        # Accessories label

        self.accessories_label = ctk.CTkLabel(
            self,
            text="Available Items",
            font=TEXT_FONT
        )

        self.accessories_label.pack()

        # Accessories list

        self.accessory_list = tk.Listbox(
            self,
            width=28,
            height=18,
            font=("Segoe UI", 11),
            exportselection=False
        )

        self.accessory_list.pack(
            pady=PADDING,
            padx=PADDING,
            fill="both",
            expand=True
        )

        self.accessory_list.bind(
            "<<ListboxSelect>>",
            self.on_accessory_selected
        )

    def select_accessory(self, index):

        """
        Select accessory in ListBox.
        """

        if index < 0:
            return

        self.accessory_list.selection_clear(
            0,
            tk.END
        )

        self.accessory_list.selection_set(index)

        self.accessory_list.activate(index)

        self.accessory_list.event_generate("<<ListboxSelect>>")

    def on_accessory_selected(self, _event):

        selection = self.accessory_list.curselection()

        if not selection:
            return

        index = selection[0]

        if hasattr(self, "selection_callback"):
            self.selection_callback(index)

    def update_accessories(self, accessories):

        self.accessory_list.delete(0, tk.END)

        for path in accessories:

            name = os.path.splitext(
                os.path.basename(path)
            )[0]

            self.accessory_list.insert(
                tk.END,
                name
            )

        if accessories:
            
            self.accessory_list.selection_clear(0, tk.END)

            self.accessory_list.selection_set(0)

            self.accessory_list.activate(0)

            self.accessory_list.event_generate(
                "<<ListboxSelect>>"
            )
