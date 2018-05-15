import numpy as np
import cv2

img = cv2.imread("anka.png")

blurred = np.hstack([
    img,
    cv2.medianBlur(img,(3)),
    cv2.medianBlur(img,(5)),
    cv2.medianBlur(img,(7))
])
cv2.imshow("Median",blurred)
cv2.waitKey(0)