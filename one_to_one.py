import socket
import sys

def run_client():
    port = int(sys.argv[2])
    addr = (sys.argv[1])
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((addr, port))
    while True:
        message = ""
        send_msg = input("Enter message: ")
        send = send_msg + "\r\n"
        sock.sendall(send.encode())
        if send == "\r\n":
            break
        
        data = sock.recv(1024).decode()
        if data == "\r\n":
            break
        message = message + data
        print("Server response: " + message)
    sock.close()

def run_server():
    port = int(sys.argv[2])
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.bind(("0.0.0.0", port))
    server_sock.listen(5)
    conn_sock, conn_addr = server_sock.accept()
    while True:
        message = ""
        data = conn_sock.recv(1024).decode()
        if data == "\r\n":
            break
        message = message + data
        print("Client response: " + message)
            
        send_msg = input("Enter message: ")
        send = send_msg + "\r\n"
        conn_sock.sendall(send.encode())
        if send == "\r\n":
            break
    conn_sock.close()

def main():
    if sys.argv[1] == "server":
        run_server()
    else:
        run_client()

main()        