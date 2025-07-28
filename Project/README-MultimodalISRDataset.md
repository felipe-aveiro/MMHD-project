> ⚠️ **Disclaimer**  
> This repository is **not the original source** of the dataset.  
> All credits for the dataset and the content below go to the original authors from the [Institute of Systems and Robotics (ISR), University of Coimbra](https://www.isr.uc.pt/).  
> The original repository can be found here: [https://github.com/kennedyk1/MID-3K](https://github.com/kennedyk1/MID-3K).  
> This repository is provided **only for academic purposes**, and no modifications to the dataset were made.

# MID-3K (Multimodal ISR Dataset with 3000 images)
## RGB Modality Repository

Main Repository with all info here -> [https://github.com/kennedyk1/MID-3K](https://github.com/kennedyk1/MID-3K)


This dataset, collected by the [ISR (Institute of Systems and Robotics)](https://www.isr.uc.pt/) Team, is a new multi-sensory dataset that was organized, calibrated, curated, and annotated. The sensory data was collected using ROS and a Jackal Clearpath mobile robot, operating in two indoor environments: three floors of the [DEEC](https://www.uc.pt/fctuc/deec/) building and two floors of [DEI](https://www.uc.pt/fctuc/dei/) building at the [University of Coimbra](https://www.uc.pt/), Polo 2, Portugal.

This main repository provides information about the Dataset, which consists of 3,083 scenes, each containing 4 images from different modalities (RGB, thermal, depth, and intensity). The images are organized by modality into separate repositories, with the links listed below:

- [MID-3K RGB Modality](https://github.com/kennedyk1/MID-3K-rgb): Contains RGB images (**This repository**).
- [MID-3K Thermal Modality](https://github.com/kennedyk1/MID-3K-thermal): Contains thermal images.
- [MID-3K Depth Modality](https://github.com/kennedyk1/MID-3K-depth): Contains depth images data captured by LiDAR.
- [MID-3K Intensity Modality](https://github.com/kennedyk1/MID-3K-intensity): Contains intensity images data captured by LiDAR.

You can clone any of these modalities to your local environment using the `git clone` command. Simply open the terminal and follow these steps:

   ```bash
   git clone https://github.com/kennedyk1/MID-3K-rgb
   git clone https://github.com/kennedyk1/MID-3K-thermal
   git clone https://github.com/kennedyk1/MID-3K-depth
   git clone https://github.com/kennedyk1/MID-3K-intensity
   ```
This dataset includes a [metainfo.csv](https://github.com/kennedyk1/MID-3K/raw/main/metainfo.csv) file that provides detailed information about each image, including the collection date and time, department, floor, and the number of thermal and RGB annotations. This file can be useful for splitting the dataset into training, validation, and test sets for CNN training, allowing for organized and efficient dataset management.


<table>
    <tr><td colspan="2" align="center"><b>Camera Info</b></td></tr>
    <tr><td>Model</td><td><em>Ximea MQ013CG-E2</em></td></tr>
    <tr><td>Type</td><td><em>Colour</em></td></tr>
    <tr><td>Resolution</td><td><em>1280x1024 pixels, 1.3 MP</em></td></tr>
    <tr><td colspan="2" align="center"><b>Scene Details</b></td></tr>
    <tr><td>University</td><td><em>University of Coimbra, Polo II Campus</em></td></tr>
    <tr><td>Departments</td><td><em>DEEC and DEI</em></td></tr>
    <tr><td>Type</td><td><em>Indoor Environment</em></td></tr>
    <tr><td colspan="2" align="center"><b>Dataset Details</b></td></tr>
    <tr><td>Modality</td><td><em>RGB/Color</em></td></tr>
    <tr><td>Image Type</td><td><em>.png</em></td></tr>
    <tr><td>Total Images</td><td><em>3,083 images</em></td></tr>
    <tr><td>Total Files Annotations</td><td><em>3,083 txt files</em></td></tr>
    <tr><td>Total Annotations</td><td><em>10,824 peoples</em></td></tr>
    <tr><td>Dataset Size</td><td><em>Approximately 1.3 GB</em></td></tr>
    <tr><td>Images Resolution</td><td><em>640x512 pixels</em></td></tr>
    <tr><td>Annotation Format</td><td><em>YOLO normalized xywh format<BR><b>class x_center y_center width height</b></em></td></tr>
</table>

## Visit the datasets through the links below.
- MID-1K - [Multimodal ISR Dataset with 1100 images](https://kennedyk1.github.io/MID-1K/) (*RGB, thermal and depth*)
- MID-3K - [Multimodal ISR Dataset with 3000 images](https://kennedyk1.github.io/MID-3K/) (*RGB, thermal, depth and intensity*)
