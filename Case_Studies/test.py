import cv2
import numpy as np
import imutils

img = cv2.imread("calculator.png")
img = imutils.resize(img, 500)
img = cv2.GaussianBlur(img, (3,3), 0)

lower_thresh = np.array([80,30,0], dtype="uint8")
upper_thresh = np.array([250,125,50], dtype="uint8")

thresholded_image = cv2.inRange(img,lower_thresh, upper_thresh)

canavas = np.zeros(img.shape[:2], dtype="uint8")

cv2.imshow("Test",cv2.bitwise_and(img, img, mask=thresholded_image))

cv2.waitKey(0)