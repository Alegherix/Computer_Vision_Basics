import numpy as np
import cv2

img = cv2.imread("anka.png")
# Konveterar bilden till gråskala.
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

eq = cv2.equalizeHist(img)

cv2.imshow("Histogram Equalization", np.hstack([img,eq]))
cv2.waitKey(0)
cv2.destroyAllWindows()
