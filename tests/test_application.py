import unittest

from ui.main_window import MainWindow

class TestApplicationStartup(unittest.TestCase):

    # ==========================
    # Stage 13.1
    # Create application
    # ==========================

    def test_create_main_window(self):

        app = MainWindow()

        self.assertIsNotNone(app)

        app.destroy()

    # ==========================
    # Stage 13.1
    # Initialize modules
    # ==========================

    def test_initialize_modules(self):

        app = MainWindow()

        self.assertIsNotNone(app.camera)
        self.assertIsNotNone(app.face_detector)
        self.assertIsNotNone(app.accessory_manager)
        self.assertIsNotNone(app.accessory_renderer)
        self.assertIsNotNone(app.photo_manager)
        self.assertIsNotNone(app.video_manager)

        app.destroy()

    # ==========================
    # Stage 13.1
    # Create UI
    # ==========================

    def test_create_interface(self):

        app = MainWindow()

        self.assertIsNotNone(app.toolbar)
        self.assertIsNotNone(app.sidebar)
        self.assertIsNotNone(app.camera_preview)
        self.assertIsNotNone(app.status_bar)

        app.destroy()

    # ==========================
    # Stage 13.1
    # Startup without exceptions
    # ==========================

    def test_application_startup(self):

        try:

            app = MainWindow()

            app.update()

            success = True

        except Exception:

            success = False

        finally:

            if "app" in locals():
                app.destroy()

        self.assertTrue(success)

if __name__ == "__main__":
    unittest.main()
