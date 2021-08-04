import socket
import threading

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

    print(f"Connection from: {host_ip} with the nickname: {nickname}")
    while 1:
        print(f"{nickname}: {s.recv(BuffSize).decode()}")
        messsage = input("Enter a message: ")
        s.send(messsage.encode())

t = threading.Thread(target=receiver)
t.start()
