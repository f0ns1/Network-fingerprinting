#!/usr/bin/python3

from scapy.layers.inet import IP, ICMP
from scapy.sendrecv import sr


class ICMPPing:

    def __init__(self, target):
        self.target= target

    def scan_ICMP(self):
        return sr(IP(dst=self.target)/ICMP(), timeout=1)

    def response_data(self, ans):
        for s,r in ans:
            print("Request : ",s.summary())
            print("Response : ", r.summary())


def main():
    ip=[]
    for i in range(255):
        ip.append("192.168.1."+str(i))
    icmp = ICMPPing(ip)
    ans, unans= icmp.scan_ICMP()
    icmp.response_data(ans)

if __name__=="__main__":
    main()