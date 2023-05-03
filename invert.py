from camera import Camera, cv2

def invert(frame):
    return cv2.bitwise_not(frame)

cam = Camera()
cam.video_capture_sync(invert)