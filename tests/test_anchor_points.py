from core.camera import Camera
from core.face_detector import FaceDetector
from core.accessory_renderer import AccessoryRenderer

camera = Camera()
detector = FaceDetector()
renderer = AccessoryRenderer()

if camera.open():

    success, frame = camera.read()

    if success:

        results = detector.detect(frame)

        if detector.has_face(results):

            points = detector.get_landmark_points(
                results,
                frame
            )

            anchors = renderer.get_anchor_points(
                points
            )

            print("Anchor points: ")
            print(anchors)
            
        else:

            print("No face detected.")

    else:

        print("Unable to read frame.")

else:

    print("Unable to open camera.")

camera.release()
detector.close()
renderer.close()
