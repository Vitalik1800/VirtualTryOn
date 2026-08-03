from core.accessory_manager import AccessoryManager
from core.accessory_renderer import AccessoryRenderer

manager = AccessoryManager()
renderer = AccessoryRenderer()

image = manager.load_accessory(
    "assets/accessories/glasses/glasses_01.png"
)

geometry = {
    "width": 250,
    "height": 320
}

scaled = renderer.scale_accessory(
    image,
    geometry,
    scale=1.2
)

print(image.shape)
print(scaled.shape)

renderer.close()
manager.close()
