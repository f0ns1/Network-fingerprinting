#!/usr/bin/python3

from Structure.ModulesStructure import Module
from scapy.layers.inet import TCP, IP
from scapy.sendrecv import sr


class ACKScan(Module):
    def __init__(self, destination, ports):
        self.destination = destination
        self.ports = ports

    def do_scan(self):
        return sr(IP(dst=self.destination) / TCP(dport=self.ports, flags="A"), timeout=2)

    def do_response(self, ans):
        for s, r in ans:
            print("Send ACK package: ", s.summary())
            print("Response ACK:  ", r.summary())

    def do_not_response(self, unans):
        for r in unans:
            print("Not response : ", r.summary())





def main():
    ports = []
    target = "192.168.1.63"
    for i in range(65535):
        ports.append(1)
    ack = ACKScan("192.168.1.1", ports)
    ans, unans = ack.do_scan()
    ack.do_response()
    ack.do_not_response(unans)
    print("Not filtered ports: ", len(ans))
    print("Filtered ports : ", len(unans))


if __name__ == "__main__":
    main()
