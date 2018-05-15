import numpy as np
import cv2

img = cv2.imread("anka.png")
cv2.imshow("Orginal",img)

#Vänder bilden vertikalt, dvs i y-led - UppochNed
flipped_y = cv2.flip(img,0)
#VÄnder bilden Horisontalt, dvs i X-led - Spegelvänt
flipped_x = cv2.flip(img,1)

flipped_x_y = cv2.flip(img,-1)

cv2.imshow("UppochNed",flipped_y)
cv2.imshow("Spegel",flipped_x)
cv2.imshow("Spegel och uppochned",flipped_x_y)

cv2.waitKey(0)