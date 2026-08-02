from core.accessory_manager import AccessoryManager

manager = AccessoryManager()

files = manager.get_accessories("glasses")

print(len(files))

for file in files:
    print(file)
