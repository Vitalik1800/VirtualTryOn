"""
    Project: Virtual Try-On

    Stage: 5
    Substage: 5.1 - Create Accessory Manager

    Description:
    Accessory management module.
"""

# ===
# Stage 5.1
# Import libraries
# ===

import os
import cv2
import logging

logger = logging.getLogger(__name__)

# ===
# Stage 5.1
# Accessory Manager
# ===

class AccessoryManager:
    """
    Manage virtual accessories.
    """

    def __init__(self):
        """
        Initialize accessory manager.
        """

        # Root accessories directory

        self.accessories_path = os.path.join(
            "assets",
            "accessories"
        )

        # Cached images

        self.cache = {}

        # Current accessory

        self.current_accessory = None

        # ===
        # Stage 5.2
        # Accessory directories
        # ===

        self.categories = [
            "glasses",
            "hats",
            "earrings",
            "necklaces",
            "masks",
            "watches"
        ]

        # ===
        # Stage 5.6
        # Current accessory
        # ===

        self.current_category = None
        self.current_accessories = []
        self.current_index = 0

    # ===
    # Stage 5.1
    # Clear manager
    # ===

    def clear(self):
        """
        Clear loaded accessories.
        """

        self.current_accessories.clear()
        self.cache.clear()
        self.current_accessory = None

    # ===
    # Stage 5.3
    # Load PNG accessory
    # ===

    def load_accessory(self, file_path):
        """
        Load PNG accessory with alpha channel.

        Args:
            file_path: Path to PNG file.

        Returns:
            OpenCV image with alpha channel or None.
        """

        # Check file exists

        if not os.path.isfile(file_path):

            logger.error(
                f"Accessory not found: {file_path}"
            )
            
            return None

        # Invalid extension

        if not file_path.lower().endswith(".png"):

            logger.error(
                f"Unsupported format: {file_path}"
            )

            return None
        
        # Load PNG with alpha channel

        image = cv2.imread(
            file_path,
            cv2.IMREAD_UNCHANGED
        )

        if image is None:

            logger.error(
                f"Unable to read PNG: {file_path}"
            )
            
            return None

        # PNG should contain alpha channel

        if len(image.shape) != 3 or image.shape[2] != 4:

            logger.error(
                f"PNG has no alpha channel: {file_path}"
            )
            
            return None

        return image

    # ===
    # Stage 5.4
    # Get accessory from cache
    # ===

    def get_accessory(self, file_path):
        """
        Return accessory from cache.

        Args:
            file_path: PNG file path.

        Returns:
            OpenCV image or None.
        """

        # Already loaded

        if file_path in self.cache:
            return self.cache[file_path]

        # Load accessory

        image = self.load_accessory(file_path)

        if image is None:
            return None

        # Save to cache

        self.cache[file_path] = image

        return image

    # ===
    # Stage 5.5
    # Get accessory list
    # ===

    def get_accessories(self, category):
        """
        Return sorted list of PNG accessories.

        Args:
            category: Accessory category.

        Returns:
            List of PNG file paths.
        """

        if category not in self.categories:
            return []

        folder = os.path.join(
            self.accessories_path,
            category
        )

        if not os.path.isdir(folder):

            logger.error(
                f"Accessory folder not found: {folder}"
            )

            raise FileNotFoundError(folder)

        accessories = []

        for file_name in sorted(os.listdir(folder)):

            if file_name.lower().endswith(".png"):

                accessories.append(
                    os.path.join(
                        folder,
                        file_name
                    )
                )

        return accessories
    
    # ===
    # Stage 5.6
    # Select accessory category
    # ===

    def select_category(self, category):
        """
        Load accessory list for category.

        Args:
            category: Accessory category.

        Returns:
            bool
        """

        accessories = self.get_accessories(category)

        if not accessories:

            logger.warning(
                f"No accessories found in '{category}'."
            )
            
            return False

        self.current_category = category
        self.current_accessories = accessories
        self.current_index = 0

        return True

    # ===
    # Stage 5.6
    # Select accessory by index
    # ===

    def select_accessory(self, index):
        """
        Select accessory by index.

        Args:
            index: Accessory index.
        """

        if not self.current_accessories:
            return False

        if index < 0 or index >= len(self.current_accessories):
            return False

        self.current_index = index

        return True

    # ===
    # Stage 5.6
    # Get current accessory
    # ===

    def get_current_accessory(self):
        """
        Return current accessory image.
        """

        if not self.current_accessories:
            return None

        path = self.current_accessories[self.current_index]

        return self.get_accessory(path)

    # ===
    # Stage 5.6
    # Get current accessory path
    # ===

    def get_current_path(self):
        """
        Return current accessory path.
        """

        if not self.current_accessories:
            return None

        return self.current_accessories[
            self.current_index
        ]

    # ===
    # Stage 5.6
    # Select next accessory
    # ===

    def next_accessory(self):
        """
        Select next accessory.
        """

        if not self.current_accessories:
            return -1

        self.current_index = (
            self.current_index + 1
        ) % len(self.current_accessories)

        self.get_current_accessory()

        return self.current_index

    # ===
    # Stage 5.6
    # Select previous accessory
    # ===

    def previous_accessory(self):
        """
        Select previous accessory.
        """

        if not self.current_accessories:
            return -1

        self.current_index = (
            self.current_index - 1
        ) % len(self.current_accessories)

        self.get_current_accessory()

        return self.current_index

    # ===
    # Stage 5.8
    # Release resources
    # ===

    def close(self):
        """
        Release Accessory Manager resources.
        """

        logger.info(
            "Closing AccessoryManager..."
        )

        # Clear image cache

        self.clear()

        # Reset current accessory

        self.current_category = None
        self.current_accessories.clear()
        self.current_index = 0

        logger.info(
            "AccessoryManager closed."
        )
