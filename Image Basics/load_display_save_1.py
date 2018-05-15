#!/usr/bin/env python3

from __future__ import print_function
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,
                help = "Path to image")
args = vars(ap.parse_args())

#Vi säger här att cv2.ska läsa in en bild ifrån dictionariet, args,
#värdet vi vill ha in är värdet som fås med nyckeln "image"
image = cv2.imread(args["image"])

# image = cv2.imread("anka.png")

#Vi vill här printa ut
print("height: {} pixels".format(image.shape[0]))
print("width: {} pixels".format(image.shape[1]))
print("channels: {}".format(image.shape[2]))

#Vi vill nu visa bilden
cv2.imshow("Image",image)
#Vi säger att den ska vänta tills den får en knapptryckning, alla andra värden är mätta i ms
cv2.waitKey(0)

#Vi callar imwrite funktionen, ger den ett namn, och anger vilken bild de är vi vill ska sparas.
cv2.imwrite("newImage.jpg",image)