import cv2
from matplotlib import pyplot as plt
import numpy as np

#Skapar en metod för att plotta upp ett histogram, för varje enskild kanal i en bild
def plot_histogram(image, title, mask=None):
    channels = cv2.split(image)
    colors = ("b", "g", "r")
    plt.figure()
    plt.title(title)
    plt.xlabel("Behållare")
    plt.ylabel("# Pixlar")

    # Skapar ett histogram för varje enskild kanal i bilden
    for chan, color in zip(channels, colors):
        hist = cv2.calcHist([chan], [0], mask, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])
        plt.ylim([0, 1000])


image = cv2.imread("anka.png")
cv2.imshow("Orginal",image)
plot_histogram(image,"Orginal Histogram")

#Skapar en mask med samma storlek som orginabilden
mask= np.zeros(image.shape[:2], dtype="uint8")

#Skapar en rektangel till masken som är ifylld med vitt.
cv2.rectangle(mask, (50, 50), (250, 250), 255, -1)

#Applicerar masken på bilden med bitwise operation
masked = cv2.bitwise_and(image,image, mask=mask)

cv2.imshow("Masked Img", masked)

#Beräkna histogramet för den maskerade bilden, och anger vilken mask vi vill använda
plot_histogram(image,"Histogram for Masked Image", mask=mask)

#Visar de 2 graferna över histogram vi skapat.
plt.show()




