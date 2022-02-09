#! /usr/bin/python3
import logging

from scapy.all import *

class FinScan:

    def __init__(self, dst_ip, ports):
        self.dst_ip=dst_ip
        self.ports=ports
        self.src_port = RandShort()

    def do_scan(self):
        output=[]
        for dst_port in self.ports:
            fin_scan_resp = sr1(IP(dst=self.dst_ip) / TCP(sport=self.src_port, dport=dst_port, flags="F"), timeout=2)
            print(str(type(fin_scan_resp)))
            if (str(type(fin_scan_resp)) == "<class 'NoneType'>"):
                print("Open|Filtered")
                output.append(str(dst_port) + ":" + "Open|Filtered")
            elif (fin_scan_resp.haslayer(TCP)):
                if (fin_scan_resp.getlayer(TCP).flags == 0x14):
                    print("Closed")
                    output.append(str(dst_port) + ":" + "Closed")
            elif (fin_scan_resp.haslayer(ICMP)):
                if (int(fin_scan_resp.getlayer(ICMP).type) == 3
                        and int(fin_scan_resp.getlayer(ICMP).code) in [1, 2, 3, 9, 10, 13]):
                    print("Filtered")
                    output.append(str(dst_port) + ":" + "Filtered")

        return output

def main():
    # { "operation": "FinScan", "target_ip":"192.168.1.22", "ports":[22, 53, 443 , 80], "type":"TCP" }
    ports = FinScan("192.168.1.22", [1, 2, 22, 80])
    ans = ports.do_scan()
    print(ans)


if __name__=="__main__":
    main()