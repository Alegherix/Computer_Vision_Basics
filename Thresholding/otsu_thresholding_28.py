import cv2
import numpy as np
import immutils
import mahotas

#läser in, fixar storlek, gråskalar
img = cv2.imread("coins.jpg")
img = immutils.resize(img, 400)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#applicerar en blur för att bli av med noise
blurred = cv2.GaussianBlur(img, (5,5), 0)
#Visar orginalet
cv2.imshow("First",np.hstack((img,blurred)))

T = mahotas.thresholding.otsu(blurred)
print("Otsus threshold: {}".format(T))
#Kopierar den gråskaliga bilden
thresh = img.copy()
#Sätter pixlar > T = Vitt, Pixlar < T = Svart
thresh[thresh > T] = 255
thresh[thresh < T] = 0
thresh = cv2.bitwise_not(thresh)
cv2.imshow("Otsu",thresh)


T = mahotas.thresholding.rc(blurred)
print("Ridler Calver threshold: {}".format(T))
thresh = img.copy()
thresh[thresh > T] = 255
thresh[thresh < T] = 0
thresh = cv2.bitwise_not(thresh)
cv2.imshow("Riddler Calver", thresh)

cv2.imshow("Masked", cv2.bitwise_and(blurred, blurred, mask=thresh))

cv2.waitKey(0)