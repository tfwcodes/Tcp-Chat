import socket
import threading
from time import sleep

nicknames = []
clients = []



def receiver():
    host = input(str("Enter the host to connect: "))
    host_ip = socket.gethostbyname(host)
    clients.append(host_ip)

    nickname2 = input("Enter the nickname: ")
    port = 8080

    BuffSize = int(2048)
    s = socket.socket()
    s.connect((host, port))
    s.send(nickname2.encode())


    nickname = s.recv(BuffSize).decode()
    nicknames.append(nickname)

    def brodcast(message):
        for client in clients:
            s.send(message)

    print(f"Connection from: {host_ip} with the nickname: {nickname}")
    while 1:
        try:
            x = f"{nickname}: {s.recv(BuffSize).decode()}"
            if x == "admin: ?kick {nickname2}":
                try:
                    print("You were kicked by an admin")
                    sleep(2)
                    s.close()
                    exit()
                except socket.error:
                    print("You were kicked by an admin")
 
            else:
                try:
                    print(x)
                    messsage = input("Enter a message: ")
                    brodcast(messsage   .encode())
                except socket.error:
                    print("You were kicked by an admin")
        except socket.error:
            print("You were kicked by an admin")

t = threading.Thread(target=receiver)
t.start()
