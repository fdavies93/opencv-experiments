from camera import Camera, cv2

def text_recognition(frame):

    grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to binarize the image
    # i.e take grayscale and make it black and white
    thresh = cv2.threshold(grayscale, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    # look for 3x3 pixel blobs and eliminate them
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

    # Find contours in the image
    contours, hierarchy = cv2.findContours(morph, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        x,y,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)

    return morph

cam = Camera()
cam.video_capture_sync(text_recognition)