import cv2
from cv2 import VideoCapture
from Case_Studies import facedetector
import immutils

#Skapar ett facedetector objekt, och passerar haar cascaden
fd = facedetector.FaceDectector("haarcascade_frontalface_default.xml")

#Säger att video input ska vara ifrån webbcam
cam = cv2.VideoCapture(0)

while True:
    #Hämtar boolean om framen hämtas, samt bilden som hämtades
    grabbed, frame = cam.read()
    #Resizear framen
    frame = immutils.resize(frame, 400)
    #Skapar en grayscale bild
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Vi säger åt facedetect att söka i den gråskaliga bilden efter ansikten, för snabbare processing
    face_rectangles = fd.detect(gray)

    #Vi gör en kopia av framen efter resize, men innan den är grayskalad, för att
    frameClone = frame.copy()

    #Måla upp rektangel
    for (x, y, w, h) in face_rectangles:
        cv2.rectangle(frameClone, (x, y), (x +w, y + h), (0, 255, 0), 2)

    #Visa ansiktet med rektangeln
    cv2.imshow("Face",frameClone)

    #bryter loopen
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()
