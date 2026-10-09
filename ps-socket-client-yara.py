import yara
import os
import socket

HOST = "127.0.0.1"  # The server's IP address
PORT = 12345        # The server's port


directory = '/pluralsight'
yara_rules = yara.compile(filepath='/pluralsight/yara_rules/test_rule.yar')

for filename in os.listdir(directory):
  matches = yara_rules.match(data=filename)
  if matches:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.send(filename + b": Matched, possibly infected!")
        data = s.recv(2048)
  else:
    print(filename + ": Clean")