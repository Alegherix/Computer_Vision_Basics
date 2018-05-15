import numpy as np
import cv2

img = cv2.imread("anka.png")
cv2.imshow("Orginal",img)

#Skapar en tom bild med samma dimensioner som våran ursprungsbild.
mask = np.zeros(img.shape[:2], dtype="uint8")
#Plockar ut center (x,y) värdena
(cX, cY) = (img.shape[1] // 2, img.shape[0] // 2)
#Skapar en vit rektangel på masken, som är helvit och ifylld
cv2.rectangle(mask,(cX-75, cY-75), (cX+75, cY+75), 255, -1)
cv2.imshow("Mask",mask)

#Applicerar masken till bilden med bitwise_and() funktionen.
masked = cv2.bitwise_and(img, img, mask = mask)
cv2.imshow("Mask Applied to Img", masked)

# cv2.waitKey(0)

#Måla upp en cirkel på mask(Svarta canavasen)
cv2.circle(mask, (cX, cY), 100, 255, -1)
#Applicera masken med cv2.bitwise_and() funktionen,
masked = cv2.bitwise_and(img, img, mask = mask)
cv2.imshow("Masked as Circle", masked)

cv2.waitKey(0)