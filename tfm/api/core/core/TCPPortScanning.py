#!/usr/bin/python3
from  scapy.layers.inet import IP, TCP
from scapy.sendrecv import sr

class TCPPortScanning:

    def __init__(self, target, init, end):
        self.target = target
        self.init= init
        self.end = end

    def scan(self):
        return sr(IP(dst=self.target)/TCP(flags="S", dport=(self.init, self.end)))

    def response_data(self, res):
        print("Summary 1 ", res)
        print(res.summary())
        print("Summary 2 ")
        #res.nsummary( lfilter=lambda s,r: (r.haslayer(TCP) and (r.getlayer(TCP).flags & 2)) )
        for s,r in res:
            if(r.haslayer(TCP) and (r.getlayer(TCP).flags & 2)):
                print("R ",r.summary())
                print("S ",s.summary())


def main():
    portScann= TCPPortScanning("192.168.1.63",1, 55635)
    res, unans=portScann.scan()
    portScann.response_data(res)
    unans.summary()

if __name__=="__main__":
    main()
