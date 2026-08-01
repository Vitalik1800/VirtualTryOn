"""
    Project: Virtual Try-On

    Stage: 3
    Substage: 3.4 - Frame Conversion

    Description:
    Convert OpenCV frames for Tkinter preview.
"""

# ===
# Stage 3.4
# Import libraries
# ===

import cv2

from PIL import Image
from PIL import ImageTk


class ImageManager:
    """
    Image conversion utilities.
    """

    @staticmethod
    def frame_to_photo(frame, size=None):

        if frame is None:
            return None

        # BGR -> RGB

        frame = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        image = Image.fromarray(frame)

        if size is not None:

            image = image.resize(size)

        return ImageTk.PhotoImage(image)
