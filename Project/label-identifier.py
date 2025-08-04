import os
import shutil

# Base directories
base_dir = r"C:\Users\felip\Desktop\RML-2025\MMHD-project\palmero-C-AALBORG-dataset"
labels_src = os.path.join(base_dir, "labels")

modalities = ["thermal", "depth", "rgb"]
image_ext = ".png"
label_ext = ".txt"

for modality in modalities:
    image_dir = os.path.join(base_dir, modality, "images")
    label_dest_dir = os.path.join(base_dir, modality, "labels")

    # Create label directory
    os.makedirs(label_dest_dir, exist_ok=True)

    # List all files in source label directory
    for label_file in os.listdir(labels_src):
        if label_file.endswith(label_ext):
            image_name = os.path.splitext(label_file)[0] + image_ext
            image_path = os.path.join(image_dir, image_name)

            if os.path.exists(image_path):
                label_src_path = os.path.join(labels_src, label_file)
                label_dest_path = os.path.join(label_dest_dir, label_file)

                shutil.copy(label_src_path, label_dest_path)
                print(f"Copied {label_file} to {label_dest_dir}")
