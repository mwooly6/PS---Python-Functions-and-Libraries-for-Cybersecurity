import socket

HOST = "127.0.0.1"  # Local IP for loopback
PORT = 12345        # The server's port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("[R]Ready")
    while True:
        client, addr = s.accept()
        with client:
            print(f"[S] Incoming Message From: {addr}")
            data = client.recv(4096)
            if data == b"Disconnect":
                print("[E] End of Message From " + str(addr))
                break
            client.sendall(b"We have received your data: " + data)
            print("[*] Message: " + str(data))
    s.close()