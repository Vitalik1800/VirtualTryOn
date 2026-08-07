import os
import shutil
import tempfile
import unittest

import numpy as np

from core.photo_manager import PhotoManager


class TestPhotoManager(unittest.TestCase):

    def setUp(self):
        self.manager = PhotoManager()

        self.temp_dir = tempfile.mkdtemp()

        self.manager.save_directory = self.temp_dir

        self.frame = np.zeros(
            (480, 640, 3),
            dtype=np.uint8
        )

    def tearDown(self):
        self.manager.close()

        shutil.rmtree(
            self.temp_dir,
            ignore_errors=True
        )

    # ==========================
    # Stage 12.5
    # Directory selection
    # ==========================

    def test_has_save_directory(self):
        self.assertTrue(
            self.manager.has_save_directory()
        )

    # ==========================
    # Stage 12.5
    # Save photo
    # ==========================

    def test_save_photo(self):
        self.manager.update_frame(self.frame)

        path = self.manager.save_photo()

        self.assertIsNotNone(path)

        self.assertTrue(
            os.path.isfile(path)
        )

    # ==========================
    # Stage 12.5
    # No frame
    # ==========================

    def test_no_frame(self):
        self.assertFalse(
            self.manager.has_frame()
        )

        result = self.manager.save_photo()

        self.assertFalse(result)

    # ==========================
    # Stage 12.5
    # Write error
    # ==========================

    def test_invalid_directory(self):
        self.manager.update_frame(self.frame)

        self.manager.save_directory = "Z:/folder/does/not/exist"

        result = self.manager.save_photo()

        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
