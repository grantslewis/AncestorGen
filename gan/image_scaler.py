from PIL import Image
import os

def scale_image(input_path, output_path, new_size=(1024, 1024)):
    """ Scale the image to be exactly 1024x1024 pixels. """
    with Image.open(input_path) as img:
        # Resize the image to 1024x1024
        img = img.resize(new_size, Image.ANTIALIAS)

        # Create output directory if it doesn't exist
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Save the scaled image
        img.save(output_path)

def resize_images_in_folder(input_folder, output_folder):
    """ Resize all images in the input folder and save them to the output folder. """
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            scale_image(input_path, output_path)

# Specify your input and output folders
input_folder = '../KinFaceW-II/images/father-dau' #'path/to/your/input/folder'
output_folder = './scaled_images/father-dau' #'path/to/your/output/folder'

resize_images_in_folder(input_folder, output_folder)
