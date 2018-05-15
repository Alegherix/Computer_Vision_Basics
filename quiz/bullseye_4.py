import numpy as np
import cv2

#Skapar tom svart bild
canavas = np.zeros((400,400,3),dtype="uint8")

#Min orginal
y_center = canavas.shape[0] // 2
x_center = canavas.shape[1] // 2

#Bättre med multiple variable assignment,.
(center_x, center_y) = (canavas.shape[1] // 2, canavas.shape[0] // 2)

for i in range(0,225,25):
    cv2.circle(canavas,(x_center,y_center),i,(128,128,0))


cv2.imshow("Bullseye",canavas)
cv2.waitKey(0)