from scapy.all import sniff




def packet_callback(packet):
    print(f"📦 Packet: {packet.summary()}")



print("🛜 Starting packet sniffing (Press Ctrl+C to stop)...")
sniff(prn=packet_callback, count=10)