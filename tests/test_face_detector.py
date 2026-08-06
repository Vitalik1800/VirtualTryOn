"""
Project: Virtual Try-On

Stage: 12
Substage: 12.2 - Face Detector Tests

Description:
Unit tests for FaceDetector module.
"""

import unittest
import cv2

from core.face_detector import FaceDetector

class TestFaceDetector(unittest.TestCase):

    def setUp(self):
        self.detector = FaceDetector()

    def tearDown(self):
        self.detector.close()

    def test_detect_face(self):
        """Face should be detected."""

        image = cv2.imread(
            "tests/test_assets/face.jpg"
        )

        landmarks = self.detector.process(image)

        self.assertIsNotNone(landmarks)

    def test_no_face(self):
        """Image without face."""

        image = cv2.imread(
            "tests/test_assets/no_face.jpg"
        )

        landmarks = self.detector.process(image)

        self.assertIsNone(landmarks)

    def test_landmarks(self):
        """Returned landmarks should be valid."""

        image = cv2.imread(
            "tests/test_assets/face.jpg"
        )

        landmarks = self.detector.process(image)

        self.assertIsInstance(landmarks, list)
        self.assertGreater(len(landmarks), 0)

        x, y = landmarks[0]

        self.assertIsInstance(x, int)
        self.assertIsInstance(y, int)

if __name__ == "__main__":
    unittest.main()
