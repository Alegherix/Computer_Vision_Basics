import cv2
import imutils
import numpy as np

class EyeTracker:
    def __init__(self, faceCascadePath, eyeCascadePath):
        # Initializerar 2 objekt, av Cascade Classifiers,
        self.faceCascade = cv2.CascadeClassifier(faceCascadePath)
        self.eyeCascade = cv2.CascadeClassifier(eyeCascadePath)

    def track(self, img):
        face_rectangles = self.faceCascade.detectMultiScale(img, scaleFactor=1.1,
                                                  minNeighbors=5, minSize=(30,30),
                                                  flags=cv2.CASCADE_SCALE_IMAGE)
        rects = []

        #Börjar leta efter ögonen
        for (fX, fY, fW, fH) in face_rectangles:
            #vi skapar ett område för ansiktsregionen via rektangeln
            faceROI = img[fY:fY + fH, fX:fX+fW]
            #Appendar rektangel till rects, för senare användning
            # rects.append((fX, fY, fX + fW, fY + fH))

            #Därefter letar vi nu efter ögonen inuti ansiktsregionen, fast med andra parametervärden, för att reducera false positives.
            eye_rectangles = self.eyeCascade.detectMultiScale(faceROI, scaleFactor=1.1, minNeighbors= 10, minSize=(20,20), flags=cv2.CASCADE_SCALE_IMAGE)

            #Vi appendar rektanglarna ifrån eye rektangels, till listan över rektangles.
            for (eX, eY, eW, eH) in eye_rectangles:
                rects.append((fX + eX, fY + eY, fX + eX + eW, fY + eY + eH))

        return rects


ec = EyeTracker("haarcascade_frontalface_default.xml", "haarcascade_eye.xml")
cam = cv2.VideoCapture(0)

while True:
    (grabbed, frame) = cam.read()

    # standard korrigeringar
    frame = imutils.resize(frame, 400)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    #Svart canavas
    canavas = np.zeros(frame.shape[:2], dtype="uint8")

    #Hämtar rektanglarna som returneras utav Cascade Classifiersen i track()
    rectangles = ec.track(gray)

    #Vi börjar loopa över rektanglarna och målar upp dem,
    # for rect in rectangles:
    #     cv2.rectangle(canavas, (rect[0],rect[1]),(rect[2],rect[3]), (np.random.randint(0,256),np.random.randint(0,256),np.random.randint(0,256)), 2)

    #Alternativ
    #Måla upp cirklar som varierar i färg
    for rect in rectangles:
        centerX = (rect[0]+ rect[2]) // (2)
        centerY = (rect[1] + rect[3]) // (2)

        radius = rect[2] - rect[0]
        radius = int(radius / 2)
        print(radius)

        cv2.circle(canavas, (centerX, centerY), radius , (np.random.randint(0,256),np.random.randint(0,256), np.random.randint(0,256)),-1)

    #Visar
    cv2.imshow("Tracking",cv2.bitwise_and(frame,frame, mask=canavas))

    #bryter
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()

