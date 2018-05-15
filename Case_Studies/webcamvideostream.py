from threading import Thread
import cv2

class WebcamVideoStream:
    def __init__(self, src = 0):
        #initalizera video camera strömmen och läsa den första framen från strömmen
        self.stream = cv2.VideoCapture(src)
        (self.grabbed, self.frame) = self.stream.read()

        #initializera variabeln som används för att indikera om tråden ska stoppas.
        self.stopped = False

    def start(self):
    #startar tråden att läsa frames ifrån video strömmen
        Thread(target= self.update, args=()).start()
        return self

    def update(self):
    #Fortsätt loopa tills tråden stannas
        while True:
            #If tråd indicator variabeln är satt till true så bryt
            if self.stopped:
                break
            #Annars så läs nästa tråd från strömmen
            (self.grabbed, self.frame) = self.stream.read()

    def read(self):
        #Returnera den senast läste framen
        return self.frame

    def stop(self):
        #Indikera att en tråd bör stoppas
        self.stopped = True