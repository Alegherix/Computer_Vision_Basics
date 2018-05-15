import numpy as np
import cv2
import math

img = cv2.imread("anka.png")
cv2.imshow("Orginal", img)

# inuti cv2.add() metoden så blir värdena cappade till 0-255,
print("Max of 255: {}".format(cv2.add(np.uint8([200]), np.uint8([100]))))
print("Min of 0: {}".format(cv2.subtract(np.uint8([50]), np.uint8([100]))))
print()

#Med vanliga aritmiska operationer så slår det över, eller under, dvs efter 255->0..>
print("wrap around: {}".format(np.uint8([200]) + np.uint8([100])))
print("wrap around: {}".format(np.uint8([50]) - np.uint8([100])))


#Skapar en numPy Array bestående av 1or, med samma storlek som våran bild.
#För att fylla ut arrayen med 100's så multiplicerar vi våran matrix med 100.
#Slutligen adderar vi matrixen till våran bild, därav ökar vi pixelintensiteten på bilden med 100.
M = np.ones(img.shape,dtype="uint8") * 100
added = cv2.add(img,M)
cv2.imshow("Added",added)


#Skapar en numpy Array bestående av 1or, som har samma dimensioner och kanaler som våran bild
# Därefter fyller vi arrayen med 50's igenom att multiplicera in 50
# Slutligen så subtraherar vi hela matrixen ifrån våran bild, så att intensiteten för varje pixel sjunker med 50.
M = np.ones(img.shape, dtype="uint8") * 50
subtracted = cv2.subtract(img,M)
cv2.imshow("Subtraherad",subtracted)
cv2.waitKey(0)