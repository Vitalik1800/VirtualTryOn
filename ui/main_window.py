"""
    Project: Virtual Try-On

    Stage: 2
    Substage: 2.1 - Create Main Window

    Description:
    Main application window.
"""

# ===
# Stage 2.1
# Import libraries
# ===

from ui.theme import *
from ui.toolbar import Toolbar
from ui.sidebar import Sidebar
from ui.camera_preview import CameraPreview
from ui.statusbar import StatusBar

# ===
# Stage 2.1
# Main window class
# ===

class MainWindow(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.configure_window()
        self.create_layout()

        # ===
        # Stage 2.8
        # Set application icon
        # ===

        try:
            self.iconbitmap("assets/icons/app.ico")
        except Exception:
            pass

        # ===
        # Stage 2.8
        # Register keyboard shortcuts
        # ===

        self.bind("<F5>", self.start_camera)
        self.bind("<Escape>", self.stop_camera)
        self.bind("<Control-q>", self.close_application)

        # ===
        # Stage 2.8
        # Window close event
        # ===

        self.protocol(
            "WM_DELETE_WINDOW",
            self.close_application
        )

    # ===
    # Stage 2.1
    # Configure application window
    # ===

    def configure_window(self):

        self.title(WINDOW_TITLE)

        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

        self.minsize(MIN_WIDTH, MIN_HEIGHT)

        self.center_window(WINDOW_WIDTH, WINDOW_HEIGHT)

    # ===
    # Stage 2.1
    # Center window on the screen
    # ===

    def center_window(self, width, height):

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        self.geometry(f"{width}x{height}+{x}+{y}")

    # ===
    # Stage 2.1
    # Run application
    # ===

    def run(self):
        self.mainloop()

    # ===
    # Stage 2.4
    # Create main application Layout
    # ===

    def create_layout(self):

        # Configure window grid

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Create main container

        self.main_frame = ctk.CTkFrame(
            master=self,
            corner_radius=0
        )

        self.main_frame.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        # Configure main container grid

        self.main_frame.grid_rowconfigure(1, weight=1)
        self.main_frame.grid_rowconfigure(2, weight=0)

        self.main_frame.grid_columnconfigure(0, weight=0)
        self.main_frame.grid_columnconfigure(1, weight=1)

        # Create toolbar

        self.toolbar = Toolbar(self.main_frame)

        self.toolbar.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="ew"
        )

        # Sidebar

        self.sidebar = Sidebar(self.main_frame)

        self.sidebar.grid(
            row=1,
            column=0,
            sticky="ns"
        )

        # ===
        # Stage 2.6
        # Create camera preview
        # ===

        self.camera_preview = CameraPreview(self.main_frame)

        self.camera_preview.grid(
            row=1,
            column=1,
            padx=20,
            pady=20,
            sticky="nsew"
        )

        # ===
        # Stage 2.7
        # Create status bar
        # ===

        self.statusbar = StatusBar(self.main_frame)

        self.statusbar.grid(
            row=2,
            column=0,
            columnspan=2,
            sticky="ew"
        )

    # ===
    # Stage 2.8
    # Start camera
    # ===

    def start_camera(self, event=None):

        print("Start camera")

    # ===
    # Stage 2.8
    # Stop camera
    # ===

    def stop_camera(self, event=None):

        print("Stop camera")

    # ===
    # Stage 2.8
    # Close application
    # ===

    def close_application(self, event=None):

        self.destroy()
