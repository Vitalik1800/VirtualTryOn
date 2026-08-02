from core.camera import Camera
from core.face_detector import FaceDetector

camera = Camera()
detector = FaceDetector()

if camera.open():

    success, frame = camera.read()

    if success:

        results = detector.detect(frame)

        points = detector.get_landmark_points(
            results,
            frame
        )

        print(f"Points: {len(points)}")

        if points:

            print(points[0])

camera.release()
detector.close()
