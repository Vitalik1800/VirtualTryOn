import os
import shutil
import tempfile
import unittest

<<<<<<< HEAD
import cv2

from ui.main_window import MainWindow

=======
from ui.main_window import MainWindow


>>>>>>> d5bf2df (Release v1.0)
class TestVideoPipeline(unittest.TestCase):

    def setUp(self):

        self.app = MainWindow()

        self.temp_dir = tempfile.mkdtemp()

        self.app.video_manager.save_directory = self.temp_dir

        self.assertTrue(self.app.camera.open())

        success, frame = self.app.camera.read()
        self.assertTrue(success)

        h, w = frame.shape[:2]

        output = self.app.video_manager.create_output_path()

        self.app.video_manager.start_recording(
            output,
            w,
            h
        )

        self.app.accessory_manager.select_category("glasses")
        self.app.accessory_manager.select_accessory(0)
<<<<<<< HEAD
    
=======

>>>>>>> d5bf2df (Release v1.0)
    def tearDown(self):

        try:
            self.app.stop_camera()
        except Exception:
            pass

        self.app.destroy()

        shutil.rmtree(
            self.temp_dir,
            ignore_errors=True
        )

    # ==========================
    # Stage 13.6
    # Start recording
    # ==========================

    def test_start_recording(self):

        self.assertTrue(
            self.app.video_manager.is_recording
        )

    # ==========================
    # Stage 13.6
    # Record several frames
    # ==========================

    def test_record_frames(self):

        for _ in range(10):
<<<<<<< HEAD

=======
>>>>>>> d5bf2df (Release v1.0)
            success, frame = self.app.camera.read()

            self.assertTrue(success)

            landmarks = self.app.face_detector.process(
                frame
            )

            accessory = (
                self.app.accessory_manager
                .get_current_accessory()
            )

            path = (
                self.app.accessory_manager
                .get_current_path()
            )

            rendered = self.app.accessory_renderer.render(
                frame.copy(),
                accessory,
                landmarks,
                path
            )

            self.app.video_manager.write(
                rendered
            )

        self.assertTrue(
            self.app.video_manager.is_recording
        )

    # ==========================
    # Stage 13.6
    # Stop recording
    # ==========================

    def test_stop_recording(self):

        self.app.video_manager.stop_recording()

        self.assertFalse(
            self.app.video_manager.is_recording
        )

    # ==========================
    # Stage 13.6
    # Video file created
    # ==========================

    def test_video_file_created(self):

        output_path = (
            self.app.video_manager.output_path
        )

        for _ in range(10):
<<<<<<< HEAD

=======
>>>>>>> d5bf2df (Release v1.0)
            success, frame = self.app.camera.read()

            self.assertTrue(success)

            landmarks = self.app.face_detector.process(
                frame
            )

            accessory = (
                self.app.accessory_manager
                .get_current_accessory()
            )

            path = (
                self.app.accessory_manager
                .get_current_path()
            )

            rendered = self.app.accessory_renderer.render(
                frame.copy(),
                accessory,
                landmarks,
                path
            )

            self.app.video_manager.write(
                rendered
            )

        self.app.video_manager.stop_recording()

        self.assertTrue(
            os.path.isfile(output_path)
        )

        self.assertGreater(
            os.path.getsize(output_path),
            0
        )

<<<<<<< HEAD
=======

>>>>>>> d5bf2df (Release v1.0)
if __name__ == "__main__":
    unittest.main()
