"""
Project: Virtual Try-On

Stage: 12
Substage: 12.1 - Camera Tests

Description:
Unit tests for Camera module.
"""

import unittest

from core.camera import Camera

class TestCamera(unittest.TestCase):

    def setUp(self):
        """Create camera before every test."""

        self.camera = Camera()

    def tearDown(self):
        """Release camera after every test."""

        if self.camera.is_opened():
            self.camera.release()

    def test_open_camera(self):
        """Camera should open if available."""

        opened = self.camera.open()

        self.assertIsInstance(opened, bool)

    def test_read_frame(self):
        """Read frame from opened camera."""

        if not self.camera.open():
            self.skipTest("Camera not available.")

        success, frame = self.camera.read()

        self.assertTrue(success)
        self.assertIsNotNone(frame)

    def test_release_camera(self):
        """Camera should close correctly."""

        self.camera.open()

        self.camera.release()

        self.assertFalse(
            self.camera.is_opened()
        )

    def test_read_widhout_open(self):
        """Reading without opening camera."""

        success, frame = self.camera.read()

        self.assertFalse(success)
        self.assertIsNone(frame)

    def test_release_twice(self):
        """Releasing camera twice should not fail."""

        self.camera.release()
        self.camera.release()

        self.assertFalse(
            self.camera.is_opened()
        )

if __name__ == "__main__":
    unittest.main()
