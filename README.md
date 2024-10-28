# Aruco Marker-Based Surgical Tool Navigation System

This project implements a real-time surgical tool navigation system using Aruco markers and augmented reality (AR). The system tracks a simulated tool (such as a pen) using a webcam and printed Aruco markers, providing visual feedback to guide the tool towards a target marker.

## Features

- **Real-time tracking** of Aruco markers using a webcam.
- **Distance calculation** between the tool marker and the target marker.
- **AR visual feedback** including arrows and distance display to guide the tool toward the target.

## System Requirements

- Python 3.x
- Webcam (external or built-in)
- Printed Aruco markers (generated using [Aruco Marker Generator](https://chev.me/arucogen/))

## Installation

1. **Clone the repository** or download the source code.
   
2. **Install the required Python libraries** by running the following command in your terminal:

    ```bash
    pip install opencv-python opencv-contrib-python numpy
    ```

3. **Print the Aruco markers**:
   - Go to the [Aruco Marker Generator](https://chev.me/arucogen/) website.
   - Print two Aruco markers:
     - One for the tool (marker ID: 1).
     - One for the target (marker ID: 2).

## Usage

1. **Run the program**:

    ```bash
    python surgical_tool_navigation.py
    ```

2. **Hold the printed Aruco markers** in front of the webcam:
   - The marker with ID 1 represents the tool.
   - The marker with ID 2 represents the target.
   
3. **Follow the AR guidance**:
   - An arrow will appear on the screen pointing from the tool marker to the target marker.
   - The distance between the tool and the target will be displayed.

4. **Press 'q'** to quit the program.

## Code Structure

- **`surgical_tool_navigation.py`**: The main Python file that captures the video feed from the webcam, detects the Aruco markers, calculates the distance between the tool and target markers, and provides AR feedback to guide the tool.

## How It Works

1. The webcam captures video frames in real time.
2. Aruco markers placed on the tool (pen) and target (surface) are detected using the OpenCV library.
3. The system calculates the distance between the tool and target and draws an arrow on the screen to help navigate the tool towards the target.
4. The distance is continuously displayed on the screen to assist the user in reaching the target.

## Demo Video

[Demo Video](#)

## Requirements

- Python 3.x
- OpenCV (cv2)
- Numpy
- Aruco markers for tracking

## Known Issues

- The accuracy of marker detection may vary depending on lighting and camera quality.
- Larger or more clearly printed Aruco markers may improve detection.

## Contributing

Feel free to fork this project and make improvements or optimizations! Pull requests are welcome.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
