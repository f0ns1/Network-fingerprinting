#!/usr/bin/python3

from scapy.layers.inet import IP
from scapy.sendrecv import sr


class IPScan:
    def __init__(self, target, init, end):
        self.target = target
        self.init= init
        self.end = end

    def scan(self):
        return sr(IP(dst="192.168.1.63", proto=(0, 255)) / "SCAPY", retry=2, timeout=1)

    def response_data(self, ans):
        ans.summary()
        for s,r in ans:
            #print("Send data: ",s.summary())
            print("raw ", r.summary())

def main():
    ip = IPScan("192.168.1.22", 0, 120)
    ans, unans =ip.scan()
    ip.response_data(ans)

if __name__=="__main__":
    main()