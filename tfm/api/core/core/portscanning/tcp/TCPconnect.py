#! /usr/bin/python3
import logging

from scapy.all import *

class TCPConnect:
    dst_ip=""
    ports=[]
    def __init__(self, dst_ip, ports):
        self.dst_ip=dst_ip
        self.ports=ports
        self.src_port = RandShort()

    def do_scan(self):
        output=[]
        for dst_port in self.ports:
            tcp_connect_scan_resp = sr1(IP(dst=self.dst_ip)/TCP(sport=self.src_port,dport=dst_port,flags="S"), timeout=2)
            print(tcp_connect_scan_resp)
            if((str(type(tcp_connect_scan_resp))=="<type 'NoneType'>") or not tcp_connect_scan_resp):
                output.append(str(dst_port) + ":" + "Closed")
            elif(tcp_connect_scan_resp.haslayer(TCP)):
                if(tcp_connect_scan_resp.getlayer(TCP).flags == 0x12):
                    ans, unans = sr(IP(dst=self.dst_ip)/TCP(sport=self.src_port,dport=dst_port,flags="AR"),timeout=2)
                    output.append(str(dst_port) + ":" + "Open")
                elif (tcp_connect_scan_resp.getlayer(TCP).flags == 0x14):
                    output.append(str(dst_port) + ":" + "Closed")
        return output

def main():
    # { "operation": "TCPConnect", "target_ip":"192.168.1.22", "ports":[22, 53, 443 , 80], "type":"TCP" }
    ports = TCPConnect("192.168.1.22", [1, 2, 22, 80])
    ans = ports.do_scan()
    print(ans)


if __name__=="__main__":
    main()