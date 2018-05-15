import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("wave.png")

channels = cv2.split(img)
colors = ("b","g","r")

#Beräkna histogramet för kanalerna,  [ [1], [2] ] Dvs grönt, rött, ange kanalerna, [0, 1] eftersom de är de enda kanaler som kommer finnas.
#Ingen mask, VIKTIGT - MÅSTE ANGE Bins för både X och Y-led, samt ranges för både X och Y-led
hist = cv2.calcHist([channels[1], channels[2]],[0,1], None, [8, 8], [0, 256, 0, 256])

#figure används om man vill måla en 2DImensionell figur, istället för en vanlig graf.
fig = plt.figure()

ax = fig.add_subplot(132)

p = ax.imshow(hist, interpolation="nearest")
#Sätter titeln för histogrammet
ax.set_title("2D color Histogram for G and R")
#Colorbar visar baren som visar färgerna, vilka som är starka och svaga.
plt.colorbar(p)
#visar grafen när den är klar
plt.show()