import cv2
import immutils
from Case_Studies import facedetector


fd = facedetector.FaceDectector("haarcascade_frontalface_default.xml")

cam = cv2.VideoCapture(0)

while True:
    #Läser in framen
    read, frame = cam.read()
    #Resizear bilden
    frame = immutils.resize(frame, 400)
    #Skapar en grayscale bild för att vi ska kunna utföra analys bättre
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Säg till att applicera Face Detection och spara returnvärdet i en variabel
    face_rectangles = fd.detect(gray)


    #Måla upp rektangeln på bilden
    for (x, y, w, h) in face_rectangles:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0,255,0), 2)

    #Säger att om jag gör en knaptrycking, och den kanpptryckningen är q, så bryt
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    cv2.imshow("Face",frame)

#Releasar camen
cam.release()
#Avslutar programmet
cv2.destroyAllWindows()