from scapy.all import *

#SNIFFING WITH PROCESSING FUNCTION
def process_pkt(packet):
    return f"Packet {packet[0][1].id}: {packet[0][1].src} ==> {packet[0][1].dst}"

sniff(filter="icmp", prn=process_pkt, store=0)