import numpy as np
import cv2
import immutils

image = cv2.imread("anka.png")
shifted = immutils.translate(image, 100, 0)
cv2.imshow("shifted image",shifted)
cv2.waitKey(0)