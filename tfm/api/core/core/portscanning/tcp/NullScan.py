#! /usr/bin/python3

import logging
from scapy.all import *

class NullScan:

    def __init__(self, dst_ip, ports):
        self.dst_ip = dst_ip
        self.ports = ports
        self.src_port = RandShort()

    def do_scan(self):
        output=[]
        for dst_port in self.ports:
            null_scan_resp = sr1(IP(dst=self.dst_ip) / TCP(sport=self.src_port, dport=dst_port, flags=""), timeout=2)
            if (str(type(null_scan_resp)) == "<class 'NoneType'>"):
                print("Open|Filtered")
                output.append(str(dst_port) + ":" + "Open|Filtered")
            elif (null_scan_resp.haslayer(TCP)):
                if (null_scan_resp.getlayer(TCP).flags == 0x14):
                    print("Closed")
                    output.append(str(dst_port) + ":" + "Closed")
            elif (null_scan_resp.haslayer(ICMP)):
                if (int(null_scan_resp.getlayer(ICMP).type) == 3 and int(null_scan_resp.getlayer(ICMP).code) in [1, 2,
                                                                                                                 3, 9,
                                                                                                                 10,
                                                                                                                 13]):
                    print("Filtered")
                    output.append(str(dst_port) + ":" + "Filtered")
        return output

def main():
    # { "operation": "NullScan", "target_ip":"192.168.1.22", "ports":[22, 53, 443 , 80], "type":"TCP" }
    ports = NullScan("192.168.1.22", [1, 2, 22, 80])
    ans = ports.do_scan()
    print(ans)

if __name__=="__main__":
    main()