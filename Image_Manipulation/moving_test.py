import numpy as np
import cv2
import immutils

img = cv2.imread("anka.png")

for i in range(360):
    rotated_image = immutils.rotate(img, -i)
    cv2.imshow("Rotating Image", rotated_image)
    cv2.waitKey(1)