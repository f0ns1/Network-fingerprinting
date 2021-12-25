#!/usr/bin/python3
from scapy.layers.inet import IP, UDP
from scapy.sendrecv import sr


class UDPping:

    def __init__(self, target, ports):
        self.target= target
        self.ports = ports


    def scan_UDP(self):
        return sr(IP(dst="192.168.1.*")/UDP(dport=self.ports))

    def response_data(self, ans):
        for s,r in ans:
            print("Send data ", s.summary())
            print("Response data ".r.summary())


def main():
    udp = UDPping("192.168.1.*.1-10", [0,1,2,3,4,5,6,7,8])
    ans, unans = udp.scan_UDP()
    udp.response_data(ans)
    ans.summary()
    unans.summary()


if __name__ == "__main__":
    main()