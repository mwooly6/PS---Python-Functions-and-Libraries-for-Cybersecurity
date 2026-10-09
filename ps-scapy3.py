from scapy.all import *
import sys

send(IP(dst='172.26.135.181')/TCP(dport=80, flags='S')/'TestMessage!results')

#SEND PING TO IP SPECIFIED IN ARGUMENTS
result=sr1(IP(dst=sys.argv[1])/ICMP())
if result:
    result.show()

