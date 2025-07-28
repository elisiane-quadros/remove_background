import pytest
from PIL import Image
import os
import sys
import numpy as np 

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.join(current_dir, '..') 
sys.path.insert(0, os.path.abspath(project_root))

from src.image_processor import process_image_file, process_images_in_directory

# Fixture para criar uma imagem de teste simples
@pytest.fixture
def create_test_image(tmp_path):
    def _create_image(filename="test_input.png", color="red"):
        img_path = tmp_path / filename
        img = Image.new('RGB', (100, 100), color=color)
        img.save(img_path)
        return str(img_path)
    return _create_image

def test_process_image_file_generates_png_with_alpha(create_test_image, tmp_path):
    """
    Testa se a função process_image_file gera um arquivo PNG
    e se ele possui um canal alfa (transparência).
    """
    input_img_path = create_test_image()
    output_img_path = tmp_path / "output.png"

    process_image_file(input_img_path, str(output_img_path))

    assert os.path.exists(output_img_path)

    output_img = Image.open(output_img_path)
    assert output_img.format == 'PNG'
    assert output_img.mode == 'RGBA' # PNGs com transparência são RGBA

    alpha_channel = np.array(output_img)[:, :, 3]
    assert np.any(alpha_channel == 0)


def test_process_image_file_handles_non_existent_input(tmp_path):
    """
    Testa se a função lida corretamente com um arquivo de entrada inexistente.
    """
    non_existent_path = tmp_path / "non_existent.jpg"
    output_path = tmp_path / "output.png"

    with pytest.raises(FileNotFoundError):
        process_image_file(str(non_existent_path), str(output_path))

    assert not os.path.exists(output_path) 

def test_process_images_in_directory_processes_multiple_images(create_test_image, tmp_path):
    """
    Testa se a função de diretório processa múltiplas imagens e cria os arquivos de saída.
    """
    input_dir = tmp_path / "raw_images"
    output_dir = tmp_path / "processed_images"
    os.makedirs(input_dir)


    img1_path = create_test_image("img1.jpg", "blue")
    img2_path = create_test_image("img2.png", "green")

    os.rename(img1_path, input_dir / "img1.jpg")
    os.rename(img2_path, input_dir / "img2.png")

    process_images_in_directory(str(input_dir), str(output_dir))

    assert os.path.exists(output_dir / "img1.png")
    assert os.path.exists(output_dir / "img2.png")
    assert len(os.listdir(output_dir)) == 2