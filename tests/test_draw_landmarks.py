import cv2

from core.camera import Camera
from core.face_detector import FaceDetector

camera = Camera()
detector = FaceDetector()

if camera.open():

    while True:

        success, frame = camera.read()

        if not success:
            break

        results = detector.detect(frame)

        frame = detector.draw_landmarks(
            frame,
            results
        )

        cv2.imshow(
            "Face Mesh",
            frame
        )

        if cv2.waitKey(1) & 0xFF == 27:
            break

camera.release()
detector.close()

cv2.destroyAllWindows()
