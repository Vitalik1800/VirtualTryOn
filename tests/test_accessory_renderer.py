import unittest
import numpy as np

from core.accessory_renderer import AccessoryRenderer

class TestAccessoryRenderer(unittest.TestCase):

    def setUp(self):
        self.renderer = AccessoryRenderer()

    def tearDown(self):
        self.renderer.close()

    def create_frame(self):
        return np.zeros((480, 640, 3), dtype=np.uint8)

    def create_accessory(self):
        accessory = np.zeros((100, 100, 4), dtype=np.uint8)

        accessory[:, :, 0] = 255
        accessory[:, :, 3] = 255

        return accessory

    def test_alpha_blending(self):
        """
        PNG should be blended with frame.
        """

        frame = self.create_frame()
        accessory = self.create_accessory()

        result = self.renderer.alpha_blend(
            frame.copy(),
            accessory,
            (100, 100)
        )

        self.assertIsNotNone(result)

        self.assertFalse(
            np.array_equal(frame, result)
        )

    def test_alpha_channel(self):
        """
        Alpha channel must affect pixels.
        """

        frame = self.create_frame()
        accessory = self.create_accessory()

        accessory[:, :, 3] = 128

        result = self.renderer.alpha_blend(
            frame.copy(),
            accessory,
            (150, 150)
        )

        self.assertIsNotNone(result)

    def test_outside_frame(self):
        """
        Accessory outside frame should not crash.
        """

        frame = self.create_frame()
        accessory = self.create_accessory()

        result = self.renderer.alpha_blend(
            frame.copy(),
            accessory,
            (1000, 1000)
        )

        self.assertTrue(
            np.array_equal(frame, result)
        )

    def test_no_landmarks(self):
        """
        Render should return original frame without landmarks.
        """

        frame = self.create_frame()

        result = self.renderer.render(
            frame.copy(),
            self.create_accessory(),
            [],
            "assets/accessories/glasses/glasses_01.png"
        )

        self.assertTrue(
            np.array_equal(frame, result)
        )

    def test_null_frame(self):
        """
        None frame should return None.
        """

        result = self.renderer.render(
            None,
            self.create_accessory(),
            [],
            "assets/accessories/glasses/glasses_01.png"
        )

        self.assertIsNone(result)

    def test_trim_transparent(self):
        """
        Transparent borders should be removed.
        """

        image = np.zeros((100, 100, 4), dtype=np.uint8)

        image[30:70, 30:70, :3] = 255
        image[30:70, 30:70, 3] = 255

        trimmed = self.renderer.trim_transparent(image)

        self.assertLess(
            trimmed.shape[0],
            image.shape[0]
        )

        self.assertLess(
            trimmed.shape[1],
            image.shape[1]
        )

    def test_calculate_angle(self):
        """
        Rotation angle should be calculated.
        """

        angle = self.renderer.calculate_angle(
            (0, 0),
            (100, 0)
        )

        self.assertEqual(angle, 0)

    def test_calculate_position(self):
        """
        Position should be calculated.
        """

        accessory = self.create_accessory()

        position = self.renderer.calculate_position(
            accessory,
            (200, 200)
        )

        self.assertIsInstance(position, tuple)

        self.assertEqual(len(position), 2)

    def test_get_accessory_type(self):
        """
        Accessory type should be determined.
        """

        accessory_type = self.renderer.get_accessory_type(
            "assets/accessories/glasses/glasses_01.png"
        )

        self.assertEqual(
            accessory_type,
            "glasses"
        )

if __name__ == "__main__":
    unittest.main()
