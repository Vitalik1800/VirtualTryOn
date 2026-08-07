import os
import shutil
import tempfile
import unittest

from ui.main_window import MainWindow

<<<<<<< HEAD
=======

>>>>>>> d5bf2df (Release v1.0)
class TestPhotoPipeline(unittest.TestCase):

    def setUp(self):

        self.app = MainWindow()

        self.temp_dir = tempfile.mkdtemp()

        self.app.photo_manager.save_directory = self.temp_dir

        self.app.start_camera()

        self.app.accessory_manager.select_category(
            "glasses"
        )

        self.app.accessory_manager.select_accessory(0)

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
    # Stage 13.5
    # Camera started
    # ==========================

    def test_camera_started(self):

        self.assertTrue(
            self.app.is_camera_running
        )

    # ==========================
    # Stage 13.5
    # Accessory rendering
    # ==========================

    def test_render_frame(self):

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

        self.assertIsNotNone(rendered)

    # ==========================
    # Stage 13.5
    # Save photo
    # ==========================

    def test_save_photo(self):

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

        self.app.photo_manager.update_frame(
            rendered
        )

        saved_path = self.app.photo_manager.save_photo()

        self.assertIsNotNone(saved_path)

    # ==========================
    # Stage 13.5
    # File created
    # ==========================

    def test_photo_file_created(self):

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

        self.app.photo_manager.update_frame(
            rendered
        )

        saved_path = self.app.photo_manager.save_photo()

        self.assertTrue(
            os.path.isfile(saved_path)
        )

<<<<<<< HEAD
=======

>>>>>>> d5bf2df (Release v1.0)
if __name__ == "__main__":
    unittest.main()
