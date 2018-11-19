from multiprocessing import Process, Condition
import time
import os


def sayhello(condition, num):
    """
    Schreibt Nachrichten nacheinander in ein File
    und verwendet dabei eine Condition, da mehrere
    Prozesse gleichzeitig darauf zugreifen.
    :param condition: die zu verwendende Condition
    :param num: die Prozessnummer
    :return: None
    """
    with condition:
        # Auf Signal warten
        condition.wait()
        with open("foo.txt", "ab") as fo:
            for i in range(100):
                fo.write("Process ".encode())
                fo.flush()
                fo.write(str(num).encode())
                fo.flush()
                fo.write(": Hello!\n".encode())
                fo.flush()
        condition.notify()


if __name__ == "__main__":
    # File loeschen, falls es bereits existiert
    if os.path.isfile("foo.txt"):
        os.remove("foo.txt")
    condition = Condition()
    # Zehn Prozesse erstellen und starten
    for num in range(10):
        Process(target=sayhello, args=(condition, num)).start()
    time.sleep(1)
    # Den Vorgang "anstossen", da ja alle Prozesse
    # zu Beginn warten
    with condition:
        condition.notify()