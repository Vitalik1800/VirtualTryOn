from core.accessory_manager import AccessoryManager
from core.accessory_renderer import AccessoryRenderer

manager = AccessoryManager()
renderer = AccessoryRenderer()

image = manager.load_accessory(
    "assets/accessories/glasses/glasses_01.png"
)

left_eye = (500, 300)
right_eye = (700, 340)

angle = renderer.calculate_angle(
    left_eye,
    right_eye
)

print(f"Angle: {angle:.2f}")

rotated = renderer.rotate_accessory(
    image,
    angle
)

print(rotated.shape)

manager.close()
renderer.close()
