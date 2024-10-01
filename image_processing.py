from PIL import Image
import numpy as np

def load_image(filepath, new_size):
    img = Image.open(filepath)
    img = img.resize(new_size)
    return np.array(img)
