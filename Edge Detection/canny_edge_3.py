import cv2
import numpy as np
import immutils

img = cv2.imread("coins.jpg")
img = immutils.resize(img, 500)
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img = cv2.GaussianBlur(img, (5,5), 0)
cv2.imshow("Blurred, Gray, Orginal Img",img)

canny = cv2.Canny(img, 40, 150)
cv2.imshow("Canny",canny)

cv2.waitKey(0)