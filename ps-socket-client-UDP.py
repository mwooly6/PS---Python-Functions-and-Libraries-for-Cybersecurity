import socket

HOST = "127.0.0.1"  # The server's IP address
PORT = 12345        # The server's port

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# No Connect as UDP is connection less
s.sendto(b"ABCDEFG",(HOST,PORT))

data, addr = s.recv(4096)
print(data)