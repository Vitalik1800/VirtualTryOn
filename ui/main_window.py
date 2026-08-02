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
from core.camera import Camera
from core.image_manager import ImageManager

# ===
# Stage 3.7
# Import message box
# ===

from tkinter import messagebox

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
        # Stage 3.5
        # Camera
        # ===

        self.camera = Camera()

        self.is_camera_running = False

        # ===
        # Stage 3.5
        # Camera update job
        # ===

        self.camera_job = None

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

        self.toolbar.start_button.configure(
            command=self.start_camera
        )

        self.toolbar.stop_button.configure(
            command=self.stop_camera
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

        self.status_bar = StatusBar(self.main_frame)

        self.status_bar.grid(
            row=2,
            column=0,
            columnspan=2,
            sticky="ew"
        )

    # ===
    # Stage 3.5
    # Start camera
    # ===

    def start_camera(self, event=None):

        if self.is_camera_running:
            return

        if self.camera.open():

            self.is_camera_running = True

            self.status_bar.set_status("Camera Started")
            self.status_bar.set_camera_status("Connected")

            self.update_camera()

        else:

            self.status_bar.set_status("Camera Error")
            self.status_bar.set_camera_status("Unavailable")

            self.show_error(
                "Camera Error",
                "Unable to access the camera.\n\n"
                "Possible reasons:\n"
                "- Camera is not connected.\n"
                "- Camera is already in use.\n"
                "- Access to the camera is denied."
            )

    # ===
    # Stage 3.5
    # Update preview
    # ===

    def update_camera(self):

        try:

            if not self.is_camera_running:
                return

            if not self.winfo_exists():
                return

            success, frame = self.camera.read()

            if not success:

                self.stop_camera()

                self.show_error(
                    "Camera Error",
                    "Failed to read video frame."
                )

                return

            image = ImageManager.frame_to_photo(
                frame,
                (
                    PREVIEW_WIDTH,
                    PREVIEW_HEIGHT
                )
            )

            if image is None:
                return

            self.camera_preview.preview_label.configure(
                image=image,
                text=""
            )

            self.camera_preview.preview_label.image = image

            if self.is_camera_running:
                self.camera_job = self.after(
                    15,
                    self.update_camera
                )

        except Exception as error:

            self.stop_camera()

            self.show_error(
                "Unexpected Error",
                str(error)
            )
        
    # ===
    # Stage 3.5
    # Stop camera
    # ===

    def stop_camera(self, event=None):

        self.is_camera_running = False

        if self.camera_job is not None:

            self.after_cancel(self.camera_job)

            self.camera_job = None

        if self.camera.is_opened():

            self.camera.release()

        # ===
        # Stage 3.6
        # Clear camera preview
        # ===

        self.camera_preview.preview_label.configure(
            image=None,
            text="Camera Preview"
        )

        self.camera_preview.preview_label.image = None

        self.status_bar.set_status("Ready")
        self.status_bar.set_camera_status("Disconnected")
        self.status_bar.set_fps(0)

    # ===
    # Stage 3.7
    # Show error message
    # ===

    def show_error(self, title, message):

        messagebox.showerror(
            title,
            message
        )

    # ===
    # Stage 3.8
    # Close application
    # ===

    def close_application(self, event=None):

        # Stop camera loop

        self.is_camera_running = False

        # Cancel scheduled update

        if self.camera_job is not None:

            self.after_cancel(self.camera_job)

            self.camera_job = None

        # Release camera

        if self.camera.is_opened():

            self.camera.release()

        # ===
        # Stage 3.8
        # Clear preview
        # ===

        if hasattr(self.camera_preview, "preview_label"):

            self.camera_preview.preview_label.configure(
                image=None,
                text="Camera Preview"
            )

            self.camera_preview.preview_label.image = None

        if hasattr(self, "face_detector"):
            self.face_detector.close()

        # Destroy application window
        
        self.destroy()

