#! /usr/bin/python3

import logging

from scapy.all import *

class WindowScan:

    def __init__(self, dst_ip, ports):
        self.dst_ip=dst_ip
        self.ports=ports
        self.src_port = RandShort()

    def do_scan(self):
        output=[]
        for dst_port in self.ports:
            window_scan_resp = sr1(IP(dst=self.dst_ip) / TCP(sport=self.src_port, dport=dst_port, flags="A"), timeout=2)
            print(window_scan_resp)
            if (str(type(window_scan_resp)) == "<class 'NoneType'>"):
                print("No response")
                output.append(str(dst_port) + ":" + "No response")
            elif (window_scan_resp.haslayer(TCP)):
                print(window_scan_resp.getlayer(TCP))
                print(window_scan_resp.getlayer(TCP).window)
                if (window_scan_resp.getlayer(TCP).window == 0):
                    print("Closed")
                    output.append(str(dst_port) + ":" + "Closed")
                elif (window_scan_resp.getlayer(TCP).window > 0):
                    print("Open")
                    output.append(str(dst_port) + ":" + "Open")
        return output

def main():
    # { "operation": "WindowScan", "target_ip":"192.168.1.22", "ports":[22, 53, 443 , 80], "type":"TCP" }
    ports = WindowScan("192.168.1.22", [1, 2, 22, 80])
    ans = ports.do_scan()
    print(ans)


if __name__=="__main__":
    main()