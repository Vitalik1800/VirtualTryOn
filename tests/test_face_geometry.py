from core.camera import Camera
from core.face_detector import FaceDetector

camera = Camera()
detector = FaceDetector()

if camera.open():

    success, frame = camera.read()

    if success:

        results = detector.detect(frame)

        geometry = detector.get_face_geometry(
            results,
            frame
        )

        print(geometry)

camera.release()
detector.close()
