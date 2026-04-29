import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('10.181.92.59', 12345))
server_socket.listen(1)

print("TCP Server waiting for connection...")

conn, addr = server_socket.accept()
print("Connected to:", addr)

data = conn.recv(1024).decode()
print("Client says:", data)

conn.send("Hello from TCP Server".encode())

conn.close()
server_socket.close()