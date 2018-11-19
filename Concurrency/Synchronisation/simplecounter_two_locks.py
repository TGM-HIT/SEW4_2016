import threading

class Counter(object):
    def __init__(self):
        self.counter = 0
    def inc(self):
        self.counter += 1
        return self.counter


class SimpleCounterThread1(threading.Thread):
    """
    Diese Klasse stellt einen Thread dar, welcher
    zwei globale Zaehler 1000-mal erhoeht.
    """

    def __init__(self, counter1, counter2, lock1, lock2):
        """
        Initialisiert die Basisklasse Thread.
        """
        threading.Thread.__init__(self)
        self.counter1 = counter1
        self.counter2 = counter2
        self.lock1 = lock1
        self.lock2 = lock2

    def run(self):
        """
        Erhoeht counter1 und counter2 1000-mal. run() wird
        aufgerufen, sobald der Thread über start()
        gestartet wird.
        :return: None
        """

        for i in range(1000):
            # Lock1 sperren (falls frei), ansonsten warten, bis sie frei ist
            with self.lock1:
                # --- Beginn kritischer Abschnitt 1 ---
                print("Counter1:" + str(self.counter1.inc()))
                # Lock2 sperren (falls frei), ansonsten warten, bis sie frei ist
                with self.lock2:
                    # --- Beginn kritischer Abschnitt 2 ---
                    print("Counter2:" + str(self.counter2.inc()))
                    # --- Ende kritischer Abschnitt 2 ---

class SimpleCounterThread2(threading.Thread):
    """
    Diese Klasse stellt einen Thread dar, welcher
    zweu globale Zaehler 1000-mal erhoeht. Hier wird
    allerdings zuerst counter2 erhöht!
    """

    def __init__(self, counter1, counter2, lock1, lock2):
        """
        Initialisiert die Basisklasse Thread.
        """
        threading.Thread.__init__(self)
        self.counter1 = counter1
        self.counter2 = counter2
        self.lock1 = lock1
        self.lock2 = lock2

    def run(self):
        """
        Erhoeht counter1 und counter2 1000-mal. run() wird
        aufgerufen, sobald der Thread über start()
        gestartet wird.
        :return: None
        """

        for i in range(1000):
            # Lock2 sperren (falls frei), ansonsten warten, bis sie frei ist
            with self.lock2:
                # --- Beginn kritischer Abschnitt 2 ---
                print("Counter2:" + str(self.counter2.inc()))
                # Lock1 sperren (falls frei), ansonsten warten, bis sie frei ist
                with self.lock1:
                    # --- Beginn kritischer Abschnitt 1 ---
                    print("Counter1:" + str(self.counter1.inc()))
                    # --- Ende kritischer Abschnitt 1 ---


lock1 = threading.Lock()
lock2 = threading.Lock()
counter1 = Counter()
counter2 = Counter()
thread1 = SimpleCounterThread1(counter1, counter2, lock1, lock2)
thread2 = SimpleCounterThread2(counter1, counter2, lock1, lock2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()