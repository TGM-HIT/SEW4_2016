from multiprocessing import Process, Value, Event


class CalculatorProcess(Process):
    """
    Stellt einen simplen Worker-Prozess dar,
    welcher auf ein Event wartet und dann
    die Summe von 1 bis n berechnet. Das Ergebnis
    wird in einen geteilten Speicher gelegt.
    """
    def __init__(self, v, event):
        """
        Initialisiert die Basisklasse Process
        :param v: ein geteilter Wert
        :param event: das Event, auf welches gewartet wird
        """
        Process.__init__(self)
        self.v = v
        self.event = event

    def run(self):
        """
        Wartet auf das Event und legt das Ergebnis
        in den geteilten Speicher
        :return: None
        """
        self.event.wait()
        summe = 0
        for i in range(self.v.value+1):
            summe += i
        self.v.value = summe


if __name__ == "__main__":
    v = Value('i', 0)
    e = Event()
    # Prozess starten
    calculator = CalculatorProcess(v, e)
    calculator.start()
    n = int(input("Bis zu welcher Zahl möchten Sie die Summe von 1 bis n berechnen?"))
    v.value = n
    # Signal geben, sobald Benutzer Eingabe getätigt hat
    e.set()
    calculator.join()
    print("Das ergebnis ist " + str(v.value))
