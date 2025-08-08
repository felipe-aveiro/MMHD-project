# 🤖 **MMHD-project - Multi-Modality Human Detection**

**MMHD** (Multi-Modality Human Detection) is a research-oriented project developed for the **Robotics and Machine Learning** course at the **University of Coimbra**.  
The goal is to explore and compare the performance of **YOLOv8 models** for **human detection** using **RGB**, **thermal**, and **depth image modalities**, individually and in a fusion-based setup.

🎓🏆 **Approved with Highest Honors!**

---

## 🎯 Objectives

- ✅ Train YOLOv8 models for **RGB**, **thermal**, and **depth** images
- ✅ Evaluate and compare performances across modalities
- ✅ Perform inference and visualize predictions
- ✅ Implement and assess late fusion strategies (e.g., NMS, Voting)
- ✅ Prepare for possible sensor fusion in real-world applications

---

## 🛠️ Model Details

| Modality | Model Used | Input Size | Dataset |
|----------|------------|------------|------------|
| RGB      | YOLOv8s    | 640×512    | [MID-3K RGB subset](./MID-3K/dataset/rgb/whole-dataset/rgb) |
| Thermal  | YOLOv8s    | 640×512    | [MID-3K Thermal subset](./MID-3K/dataset/thermalwhole-dataset/thermal) |
| Depth  | YOLOv8s    | 640×512    | [MID-3K Depth subset](./MID-3K/dataset/depthwhole-dataset/depth) |

---

## 📁 Project Structure
```
MMHD-project/
|
├── README.md # 📌 This file!
|
├── AAU-VAP-trimodal-dataset/ # 🗂️ Trimodal dataset with aligned RGB, thermal, and depth images
├── MID-3K/ # 🗂️ Base dataset
│ └── dataset/
│   ├── rgb/ # 🌈 RGB images and labels (split & full)
│   ├── thermal/ # 🌡️ Thermal images and labels (split & full)
│   └── depth/ # 🕳️ Depth images and labels (split & full)
|
├── Project/ # 💻 Scripts and project related files
|   ├── RML-2025-report-FelipeTassariAveiro.pdf # 📝 Final report!
|   ├── dataset-separator.py # ✂️ Python script to split dataset
|   ├── RML-project-MMHD.py # 🏋️ Python script to train models
|   ├── label-identifier.py # 🏷️ Python script to organize AAU VAP Trimodal dataset labels
|   ├── Depth.png # 📊 Normalized confusion matrices for depth modality
|   ├── RGB.png # 📊 Normalized confusion matrices for RGB modality
|   ├── Thermal.png # 📊 Normalized confusion matrices for thermal modality
│   └── README-MultimodalISRDataset.md # 📘 README file with description on MID-3K dataset
|
├── RML-project-MMHD/ # 📁 Contains training outputs of each modality
|   ├── rgb/ # 🌈 YOLO training results for RGB modality (metrics, predictions, weights)
|   ├── thermal/ # 🌡️ YOLO training results for thermal modality (metrics, predictions, weights)
|   ├── depth/ # 🕳️ YOLO training results for depth modality (metrics, predictions, weights)
|   ├── test_eval_rgb/ # 🧪 Validation metrics and plots on test set using RGB-trained model
|   ├── test_eval_AAU_rgb/ # 🧪 Validation metrics and plots on test set using RGB-trained model (AAU VAP Trimodal dataset)
|   ├── test_eval_thermal/ # 🧪 Validation metrics and plots on test set using thermal-trained model
|   ├── test_eval_AAU_thermal/ # 🧪 Validation metrics and plots on test set using thermal-trained model (AAU VAP Trimodal dataset)
|   ├── test_eval_depth/ # 🧪 Validation metrics and plots on test set using depth-trained model
|   └── test_eval_AAU_depth/ # 🧪 Validation metrics and plots on test set using depth-trained model (AAU VAP Trimodal dataset)
|
├── predictions # 🧠 Inference results
|  └── late_fusion/ # 🤖 Late fusion inference results
│    ├── comparison/ # 🧩 Predictions comparison between Voting and NMS 
│    ├── eval_summary/ # 📈 Computed metrics 
│    ├── nms/ # 🧮 NMS predictions 
│    └── voting/ # ⚖️ Voting predictions 
|
├── rgb.yaml # ⚙️ Configuration file for training with RGB images
├── thermal.yaml # ⚙️ Configuration file for training with thermal images
├── depth.yaml # ⚙️ Configuration file for training with depth images
|
├── yolo11n.pt # 🤖 Pretrained YOLOv11n model weights
├── yolov8s.pt # 🤖 Pretrained YOLOv8s model weights
|
└── MMHD_project.ipynb # 👨‍💻 Colab notebook
```

---

## 🧪 Setup & Requirements

- ✅ Google Colab environment
- ✅ [Ultralytics YOLOv8](https://docs.ultralytics.com/)
- ✅ Dataset preprocessing and splits handled automatically
- ✅ Custom YAML configurations for each modality
- ✅ Compatible with fusion-based inference
---

## 👨‍💻 Felipe Tassari Aveiro

**_Master's in Mechanical Engineering_**,
_Robotics and Machine Learning (2025)_

🎓🏆 **Approved with Highest Honors**

University of Coimbra

---

## 📎 References

- [**Ultralytics YOLOv8**](https://docs.ultralytics.com/)

- [**MID-3K** (Multimodal ISR Dataset with 3000 images)](https://github.com/kennedyk1/MID-3K)

- [**AAU-VAP Dataset**](https://www.kaggle.com/datasets/aalborguniversity/trimodal-people-segmentation)
