#!/usr/bin/python3

from ACKScan import ACKScan
from tfm.api.core.ARPping import ARPPing
from XmasScan import XmasScan
from fingerprinting.IPScan import IPScan


def ack_scan():
    target="192.168.1.63"
    ports=[]
    for i in range(65535):
        ports.append(i)
    print("Number of ports : ",len(ports))
    ack = ACKScan(target,ports)
    ans, unans = ack.ack()
    ans.summary()
    #ack.response_ports(ans)
    #ack.not_response(unans)

def arp_ping():
    arp = ARPPing("192.168.1.1/24")
    ans, unans = arp.scan_arp()
    ans.summary()

def xmas_scan():
    xmas = XmasScan("192.168.1.63", [22, 80, 443, 21])
    ans, unans = xmas.scan()
    xmas.response_data(ans)
    xmas.not_response_data(unans)

def ip_scan():
    ip = IPScan("192.168.1.63",0,255)
    ans, unans = ip.scan()
    ip.response_data(ans)

if __name__=="__main__":
    #arp_pin()
    #xmas_scan()
    ip_scan()

