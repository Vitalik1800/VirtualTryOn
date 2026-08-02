from core.accessory_manager import AccessoryManager

manager = AccessoryManager()

manager.select_category("glasses")

print(len(manager.cache))

manager.close()

print(manager.current_category)
print(manager.current_accessories)
print(manager.current_index)
print(len(manager.cache))
