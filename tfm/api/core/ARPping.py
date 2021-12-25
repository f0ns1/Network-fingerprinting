#!/usr/bin/python3
import sys
from scapy.layers.inet import Ether, IP
from scapy.layers.l2 import ARP
from scapy.sendrecv import sr, srp
from .Structure.ModulesStructure import Module


class ARPPing(Module):

    def do_response(self, ans):
        for req, resp in ans:
            print("req ", req)
            print("req ", resp)

    def do_not_response(self,ans):
        pass

    def do_scan(self):
        return srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=self.destination), timeout=5)

    def __init__(self, destination):
        self.destination = destination


def main():
    arp = ARPPing("192.168.1.0/24")
    ans , unans = arp.do_scan()
    ans.summary()


if __name__=="__main__":
    main()


