"""
    Project: Virtual Try-On

    Stage: 9
    Substage: 9.1 - Create Video Manager

    Description:
    Video recording manager.
"""

# ===
# Stage 9.1
# Import libraries
# ===

import cv2
import logging

from datetime import datetime
import os

from tkinter import filedialog

logger = logging.getLogger(__name__)

# ===
# Stage 9.1
# Video Manager
# ===

class VideoManager:
    """
    Manage video recording.
    """

    def __init__(self):
        """
        Initialize video manager.
        """

        # OpenCV VideoWriter

        self.video_writer = None

        # Recording state

        self.is_recording = False

        # Output directory

        self.save_directory = None

        # Output file path

        self.output_path = None

        # Video properties

        self.fps = 30

        self.frame_width = 0
        self.frame_height = 0

    # ===
    # Stage 9.2
    # Start video recording
    # ===

    def start_recording(
        self,
        output_path,
        width,
        height,
        fps=30
    ):
        """
        Create VideoWriter and start recording.

        Args:
            output_path: Output video path.
            width: Frame width.
            height: Frame height.
            fps: Frames per second.

        Returns:
            True if recording started successfully.
        """

        # Release previous writer

        if self.video_writer is not None:

            self.video_writer.release()

            self.video_writer = None

        self.output_path = output_path
        self.frame_width = width
        self.frame_height = height
        self.fps = fps

        if output_path.lower().endswith(".avi"):

            fourcc = cv2.VideoWriter_fourcc(
                *"XVID"
            )

        else:

            fourcc = cv2.VideoWriter_fourcc(
                *"mp4v"
            )

        self.video_writer = cv2.VideoWriter(
            output_path,
            fourcc,
            fps,
            (width, height)
        )

        if not self.video_writer.isOpened():

            logger.error(
                "Unable to create VideoWriter."
            )

            self.video_writer = None

            return False

        self.is_recording = True

        logger.info(
            f"Recording started: {output_path}"
        )

        return True

    # ===
    # Stage 9.3
    # Create output path
    # ===

    def create_output_path(self):
        """
        Create output path for video recording.
        """

        self.save_directory = "videos"

        os.makedirs(
            self.save_directory,
            exist_ok=True
        )

        filename = datetime.now().strftime(
            "video_%Y%m%d_%H%M%S.mp4"
        )

        self.output_path = os.path.join(
            self.save_directory,
            filename
        )

        return self.output_path

    # ===
    # Stage 9.5
    # Stop video recording
    # ===

    def stop_recording(self):
        """
        Stop video recording.
        """

        if self.video_writer is not None:

            self.video_writer.release()
            self.video_writer = None

        self.is_recording = False

        logger.info(
            "Recording stopped."
        )

    # ===
    # Stage 9.4
    # Write video frame
    # ===

    def write(self, frame):
        """
        Write frame to video.

        Args:
            frame: OpenCV frame.
        """

        if (
            not self.is_recording
            or self.video_writer is None
            or frame is None
        ):
            return

        try:

            self.video_writer.write(frame)

        except Exception as error:

            logger.error(error)

            self.stop_recording()

    # ===
    # Stage 9.6
    # Create output path
    # ===

    def create_output_path(self):
        """
        Create output path for recorded video.

        Returns:
            Full output file path.
        """

        if not self.has_save_directory():
            return None

        os.makedirs(
            self.save_directory,
            exist_ok=True
        )

        filename = datetime.now().strftime(
            "video_%Y%m%d_%H%M%S.mp4"
        )

        self.output_path = os.path.join(
            self.save_directory,
            filename
        )

        return self.output_path

    # ===
    # Stage 9.7
    # Select save directory
    # ===

    def select_directory(self):
        """
        Select directory for saving videos.

        Returns:
            Selected directory or None.
        """

        directory = filedialog.askdirectory(
            title="Select folder to save video"
        )

        if not directory:
            return None

        self.save_directory = directory

        return directory

    # ===
    # Stage 9.7
    # Check save directory
    # ===

    def has_save_directory(self):
        """
        Check whether save directory is selected.
        """

        return self.save_directory is not None

    # ===
    # Stage 9.5
    # Release resources
    # ===

    def close(self):
        """
        Release VideoManager resources.
        """

        self.stop_recording()

        self.output_path = None
        self.save_directory = None

        self.frame_width = 0
        self.frame_height = 0

        self.fps = 30
