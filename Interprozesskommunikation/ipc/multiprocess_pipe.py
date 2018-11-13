from multiprocessing import Process, Pipe


class SenderProcess(Process):
    """
    Stellt einen einfachen Sender dar, welcher
    eine Nachricht in eine Pipe stellt.
    """
    def __init__(self, pipe):
        """
        Initialisiert die Basisklasse Process
        :param pipe: die Pipe, in welche geschickt wird
        """
        Process.__init__(self)
        self.pipe = pipe

    def run(self):
        """
        Schickt eine Nachricht in die Pipe
        :return: None
        """
        self.pipe.send((123,"Hallo Pipe!"))


class ReceiverProcess(Process):
    """
    Ein einfacher Empfänger einer Pipe.
    """
    def __init__(self, pipe):
        """
        Initialisiert die Basisklasse Process
        :param pipe: die Pipe, in welche geschickt wird
        """
        Process.__init__(self)
        self.pipe = pipe

    def run(self):
        """
        Empfängt die Nachricht und gibt sie aus.
        :return: None
        """
        print(self.pipe.recv())


if __name__ == "__main__":
    parent_connection, child_connection = Pipe()
    receiver = ReceiverProcess(child_connection)
    receiver.start()
    sender = SenderProcess(parent_connection)
    sender.start()
    receiver.join()
    sender.join()