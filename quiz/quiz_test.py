import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("wave.png")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray",gray)

hist = cv2.calcHist([gray],[0],None, [256],[0,256])

plt.plot(hist)
plt.title("GrayScale")
plt.xlabel("Bins")
plt.ylabel("# Pixels")
plt.xlim([0, 256])
plt.show()