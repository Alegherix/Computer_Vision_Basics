from Case_Studies.fps import FPS
from Case_Studies.webcamvideostream import WebcamVideoStream
import cv2
import immutils

#Vi börjar med icke trådad och blockering av I/O när man läser frames från strömmen.
#Detta skapar en baselines
print("Sampling frames from webcam...")
stream = cv2.VideoCapture(0)
#Skapar ett FPS objekt, och callar .start() metoden på den för att starta timern
fps = FPS().start()

#Loopa över frames
while fps._num_Frames <= 500:
    #Hämta framen och resizea den att ha en maxbredd av 400px
    (grabbed, frame) = stream.read()
    frame = immutils.resize(frame, 400)
    cv2.imshow("Frame",frame)
    cv2.waitKey(1)

    fps.update()

#Stanna timern och beräkna FPS
fps.end()
cv2.destroyAllWindows()
print("Tidåtången är: {:.2f}".format(fps.elapsed()))
print("Antalet FPS: {:.2f}".format(fps.fps()))

#Stäng ner strömmen
stream.release()
cv2.destroyAllWindows()


#Starta en trådad ström, tillåt camera sensorn att vakna till, och börja FPS räknaren
threaded_cam = WebcamVideoStream().start()
fps = FPS().start()

#loopar över frames, denna gången med en trådad ström
while fps._num_Frames <=500:

    #Vi läser in framen med objektet read() metod
    frame = threaded_cam.read()
    #Vi resizear precis som vanligt
    frame = immutils.resize(frame, 400)

    cv2.imshow("Frame", frame)
    cv2.waitKey(1)

    #Uppdatera antalet frames
    fps.update()

#Avsluta räknaren
fps.end()
#Stäng ner tråden
threaded_cam.stop()
#Ta ner alla öppna fönster
cv2.destroyAllWindows()
print("Tidsåtgången för Trådad ström är: {:.2f}".format(fps.elapsed()))
print("Antalet FPS {:.2f}".format(fps.fps()))

