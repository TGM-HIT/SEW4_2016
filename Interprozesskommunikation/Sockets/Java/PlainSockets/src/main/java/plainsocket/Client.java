package plainsocket;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;

public class Client extends Thread {

    Socket socket;
    BufferedReader in;
    PrintWriter out;

    String message;
    boolean listening = true;

    String host;
    Integer port;

    public Client(String host, Integer port) {
        this.host = host;
        this.port = port;
    }

    public static void main(String[] args) {
        Client cool = new Client("localhost", 12345);
        cool.init();
        new Thread(cool).start();
    }

    public void init() {
        try {
            socket = new Socket(host, port);
            in = new BufferedReader(new InputStreamReader(
                    socket.getInputStream()));
            out = new PrintWriter(socket.getOutputStream(), true);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void run() {
        while (listening) {
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
