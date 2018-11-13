import threading

class EndlosschleifenThread(threading.Thread):
    """
    Diese Klasse stellt einen Thread dar, welcher
    in einer Endlosschleife ausgeführt wird.
    """

    def __init__(self):
        """
        Initialisiert die Basisklasse Thread.
        """
        threading.Thread.__init__(self)

    def run(self):
        """
        Läuft in einer Endlosschleife. run() wird
        aufgerufen, sobald der Thread über start()
        gestartet wird.
        :return: None
        """
        while True:
            pass

# Zwei Instanzen der Thread-Klasse erstellen
t1 = EndlosschleifenThread()
t2 = EndlosschleifenThread()

# Beide Threads starten - ab jetzt laufen sie parallel
# Frage: Wie viele Threads laufen jetzt insgesamt?
t1.start()
t2.start()

# Auf die Terminierung beider Threads warten (endlos)
# BLOCKIERENDER AUFRUF
#t1.join()
t2.join()
