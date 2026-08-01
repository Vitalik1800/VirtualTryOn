"""
    Project: Virtual Try-On

    Stage: 3
    Substage: 3.3 - Camera Test
"""

from core.camera import Camera

camera = Camera()

if camera.open():

    success, frame = camera.read()

    if success:

        print("Frame captured successfully.")
        print(frame.shape)

    else:

        print("Frame capture failed.")

    camera.release()

else:

    print("Unable to open camera.")
