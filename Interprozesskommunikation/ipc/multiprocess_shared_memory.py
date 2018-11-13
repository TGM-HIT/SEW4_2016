from multiprocessing import Process, Value, Array


class WorkerProcess(Process):
    """
    Stellt einen simplen Worker-Prozess dar,
    welcher einen geteilten Wert speichert und ein
    geteiltes Array verändert.
    """
    def __init__(self, v, arr):
        """
        Initialisiert die Basisklasse Process
        :param v: ein geteilter Wert
        :param arr: ein geteiltes Array
        """
        Process.__init__(self)
        self.v = v
        self.arr = arr

    def run(self):
        """
        Ändert den Wert und das Array
        :return: None
        """
        with self.v.get_lock():
            self.v.value += 2
        with self.arr:
            for i in range(len(self.arr)):
                self.arr[i] = -self.arr[i]


if __name__ == "__main__":
    v = Value('d', 0.0)
    arr = Array('i', range(10))

    workers = []
    for i in range(400):
        w = WorkerProcess(v, arr)
        workers.append(w)
        w.start()

    for w in workers:
        w.join()

    print(v.value)
    print(arr[:])
