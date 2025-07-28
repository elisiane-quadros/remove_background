import os
from src.image_preocessor import process_images_in_directory

if __name__ == "__main__":
    input_dir = 'images/raw_images'
    output_dir = 'images/processed_images'

    os.makedirs(output_dir, exist_ok=True)

    print(f"Iniciando o processamento de imagens de: {input_dir}")
    print(f"Os resultados serão salvos em: {output_dir}\n")

    process_images_in_directory(input_dir, output_dir)

    print("\nProcessamento concluído!")
