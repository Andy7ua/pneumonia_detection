import pandas as pd
import os
import shutil

# Load the label data
labels_df = pd.read_csv("/Users/andy/Downloads/rsna-pneumonia-detection-challenge/stage_2_train_labels.csv")

# Create a directory for the new labeled dataset
output_dir = "/Users/andy/Downloads/rsna-pneumonia-detection-challenge/labeled_dataset"
os.makedirs(output_dir, exist_ok=True)

# Iterate through the data and copy images according to the labels
for index, row in labels_df.iterrows():
    patient_id = row["patientId"]
    target = row["Target"]
    src_image_path = os.path.join("/Users/andy/Downloads/rsna-pneumonia-detection-challenge/stage_2_train_images", f"{patient_id}.dcm")

    # Determine the destination directory based on the label
    if target == 0:
        dest_dir = os.path.join(output_dir, "Normal")
    else:
        dest_dir = os.path.join(output_dir, "Pneumonia")

    # Create the destination directory if it doesn't exist
    os.makedirs(dest_dir, exist_ok=True)

    # Copy the image to the destination directory
    shutil.copy(src_image_path, dest_dir)
    print(f"Copied {src_image_path} to {dest_dir}")

print("Data labeling completed.")
