import cv2
import numpy as np
import immutils

#Todo Importera bild, konverera, blurra, Hitta Kanter, Hitta konturer, Måla konturer,

img = cv2.imread("coins.jpg")
img = immutils.resize(img, 400)

orginal = img.copy()

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.GaussianBlur(img, (5,5), 0)
img = cv2.Canny(img, 30, 150)


#Måla upp en tom canavas för våran mask
canavas = np.zeros(img.shape[:2], dtype="uint8")

#Hämta konturer
(_, contours, _) = cv2.findContours(img.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#Måla upp den första konturen för cirkeln
cv2.drawContours(canavas, contours, -1 , 255, 2)

for i in range(len(contours)):
#Hämtar pixel värdena för konturen
    ((cX, cY), r) = cv2.minEnclosingCircle(contours[i])

    #Målar upp en cirkel på canavasen(MASKEN) ifyllt, baserat på nuvarande cirkel - vilket skapar masken.
    cv2.circle(canavas, (int(cX),int(cY)), int(r), 255, -1)


cv2.imshow("canavas", canavas)
cv2.imshow("orginal", orginal)

#Applicerar masken med bitwise_and(), då det enda stället som de båda kommer vara aktiverade på är det maskerade området
cv2.imshow("Fixad", cv2.bitwise_and(orginal, orginal, mask = canavas))
cv2.waitKey(0)

#importerar bild, skapar en tom canavas med samma storlek som orginalbilden, målar upp formen som ska utgöra masken på canavasen, sedan en bitwise and på orginalbilden, med canavasen som mask, då det blir det enda stället med alla pixlar aktiverade