import numpy as np
import cv2
import immutils

image = cv2.imread("anka.png")
cv2.imshow("Orginal",image)

#Hämtar ut höjden, och bredden igenom att slicea arrayen för bildens form, dvs 0-1 - SMART, och casta de till en tupple
(h,w) = image.shape[:2]
#Hämta ut en center i bilden igenom att dela bredden och höjden med 2.
center = (w // 2, h // 2)

#Vi definerar en matrix för att rotera bilden,
M = cv2.getRotationMatrix2D(center,45,1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by 45 Degrees",rotated)


second_rotation = immutils.rotate(image, 78)
cv2.imshow("Second Rotation",second_rotation)


