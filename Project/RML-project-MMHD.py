from ultralytics import YOLO #  use YOLOv8
import shutil
import torch
from PIL import Image
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__),"..", "MID-3K"))

# RGB YAML
rgb_yaml_path = os.path.join(BASE_DIR, "dataset", "rgb.yaml")
rgb_yaml_content = f"""
path: {BASE_DIR}/dataset/rgb
train: train/rgb
val: val/rgb
test: test/rgb
names:
  0: human
"""

# THERMAL YAML
thermal_yaml_path = os.path.join(BASE_DIR, "dataset", "thermal.yaml")
thermal_yaml_content = f"""
path: {BASE_DIR}/dataset/thermal
train: train/thermal
val: val/thermal
test: test/thermal
names:
  0: human
"""

# Save
with open(rgb_yaml_path, "w") as f:
    f.write(rgb_yaml_content.strip())

with open(thermal_yaml_path, "w") as f:
    f.write(thermal_yaml_content.strip())

print("✅ Checkpoint:\n")
print("\t📄 ", rgb_yaml_path)
print("\t📄 ", thermal_yaml_path)

print("🏃‍♂️💨 Using GPU..." if torch.cuda.is_available() else "🐌 Using CPU...")

#REMOVE OTHERS RGB FOLDERS
if os.path.exists("RML-project-MMHD/rgb"):
    shutil.rmtree("RML-project-MMHD/rgb")

# Training parameters
# NUMBER OF EPOCHS TO TRAIN
num_epochs_rgb = 50

# LOAD YOLOv8 SMALL MODEL FOR RGB MODALITY (nano, small, medium...)
model_rgb = YOLO('yolov8s.pt') # LOAD YOLO MODEL FOR TRAINNING Ex.: yolov8n.pt, yolov8s.pt, yolov8m.pt ...

rgb_yaml_path = os.path.join(BASE_DIR, "dataset", "rgb.yaml")

# Start training
#https://docs.ultralytics.com/usage/cfg/#train-settings
model_rgb.train(
    pretrained = False, # DEFINE IF USE PRETRAINED WEIGHTS
    data = rgb_yaml_path, # DATASET CONFIG FILE
    epochs = num_epochs_rgb, #NUMBER OF EPOCHS
    device = 0 if torch.cuda.is_available() else 'cpu', # USE GPU
    patience = num_epochs_rgb, # SET patience = num_epochs_rgb TO DISABLE EARLY STOP
    imgsz = 640, # TO REZISE IMAGES, DEFAULT 640
    save = True, # TO SAVE CHECKPOINTS AND FINAL MODEL WEIGHTS
    project='RML-project-MMHD', #NAME OF PROJECT
    name = 'rgb', # SUB-NAME OF PROJECT or MODALITY
    plots = True # TO SHOW PLOTS OF TRAINING AND VALIDATION METRICS
)

#REMOVE OTHERS THERMAL FOLDERS
if os.path.exists("RML-project-MMHD/thermal"):
    shutil.rmtree("RML-project-MMHD/thermal")

# Training parameters
# NUMBER OF EPOCHS TO TRAIN
num_epochs_thermal = 50

# LOAD YOLOv8 SMALL MODEL FOR THERMAL MODALITY (nano, small, medium...)
model_thermal = YOLO('yolov8s.pt') # LOAD YOLO MODEL FOR TRAINNING Ex.: yolov8n.pt, yolov8s.pt, yolov8m.pt ...

thermal_yaml_path = os.path.join(BASE_DIR, "dataset", "thermal.yaml")

# Start training
#https://docs.ultralytics.com/usage/cfg/#train-settings
model_thermal.train(
    pretrained = False, # DEFINE IF USE PRETRAINED WEIGHTS
    data = thermal_yaml_path, # DATASET CONFIG FILE
    epochs = num_epochs_thermal, #NUMBER OF EPOCHS
    device = 0 if torch.cuda.is_available() else 'cpu', # USE GPU
    patience = num_epochs_thermal, # SET patience = num_epochs_thermal TO DISABLE EARLY STOP
    imgsz = 640, # TO REZISE IMAGES, DEFAULT 640
    save = True, # TO SAVE CHECKPOINTS AND FINAL MODEL WEIGHTS
    project='RML-project-MMHD', #NAME OF PROJECT
    name = 'thermal', # SUB-NAME OF PROJECT or MODALITY
    plots = True # TO SHOW PLOTS OF TRAINING AND VALIDATION METRICS
)

# https://docs.ultralytics.com/modes/val/#arguments-for-yolo-model-validation
# Evaluate on the test set
results_test_rgb = model_rgb.val(
    data='rgb.yaml',
    split='test',
    project='RML-project-MMHD',
    name='test_eval_rgb',
    plots=True
)

# https://docs.ultralytics.com/modes/val/#arguments-for-yolo-model-validation
# Evaluate on the test set
results_test_thermal = model_thermal.val(
    data='thermal.yaml',
    split='test',
    project='RML-project-MMHD',
    name='test_eval_thermal',
    plots=True
)
