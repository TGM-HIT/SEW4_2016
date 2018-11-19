import threading


class SimpleWorker(threading.Thread):
    """
    Diese Klasse stellt einen Thread dar, welcher
    jedes Zeichen eines Wortes um eine bestimmte Zahl
    im Alphabet verschiebt.
    """

    def __init__(self, event, threadnumber):
        """
        Initialisiert die Basisklasse Thread und
        übernimmt ein event und zahl als Parameter.
        :param event: Das event, auf welches gewartet wird
        :param threadnumber: Die Threadnummer
        """
        threading.Thread.__init__(self)
        self.event = event
        self.threadnumber = threadnumber

    def run(self):
        """
        Wartet auf das Event und verschiebt anschließend
        jedes Zeichen des Wortes.
        :return: None
        """

        # Wort als globale Variable "importieren"
        global word
        # Auf das Event warten (blockiert)
        self.event.wait()
        temp = []

        for i in range(len(word)):
            temp += [chr(ord(word[i]) + self.threadnumber)]

        print('Thread ' + str(self.threadnumber) + ':' + ''.join(temp))


event = threading.Event()
# 10 Instanzen der Thread-Klasse erstellen
threads = []
for i in range(0, 10):
    thread = SimpleWorker(event, i)
    threads += [thread]
    thread.start()

word = input("Wie lautet das Wort?")

# Event auslösen - Threads werden aufgeweckt
event.set()

# Auf die Kind-Threads warten
for x in threads:
    x.join()
