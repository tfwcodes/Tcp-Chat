import socket
from colorama import Fore, Back, Style
from time import sleep
import colorama
import threading

colorama.init(autoreset=True)

print("\n" + Fore.BLUE + "[!] Enter tcp_chat to start the chat" + "\n" + Fore.BLUE + "[!] Enter exit to exit" + "\n")

command = input(Fore.GREEN + "[+] Enter a command: ")

clients2 = []
nicknames2 = []

clients = []
nicknames = []

if command == "tcp_chat":
    host = socket.gethostname()
    print("The host that the client needs to connect is: ", str(host))
    port = 8080
    nickname = input("Enter your nickname: ")
    if nickname == "admin":
        passw = str("admin1234")
        password = input("Enter the password for the admin: ")
        if password == passw:
            BuffSize2 = int(2048)
            def client():
                port2 = int(8080)
                s2 = socket.socket()
                s2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                s2.bind((host, port2))
                print("Waiting for the client to connect")
                s2.listen(1)
                conn, addr = s2.accept()

                clients2.append(addr)

                nickname2 = conn.recv(BuffSize2).decode()
                nicknames2.append(nickname2)
                   
                conn.send(nickname.encode())
                print(f"Connection from: {addr} with the username: {nickname2}")
                while 1:
                    if nickname2 in nicknames2:
                        message = str(input("Enter a message: "))
                        if message == "?kick " + nickname2:
                            conn.send(message.encode())
                            print(f"{nickname2} was kicked")
                            conn.close()
                        else:
                            conn.send(message.encode())
                            print(f"{nickname2}: {conn.recv(BuffSize2).decode()}")
                            
                    else:
                        print("The username which you are chating with does not exist")

            t2 = threading.Thread(target=client)
            t2.start()

        else:
            print("Wrong password")
            sleep(1)
            exit()
    else:
        BuffSize = int(2048)



        def client():
            s = socket.socket()
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((host, port))
            print("Waiting for the client to connect")
            s.listen(1)
            conn, addr = s.accept()
            clients.append(addr)

            def brodcast(message):
                for client in clients:
                    conn.send(message)

            nickname2 = conn.recv(BuffSize).decode()
            nicknames.append(nickname2)

            conn.send(nickname.encode())
            print(f"Connection from: {addr} with the username: {nickname2}")
            while 1:
                message = input("Enter a message: ")
                brodcast(message.encode())
                print(f"{nickname2}: {conn.recv(BuffSize).decode()}")





        t = threading.Thread(target=client)
        t.start()

elif command == "exit":
    exit()
