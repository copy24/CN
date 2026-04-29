import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('10.181.92.59', 12345))

client_socket.send("Hello from TCP Client".encode())

data = client_socket.recv(1024).decode()
print("Server says:", data)

client_socket.close()