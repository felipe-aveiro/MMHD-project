import os
import random
import shutil
import time
from tqdm import tqdm

# Base directory
BASE_DIR = "/content/MMHD-project/MID-3K"

def process_dataset(BASE_DIR, modality):
    print(f"\n🧰 Processing modality: {modality.upper()}")
    
    # Paths to the images and labels of the selected modality
    images_dir = os.path.join(BASE_DIR, "dataset", modality, "whole-dataset", modality, "images")
    labels_dir = os.path.join(BASE_DIR, "dataset", modality, "whole-dataset", modality, "labels")

    # Build output directories for a given split (train, val, test)
    def build_output_path(split):
        return {
            "images": os.path.join(BASE_DIR, "dataset", modality, split, modality, "images"),
            "labels": os.path.join(BASE_DIR, "dataset", modality, split, modality, "labels"),
        }

    # Collect and shuffle all image files
    image_files = [f for f in os.listdir(images_dir) if f.endswith('.png')]
    random.shuffle(image_files)

    # Split ratios
    train_percentage = 0.65
    val_percentage = 0.15
    test_percentage = 0.20

    # Calculate the split sizes
    total = len(image_files)
    train_split = int(total * train_percentage)
    val_split = int(total * val_percentage)
    test_split = total - train_split - val_split # ensure total coverage

    # Lists for each split
    train_files = image_files[:train_split]
    val_files = image_files[train_split:train_split + val_split]
    test_files = image_files[train_split + val_split:]

    print(f"📊 Total {modality} images: {total}\n")

    print(f"🟢 Train: {len(train_files)}")
    print(f"🔵 Validation: {len(val_files)}")
    print(f"🟣 Test: {len(test_files)}")

 # Delete and recreate output folders
    def prepare_output_folders(splits=["train", "val", "test"]):
        for split in splits:
            paths = build_output_path(split)
            for subpath in paths.values():
                if os.path.exists(subpath):
                    shutil.rmtree(subpath)
                os.makedirs(subpath, exist_ok=True)

    prepare_output_folders()

    # Copy images and corresponding labels to each split folder
    def copy_files(file_list, split):
        paths = build_output_path(split)
        print(f"\n📦 Copying {split} set ({len(file_list)} files):")
        for img_file in tqdm(file_list, desc=f"→ {split.capitalize()} progress", unit=" images"):
            label_file = os.path.splitext(img_file)[0] + ".txt"
            src_img = os.path.join(images_dir, img_file)
            src_lbl = os.path.join(labels_dir, label_file)
            dst_img = os.path.join(paths["images"], img_file)
            dst_lbl = os.path.join(paths["labels"], label_file)

            if os.path.exists(src_img) and os.path.exists(src_lbl):
                shutil.copy2(src_img, dst_img)
                shutil.copy2(src_lbl, dst_lbl)
            else:
                print(f"⚠️ Skipped (missing image or label): {img_file}")

    # Run the file copying process and measure time
    start_time = time.perf_counter()
    copy_files(train_files, "train")
    copy_files(val_files, "val")
    copy_files(test_files, "test")
    elapsed = time.perf_counter() - start_time
    print(f"\n\n🔔 {modality.upper()} dataset split completed in {elapsed:.2f} seconds!")

# Process RGB and Thermal datasets
process_dataset(BASE_DIR, "rgb")
process_dataset(BASE_DIR, "thermal")
