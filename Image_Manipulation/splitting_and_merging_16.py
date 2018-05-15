import numpy as np
import cv2

img = cv2.imread("anka.png")

#Plockar ut de 3 kanalerna med hjälp utav cv2.split() metoden.
(b, g, r) = cv2.split(img)

#Visa varje enskild kanal
cv2.imshow("Red",r)
cv2.imshow("Green",g)
cv2.imshow("Blue",b)


#Mergea tillbaka bilden
merged = cv2.merge([b, g, r])
cv2.imshow("Merged", merged)

# #Om man ska skapa en bild helt fylld av en enda kanal
zeros = np.zeros(img.shape[0:2],dtype="uint8")
cv2.imshow("Red",cv2.merge([zeros, zeros, r]))
cv2.imshow("Green",cv2.merge([zeros, g, zeros]))
cv2.imshow("Blue",cv2.merge([b, zeros, zeros]))

print(type(zeros))
print(type(r))

cv2.waitKey(0)
cv2.destroyAllWindows()