#! usr/bin/python3

import socket
import sys

port = int(sys.argv[2])
addr = (sys.argv[1])
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((addr, port))
message = ""
send_msg = input("Enter message: ")
send = send_msg + "\r\n"
sock.sendall(send.encode())

while True:
    data = sock.recv(1024).decode()
    break
    if not data:
        break
    message = message + data
print("server response: " + message)
sock.close()