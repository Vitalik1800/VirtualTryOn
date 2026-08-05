"""
    Project: Virtual Try-On

    Stage: 8
    Substage: 8.1 - Create Photo Manager

    Description:
    Photo management module.
"""

# ===
# Stage 8.1
# Import libraries
# ===

import logging
from tkinter import filedialog
from datetime import datetime
import os
import cv2

logger = logging.getLogger(__name__)

# ===
# Stage 8.1
# Photo Manager
# ===

class PhotoManager:
    """
    Manage photo saving.
    """

    def __init__(self):
        """
        Initialize photo manager.
        """

        logger.info(
            "PhotoManager initialized."
        )

        self.current_frame = None
        self.save_directory = None

    # ===
    # Stage 8.2
    # Update current frame
    # ===

    def update_frame(self, frame):
        """
        Store current camera frame.

        Args:
            frame: OpenCV frame.
        """

        self.current_frame = frame

    # ===
    # Stage 8.2
    # Get current frame
    # ===

    def get_current_frame(self):
        """
        Return current frame.

        Returns:
            OpenCV frame or None.
        """

        return self.current_frame

    # ===
    # Stage 8.2
    # Check frame availability
    # ===

    def has_frame(self):
        """
        Check whether current frame exists.

        Returns:
            bool
        """

        return self.current_frame is not None

    # ===
    # Stage 8.3
    # Select save directory
    # ===

    def select_directory(self):
        """
        Select directory for saving photos.

        Returns:
            Selected directory or None.
        """

        directory = filedialog.askdirectory(
            title="Select Save Directory"
        )

        if not directory:

            logger.info(
                "Directory selection cancelled."
            )

            return None

        self.save_directory = directory

        logger.info(
            f"Save directory: {directory}"
        )

        return directory

    # ===
    # Stage 8.3
    # Get save directory
    # ===

    def get_save_directory(self):
        """
        Return selected save directory.

        Returns:
            Directory path or None.
        """

        return self.save_directory
    
    # ===
    # Stage 8.3
    # Check save directory
    # ===

    def has_save_directory(self):
        """
        Check whether save directory exists.

        Returns:
            bool
        """

        return self.save_directory is not None

    # ===
    # Stage 8.4
    # Generate photo filename
    # ===

    def generate_filename(self):
        """
        Generate unique photo filename.

        Returns:
            File name.
        """

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        return f"photo_{timestamp}.png"

    # ===
    # Stage 8.4
    # Generate output path
    # ===

    def generate_output_path(self):
        """
        Generate full output path.

        Returns:
            Full file path or None.
        """

        if self.save_directory is None:
            return None

        filename = self.generate_filename()

        return os.path.join(
            self.save_directory,
            filename
        )

    # ===
    # Stage 8.5
    # Save photo
    # ===

    def save_photo(self):
        """
        Save current frame as PNG.

        Returns:
            True if photo was saved successfully,
            otherwise False.
        """

        # No frame

        if self.current_frame is None:

            logger.error(
                "No frame available."
            )

            return False

        # No save directory

        if self.save_directory is None:

            logger.error(
                "Save directory not selected."
            )

            return False

        output_path = self.generate_output_path()

        if output_path is None:

            logger.error(
                "Save directory not selected."
            )

            return False

        try:

            success = cv2.imwrite(
                output_path,
                self.current_frame
            )

            if not success:

                logger.error(
                    f"Unable to save photo: {output_path}"
                )

                return False
            
        except PermissionError:

            logger.error(
                "Permission denied."
            )

            return False

        except Exception:

            logger.exception(
                "Failed to save photo."
            )

            return False

        logger.info(
            f"Photo saved: {output_path}"
        )

        return output_path

    # ===
    # Stage 8.9
    # Clear photo manager
    # ===

    def clear(self):
        """
        Clear temporary photo data.
        """

        self.current_frame = None
        self.save_directory = None
    
    # ===
    # Stage 8.9
    # Release resources
    # ===

    def close(self):
        """
        Release PhotoManager resources.
        """

        logger.info(
            "Closing PhotoManager..."
        )

        self.clear()

        logger.info(
            "PhotoManager closed."
        )
