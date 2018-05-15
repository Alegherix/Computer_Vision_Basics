import cv2
import immutils

class FaceDectector:
    def __init__(self, faceCascadePath):
        self.faceCascade = cv2.CascadeClassifier(faceCascadePath)

    # Returnerar 4 värden som utgör en rektangel
    def detect(self, image, scaleFactor = 1.1, minNeighbors =5, minSize = (30, 30)):
        rectangles = self.faceCascade.detectMultiScale(image, scaleFactor = scaleFactor,
                                                  minNeighbors= minNeighbors, minSize = minSize,
                                                  flags = cv2.CASCADE_SCALE_IMAGE)

        return rectangles



def test_detect():
    fd = FaceDectector("haarcascade_frontalface_default.xml")

    img = cv2.imread("IMG_8247.jpg")
    img = immutils.resize(img, 400)

    face_rectangles = fd.detect(img, scaleFactor=1.5, minNeighbors=5)
    print("I found {} faces".format(len(face_rectangles)))

    for (x, y, w, h) in face_rectangles:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Faces",img)
    cv2.waitKey(0)
