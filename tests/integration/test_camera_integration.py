import unittest

from ui.main_window import MainWindow

class TestCameraIntegration(unittest.TestCase):

    def setUp(self):

        self.app = MainWindow()

    def tearDown(self):

        try:
            self.app.stop_camera()
        except Exception:
            pass

        self.app.destroy()

    # ==========================
    # Stage 13.2
    # Camera startup
    # ==========================

    def test_start_camera(self):

        self.app.start_camera()

        self.assertTrue(
            self.app.is_camera_running
        )

    # ==========================
    # Stage 13.2
    # Read camera frame
    # ==========================

    def test_read_frame(self):

        self.app.start_camera()

        success, frame = self.app.camera.read()

        self.assertTrue(success)

        self.assertIsNotNone(frame)

    # ==========================
    # Stage 13.2
    # Camera -> Face Detector
    # ==========================

    def test_face_detector_pipeline(self):

        self.app.start_camera()

        success, frame = self.app.camera.read()

        self.assertTrue(success)

        landmarks = self.app.face_detector.process(
            frame
        )

        self.assertIsNotNone(landmarks)

    # ==========================
    # Stage 13.2
    # Preview update
    # ==========================

    def test_preview_update(self):

        self.app.start_camera()

        self.app.update_camera()

        image = (
            self.app.camera_preview
            .preview_label
            .image
        )

        self.assertIsNotNone(image)


if __name__ == "__main__":
    unittest.main()
