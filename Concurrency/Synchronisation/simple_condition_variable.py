import threading, time


class Producer(threading.Thread):
    """
    Diese Klasse stellt einen Erzeuger dar,
    welcher eine Reihe von Zahlen in eine gemeinsame
    Liste legt.
    """

    def __init__(self, numbers, condition):
        """
        Initialisiert die Basisklasse Thread.
        :param numbers: Geteilte Zahlen-Liste
        :param condition: Geteilte Bedingungsvariable zur Synchronisation
        """
        threading.Thread.__init__(self)
        self.numbers = numbers
        self.condition = condition

    def run(self):
        """
        Erzeugt Reihe an Zahlen und legt sie in die
        geteilte Liste self.numbers. Verwendet die Bedingungsvariable
        self.condition zur Synchronisation.
        :return: None
        """
        number = 0
        while True:
            # Bedingungsvariable sperren
            with self.condition:
                print("Producer sperrt condition")
                number = number + 1
                print("Producer erzeugt zahl %d" % number)
                # Zahl in geteilte Liste legen
                self.numbers.append(number)
                print("Producer gibt condition wieder frei")
                # Schlafende Threads wecken und Bedingungsvariable freigeben
                self.condition.notify()
            time.sleep(2)


class Consumer(threading.Thread):
    """
    Diese Klasse stellt einen Consumer dar.
    """

    def __init__(self, numbers, condition):
        """
        Initialisiert die Basisklasse Thread.
        :param numbers: Geteilte Zahlen-Liste
        :param condition: Geteilte Bedingungsvariable zur Synchronisation
        """
        threading.Thread.__init__(self)
        self.numbers = numbers
        self.condition = condition

    def run(self):
        """
        Gibt alle Zahlen aus, die in der geteilten Liste self.numbers landen.
        Verwendet die Bedingungsvariable self.condition zur Synchronisation.
        :return: None
        """

        while True:
            # Bedingungsvariable sperren
            with self.condition:
                print("Consumer sperrt condition")
                while True:
                    # Prüfen, ob self.integers nicht leer ist
                    # (in einer Schleife, da ja mehrere Zahlen
                    # in der Liste sein können)
                    if self.numbers:
                        print("Consumer empfing Zahl: %d" % self.numbers.pop())
                    else:
                        break
                print("Consumer gibt condition wieder frei")
                # Auf das Signal warten und Bedingungsvariable freigeben
                self.condition.wait()

if __name__ == '__main__':
    numbers = []
    condition = threading.Condition()
    t1 = Producer(numbers, condition)
    t2 = Consumer(numbers, condition)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
