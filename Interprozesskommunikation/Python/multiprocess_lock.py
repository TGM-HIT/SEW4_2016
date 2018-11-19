from multiprocessing import Process, Lock
import os


def sayhello(lock, num):
    """
    Schreibt Nachrichten nacheinander in ein File
    und verwendet dabei eine Lock, da mehrere
    Prozesse gleichzeitig darauf zugreifen.
    :param lock: die zu verwendende Lock
    :param num: die Prozessnummer
    :return: None
    """
    with open("foo.txt", "ab") as fo:
        for i in range(100):
            with lock:
                fo.write("Process ".encode())
                fo.flush()
                fo.write(str(num).encode())
                fo.flush()
                fo.write(": Hello!\n".encode())
                fo.flush()


if __name__ == "__main__":
    # File loeschen, falls es bereits existiert
    if os.path.isfile("foo.txt"):
        os.remove("foo.txt")
    lock = Lock()
    # Zehn Prozesse erstellen und starten
    for num in range(10):
        print("Starting Process %i" % (num))
        Process(target=sayhello, args=(lock, num)).start()
