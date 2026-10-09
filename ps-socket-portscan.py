import socket

machine    = input("Enter the target Name or IP: ")
IPscanned  = socket.gethostbyname(machine)

print("Scanning {} ({}) For Open Ports....".format(machine, IPscanned))

for port in range(12344,12347):  
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((IPscanned, port))  #connect_ex returns an error indicator.
    if result == 0:
        print("Port {}:   Open".format(port))
    else:
        print("Port {}:".format(port))
    s.close()