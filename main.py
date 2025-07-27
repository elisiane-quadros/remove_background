from rembg import remove
from PIL import Image
import os
import io

input_dir = 'images/raw_images'
output_dir = 'images/processed_images'

os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(input_dir):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        input_path = os.path.join(input_dir, filename)
        base_name = os.path.splitext(filename)[0]
        output_path = os.path.join(output_dir, base_name + '.png')

        with open(input_path, 'rb') as f:
            input_bytes = f.read()
            output_bytes = remove(input_bytes)

        img_no_bg = Image.open(io.BytesIO(output_bytes))

        img_no_bg.save(output_path, format='PNG')

        print(f"Processed: {filename} -> {output_path}")
