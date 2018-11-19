from multiprocessing import Process, Queue


class SenderProcess(Process):
    """
    Stellt einen einfachen Sender dar, welcher
    eine Nachricht in eine Queue stellt.
    """
    def __init__(self, queue):
        """
        Initialisiert die Basisklasse Process
        :param queue: die Queue, in welche geschickt wird
        """
        Process.__init__(self)
        self.queue = queue

    def run(self):
        """
        Schickt eine Nachricht in die Queue
        :return: None
        """
        self.queue.put((123,"Hallo Queue!"))


class ReceiverProcess(Process):
    """
    Ein einfacher Empfänger einer Queue.
    """
    def __init__(self, queue):
        """
        Initialisiert die Basisklasse Process
        :param queue: die Queue, in welche geschickt wird
        """
        Process.__init__(self)
        self.queue = queue

    def run(self):
        """
        Empfängt die Nachricht und gibt sie aus.
        :return: None
        """
        while not self.queue.empty():
            print(self.queue.get())


if __name__ == "__main__":
    q = Queue()
    sender = SenderProcess(q)
    sender.start()
    sender1 = SenderProcess(q)
    sender1.start()
    sender.join()
    sender1.join()
    receiver = ReceiverProcess(q)
    receiver.start()
    receiver.join()
