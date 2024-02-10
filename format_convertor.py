import os
import pydicom
from PIL import Image

def convert_dcm_to_jpg(input_dir, output_dir):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Loop through all files in the input directory
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.endswith('.dcm'):
                # Read the DICOM file
                dcm_path = os.path.join(root, file)
                dcm = pydicom.dcmread(dcm_path)

                # Extract pixel data
                pixel_array = dcm.pixel_array

                # Convert pixel array to a PIL image
                image = Image.fromarray(pixel_array)

                # Save the image as JPEG
                output_file = os.path.splitext(file)[0] + '.jpg'
                output_path = os.path.join(output_dir, output_file)
                image.save(output_path)

                print(f"Converted {file} to {output_file}")

# Example usage
input_directory = '/Users/andy/Downloads/rsna-pneumonia-detection-challenge/labeled_dataset/Pneumonia'
output_directory = '/Users/andy/Downloads/rsna-pneumonia-detection-challenge/labeled_dataset_jpg/Pneumonia'
convert_dcm_to_jpg(input_directory, output_directory)
