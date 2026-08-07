import os
import shutil
import tempfile
import unittest

from ui.main_window import MainWindow

<<<<<<< HEAD
=======

>>>>>>> d5bf2df (Release v1.0)
class TestFullApplication(unittest.TestCase):

    def setUp(self):

        self.app = MainWindow()

        self.temp_dir = tempfile.mkdtemp()

        self.app.photo_manager.save_directory = self.temp_dir
        self.app.video_manager.save_directory = self.temp_dir

    def tearDown(self):

        try:
            self.app.video_manager.stop_recording()
        except Exception:
            pass

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
    # Stage 13.7
    # Full user scenario
    # ==========================

    def test_full_user_scenario(self):

        # ---- Start camera ----

        self.assertTrue(
            self.app.camera.open()
        )

        success, frame = self.app.camera.read()

        self.assertTrue(success)

        height, width = frame.shape[:2]

        # ---- Start video recording ----

        output_video = (
            self.app.video_manager.create_output_path()
        )

        self.assertTrue(

            self.app.video_manager.start_recording(
                output_video,
                width,
                height
            )
<<<<<<< HEAD
            
=======

>>>>>>> d5bf2df (Release v1.0)
        )

        # ---- Detect face ----

        landmarks = self.app.face_detector.process(
            frame
        )

        # ---- Select category ----

        self.assertTrue(

            self.app.accessory_manager.select_category(
                "glasses"
            )
<<<<<<< HEAD
            
=======

>>>>>>> d5bf2df (Release v1.0)
        )

        # ---- Select accessory ----

        self.assertTrue(

            self.app.accessory_manager.select_accessory(
                0
            )
<<<<<<< HEAD
            
=======

>>>>>>> d5bf2df (Release v1.0)
        )

        accessory = (
            self.app.accessory_manager
            .get_current_accessory()
        )

        path = (
            self.app.accessory_manager
            .get_current_path()
        )

        # ---- Render ----

        rendered = self.app.accessory_renderer.render(
            frame.copy(),
            accessory,
            landmarks,
            path
        )

        self.assertIsNotNone(rendered)

        # ---- Preview ----

        self.app.photo_manager.update_frame(
            rendered
        )

        self.assertTrue(
            self.app.photo_manager.has_frame()
        )

        # ---- Save photo ----

        photo_path = (
            self.app.photo_manager.save_photo()
        )

        self.assertIsNotNone(photo_path)

        self.assertTrue(
            os.path.isfile(photo_path)
        )

        # ---- Record video ----

        for _ in range(20):
<<<<<<< HEAD

=======
>>>>>>> d5bf2df (Release v1.0)
            success, frame = self.app.camera.read()

            self.assertTrue(success)

            landmarks = self.app.face_detector.process(
                frame
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

        # --- Finish recording ----

        self.app.video_manager.stop_recording()

        self.assertTrue(
            os.path.isfile(output_video)
        )

        self.assertGreater(
            os.path.getsize(output_video),
            0
        )

        # ---- Close camera ----

        self.app.camera.release()

        self.assertFalse(
            self.app.camera.is_opened()
        )
<<<<<<< HEAD
    
=======


>>>>>>> d5bf2df (Release v1.0)
if __name__ == "__main__":
    unittest.main()
