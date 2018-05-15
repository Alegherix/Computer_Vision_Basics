import imutils
import numpy as np
import mahotas
import cv2




def load_digits(datasetPath):
    data = np.genfromtxt(datasetPath, delimiter=",", dtype="uint8")
    target = data[:, 0]
    data = data[:, 1:].reshape(data.shape[0], 28, 28)

    return (data, target)

load_digits("train.csv")

def deskew(image, width):
    #Hämtar höjd och bredd av bilden
    (h,w) = image.shape[:2]
    #hämtar information om bilden såsom orientering, center etc
    moments = cv2.moments(image)

    #används för att beräkna ut lutning
    skew = moments["mu11"] / moments["mu02"]

    #Används för att justera bilden så den blir upprätt
    M = np.float32([
        [1, skew, -0.5*w*skew],
        [0,1,0]
    ])

    #Utför själva deskewingen på bilden, med matrixen, bilden ska ha storleken, (w,h) och vi vill använda linear interpolation
    image = cv2.warpAffine(image, M, (w, h),
                           flags=cv2.WARP_INVERSE_MAP | cv2.INTER_LINEAR)

    #resizaer
    image = imutils.resize(image, width=width)

    #Returnerar
    return image

def center_extent(image, size):
    (eW, eH) = size
    
    if image.shape[1] > image.shape[0]:
        image = imutils.resize(image, width=eW)

    else:
        image = imutils.resize(image, height=eH)

    #Skapar en tom canavas med samma storlek som bilden
    extent = np.zeros((eH, eW), dtype="uint8")