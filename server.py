import socket
from colorama import Fore, Back, Style
import colorama
import threading

colorama.init(autoreset=True)

class Chat:
    while True:
        rooms = 'room1', 'room2'
        print ("\n" + Fore.BLUE +  "[!] Enter rooms_avaliable to see the rooms that are avaliable" + "\n" + Fore.BLUE +  "[!] Enter join_room to join a room" + "\n")
        command = input(Fore.GREEN + "[+] Enter a command: ")
        
        if command == "rooms_avaliable":
            print(rooms)
        
        if command == "join_room":
            g = input(Fore.GREEN + "[+] Enter the name of the room: ")
            if g not in rooms:
                print("[!] The room does not exist")
            
            else:
                class Server:
                    print(Fore.BLUE + "[!] Room joined")
    
                    s = socket.socket()
    
                    ip = input(Fore.GREEN + "[+] Enter the ip to connect: ")
                    port = 5555
                    s.bind((ip, port))
                    s.listen()
                    print(Fore.BLUE + "[!] Waiting for client")
                    c, add = s.accept()
                    print(Fore.BLUE + "[!] Client added")
    
                    
                    while True:
                        msg = input(Fore.GREEN + "[+] Enter your message: ")
                        c.send(msg.encode())
                        print(c.recv(1024).decode())
            
            