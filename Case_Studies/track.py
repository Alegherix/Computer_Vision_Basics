import numpy as np
import time
import cv2
import imutils

video = cv2.VideoCapture(0)

#Sätt nedre och övre gränser för color rangen
blue_lower = np.array([40,65,2], dtype="uint8")
blue_upper = np.array([250,215,34], dtype="uint8")

while True:
    (grabbed, frame) = video.read()

    if not grabbed:
        break

    frame = imutils.resize(frame, 400)

    #Hämtar en thresholdad bild
    blue = cv2.inRange(frame, blue_lower, blue_upper)
    #Applicerar Gaussian blur
    blue = cv2.GaussianBlur(blue, (3, 3), 0)

    #Hämtar konturen
    (_, contours, _) = cv2.findContours(blue.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) > 0:
        #Sorterar contours listan, efter storleken på det contourade Areat, och gör den största till först, sedan hämtar vi första elementet.
        cnt = sorted(contours, key = cv2.contourArea, reverse=True)[0]

        #Målar upp en box över den största konturen, sparar boxen som en lista över punkter, i en int32 variabel med hjälp utav numpy.
        rect = np.int32(cv2.boxPoints(cv2.minAreaRect(cnt)))

        #Målar upp konturen för boxen.
        cv2.drawContours(frame, [rect], -1, (0,255,0), 2)

        cv2.imshow("Tracking",frame)
        cv2.imshow("Binary",blue)

        # time.sleep(0.025)


        if cv2.waitKey(1) % 0xFF == ord("q"):
            break

video.release()
cv2.destroyAllWindows()

