import numpy as np
import argparse
import cv2

#Orginal bild
image = cv2.imread("anka.png")
cv2.imshow("Orginal",image)

#Deklarear en Translation Matrix, M
#Först anger vi X, och antal pixlar, förskjutning, sedan y och förskjutning.
M = np.float32([[1,0,25], [0,1,50]])

#
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))



cv2.imshow("Shifted down and right",shifted)

image = cv2.imread("anka.png")
M = np.float32([[1,0,-50], [0,1,-90]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted up and left",shifted)
cv2.waitKey(0)