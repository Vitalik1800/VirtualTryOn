from core.accessory_manager import AccessoryManager
from core.accessory_renderer import AccessoryRenderer

manager = AccessoryManager()
renderer = AccessoryRenderer()

image = manager.load_accessory(
    "assets/accessories/glasses/glasses_01.png"
)

position = renderer.calculate_position(
    image,
    (640, 320)
)

print(position)

manager.close()
renderer.close()
