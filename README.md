# spooof
This is a ARP Spoofing simple tool built by @namikaze88

# How ARP Spoofing Works
ARP entries can easily be manipulated using falsified data packets. These cases are referred to using the term ARP spoofing, a man-in-the-middle attack that enables hackers to switch unnoticed between two communicating systems.

# ARP spoofing attacks typically follow a similar progression. The steps to an ARP spoofing attack usually include:
The attacker opens an ARP spoofing tool and sets the tool’s IP address to match the IP subnet of a target. Examples of popular ARP spoofing software include Arpspoof, Cain & Abel, Arpoison and Ettercap. The attacker uses the ARP spoofing tool to scan for the IP and MAC addresses of hosts in the target’s subnet. The attacker chooses its target and begins sending ARP packets across the LAN that contain the attacker’s MAC address and the target’s IP address. As other hosts on the LAN cache the spoofed ARP packets, data that those hosts send to the victim will go to the attacker instead. From here, the attacker can steal data or launch a more sophisticated follow-up attack.


To send the response packets into the network, First you have to enable port forwarding feature in your kali machine.
To enable:
```
echo 1 > /proc/sys/net/ipv4/ip_forward
```
# Process of use:

First find the target Ip Address into the network by using a network scanner. You dont need to find the mac address, my code's get mac function will find the mac address of target and gateway devices. After that find your gateway ip address by using `route -n`.
Then follow the procedure:

```
git clone https://github.com/namikaze88/spooof
```
```
pip install scapy
```
```
sudo python3 spooof.py
```
```
Enter Target IP Address:
Enter Gateway IP Address:
```
This code has the feature to resent the routing table for actual format. Just Press Ctrl+C, the program will terminate and the routing table will be reset.
