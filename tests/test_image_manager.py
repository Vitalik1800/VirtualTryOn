"""
    Project: Virtual Try-On

    Stage: 3
    Substage: 3.4 - Image Conversion Test
"""

from core.camera import Camera
from core.image_manager import ImageManager

camera = Camera()

if camera.open():

    success, frame = camera.read()

    if success:

        rgb = ImageManager.bgr_to_rgb(frame)
        pillow = ImageManager.rgb_to_pillow(rgb)
        image = ImageManager.pillow_to_ctk(
            pillow,
            size=(640, 480)
        )

        print("Image conversion successful.")
        print(type(image))

    else:

        print("Failed to capture frame.")

    camera.release()

else:

    print("Camera initialization failed.")
