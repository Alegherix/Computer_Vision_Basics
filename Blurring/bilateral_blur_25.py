import numpy as np
import cv2

img = cv2.imread("anka.png")

blurred = np.hstack([
    img,
    cv2.bilateralFilter(img, 5, 21, 21),
    cv2.bilateralFilter(img, 7, 31, 31),
    cv2.bilateralFilter(img, 9, 41, 41)])
cv2.imshow("Bilateral",blurred)
cv2.waitKey(0)