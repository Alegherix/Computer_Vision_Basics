import datetime

class FPS:
    # Lagra start tiden, slut tiden, och antalet framed
    # Som vi undersöka mellan start och slutintervalelt
    def __init__(self):
        self._start = None
        self._end = None
        self._num_Frames = 0

    def start(self):
        #Starta timern
        self._start = datetime.datetime.now()
        return self

    def end(self):
        #Sluta timern
        self._end = datetime.datetime.now()

    def update(self):
        #Uppdaterar antalet frames som undersöks under intervallet
        self._num_Frames += 1

    def elapsed(self):
        #Returnera totala antalet sekunder mellan start och slutintervallet
        return (self._end - self._start).total_seconds()

    def fps(self):
        #beräkna upskattnignsvis antal frames per sekund
        return (self._num_Frames / self.elapsed())