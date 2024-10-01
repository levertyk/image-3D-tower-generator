from PIL import Image
import numpy as np

def load_image(filepath, new_size):
    img = Image.open(filepath)
    img = img.resize(new_size)
    return np.array(img)

def sample_color(image_data, x, y):
    return image_data[y, x]

def average_color(image_data, x, y, size):
    region = image_data[y:y+size, x:x+size]
    return np.mean(region, axis=(0, 1))
