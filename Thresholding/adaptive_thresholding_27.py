import numpy as np
import cv2


img = cv2.imread("coins.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(img,(5,5), 0)

#Sätter en adaptive threshold på den blurrade bilden, via bild, metod, threshold typ,
thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 4)
cv2.imshow("Mean thresh", thresh)

thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 15, 3)
cv2.imshow("Gaussian thresh", thresh)

cv2.imshow("Masked", cv2.bitwise_and(blurred, blurred, mask=thresh))

cv2.waitKey(0)
cv2.destroyAllWindows()