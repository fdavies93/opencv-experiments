from camera import Camera, cv2

def edges(frame):
    return cv2.Canny(frame, 100, 150)

cam = Camera()
cam.video_capture_sync(edges)