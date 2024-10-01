from gui import run_gui
from tower_generator import generate_towers
from image_processing import load_image

if __name__ == "__main__":
    image = load_image("data\\frog.jpg", (100, 100))  # Load the image
    run_gui(generate_towers(image, 0, 0, 10))  # Start the application
