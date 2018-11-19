import threading, time, queue


class Producer(threading.Thread):
    """
    Diese Klasse stellt einen Erzeuger dar,
    welcher eine Reihe von Zahlen durch eine
    Queue an den Verbraucher schickt.
    """

    def __init__(self, queue):
        """
        Initialisiert die Basisklasse Thread.
        :param queue: Die Queue, an welche die Zahlen geschickt werden.
        """
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        """
        Erzeugt Reihe an Zahlen und sendet sie an die
        geteilte Queue.
        :return: None
        """
        number = 0
        while True:
            number = number + 1
            self.queue.put(number)
            self.queue.join()


class Consumer(threading.Thread):
    """
    Diese Klasse stellt einen Consumer dar.
    """

    def __init__(self, queue):
        """
        Initialisiert die Basisklasse Thread.
        :param queue: Die geteilte Queue.
        """
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        """
        Gibt alle Zahlen aus, die aus der geteilten Queue
        empfangen werden.
        :return: None
        """

        while True:
            number = self.queue.get()
            print("Consumer empfing Zahl: %d" % number)
            self.queue.task_done()


if __name__ == '__main__':
    queue = queue.Queue()
    t1 = Producer(queue)
    t2 = Consumer(queue)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
