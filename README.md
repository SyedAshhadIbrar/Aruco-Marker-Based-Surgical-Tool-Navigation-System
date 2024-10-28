
# Aruco Marker-Based Surgical Tool Navigation System

This project simulates a surgical tool navigation system using Aruco markers and OpenCV to track a tool in real-time. The system provides augmented reality (AR) visual feedback, including distance measurements and directional arrows, to guide the tool toward a target marker. The mobile phone camera is used as the webcam via **DroidCam** for capturing the video feed.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Using DroidCam](#using-droidcam)
- [Hardware Setup](#hardware-setup)
- [Code Structure](#code-structure)
- [Project Findings](#project-findings)
- [License](#license)

## Introduction

This project tracks two Aruco markers: one attached to a simulated tool and another placed on a target surface. It uses **DroidCam** to turn a mobile phone into a webcam, allowing the system to track the tool’s movement in real time and provide AR feedback on the screen.

## Features

- Real-time tracking of tool and target Aruco markers using a mobile phone camera via DroidCam.
- AR visual feedback to assist navigation:
  - Distance indicator between tool and target.
  - Directional arrow guiding the tool towards the target.
- Augmented reality (AR) overlay using OpenCV.

## Installation

### Prerequisites

Ensure you have the following installed:
- Python 3.x
- OpenCV with Aruco module
- Numpy
- **DroidCam** (for mobile phone as webcam)


## Usage

1. **Generate Aruco Markers**:
   Generate Aruco markers online at: [Aruco Marker Generator](https://chev.me/arucogen/). Print the generated markers and use one for the tool and one for the target.

2. **Run the Tool Tracking System**:
   Use the `detect_marker.py` script to detect the tool and target markers.

   ```bash
   python detect_marker.py
   ```

3. **Connect via DroidCam**:
   Ensure your phone is connected to the computer as a webcam using **DroidCam**.

## Using DroidCam

1. **Install DroidCam on Your Phone**:
   - Download DroidCam from:
     - [Android Play Store](https://play.google.com/store/apps/details?id=com.dev47apps.droidcam)
     - [iOS App Store](https://apps.apple.com/us/app/droidcam-wireless-webcam/id1510258102)

2. **Install DroidCam Client on Your PC**:
   Download and install the DroidCam Client for your operating system from [DroidCam Official Website](https://www.dev47apps.com/droidcam/windows/).

3. **Start Streaming**:
   - Open the DroidCam app on your phone.
   - Open the DroidCam client on your PC.
   - Select the connection type (Wi-Fi or USB) and enter the IP or connect via USB tethering.
   - Start the stream.

4. **Configure OpenCV to Use DroidCam**:
   DroidCam acts as a webcam, so you can access it using OpenCV:

   ```python
   cap = cv2.VideoCapture(0)  # Use index 1 if 0 doesn't work
   ```

## Hardware Setup

1. **Webcam**: Use your mobile phone as a webcam via DroidCam.
2. **Aruco Markers**: Print two Aruco markers generated online:
   - One to attach to the tool (e.g., a pen).
   - One to place on a target surface.
3. Ensure the phone’s camera has a clear view of both markers for accurate tracking.

## Code Structure

```
├── detect_marker.py      # Main script to detect markers and guide tool
├── requirements.txt      # Required Python dependencies
└── README.md             # Project documentation
```

### Key Files/s:
- `detect_marker.py`: Main script that uses OpenCV to detect Aruco markers and calculate the distance between them.

### Challenges
- **Marker Detection**: Initial challenges with outdated OpenCV functions were solved by using the correct Aruco modules.
- **DroidCam Latency**: Some latency was observed when using DroidCam over Wi-Fi, which was reduced by lowering the video resolution and using a USB connection.

