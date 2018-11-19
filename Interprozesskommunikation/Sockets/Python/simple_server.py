import socket

class SimpleServer(object):
    """
    Stellt einen simplen Server dar, welcher auf eingehende Verbindungen wartet.
    """
    def __init__(self, port):
        """
        Speichert den Port, auf welchen gehorcht werden soll.
        :param port: Port, auf den der Server horchen wird
        """
        self.port = port

    def bind_and_listen(self):
        # eine TCP Connection (Stream) über host und port erstellen
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serversocket:
            # Binding erstellen und auf localhost am angegebenen Port horchen
            serversocket.bind(('localhost', self.port))
            # Eingehende Verbindungen ab jetzt annehmen (mit maximal 5 pending connections)
            serversocket.listen(5)
            try:
                while True:
                    print("Auf client warten...")
                    # Blockierender Aufruf! Client wird empfangen (Gegenpart: connect() )
                    (clientsocket, address) = serversocket.accept()
                    print("Client verbunden! Warte auf Nachricht...")
                    while True:
                        # Nachricht empfangen
                        data = clientsocket.recv(1024).decode()
                        if not data:
                            # Schließen, falls Verbindung geschlossen wurde
                            clientsocket.close()
                            break
                        print("Client: %s" % data)
                        if data == "exit":
                            # Bei "Exit" Verbindung schließen
                            clientsocket.send("Bye!".encode())
                            clientsocket.close()
                            break
                        else:
                            msg = input("Antwort an Client: ")
                            # Antwort senden
                            clientsocket.send(msg.encode())
            except socket.error as serr:
                print("Socket closed.")

if __name__ == "__main__":
    server = SimpleServer(50000)
    server.bind_and_listen()