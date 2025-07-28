import os
import random
import shutil
import time
from tqdm import tqdm

# Base path
BASE_DIR_rgb = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "MID-3K"))
images_dir = os.path.join(BASE_DIR_rgb, "dataset", "rgb", "whole-dataset", "rgb", "images")
labels_dir = os.path.join(BASE_DIR_rgb, "dataset", "rgb", "whole-dataset", "rgb", "labels")

# Output directory builder
def build_output_path(split):
    return {
        "images": os.path.join(BASE_DIR_rgb, "dataset", "rgb", split, "rgb", "images"),
        "labels": os.path.join(BASE_DIR_rgb, "dataset", "rgb", split, "rgb", "labels"),
    }

# Collect and shuffle all image files
image_files = [f for f in os.listdir(images_dir) if f.endswith(('.jpg', '.png'))]
random.shuffle(image_files)

# Split sizes
train_percentage = 0.65
val_percentage = 0.15
test_percentage = 0.20

total = len(image_files)
train_split = int(total * train_percentage)
val_split = int(total * val_percentage)
test_split = total - train_split - val_split  # guarantees full coverage

train_files = image_files[:train_split]
val_files = image_files[train_split:train_split + val_split]
test_files = image_files[train_split + val_split:]

print(f"📊 Total images: {total}")
print(f"🟢 Train: {len(train_files)}")
print(f"🔵 Validation:   {len(val_files)}")
print(f"🟣 Test:  {len(test_files)}")

# Clean and recreate output folders
def prepare_output_folders(splits=["train", "validation", "test"]):
    for split in splits:
        paths = build_output_path(split)
        for subpath in paths.values():
            if os.path.exists(subpath):
                shutil.rmtree(subpath)
            os.makedirs(subpath, exist_ok=True)

prepare_output_folders()

# Function to copy paired image-label files
def copy_files(file_list, split):
    paths = build_output_path(split)
    print(f"\n📦 Copying {split} set ({len(file_list)} files):")
    for img_file in tqdm(file_list, desc=f"→ {split.capitalize()} progress"):
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

# Time execution
start_time = time.perf_counter()

copy_files(train_files, "train")
copy_files(val_files, "validation")
copy_files(test_files, "test")

elapsed = time.perf_counter() - start_time
print(f"\n✅ Dataset split completed in {elapsed:.2f} seconds.\n")
