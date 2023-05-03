import cv2, glob

class Camera:
    def __init__(self, fps = 30.0, device = 0):
        self.fps = fps
        self.device = device

    # note that this method, while simple, only works on UNIX
    @classmethod
    def get_devices_unix(cls):
        return [int(camera[len("/dev/video") :]) for camera in glob.glob("/dev/video?")]

    def video_capture_sync(self, callback = None):
        cam = cv2.VideoCapture(self.device)
        cv2.namedWindow("Webcam")
        while True:
            ret, frame = cam.read()
            if not ret:
                break
            final_frame = frame
            if callback is not None:
                final_frame = callback(frame)
            cv2.imshow("Webcam", final_frame)
            k = cv2.waitKey(int(1000 / self.fps))
            # if we pressed ESCAPE
            if k == 27:
                break

        cam.release()
        cv2.destroyAllWindows()