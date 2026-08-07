"""
    Project: Virtual Try-On

    Stage: 2
    Substage: 2.7 - Create Status Bar

    Description:
    Application status bar.
"""

# ===
# Stage 2.7
# Import libraries
# ===

from ui.theme import *


# ===
# Stage 2.7
# Status Bar
# ===

class StatusBar(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.status_label = None
        self.fps_label = None
        self.camera_label = None

        self.configure_statusbar()
        self.create_widgets()

    # ===
    # Stage 2.7
    # Configure status bar
    # ===

    def configure_statusbar(self):
        self.configure(
            height=40,
            corner_radius=0
        )

        self.grid_propagate(False)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=0)

    # ===
    # Stage 2.7
    # Create widgets
    # ===

    def create_widgets(self):
        # Application status

        self.status_label = ctk.CTkLabel(
            self,
            text="Status: Ready",
            font=STATUS_FONT,
            anchor="w"
        )

        self.status_label.grid(
            row=0,
            column=0,
            padx=15,
            sticky="w"
        )

        # FPS

        self.fps_label = ctk.CTkLabel(
            self,
            text="FPS: 0",
            font=STATUS_FONT
        )

        self.fps_label.grid(
            row=0,
            column=1,
            padx=20
        )

        # Camera information

        self.camera_label = ctk.CTkLabel(
            self,
            text="Camera: Not Connected",
            font=STATUS_FONT
        )

        self.camera_label.grid(
            row=0,
            column=2,
            padx=15
        )

    # ===
    # Stage 2.7
    # Update status
    # ===

    def set_status(self, text):
        self.status_label.configure(
            text=f"Status: {text}"
        )

    # ===
    # Stage 2.7
    # Update FPS
    # ===

    def set_fps(self, fps):
        self.fps_label.configure(
            text=f"FPS: {fps}"
        )

    # ===
    # Stage 2.7
    # Update camera status
    # ===

    def set_camera_status(self, text):
        self.camera_label.configure(
            text=f"Camera: {text}"
        )
