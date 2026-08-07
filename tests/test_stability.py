import gc
import tempfile
import shutil
import unittest

from ui.main_window import MainWindow

class TestStability(unittest.TestCase):

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
    # Stage 13.8
    # Camera restart
    # ==========================

    def test_camera_restart(self):

        for _ in range(10):

            self.assertTrue(
                self.app.camera.open()
            )

            self.assertTrue(
                self.app.camera.is_opened()
            )

            self.app.camera.release()

            self.assertFalse(
                self.app.camera.is_opened()
            )

    # ==========================
    # Stage 13.8
    # Fast accessory switching
    # ==========================

    def test_fast_accessory_switching(self):

        category = "glasses"

        self.app.accessory_manager.select_category(
            category
        )

        accessories = (
            self.app.accessory_manager.get_accessories(
                category
            )
        )

        count = len(accessories)

        self.assertGreater(count, 0)

        for _ in range(20):

            for index in range(count):

                self.assertTrue(
                    self.app.accessory_manager.select_accessory(
                        index
                    )
                )

    # ==========================
    # Stage 13.8
    # Cache cleanup
    # ==========================

    def test_cache_cleanup(self):

        renderer = self.app.accessory_renderer

        renderer.scaled_cache["a"] = object()
        renderer.rotated_cache["b"] = object()
        renderer.cache["c"] = object()

        renderer.clear_cache()

        self.assertEqual(
            len(renderer.scaled_cache),
            0
        )

        self.assertEqual(
            len(renderer.rotated_cache),
            0
        )

        self.assertEqual(
            len(renderer.cache),
            0
        )

    # ==========================
    # Stage 13.8
    # Long running stability
    # ==========================

    def test_long_running(self):

        self.assertTrue(
            self.app.camera.open()
        )

        self.app.accessory_manager.select_category(
            "glasses"
        )

        self.app.accessory_manager.select_accessory(
            0
        )

        accessory = (
            self.app.accessory_manager
            .get_current_accessory()
        )

        path = (
            self.app.accessory_manager
            .get_current_path()
        )

        for _ in range(100):

            success, frame = self.app.camera.read()

            self.assertTrue(success)

            landmarks = (
                self.app.face_detector.process(
                    frame
                )
            )

            rendered = (
                self.app.accessory_renderer.render(
                    frame.copy(),
                    accessory,
                    landmarks,
                    path
                )
            )

            self.assertIsNotNone(
                rendered
            )

    # ==========================
    # Stage 13.8
    # Resource cleanup
    # ==========================

    def test_resource_cleanup(self):

        self.app.camera.open()

        self.app.camera.release()

        self.app.face_detector.close()

        self.app.accessory_renderer.close()

        gc.collect()

        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
