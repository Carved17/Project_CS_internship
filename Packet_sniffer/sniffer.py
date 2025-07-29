from scapy.all import sniff, IP, TCP, UDP
from packet_sniffer.db import log_packet

def packet_callback(packet):
    if IP in packet:
        ip_layer = packet[IP]
        proto = packet.proto
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst
        length = len(packet)
        src_port, dst_port, flags = None, None, None

        if TCP in packet:
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
            flags = packet[TCP].flags
        elif UDP in packet:
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport

        log_packet(src_ip, dst_ip, proto, src_port, dst_port, length, str(flags))

def start_sniffing():
    sniff(prn=packet_callback, store=False)
