from core.accessory_manager import AccessoryManager

manager = AccessoryManager()

path = "assets/accessories/glasses/glasses_01.png"

image1 = manager.get_accessory(path)
image2 = manager.get_accessory(path)

print(image1 is image2)
print(len(manager.cache))
