import numpy as np
import cv2

canavas = np.zeros((300,300,3),dtype="uint8")

for i in range(0,300,5):
    cv2.rectangle(canavas,(i,i-5),(i,i+5),(0,0,255),-1)

#måla upp en grön cirkel i mitten
cv2.circle(canavas,(canavas.shape[0]//2,canavas.shape[1]//2),canavas.shape[1]//8,(0,255,0),-1)

cv2.imshow("Bilden",canavas)
cv2.waitKey(0)