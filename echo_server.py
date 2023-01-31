#! usr/bin/python3

import threading
import time
import socket
import sys

THREADS = 5
def run_server():
    port = int(sys.argv[1])
    server_sock = build_socket(port)

    while True:
        conn_sock, conn_addr = server_sock.accept()
        new_thread = threading.Thread(target=echo, args=(conn_sock,)).start()
    
def build_socket(port):
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.bind(("0.0.0.0", port))
    server_sock.listen(5)
    return server_sock

def echo(conn_sock):
    confirm = "Connection established"
    print(confirm)
    
    while True:
        data = conn_sock.recv(1048)
        if not data:
            break
        conn_sock.sendall(data)
    conn_sock.close()


run_server()