import numpy as np
import image_processing

def generate_towers(image, layout, tower_height, max_height):
    towers = []
    for x in range(image.shape[1]):
        for y in range(image.shape[0]):
            color = image_processing.sample_color(image, x, y)
            height = max_height * (color[0] / 255) # red channel TODO make user input
            towers.append({'x' : x, 'y' : y, 'height': height})
    return towers