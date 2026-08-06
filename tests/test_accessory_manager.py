"""
Project: Virtual Try-On

Stage: 12
Substage: 12.3 - Accessory Manager Tests

Description:
Unit tests for AccessoryManager module.
"""

import os
import shutil
import tempfile
import unittest

from core.accessory_manager import AccessoryManager

class TestAccessoryManager(unittest.TestCase):

    def setUp(self):

        self.manager = AccessoryManager()

    def tearDown(self):

        self.manager.close()

    # ==========================================
    # Categories
    # ==========================================

    def test_categories_load(self):
        """
        Categories should be initialized.
        """

        self.assertGreater(
            len(self.manager.categories),
            0
        )

        self.assertIn(
            "glasses",
            self.manager.categories
        )

        self.assertIn(
            "hats",
            self.manager.categories
        )

        self.assertIn(
            "masks",
            self.manager.categories
        )

    # ==========================================
    # PNG list
    # ==========================================

    def test_get_categories(self):
        """
        PNG accessory list should be returned.
        """

        accessories = self.manager.get_accessories(
            "glasses"
        )

        self.assertIsInstance(
            accessories,
            list
        )

        self.assertGreater(
            len(accessories),
            0
        )

        for accessory in accessories:

            self.assertTrue(
                accessory.endswith(".png")
            )

            self.assertTrue(
                os.path.isfile(accessory)
            )

    # ==========================================
    # Cache
    # ==========================================

    def test_cache(self):
        """
        Loaded accessory should be cached.
        """

        accessories = self.manager.get_accessories(
            "glasses"
        )

        path = accessories[0]

        image1 = self.manager.get_accessory(path)
        image2 = self.manager.get_accessory(path)

        self.assertIsNotNone(image1)

        self.assertIs(
            image1,
            image2
        )

    # ==========================================
    # Missing folder
    # ==========================================

    def test_missing_folder(self):
        """
        Missing folder should return empty list.
        """

        accessories = self.manager.get_accessories(
            "unknown_category"
        )

        self.assertEqual(
            accessories,
            []
        )

    # ==========================================
    # Broken PNG
    # ==========================================

    def test_invalid_png(self):
        """
        Invalid PNG should not be loaded.
        """

        temp_dir = tempfile.mkdtemp()

        try:

            invalid_png = os.path.join(
                temp_dir,
                "broken.png"
            )

            with open(
                invalid_png,
                "w",
                encoding="utf-8"
            ) as file:

                file.write(
                    "Not a PNG file"
                )

            image = self.manager.load_accessory(
                invalid_png
            )

            self.assertIsNone(
                image
            )

        finally:

            shutil.rmtree(temp_dir)

    # ==========================================
    # Accessory switching
    # ==========================================

    def test_switch_accessories(self):
        """
        Next/previous accessory switching.
        """

        self.assertTrue(
            self.manager.select_category(
                "glasses"
            )
        )

        first = self.manager.current_index

        second = self.manager.next_accessory()

        self.assertNotEqual(
            first,
            second
        )

        previous = self.manager.previous_accessory()

        self.assertEqual(
            previous,
            first
        )

if __name__ == "__main__":

    unittest.main()
