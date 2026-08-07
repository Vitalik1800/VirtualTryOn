import os
import shutil
import tempfile
import unittest

import numpy as np

from core.video_manager import VideoManager


class TestVideoManager(unittest.TestCase):

    def setUp(self):
        self.manager = VideoManager()

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
    # Stage 12.6
    # Create video file
    # ==========================

    def test_create_video(self):
        output = self.manager.create_output_path()

        result = self.manager.start_recording(
            output,
            640,
            480
        )

        self.assertTrue(result)

        self.assertTrue(
            self.manager.is_recording
        )

    # ==========================
    # Stage 12.6
    # Write frames
    # ==========================

    def test_write_frame(self):
        output = self.manager.create_output_path()

        self.manager.start_recording(
            output,
            640,
            480
        )

        self.manager.write(self.frame)

        self.assertTrue(
            self.manager.is_recording
        )

    # ==========================
    # Stage 12.6
    # Stop recording
    # ==========================

    def test_stop_recording(self):
        output = self.manager.create_output_path()

        self.manager.start_recording(
            output,
            640,
            480
        )

        self.manager.stop_recording()

        self.assertFalse(
            self.manager.is_recording
        )

        self.assertTrue(
            os.path.isfile(output)
        )

    # ==========================
    # Stage 12.6
    # Invalid output path
    # ==========================

    def test_invalid_output(self):
        result = self.manager.start_recording(
            "Z:/invalid/folder/video.mp4",
            640,
            480
        )

        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
