#!/usr/bin/python3
from scapy.layers.inet import IP,TCP
from scapy.sendrecv import sr

class TCPping:

    def __init__(self, target, ports):
        self.target = target
        self.ports = ports

    def scan_TCP(self, ip):
        return sr(IP(dst=ip)/TCP(dport=self.ports, flags="S"),timeout=2)

    def response_data(self, ans):
        for s,r in ans :
            #print("Send request : ", s.summary())
            print(r.summary())



def main():
    target="192,168.1.63"
    ports=[80, 443, 22, 21, 55, 90, 125, 132, 21]
    #for i in range(55635):
    #    ports.append(i)
    tcp = TCPping(target, ports)
    ans, unans = tcp.scan_TCP("192.168.1.1")
    tcp.response_data(ans)


if __name__ == "__main__":
    main()