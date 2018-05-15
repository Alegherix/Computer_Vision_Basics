import numpy as np
import cv2

def translate(image,x,y):
    M = np.float32([[1,0,x],[0,1,y]])
    shifted = cv2.warpAffine(image,M,(image.shape[1],image.shape[0]))
    return shifted

def rotate(image,angle,center=None,scale=1.0):
    (h,w) = image.shape[:2]

    #Säger att om inget rotationscentrum ges, så är det mitten av bilden.
    if center is None:
        center = (w // 2, h // 2)

    #Skapar en rotationsMatrix
    M = cv2.getRotationMatrix2D(center,angle,scale)
    #Applicerar rotationsmatrixen till bilden
    rotated_image = cv2.warpAffine(image, M, (w, h))
    return rotated_image

def resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    dim = None
    (h,w) = image.shape[:2]
    if height is None and width is None:
       return image

   #Om höjden ej anges, ta nya bredden, delat på den gamla för att få ett förhållande
   #Sedan ta den nya bredden x, och höjden * aspekt ration, och casta sedan till en int
    if height is None:
        ratio = width / float(w)
        dim = (width, int(h*ratio))

    #Annars ta nya höjden, delat med gamla för att få ett förhållande
    #Sätt dimensionerna till - bredden * ration och casta till en Integer för att få ny integer av antal pixlar i x-led, samt det nya höjd värdet
    else:
        ratio = height / float(h)
        dim = (int(w * ratio), height)

    resized = cv2.resize(image, dim, interpolation=inter)

    #returnera den nya resizade bilden
    return resized
