import cv2
import numpy as np

frames_per_second = 30

# load our source image
master_image = cv2.imread("datasets/license-plates.jpg")
# x, y, width, height of the 0, 9
coords_0 = (416, 64, 67, 139)
coords_9 = (281,52,72,148)
template_x, template_y, template_w, template_h = coords_9
template_0_x, template_0_y, template_0_w, template_0_h = coords_0

# clip the master image to a smaller subimage
hawaii_0 = master_image[coords_0[1] : coords_0[1] + coords_0[3], coords_0[0] : coords_0[0] + coords_0[2]]
hawaii_9 = master_image[coords_9[1] : coords_9[1] + coords_9[3], coords_9[0] : coords_9[0] + coords_9[2]]

# make the 0 and 9 images black and white (technically, change their color space to greyscale)
hawaii_0_bw = cv2.cvtColor(hawaii_0, cv2.COLOR_BGR2GRAY)
hawaii_9_bw = cv2.cvtColor(hawaii_9, cv2.COLOR_BGR2GRAY)

# TODO: what's the difference between these methods in practice? and even in 'what are they?'
# methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
#             'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']

# use the whole image because we're finding multiple matches
img_copy = master_image.copy()
# take the 2 right-hand columns of the image ONLY (because we used the left for the source)
# img_copy = master_image.copy()[: , template_0_x + template_0_w : ]
# make it black and white
img_copy = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)
# adjust the black and white template for matching
# alpha is relative contrast, beta is absolute brightness
img_copy = cv2.convertScaleAbs(img_copy, alpha=3.5, beta=-150.0)

# get matching spaces for the 0 and the 9 template using the TM_CCOEFF method (whatever this is)
res_0 = cv2.matchTemplate(img_copy, hawaii_0_bw, cv2.TM_CCOEFF)
res_9 = cv2.matchTemplate(img_copy, hawaii_9_bw, cv2.TM_CCOEFF)

# for both templates (0, 9)
for res in [res_0, res_9]:
    # find the location of the best match
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # calculate a cutoff point based on the closest match for any valid matches
    max_thresh = (max_val + 1e-6) * 0.55
    # cut off the matches array based on threshold
    match_locations = np.where(res>=max_thresh)
    
    # draw a square for each match meeting the threshold
    for (x, y) in zip(match_locations[1], match_locations[0]):
        cv2.rectangle(master_image, (x, y), (x + template_w, y + template_h), 255, 2)
    # top_left = max_loc
    # bottom_right = (top_left[0] + template_w, top_left[1] + template_h)

    # # draw a white rectangle on the source image
    # cv2.rectangle(img_copy, top_left, bottom_right, 255, 2)

# make a window called "License Plate"
cv2.namedWindow("License Plate")

while True:
    # show the image in the window
    cv2.imshow("License Plate", master_image)
    k = cv2.waitKey(int(1000 / frames_per_second))
    # if we pressed ESCAPE, exit the program
    if k == 27:
        break