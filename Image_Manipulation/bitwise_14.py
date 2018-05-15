import numpy as np
import cv2

#Målar upp en vit kvadrat.
canavas = np.zeros((300,300),dtype="uint8")
rectangle = cv2.rectangle(canavas,(25,25), (275,275), 255, -1)
# cv2.imshow("Rec",canavas)

#Målar upp en vit cirkel
c_canavas = np.zeros((300,300),dtype="uint8")
cv2.circle(c_canavas,(150 , 150), 150, 255, -1)
# cv2.imshow("Circle",c_canavas)


bitwiseAND = cv2.bitwise_and(canavas,c_canavas)
cv2.imshow("AND",bitwiseAND)

bitwiseOR = cv2.bitwise_or(canavas,c_canavas)
cv2.imshow("OR",bitwiseOR)

bitwiseXOR = cv2.bitwise_xor(canavas,c_canavas)
cv2.imshow("XOR",bitwiseXOR)

bitwiseNOT = cv2.bitwise_not(canavas,c_canavas)
cv2.imshow("NOT",bitwiseNOT)

cv2.waitKey(0)