import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 12346))

print("UDP Server waiting...")

data, addr = server_socket.recvfrom(1024)
print("Client says:", data.decode())

server_socket.sendto("Hello from UDP Server".encode(), addr)

server_socket.close()