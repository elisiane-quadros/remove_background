from rembg import remove
from PIL import Image
import io
import os

def process_image_file(input_path: str, output_path: str):
    try:
        with open(input_path, 'rb') as f:
            input_bytes = f.read()
        output_bytes = remove(input_bytes)

        img_no_bg = Image.open(io.BytesIO(output_bytes))
        img_no_bg.save(output_path, format='PNG')
        print(f"Processed: {os.path.basename(input_path)} -> {output_path}")
    except FileNotFoundError:
        print(f"Error: Input file not found at {input_path}")
        raise
    except Exception as e:
        print(f"Error processing {input_path}: {e}")
        raise

def process_images_in_directory(input_dir: str, output_dir: str):
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(input_dir, filename)
            base_name = os.path.splitext(filename)[0]
            output_path = os.path.join(output_dir, base_name + '.png')
            try:
                process_image_file(input_path, output_path)
            except Exception as e:
                print(f"Skipping {filename} due to error: {e}")


if __name__ == "__main__":
    input_dir = 'images/raw_images'
    output_dir = 'images/processed_images'
    process_images_in_directory(input_dir, output_dir)