import numpy as np
import cv2
import immutils


#Importerar bild och konverterar till gråskala
img = cv2.imread("coins.jpg")
img = immutils.resize(img, 400)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Applicerar en GaussianBlur till bilden
blurred = cv2.GaussianBlur(img, (5, 5), 0)
cv2.imshow("Image", img)
#Utför en Binär thresholding -> alla värden över 245 blir vita, alla under blir svarta
(T, thresh) = cv2.threshold(blurred, 247, 255, cv2.THRESH_BINARY)
cv2.imshow("Threshold Binary", thresh)
#Utför en inverterad binär thresholding på bilden. -> alla värden över 245 kommer bli svarta, och alla under 245 blir vita.
(T, thresh_inv) = cv2.threshold(blurred, 247, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold Binary Inverse",thresh_inv)


cv2.imshow("Coins", cv2.bitwise_and(img,img, mask=thresh_inv))

cv2.waitKey(0)
cv2.destroyAllWindows()