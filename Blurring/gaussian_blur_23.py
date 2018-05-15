import numpy as np
import cv2

img = cv2.imread("anka.png")

blurred = np.hstack([
    img,
    cv2.GaussianBlur(img, (3,3), 0),
    cv2.GaussianBlur(img, (5,5), 0),
    cv2.GaussianBlur(img, (7,7), 0)
])
cv2.imshow("Gaussian Average",blurred)
cv2.waitKey(0)