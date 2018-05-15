import numpy as np
import cv2

#Skapar en tom yta, helt svart. 300*300 pixlar, med 3 kanaler, och sätter datatypen till unsigned integer8 för att få färgvärden från 0-255
canavas = np.zeros((300,300,3),dtype="uint8")

green = (0,255,0)
red = (0,0,255)
blue = (255,0,0)

#Målar up en grön linje som går nedåt till höger.
cv2.line(canavas,(0,0),(300,300),green)
cv2.line(canavas,(150,0),(200,150),red,thickness=3)

#Målar upp en fylld rektangel som har sin ena ände i pixeln (10,10), och den andra i (50,100)
cv2.rectangle(canavas,(10,10),(50,100),blue,-1)

#Plockar ut center av bilden igenom att ta reda på höjden, och längden på bilden och dividera med 2.
y_center = canavas.shape[0] // 2
x_center = canavas.shape[1] // 2


#Målar upp en ifylld cirkel
cv2.circle(canavas,(y_center,x_center),30,blue,-1)

cv2.imshow("Bild",canavas)
cv2.waitKey()