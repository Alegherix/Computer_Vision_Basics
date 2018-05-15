import cv2
import numpy as np
import immutils


def auto_canny(image, sigma=0.33):
    #Compute the median of the single channel pixel intensitet.
    v = np.median(image)

    #applicera automatiskt canny edge detection using the computed median
    lower = int(max(0, (1.0-sigma)* v))
    upper = int(min(255, (1.0+sigma)* v))
    edged = cv2.Canny(image,lower,upper)

    return edged


#Test del
def test():
    img = cv2.imread("clonazepam_1mg.png")

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = immutils.resize(img, 400)
    img = cv2.GaussianBlur(img, (5, 5), 0)

    first = cv2.Canny(img, 200, 250)
    second = cv2.Canny(img, 10, 200)
    third = cv2.Canny(img, 240,250)

    #Visa bilderna
    cv2.imshow("Pictures", np.hstack([first,second,third]))
    cv2.waitKey(0)

test()