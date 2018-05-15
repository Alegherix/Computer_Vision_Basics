import cv2
from matplotlib import pyplot as plt

img = cv2.imread("anka.png")
channels = cv2.split(img)
colors = ("b","g","r")

for channel in channels:
    cv2.imshow("Channel",channel)
    cv2.waitKey(0)