import socket

class SimpleClient(object):
    """
    Ein einfacher Client, welcher sich mit einem Server Socket verbindet.
    :ivar port: Port, zu welchen sich der Client verbinden soll
    :ivar host: Host, zu dem sich der Client verbindet
    """
    def __init__(self, port, host):
        """
        Übernimmt Port und Host.
        :param port: Port, zu welchen sich der Client verbinden soll
        :param host: Host, zu dem sich der Client verbindet
        """
        self.port = port
        self.host = host

    def connect_with_server(self):
        """
        Stellt eine Verbindung zum Server unter Verwendung
        des Hosts und Ports her.
        :return: None
        """

        # eine TCP Connection (Stream) über host und port erstellen
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientsocket:
            try:
                # Verbindung herstellen (Gegenpart: accept() )
                clientsocket.connect((self.host, self.port))
                while True:
                    msg = input("Was soll an den Server gesendet werden?")
                    # Nachricht schicken
                    clientsocket.send(msg.encode())
                    # Antwort empfangen
                    data = clientsocket.recv(1024).decode()
                    if not data:
                        # Schließen, falls Verbindung geschlossen wurde
                        clientsocket.close()
                        break
                    print("Server: %s" % data)
                    if data == "Bye!":
                        # Verbindung trennen
                        clientsocket.close()
                        break
            except socket.error as serr:
                print("Socket error: " + serr.strerror)

if __name__ == "__main__":
    client = SimpleClient(50000, 'localhost')
    client.connect_with_server()