from camera import Camera, cv2

def edges(frame):
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

cam = Camera()
cam.video_capture_sync(edges)