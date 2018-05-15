import numpy as np
import cv2
import immutils

img = cv2.imread("coins.jpg")
img = immutils.resize(img, 400)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(img, (5,5), 0)
cv2.imshow("Orginal",img)
#Vi beräknar gradienten, och sätter output datatypen till 64bitars float.
lap = cv2.Laplacian(img, cv2.CV_64F)
#Konverterar absolutbeloppet för 64bitars floaten, till en 8bitars unsigned integer.
lap = np.uint8(np.absolute(lap))

cv2.imshow("Laplacian",lap)
cv2.waitKey(0)
# cv2.destroyAllWindows()

#Beräknar den gradienta magnituden i X-led
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
#Beäknar den gradienta magnituden i Y-led
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)

#Konverterar det 64bitars osignerade floating point värdet till ett absolut belopp utav ett 8bitars osignerat värde.
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))


sobelCombined = cv2.bitwise_and(sobelX,sobelY)

cv2.imshow("Sobel X", sobelX)
cv2.imshow("SobelY", sobelY)
cv2.imshow("Sobel Combined", sobelCombined)
cv2.waitKey(0)