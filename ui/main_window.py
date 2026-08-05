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

from core.settings import *
from ui.theme import *
from ui.toolbar import Toolbar
from ui.sidebar import Sidebar
from ui.camera_preview import CameraPreview
from ui.statusbar import StatusBar
from core.camera import Camera
from core.image_manager import ImageManager
from core.face_detector import FaceDetector
from core.accessory_manager import AccessoryManager
from core.accessory_renderer import AccessoryRenderer
from core.photo_manager import PhotoManager
from core.video_manager import VideoManager
import cv2
import time
import gc
import os
from ui.tooltip import ToolTip

# ===
# Stage 3.7
# Import message box
# ===

from tkinter import messagebox
import logging

logger = logging.getLogger(__name__)

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
        self.face_detector = FaceDetector()
        self.accessory_manager = AccessoryManager()

        # ===
        # Stage 6.2
        # Accessory Renderer
        # ===

        self.accessory_renderer = AccessoryRenderer()

        self.is_camera_running = False

        self.photo_manager = PhotoManager()

        self.video_manager = VideoManager()

        # ===
        # Stage 3.5
        # Camera update job
        # ===

        self.camera_job = None

        # ===
        # Stage 2.8
        # Register keyboard shortcuts
        # ===

        self.bind("<F1>", self.show_shortcuts)
        self.bind("<F2>", self.show_about)
        self.bind("<F5>", self.start_camera)
        self.bind("<Escape>", self.stop_camera)
        self.bind("<Control-q>", self.close_application)
        self.bind_all("<Left>", self.previous_accessory)
        self.bind_all("<Right>", self.next_accessory)

        # ===
        # Stage 2.8
        # Window close event
        # ===

        self.protocol(
            "WM_DELETE_WINDOW",
            self.close_application
        )

        self.update_controls()

        self.last_time = time.perf_counter()

        self.fps = 0

    def show_shortcuts(self, event=None):

        messagebox.showinfo(
            "Keyboard Shortcuts",
            "F1       Help\n"
            "F2       About\n"
            "F5       Start Camera\n"
            "Esc      Stop Camera\n"
            "← / →    Change Accessory\n"
            "Ctrl+Q   Exit"
        )

    def show_about(self, event=None):

        messagebox.showinfo(
            f"About {APP_NAME}",
            f"{APP_NAME}\n"
            f"Version {APP_VERSION}\n\n"
            "Developed by Vitaly Semchyshyn\n\n"
            "Technologies:\n"
            "• Python\n"
            "• OpenCV\n"
            "• MediaPipe\n"
            "• CustomTkinter"
        )
        
    # ===
    # Stage 2.1
    # Configure application window
    # ===

    def configure_window(self):

        self.title(WINDOW_TITLE)

        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

        self.minsize(MIN_WIDTH, MIN_HEIGHT)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

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

        self.toolbar.save_button.configure(
            command=self.save_photo
        )

        ToolTip(self.toolbar.start_button, "Start camera (F5)")
        ToolTip(self.toolbar.stop_button, "Stop camera (Esc)")
        ToolTip(self.toolbar.save_button, "Save photo")

        # Sidebar

        self.sidebar = Sidebar(
            self.main_frame,
            self.change_category,
            self.change_accessory
        )

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
            padx=PADDING_LARGE,
            pady=PADDING_LARGE,
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

        self.status_bar.set_status("Starting camera...")
        self.update_idletasks()

        if self.camera.open():

            self.is_camera_running = True

            self.update_controls()

            self.status_bar.set_status(
                "Camera Started. Recording..."
            )
            self.status_bar.set_camera_status("Connected")

            if not self.video_manager.has_save_directory():

                self.video_manager.select_directory()

                if not self.video_manager.has_save_directory():
                    self.stop_camera()
                    return

            output_path = self.video_manager.create_output_path()

            width = int(
                self.camera.capture.get(
                    cv2.CAP_PROP_FRAME_WIDTH
                )
            )

            height = int(
                self.camera.capture.get(
                    cv2.CAP_PROP_FRAME_HEIGHT
                )
            )

            if not self.video_manager.start_recording(
                output_path,
                width,
                height
            ):
                self.show_error(
                    "Video Error",
                    "Unable to record video.\n\n"
                    "Please choose another folder or check write permissions."
                )

                self.stop_camera()

                return

            self.last_time = time.perf_counter()
            
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

            if not success or frame is None:

                self.stop_camera()

                self.show_error(
                    "Camera Error",
                    "Unable to access the camera.\n\n"
                    "Please make sure that:\n"
                    "• the camera is connected;\n"
                    "• it is not being used by another application;\n"
                    "• camera permissions are enabled."
                )

                return

            current = time.perf_counter()

            delta = current - self.last_time

            self.last_time = current

            if delta > 0:

                current_fps = 1.0 / delta

                self.fps = self.fps * 0.9 + current_fps * 0.1

                self.status_bar.set_fps(round(self.fps))
                        
            # ===
            # Stage 6.2
            # Accessory rendering
            # ===

            points = self.face_detector.process(frame)

            accessory = self.accessory_manager.get_current_accessory()

            path = self.accessory_manager.get_current_path()

            frame = self.accessory_renderer.render(
                frame,
                accessory,
                points,
                path
            )

            if self.video_manager.is_recording:
                self.video_manager.write(frame)

            self.photo_manager.update_frame(frame)

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

            if self.is_camera_running and self.winfo_exists():
                
                processing_time = (time.perf_counter() - current) * 1000

                delay = max(
                    1,
                    int(1000 / FPS_LIMIT - processing_time)
                )

                self.camera_job = self.after(
                    delay,
                    self.update_camera
                )

        except Exception:

            logger.exception(
                "Camera update failed."
            )

            self.stop_camera()

            self.show_error(
                "Unexpected Error",
                "Unexpected error occurred."
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
        # Stage 9.5
        # Stop video recording
        # ===

        self.status_bar.set_camera_status("Disconnected")
        self.status_bar.set_fps(0)

        if self.video_manager.is_recording:

            self.video_manager.stop_recording()

            self.status_bar.set_status(
                "Video recording completed."
            )

            self.after(
                1500,
                lambda: self.status_bar.set_status("Ready")
            )

        else:

            self.status_bar.set_status("Ready")

        # ===
        # Stage 3.6
        # Clear camera preview
        # ===

        self.camera_preview.preview_label.configure(
            image=None,
            text="Camera Preview"
        )

        self.camera_preview.preview_label.image = None

        self.status_bar.set_camera_status("Disconnected")
        self.status_bar.set_fps(0)

        self.update_controls()

    # ===
    # Stage 3.7
    # Show error message
    # ===

    def show_error(self, title, message):

        messagebox.showerror(
            title,
            message
        )

    def update_controls(self):

        running = self.is_camera_running

        self.toolbar.start_button.configure(
            state="disabled" if running else "normal"
        )

        self.toolbar.stop_button.configure(
            state="normal" if running else "disabled"
        )

        state = "normal" if running else "disabled"

        self.sidebar.category_menu.configure(
            state=state
        )

        self.sidebar.accessory_list.configure(
            state=state
        )

        self.toolbar.save_button.configure(
            state=state
        )

    def change_accessory(self, index):

        self.accessory_manager.select_accessory(index)

        path = self.accessory_manager.get_current_path()

        if path:
            name = os.path.splitext(
                os.path.basename(path)
            )[0]

            self.status_bar.set_status(
                f"Accessory: {name}"
            )

        else:

            self.status_bar.set_status(
                "Accessory file not found."
            )

            return
            
            
    def change_category(self, value):

        self.status_bar.set_status(
            "Loading accessories..."
        )
        self.update_idletasks()

        try:

            if self.accessory_manager.select_category(value.lower()):

                accessories = (
                    self.accessory_manager.current_accessories
                )

                if not accessories:

                    self.sidebar.update_accessories([])

                    self.status_bar.set_status(
                        "No accessories available."
                    )

                    return

                self.sidebar.update_accessories(
                    accessories
                )

                self.sidebar.select_accessory(0)

                self.status_bar.set_status(
                    f"Category: {value.title()}"
                )

        except FileNotFoundError as e:

            self.status_bar.set_status(
                "Accessory folder not found."
            )

            self.show_error(
                "Folder Missing",
                f"Folder not found:\n\n{e}"
            )

    def previous_accessory(self, event=None):

        index = self.accessory_manager.previous_accessory()

        self.sidebar.select_accessory(index)

    def next_accessory(self, event=None):

        index = self.accessory_manager.next_accessory()

        self.sidebar.select_accessory(index)

    # ===
    # Stage 8.6
    # Save photo
    # ===

    def save_photo(self):
        """
        Save current camera frame.
        """

        if not self.is_camera_running:

            self.show_error(
                "Save Error",
                "Camera is not running."
            )

            return

        if not self.photo_manager.has_frame():

            self.show_error(
                "Save Error",
                "No frame available."
            )

            return

        if not self.photo_manager.has_save_directory():

            self.photo_manager.select_directory()

            if not self.photo_manager.has_save_directory():
                return

        saved_path = self.photo_manager.save_photo()

        if saved_path:

            self.status_bar.set_status(
                "Photo saved successfully."
            )

        else:

            self.show_error(
                "Save Error",
                "Unable to save the photo.\n\n"
                "Please check:\n"
                "• the selected folder exists;\n"
                "• you have write permission;\n"
                "• enough disk space is available."
            )

    # ===
    # Stage 3.8
    # Close application
    # ===

    def close_application(self, event=None):

        gc.collect()

        logger.info(
            "All resources released successfully."
        )

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

        self.face_detector.close()

        self.accessory_manager.close()

        self.accessory_renderer.close()

        self.photo_manager.close()

        self.video_manager.close()

        self.camera = None
        self.face_detector = None
        self.accessory_renderer = None
        self.photo_manager = None
        self.video_manager = None
            
        # Destroy application window
        
        self.destroy()

