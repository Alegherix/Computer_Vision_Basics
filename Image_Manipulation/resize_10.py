import numpy as np
import cv2
import immutils

img = cv2.imread("anka.png")
cv2.imshow("Orginal",img)


#Skapar ett float som är 150 / bredden på bilden
#Detta ger oss aspekt förhållandet
r = 800.0 / img.shape[1]

#Här skapar vi de nya dimensionerna för bilden igenom att sätta bredden till 150 pixlar, dvs måste vara samma som de vi angav för att ge aspekt förhållandet
#Därefter så måste vi anpassa höjden, y-värdet, Det tar vi igenom att multiplicera höjden med aspekt förhållandet.
#VIKTIGT - GLÖM EJ ATT CASTA TILL INT, får inte ha floating point värden som (x,y) värden.
dim = (800, int(img.shape[0] * r ))


resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized (Width)" , resized)

resized_utils = immutils.resize(img, 350)
cv2.imshow("Resized with utils",resized_utils)

cv2.waitKey(0)
