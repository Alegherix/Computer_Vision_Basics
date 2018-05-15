from matplotlib import pyplot as plt
import cv2

img = cv2.imread("anka.png",cv2.COLOR_BGR2GRAY)

hist = cv2.calcHist(img,[0], None, [256], [0, 256])

#Skapar ett graf objekt
plt.figure()
#Lägger till titlar till grafen
plt.title("GrayScale Histogram")
plt.xlabel("Staplar")
plt.ylabel("# pixlar")
#Plottar nu upp higtogramet på grafen
plt.plot(hist)
#Sätter x-Leds begränsningar
plt.xlim([0, 256])
#Väljer nu att faktiskt visa grafen
plt.show()
cv2.waitKey(0)
