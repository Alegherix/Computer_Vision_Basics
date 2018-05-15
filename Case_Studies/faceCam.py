import cv2
import immutils
from Case_Studies.facedetector import FaceDectector

fd = FaceDectector("haarcascade_frontalface_default.xml")
cam = cv2.VideoCapture(0)

while True:

    boolean, frame = cam.read()
    frame = immutils.resize(frame, 400)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    rectangles = fd.detect(gray)

    for (x, y, w, h) in rectangles:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0,255,0), 2)

    if cv2.waitKey(1) % 0xFF == ord("q"):
        break

    cv2.imshow("Frame",frame)

cam.release()
cv2.destroyAllWindows()