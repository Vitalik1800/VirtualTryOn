import unittest

from ui.main_window import MainWindow

<<<<<<< HEAD
=======

>>>>>>> d5bf2df (Release v1.0)
class TestAccessoryPipeline(unittest.TestCase):

    def setUp(self):

        self.app = MainWindow()

        self.app.start_camera()

        self.app.accessory_manager.select_category(
            "glasses"
        )

    def tearDown(self):

        try:
            self.app.stop_camera()
        except Exception:
            pass

        self.app.destroy()

    # ==========================
    # Stage 13.4
    # Category selection
    # ==========================

    def test_select_category(self):

        result = self.app.accessory_manager.select_category(
            "glasses"
        )

        self.assertTrue(result)

        self.assertGreater(
            len(self.app.accessory_manager.current_accessories),
            0
        )

    # ==========================
    # Stage 13.4
    # Accessory selection
    # ==========================

    def test_select_accessory(self):

        result = self.app.accessory_manager.select_accessory(0)

        self.assertTrue(result)

        path = self.app.accessory_manager.get_current_path()

        self.assertIsNotNone(path)

    # ==========================
    # Stage 13.4
    # PNG loading
    # ==========================

    def test_load_png(self):

        path = self.app.accessory_manager.get_current_path()

        accessory = self.app.accessory_manager.get_current_accessory()

        self.assertIsNotNone(path)

        self.assertIsNotNone(accessory)

    # ==========================
    # Stage 13.4
    # Render accessory
    # ==========================

    def test_render_accessory(self):

        success, frame = self.app.camera.read()

        self.assertTrue(success)

        landmarks = self.app.face_detector.process(frame)

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
    # Stage 13.4
    # Preview update
    # ==========================

    def test_preview_update(self):

        self.app.update_camera()

        image = (
            self.app.camera_preview
            .preview_label
            .image
        )

        self.assertIsNotNone(image)

<<<<<<< HEAD
=======

>>>>>>> d5bf2df (Release v1.0)
if __name__ == "__main__":
    unittest.main()
