import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 5000  # The port used by the server

message = "tiddies"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(message.encode("utf-8", "strict"))
    data = s.recv(1024)

print(f"Received {data!r}")
