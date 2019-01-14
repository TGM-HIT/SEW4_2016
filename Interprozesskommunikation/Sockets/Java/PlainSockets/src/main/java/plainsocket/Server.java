package plainsocket;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;

public class Server {

    ServerSocket serverSocket;

    String message;
    boolean listening = true;

    String host;
    Integer port;

    public Server(String host, Integer port) {
        this.host = host;
        this.port = port;
    }

    public static void main(String[] args) {
        Server cool = new Server("localhost", 12345);
        cool.init();
    }

    public void init() {
        try {
            serverSocket = new ServerSocket(port);
            while (listening) {
                Socket s = serverSocket.accept();
                ClientWorkerThread worker = new ClientWorkerThread(s);

            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

class ClientWorkerThread extends Thread {
    Socket socket;
    BufferedReader in;
    PrintWriter out;
    String message;
    boolean listening = true;

    public ClientWorkerThread(Socket s) {
        this.socket = s;
        try {
            in = new BufferedReader(new InputStreamReader(
                    socket.getInputStream()));
            out = new PrintWriter(socket.getOutputStream(), true);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void run() {
        while (true) {
            try {
                if ((message = in.readLine()) != null && listening) break;
            } catch (IOException e) {
                e.printStackTrace();
            }
            if (message.equals("EXIT")) listening = false;
            System.out.println(message);
        }
    }
}
