import socket

s= socket.socket()
ip="192.168.101.129"
port = 5555
s.connect((ip ,port))
print("connected! Welcome...")

while True:
    print(s.recv(1024).decode())
    msg = input("your message: ")
    s.send(msg.encode())