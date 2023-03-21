# Virtual_Eye_Mouse

This program uses Mediapipe and OpenCV libraries to detect facial landmarks and control the mouse movements on the screen using PyAutoGUI.

## Prerequisites

-Python 3.x
-OpenCV
-Mediapipe
-PyAutoGUI

## Installations

To install the necessary libraries, use the following commands:

```bash
pip install opencv-python
pip install mediapipe
pip install pyautogui
```

## How to run the program:

1. Clone or download the code from the repository.
2. Open a terminal window and navigate to the folder containing the code.
3. Run the program using the following command:

```bash
py main.py
```

4.The webcam window will appear on the screen, showing the user's face. Move the face closer to the camera for better detection.
5. To control the mouse pointer, close one eye to move the mouse pointer and wink to click on the current mouse position.

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Acknowledgments

This project was inspired by Murtaza's Workshop - Robotics and AI(https://www.youtube.com/channel/UCYUjYU5FveRAscQ8V21w81A) and their tutorial on Virtual Controlled Mouse using Mediapipe and OpenCV.
