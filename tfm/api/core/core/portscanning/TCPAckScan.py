#! /usr/bin/python3

import logging
from scapy.all import *


class TCPAckScan:
    dst_ip=""
    ports=[]
    def __init__(self, dst_ip, ports):
        self.dst_ip = dst_ip
        self.ports = ports
        self.src_port = RandShort()

    def do_scan(self):
        output=[]
        for dst_port in self.ports:
            ack_flag_scan_resp = sr1(IP(dst=self.dst_ip) / TCP(dport=dst_port, flags="A"), timeout=2)
            if (str(type(ack_flag_scan_resp)) == "<class 'NoneType'>"):
                print("Stateful firewall presentn(Filtered)")
                output.append(str(dst_port) + ":" + "FW present (Filtered)")
            elif (ack_flag_scan_resp.haslayer(TCP)):
                if (ack_flag_scan_resp.getlayer(TCP).flags == 0x4):
                    print("No firewalln(Unfiltered)")
                    output.append(str(dst_port) + ":" + "No FW (Unfiltered)")
            elif (ack_flag_scan_resp.haslayer(ICMP)):
                if (int(ack_flag_scan_resp.getlayer(ICMP).type) == 3 and int(
                        ack_flag_scan_resp.getlayer(ICMP).code) in [1, 2, 3, 9, 10, 13]):
                    print("Stateful firewall presentn(Filtered)")
                    output.append(str(dst_port) + ":" + "FW present (Filtered)")
        return output

def main():
    # { "operation": "TCPACKScan", "target_ip":"192.168.1.22", "ports":[22, 53, 443 , 80], "type":"TCP" }
    ports = TCPAckScan("192.168.1.22", [1, 2, 22, 80])
    ans = ports.do_scan()
    print(ans)

if __name__=="__main__":
    main()