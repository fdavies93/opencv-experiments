# OpenCV Experiments

For Python study group.

## Installation

This assumes you have basic tools i.e. Python 3, venv, pip installed.

* Clone this repo to your local machine.
* Setup a virtual environment with `python -m venv venv`.
* Enter the virtual environment with `. ./venv/bin/activate`.
* Install requirements with `pip install -r requirements.txt`.

## Getting Started

`camera.py` includes a basic script for capturing webcam footage.

You can setup a webcam with default settings as follows:

```python
from camera import Camera

cam = Camera()
cam.video_capture_sync()
```

You can pass a function as a callback to `video_capture_sync`:

```python
from camera import Camera, cv2

def invert(frame):
    return cv2.bitwise_not(frame)

cam = Camera()
cam.video_capture_sync(invert)
```