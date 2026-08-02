"""
    Project: Virtual Try-On

    Stage: 3
    Substage: 3.1 - Implement Camera Class

    Description:
    Camera module based on OpenCV.
"""

# ===
# Stage 3.1
# Import Libraries
# ===

import cv2

from core.settings import (
    DEFAULT_CAMERA_INDEX,
    CAMERA_WIDTH,
    CAMERA_HEIGHT,
    FPS_LIMIT
)

import logging

# ===
# Stage 3.2
# Configure Logger
# ===

logger = logging.getLogger(__name__) 

class Camera:
    """
    Camera module.
    """

    def __init__(self):

        # ===
        # Stage 3.1
        # Initialize camera variables
        # ===

        self.capture = None
        self.camera_index = DEFAULT_CAMERA_INDEX

    def open(self) -> bool:
        """
        Initialize camera.
        """

        # ===
        # Stage 3.1
        # Open camera
        # ===

        self.capture = cv2.VideoCapture(
            self.camera_index,
            cv2.CAP_DSHOW
        )

        if not self.capture.isOpened():

            logging.error("Camera initialization failed.")
            
            return False


        # ===
        # Stage 3.2
        # Configure camera
        # ===
        
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, CAMERA_WIDTH)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, CAMERA_HEIGHT)
        self.capture.set(cv2.CAP_PROP_FPS, FPS_LIMIT)

        # ===
        # Stage 3.2
        # Read actual camera parameters
        # ===

        width = int(
            self.capture.get(cv2.CAP_PROP_FRAME_WIDTH)
        )

        height = int(
            self.capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
        )

        fps = int(
            self.capture.get(cv2.CAP_PROP_FPS)
        )

        logger.info(
            f"Camera initialized: {width}x{height} @ {fps} FPS"
        )

        return True

    def read(self):
        """
        Read a frame from the camera.

        Returns:
            tuple[bool, numpy.ndarray | None]
        """

        # ===
        # Stage 3.1
        # Read frame
        # ===

        if not self.is_opened():

            logger.warning("Camera is not opened.")

            return False, None

        # ===
        # Stage 3.3
        # Read frame
        # ===

        success, frame = self.capture.read()

        if not success:

            logger.warning("Failed to read frame.")

            return False, None

        if frame is None:

            logger.warning("Frame is empty.")

            return False, None

        # ===
        # Stage 3.3
        # Return OpenCV frame
        # ===
        
        return True, frame

    def is_opened(self) -> bool:
        """
        Check camera state.
        """

        return (
            self.capture is not None
            and
            self.capture.isOpened()
        )

    def release(self):
        """
        Release camera.
        """

        # ===
        # Stage 3.8
        # Release camera resources
        # ===

        if self.capture is not None:

            if self.capture.isOpened():

                self.capture.release()

            self.capture = None

            logger.info("Camera released.")

    def get_camera_info(self) -> dict:
        """
        Return camera information.
        """

        if not self.is_opened():

            return {}

        return {

            "width": int(
                self.capture.get(cv2.CAP_PROP_FRAME_WIDTH)
            ),

            "height": int(
                self.capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
            ),

            "fps": int(
                self.capture.get(cv2.CAP_PROP_FPS)
            )
        }

    def has_frame(self) -> bool:
        """
        Check whether the camera can provide a frame.
        """

        success, _ = self.read()

        return success
