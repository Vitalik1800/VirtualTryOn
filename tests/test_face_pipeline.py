import unittest

from ui.main_window import MainWindow

class TestFacePipeline(unittest.TestCase):

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
    # Stage 13.3
    # Camera -> Face Detector
    # ==========================

    def test_camera_to_detector(self):

        success, frame = self.app.camera.read()

        self.assertTrue(success)

        landmarks = self.app.face_detector.process(frame)

        self.assertIsNotNone(landmarks)

    # ==========================
    # Stage 13.3
    # Landmark extraction
    # ==========================

    def test_landmark_generation(self):

        success, frame = self.app.camera.read()

        self.assertTrue(success)

        landmarks = self.app.face_detector.process(frame)

        self.assertIsInstance(
            landmarks,
            list
        )

    # ==========================
    # Stage 13.3
    # Landmarks -> Renderer
    # ==========================

    def test_renderer_pipeline(self):

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

        result = self.app.accessory_renderer.render(
            frame.copy(),
            accessory,
            landmarks,
            path
        )

        self.assertIsNotNone(result)

    # ==========================
    # Stage 13.3
    # Pipeline stability
    # ==========================

    def test_pipeline_without_exception(self):

        success, frame = self.app.camera.read()

        self.assertTrue(success)

        try:

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

            self.app.accessory_renderer.render(
                frame,
                accessory,
                landmarks,
                path
            )

            ok = True
            
        except Exception:

            ok = False

        self.assertTrue(ok)

if __name__ == "__main__":
    unittest.main()
