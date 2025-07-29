# 🤖 **MMHD-project - Multi-Modality Human Detection**

**MMHD** (Multi-Modality Human Detection) is a research-oriented project developed for the **Robotics and Machine Learning** course at the **University of Coimbra**.  
The goal is to explore and compare the performance of **YOLOv8 models** for **human detection** using **RGB** and **thermal image modalities**, individually and in a fusion-based setup.

---

## 🎯 Objectives

- ✅ Train YOLOv8 models for **RGB** and **thermal** images
- ✅ Evaluate and compare performances across modalities
- ✅ Perform inference and visualize predictions
- ✅ Prepare for possible sensor fusion in real-world applications

---

## 🛠️ Model Details

| Modality | Model Used | Input Size | Dataset |
|----------|------------|------------|------------|
| RGB      | YOLOv8s    | 640×640    | [MID-3K RGB subset](https://github.com/felipe-aveiro/MMHD-project/MID-3K/dataset/rgb) |
| Thermal  | YOLOv8s    | 640×640    | [MID-3K Thermal subset](https://github.com/felipe-aveiro/MMHD-project/dataset/thermal) |

---

## 📁 Project Structure
```
MMHD-project/
├── MID-3K/ # Dataset base
│ └── dataset/
│   ├── rgb/ # RGB images and labels (split & full)
│   ├── thermal/ # Thermal images and labels (split & full)
│   ├── rgb.yaml
│   └── thermal.yaml
|
├── Project/ # Training outputs (weights, metrics)
|   ├── dataset-separator.py # Python script to split dataset
|   ├── RML-project-MMHD.py # Python script to train models
|   ├── MULTIMODALITY-HUMAN-DETECTION.txt # Project pipeline
│   └── README-MultimodalISRDataset.md # README file with description on dataset
|
├── README.md # 📌 This file!
└── *.ipynb # Colab notebook
```

---

## 📌 Notes

- ✅ Developed in Google Colab
- ✅ Uses Ultralytics YOLOv8 library
- ✅ Dataset preprocessing and splits are performed automatically
- ✅ Compatible with custom YAML config and multiple modalities

---

## 👨‍💻 Felipe Tassari Aveiro

**_Master's in Mechanical Engineering_**,
_Robotics and Machine Learning (2025)_

University of Coimbra

---

## 📎 References

- [**Ultralytics YOLOv8**](https://docs.ultralytics.com/)

- [**MID-3K** (Multimodal ISR Dataset with 3000 images)](https://github.com/kennedyk1/MID-3K)
