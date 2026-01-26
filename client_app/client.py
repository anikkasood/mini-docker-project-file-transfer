import socket
import sys

SERVER_IP = sys.argv[1]
PORT = int(sys.argv[2])
SAVE_PATH = "/client_storage/mydata.txt"

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, PORT))

with open(SAVE_PATH, 'wb') as f:
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        f.write(data)

client_socket.close()