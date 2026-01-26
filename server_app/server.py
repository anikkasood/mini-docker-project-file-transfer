import socket
import sys

PORT = int(sys.argv[1])
FILE_PATH = "/server_storage/mydata.txt"

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', PORT))
server_socket.listen(1)

while True:
    conn, addr = server_socket.accept()
    with open(FILE_PATH, 'rb') as f:
        data = f.read()
        conn.sendall(data)
    conn.close()
    break 