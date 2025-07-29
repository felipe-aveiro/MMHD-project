from ultralytics import YOLO #  use YOLOv8
import matplotlib.pyplot as plt
from PIL import Image
import os

BASE_DIR_rgb = os.path.abspath(os.path.join(os.path.dirname(__file__),"..", "MID-3K"))

rgb_yaml_content = f"""
path: {BASE_DIR_rgb}/dataset/rgb
train: train/rgb/
val: validation/rgb/
test: test/rgb/
# class names
names:
  0: human
"""

with open("rgb.yaml", "w") as f:
    f.write(rgb_yaml_content.strip())

# Training parameters
num_epochs = 50

# Load YOLOv8 nano model
model_rgb = YOLO('yolov8n.pt')

# Start training
model_rgb.train(
    pretrained = False, #DEFINE IF USE PRETRAINED WEIGHTS
    data = 'rgb.yaml', #DATASET CONFIG FILE
    epochs = num_epochs, #NUMBER OF EPOCHS
    patience = num_epochs, # SET patience = num_epochs TO DISABLE EARLY STOP
    imgsz = 640, #TO REZISE IMAGES, DEFAULT 640
    save = True, #TO SAVE CHECKPOINTS AND FINAL MODEL WEIGHTS
    project='RML-project-MMHD', #NAME OF PROJECT
    name = 'rgb', #SUB-NAME OF PROJECT or MODALITY
    plots = True #TO SHOW PLOTS OF TRAINING AND VALIDATION METRICS
)

# Evaluate on the test set
results_test = model_rgb.val(
    data='rgb.yaml',
    split='test',
    project='RML-project-MMHD',
    name='test_eval',
    plots=True
)
