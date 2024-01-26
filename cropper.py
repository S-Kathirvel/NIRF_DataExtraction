from PIL import Image
import os

# Define the source and destination folders
source_folder = 'F:/NIRF/Images/2022_Engineering/'
destination_folder = 'F:/NIRF/Cropped_Images/2022/'

# Define the cropping box (adjust these coordinates as needed)
crop_box = (0, 369, 1366, 467)

# Iterate through all images in the source folder
for filename in os.listdir(source_folder):

    print(f"Processing Image: {filename}")
    if filename.endswith('.png'):  # Only process PNG files
        # Get the full path of the image
        image_path = os.path.join(source_folder, filename)

        # Open the image
        img = Image.open(image_path)

        # Crop the image
        cropped_img = img.crop(crop_box)

        # Construct the new filename with "c_" prefix
        new_filename = f"c_{filename}"

        # Save the cropped image to the destination folder
        cropped_img.save(os.path.join(destination_folder, new_filename))

print("done!")
