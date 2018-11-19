import threading, time


class CounterThread(threading.Thread):
    """
    Diese Klasse stellt einen Thread dar,
    welcher bis zum vorgegebenen Wert
    hinaufzählt.

    :ivar int count_to: Zahl, bis zu welcher hinauf gezählt werden soll
    :ivar int thread_number: Nummer des Threads
    :param int count_to: Zahl, bis zu welcher hinauf gezählt werden soll
    :param int thread_number: Nummer des Threads
    """

    # Klassenvariable für die Anzahl an Threads
    __anzahl = 0
    def __init__(self, thread_number, count_to):
        """
        Initialisiert die Superklasse und speichert
        die Parameter in die Instanzvariablen.
        :param thread_number: Nummer des neuen Threads
        :param count_to: Zahl, bis zu welcher hinauf gezählt werden soll
        """
        threading.Thread.__init__(self)
        self.thread_number = thread_number
        self.count_to = count_to
        CounterThread.__anzahl += 1

    @classmethod
    def get_thread_anzahl(cls):
        """
        Liefert die Gesamtanzahl an Threads zurück.
        :return: Anzahl an erzeugten Threads
        """
        return cls.__anzahl

    def run(self):
        """
        Zählt von 1 bis count_to hinauf und gibt den Zähler aus.
        :return: None
        """
        for i in range(1, self.count_to):
            print('Thread %d: Current count is %d' % (self.thread_number, i))
            #time.sleep(0.01)


# Fünf Threads erstellen und in einer Liste speichern
threads = []
for i in range(1, 6):
    thread = CounterThread(i, 100 * i)
    threads += [thread]
    # Thread gleich starten
    thread.start()

print('Started %d threads!' % CounterThread.get_thread_anzahl())

# Auf die Terminierung aller Threads warten
for x in threads:
    x.join()
