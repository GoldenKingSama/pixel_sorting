import numpy as np
from PIL import Image

def load_image(file_path):
    image = Image.open(file_path)
    return image

def pixel_sort(image):
    img_array = np.array(image)
    height, width, _ = img_array.shape

    for row in range(height):
        sorted_row = sorted(img_array[row], key=lambda pixel: sum(pixel))
        img_array[row] = sorted_row

    sorted_image = Image.fromarray(img_array)
    return sorted_image

def save_image(image, output_path):
    image.save(output_path)

if __name__ == "__main__":
    input_path = input("Enter the input image path: ")
    output_path = input("Enter the output image path: ")

    original_image = load_image(input_path)
    sorted_image = pixel_sort(original_image)

    save_image(sorted_image, output_path)