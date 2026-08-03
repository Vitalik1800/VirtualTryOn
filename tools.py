from PIL import Image
import colorsys
import os

INPUT_IMAGE = r"D:\Folder_For_Vitaliy\28.07.2026\Dyplom\VirtualTryOn\assets\accessories\glasses\glasses_01.png"
OUTPUT_FOLDER = "colored"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

img = Image.open(INPUT_IMAGE).convert("RGBA")
alpha = img.getchannel("A")

NUM_IMAGES = 20

for i in range(NUM_IMAGES):
    # Генеруємо рівномірно розподілені кольори
    hue = i / NUM_IMAGES
    r, g, b = colorsys.hsv_to_rgb(hue, 1.0, 1.0)

    color = (
        int(r * 255),
        int(g * 255),
        int(b * 255),
        255
    )

    colored = Image.new("RGBA", img.size, color)
    colored.putalpha(alpha)

    output_path = os.path.join(
        OUTPUT_FOLDER,
        f"glasses_{i+1:02d}.png"
    )

    colored.save(output_path)

print(f"Створено {NUM_IMAGES} кольорових копій.")
