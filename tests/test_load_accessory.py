from core.accessory_manager import AccessoryManager

manager = AccessoryManager()

image = manager.load_accessory(
    "assets/accessories/glasses/example.png"
)

print(image is not None)

if image is not None:
    print(image.shape)
