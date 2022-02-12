import logging
from scapy.all import *

class FilterPort:

    def __init__(self, dst_ip, ports):
        self.dst_ip = dst_ip
        self.ports = ports
        self.src_port = RandShort()

    def do_scan(self):
        output=[]
        for dst_port in self.ports:
            stealth_scan_resp = sr1(IP(dst=self.dst_ip) / TCP(sport=self.src_port, dport=dst_port, flags="S"), timeout=2)
            if (str(type(stealth_scan_resp)) == "<class 'NoneType'>"):
                print("Filtered port")
                output.append(str(dst_port) + ":" + "Filtered port")
            elif (stealth_scan_resp.haslayer(TCP)):
                if (stealth_scan_resp.getlayer(TCP).flags == 0x12):
                    send_rst = sr(IP(dst=self.dst_ip) / TCP(sport=self.src_port, dport=dst_port, flags="R"), timeout=2)
                    print(send_rst)
                    output.append(str(dst_port) + ":" + "Open port")
                elif (stealth_scan_resp.getlayer(TCP).flags == 0x14):
                    print("closed port")
                    output.append(str(dst_port) + ":" + "Closed port")
            elif (stealth_scan_resp.haslayer(ICMP)):
                if (int(stealth_scan_resp.getlayer(ICMP).type) == 3
                        and int(stealth_scan_resp.getlayer(ICMP).code) in [ 1, 2, 3, 9, 10, 13]):
                    print("Filterd port")
                    output.append(str(dst_port) + ":" + "Filtered port")
        return output

def main():
    # { "operation": "FilterPort", "target_ip":"192.168.1.22", "ports":[22, 53, 443 , 80], "type":"TCP" }
    ports = FilterPort("192.168.1.22", [1, 2, 22, 80])
    ans = ports.do_scan()
    print(ans)

if __name__=="__main__":
    main()