

https://github.com/Yash1th1/Follow_My_Face_Drone/assets/76571496/d67bd01d-3513-4781-9c43-0de02c0d3f01

# Follow_My_Face_Drone
This repository contains code for a face-tracking drone project using a DJI Tello drone. The project involves using OpenCV for face detection and tracking, and controlling the DJI Tello drone to follow a detected face. The project also includes video recording capabilities and manual control with position tracking.

## Features

- **Face Detection and Tracking**: Uses OpenCV's Haar Cascade Classifier to detect and track faces in real-time.
- **Drone Control**: Utilizes the `djitellopy` library to control the DJI Tello drone.
- **Video Recording**: Records video streams during flight and saves them in AVI and MP4 formats.
- **Keyboard Control**: Allows manual control of the drone using keyboard inputs.
- **Position Tracking**: Tracks and visualizes the drone's position during manual control.

## Requirements

- Python 3.7.6
- OpenCV
- NumPy
- `djitellopy`
- `keyboard` library

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/FollowMyFaceDrone.git
    cd FollowMyFaceDrone
    ```

2. Install the required Python libraries:
    ```sh
    pip install opencv-python-headless numpy djitellopy keyboard
    ```

## Usage

### Face Tracking and Drone Control

1. Connect the DJI Tello drone to your computer's Wi-Fi.
2. Run the face tracking script:
    ```sh
    python face_tracking_drone.py
    ```
3. Use the keyboard to control the drone manually:
    - `LEFT`, `RIGHT`: Move left or right
    - `UP`, `DOWN`: Move forward or backward
    - `w`, `s`: Move up or down
    - `a`, `d`: Rotate left or right
    - `q`: Land the drone
    - `SPACE`: Take off
    - `z`: Start/Pause recording
    - `x`: Stop recording

### Position Tracking

1. Run the position tracking script:
    ```sh
    python position_tracking_drone.py
    ```
2. Use the keyboard to control the drone manually:
    - `LEFT`, `RIGHT`: Move left or right
    - `UP`, `DOWN`: Move forward or backward
    - `w`, `s`: Move up or down
    - `a`, `d`: Rotate left or right
    - `q`: Land the drone
    - `SPACE`: Take off

### Scripts

- `face_tracking_drone.py`: Script for face detection, tracking, and drone control.
- `keyboard_control_drone.py`: Script for manual drone control and video recording.
- `position_tracking_drone.py`: Script for manual drone control with position tracking.

## Project Structure

- `Resources/`: Directory containing resources such as Haar Cascade XML file for face detection.
- `Resources/Videos/`: Directory where recorded videos will be saved.
- `face_tracking_drone.py`: Script for face tracking and drone control.
- `keyboard_control_drone.py`: Script for manual drone control and video recording.
- `position_tracking_drone.py`: Script for manual drone control with position tracking.

## License

This project is licensed under the MIT License.

## Acknowledgements

- [djitellopy](https://github.com/damiafuentes/DJITelloPy): A Python library to interact with the DJI Tello drone.
- [OpenCV](https://opencv.org/): Open Source Computer Vision Library.
- 

https://github.com/Yash1th1/Follow_My_Face_Drone/assets/76571496/fff206ce-e03e-4b39-9cd3-8538ef57054a



https://github.com/Yash1th1/Follow_My_Face_Drone/assets/76571496/f831be14-aad0-406f-8339-dd31bb9337d0


