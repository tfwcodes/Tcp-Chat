import socket
from colorama import Fore, Back, Style
import colorama
import threading

colorama.init(autoreset=True)

print(
    "\n" + Fore.BLUE + "[!] Enter tcp_chat to start the chat" + "\n" + Fore.BLUE + "[!] Enter exit to exit" + "\n")

command = input(Fore.GREEN + "[+] Enter a command: ")


if command == "tcp_chat":
    host = socket.gethostname()
    print("The host that the client needs to connect is: ", str(host))
    port = 8080
    nickname = input("Enter your nickname: ")
    BuffSize = int(2048)

    def client():
        s = socket.socket()
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        print("Waiting for the client to connect")
        s.listen(1)
        conn, addr = s.accept()
        nickname2 = conn.recv(BuffSize).decode()
        conn.send(nickname.encode())
        print(f"Connection from: {addr} with the username: {nickname2}")
        while 1:
            message = input("Enter a message: ")
            conn.send(message.encode())
            print(f"{nickname2}: {conn.recv(BuffSize).decode()}")

    t = threading.Thread(target=client)
    t.start()

elif command == "exit":
    exit()