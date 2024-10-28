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

### Installing Dependencies

Clone this repository and install the required Python packages:

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
pip install -r requirements.txt
