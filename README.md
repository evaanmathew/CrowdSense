# CrowdSense – Real-Time Crowd Density Estimation on Trains 🚆

**An AI-powered crowd detection and passenger counting system using YOLOv8, Python, and OpenCV.**

CrowdSense is a computer vision-based project designed to estimate passenger counts in crowded environments, particularly Mumbai's suburban railway coaches. It uses a trained YOLO model to detect people from a live camera feed and display real-time counting results.

The project aims to make public transportation smarter by providing insights into passenger occupancy and crowd levels, helping improve commuter awareness, safety, and travel experience.

## 🎯 Project Objectives

- Detect people from live camera feeds using a trained YOLO model.
- Perform real-time passenger detection and counting.
- Display visual detection results with bounding boxes.
- Generate live numerical passenger counts.
- Explore AI-based crowd monitoring for Mumbai's suburban railway network.

## ✨ Features

### 1. Real-Time Crowd Detection (`count_detect.py`)
- Opens the connected camera and captures live video.
- Performs real-time object detection using the trained YOLO model.
- Displays bounding boxes around detected people.
- Shows the passenger count alongside the live detection feed.

### 2. Live Integer Crowd Count (`count_int.py`)
- Processes the live camera feed.
- Calculates the number of detected people.
- Displays the live passenger count as an integer.
- Provides a simplified numerical output for monitoring crowd levels.

### 3. Custom-Trained YOLO Model
- Uses custom-trained model weights (`my_model.pt`).
- Supports real-time inference.
- Uses OpenCV for camera handling and video processing.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| YOLOv8 (Ultralytics) | Object detection |
| OpenCV | Live camera feed and image processing |
| NumPy | Numerical operations |
| Anaconda | Python environment management |
| Visual Studio Code | Development environment |

## 📁 Project Structure

```text
MY_MODEL/
│
├── train2/                 # Training-related files
│
├── my_model.pt             # Trained YOLO model weights
│
├── count_detect.py         # Live detection with visual count
│
├── count_int.py            # Live integer passenger count
│
├── yolo_detect.py          # YOLO detection script
│
├── .gitignore
│
└── README.md
```

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.8 or above
- Anaconda / Anaconda Navigator
- Visual Studio Code (recommended)
- A working webcam or USB camera

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/CrowdSense.git
```

Navigate into the project directory:

```bash
cd YOLO-Object-Detection
```

### Step 2: Create an Anaconda Environment

Open Anaconda Prompt or the VS Code terminal.

Create a new environment:

```bash
conda create -n crowdsense python=3.10 -y
```

Activate the environment:

```bash
conda activate crowdsense
```

### Step 3: Install Dependencies

```bash
pip install ultralytics opencv-python numpy
```

### Step 4: Verify Installation

```bash
python -c "import cv2, numpy; from ultralytics import YOLO; print('All dependencies installed successfully!')"
```

### Step 5: Verify the Model

Ensure that `my_model.pt` is present in the project directory.

## ▶️ Running the Project

Make sure your Anaconda environment is activated and your camera is connected.

### 1. Run Real-Time Detection with Visual Count

```bash
python count_detect.py
```

This opens the camera and displays the live detection feed with bounding boxes and the detected passenger count.

### 2. Run Live Integer Counting

```bash
python count_int.py
```

This runs the live counting implementation and displays the detected passenger count as an integer.

**Note:** Both scripts require access to the trained model weights. If the model path is configured inside the scripts, ensure it points to `my_model.pt`.

To exit the camera window, use the exit key configured in the script (commonly `q`).

## 🧠 How It Works

1. **Video Input:** The camera captures a live video stream.
2. **Frame Processing:** OpenCV reads and processes individual video frames.
3. **Object Detection:** The trained YOLO model identifies people in each frame.
4. **Counting:** The detected objects are counted to obtain the current passenger count.
5. **Output:** The system displays the detection results and live numerical count.

## 🚉 Application in Mumbai Local Trains

Mumbai's suburban railway network handles millions of commuters daily. CrowdSense explores how computer vision and AI can help address challenges associated with overcrowding.

Potential applications include:

- Real-time coach occupancy estimation.
- Identification of less crowded train compartments.
- Improved passenger distribution.
- Supporting smarter railway crowd management.

The broader CrowdSense vision also includes edge-based processing, commuter assistance, route planning, train schedules, and multilingual interaction.

## 🔮 Future Scope

- Integrating the detection model with existing railway CCTV infrastructure.
- Deploying the model on edge devices for local inference.
- Improving counting accuracy in highly congested environments.
- Integrating coach-wise crowd information into a commuter-facing mobile application.
- Developing crowd-level prediction and analytics.

## 👥 Project Team

**CrowdSense – Real-Time Crowd Density Estimation on Trains**

Bachelor of Engineering – Computer Engineering

Fr. Conceicao Rodrigues Institute of Technology (FCRIT), Vashi

- Aleph Lakra
- Evan Mathew
- Sahil Sampat Salunke

**Project Supervisor:** Mrs. Prachi Verma

## 📜 License

This project was developed for academic and educational purposes as part of the Bachelor of Engineering curriculum.

---

**CrowdSense – Making Every Journey Smarter.** 🚆
