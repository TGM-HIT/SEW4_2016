from multiprocessing import Process, Semaphore
import os


def writefile(semaphore, num):
    """
    Schreibt Nachrichten nacheinander in getrennte Files
    und verwendet dabei einen Semaphor, damit nicht zu viele
    Prozesse gleichzeitig das Filesystem belasten.
    :param semaphore: der zu verwendende Semaphor
    :param num: die Prozessnummer
    :return: None
    """
    print("Process "+str(num)+": Waiting for semaphore...")
    with semaphore:
        print("Process "+str(num)+": Acquired semaphore!")
        with open("foo"+str(num)+".txt", "ab") as fo:
            for i in range(500000):
                fo.write("Process ".encode())
                fo.write(str(num).encode())
                fo.write(": Hello!\n".encode())
    print("Process "+str(num)+": Released semaphore!")

if __name__ == "__main__":
    # Files löschen, falls sie bereits existieren
    for num in range(10):
        if os.path.isfile("foo"+str(num)+".txt"):
            os.remove("foo"+str(num)+".txt")
    # Zwei Prozesse dürfen gleichzeitig schreiben
    sem = Semaphore(value=2)
    # Zehn Prozesse erstellen und starten
    for num in range(10):
        Process(target=writefile, args=(sem, num)).start()