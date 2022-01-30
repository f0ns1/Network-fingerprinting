#! /usr/bin/python3

import logging
from scapy.all import *
dst_ip = "192.168.1.26"
src_port = RandShort()
dst_port=23
class TCPConnect:

    dst_ip=""
    ports=[]
    def __init__(self, dst_ip, ports):
        self.dst_ip=dst_ip
        self.ports=ports

    def do_scan(self):
        output=[]
        for i in self.ports:
            dst_port=i
            tcp_connect_scan_resp = sr1(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="S"), timeout=2)
            if(str(type(tcp_connect_scan_resp))=="<type 'NoneType'>"):
                output.append(str(dst_port) + ":" + "Closed")
            elif(tcp_connect_scan_resp.haslayer(TCP)):
                if(tcp_connect_scan_resp.getlayer(TCP).flags == 0x12):
                    ans, unans = sr(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="AR"),timeout=2)
                    output.append(str(dst_port) + ":" + "Open")
                elif (tcp_connect_scan_resp.getlayer(TCP).flags == 0x14):
                    output.append(str(dst_port) + ":" + "Closed")
        return output

def main():
    ports = TCPConnect("192.168.1.26", [1, 2, 22, 80])
    ans = ports.do_scan()
    print(ans)


if __name__=="__main__":
    main()