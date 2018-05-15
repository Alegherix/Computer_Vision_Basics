import numpy as np
import cv2

img = cv2.imread("anka.png")

blurred = np.hstack([
    img,
    cv2.blur(img, (3,3)),
    cv2.blur(img, (5,5)),
    cv2.blur(img, (7,7))
])
cv2.imshow("Avereged",blurred)
cv2.waitKey(0)