import argparse
import cv2

# #Skapar ett argument tolk objekt
# ap = argparse.ArgumentParser()
# #Lägger till argument till objektet
# ap.add_argument("-i","--image",required=True,
#                 help = "path to image")
# #Tolka argumenten för objektet och, returnera objektets dictionary attribut, och spara de i args.
# args = vars(ap.parse_args())
#
# #Läs in bilden ifrån argumentet
# image = cv2.imread(args["image"])

image = cv2.imread("C://Users/Martin/Pictures/anka.png")

#Visa bilden
# cv2.imshow("Original",image)

#Skapar en tuppel, med de 3  rgb värdena som returneras ifrån pixelns x och y position.
(b,g,r) = image[0,0]
print("pixeln vid (0,0) - Red {}, Green - {}, Blue {}".format(r,g,b))

#Här byter vi nu ut pixeln mot en helröd, dvs vi manipulerar pixeln
image[0,0]=(0,0,255)
# Här hämtar vi återigen världen och skriver ut för att få ett nytt svar
(b,g,r) = image[0,0]
print("pixeln vid (0,0) - Red {}, Green - {}, Blue {}".format(r,g,b))

#Höjd -> Bredd : Plockar ut en bit
corner = image[0:100, 0:500]
cv2.imshow("Corner",corner)

#Tar en slice av bilden, och likställer den med rgb färgen blå 
image[0:100,0:100] = (255, 0, 0)
cv2.imshow("Bilden",image)


cv2.waitKey(0)