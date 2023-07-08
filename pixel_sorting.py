from PIL import Image
import numpy as np

input_path = input("Enter the input image path: ")
output_path = input("Enter the output image path: ")

# Load Image
image = Image.open(input_path)
img_array = np.array(image)
height, width, _ = img_array.shape

# Pixel Sorting
for row in range(height):
    sorted_row = sorted(img_array[row], key=lambda pixel: sum(pixel))
    img_array[row] = sorted_row

sorted_image = Image.fromarray(img_array)

# Save Image
sorted_image.save(output_path)
