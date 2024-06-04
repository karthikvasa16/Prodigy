from scapy.all import sniff, IP, TCP, UDP, Raw

def packet_callback(packet):
    # Check if the packet has an IP layer
    if IP in packet:
        ip_layer = packet[IP]
        protocol = ""
        payload = ""

        # Determine the protocol and get payload if exists
        if TCP in packet:
            protocol = "TCP"
            if Raw in packet:
                payload = packet[Raw].load
        elif UDP in packet:
            protocol = "UDP"
            if Raw in packet:
                payload = packet[Raw].load
        else:
            protocol = packet.proto
        
        # Print packet information
        print(f"Source IP: {ip_layer.src}")
        print(f"Destination IP: {ip_layer.dst}")
        print(f"Protocol: {protocol}")
        if payload:
            print(f"Payload: {payload}")
        print("-" * 50)

# Sniff packets
sniff(prn=packet_callback, store=0)
