import unittest

import numpy as np

from core.image_manager import ImageManager


class TestImageManager(unittest.TestCase):

    def setUp(self):
        self.frame = np.zeros(
            (480, 640, 3),
            dtype=np.uint8
        )

    # ==========================
    # Stage 12.7
    # Invalid frame
    # ==========================

    def test_none_frame(self):
        image = ImageManager.frame_to_photo(
            None,
            (640, 480)
        )

        self.assertIsNone(image)

    # ==========================
    # Stage 12.7
    # Empty frame
    # ==========================

    def test_empty_frame(self):
        frame = np.zeros(
            (0, 0, 3),
            dtype=np.uint8
        )

        image = ImageManager.frame_to_photo(
            frame,
            (640, 480)
        )

        self.assertIsNone(image)


if __name__ == "__main__":
    unittest.main()
