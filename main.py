print("✅ main.py is running")

from packet_sniffer.sniffer import start_sniffing
from packet_sniffer.analyser import detect_port_scanning
from packet_sniffer.alert import send_email_alert
import threading
import time

def monitor():
    while True:
        time.sleep(10)
        suspects = detect_port_scanning()
        if suspects:
            for ip in suspects:
                print(f"⚠️ Potential port scanning detected from {ip[0]}")
                send_email_alert("Alert: Port Scan Detected", f"Source IP: {ip[0]}", "receiver@example.com")

if __name__ == "__main__":
    threading.Thread(target=monitor, daemon=True).start()
    start_sniffing()
