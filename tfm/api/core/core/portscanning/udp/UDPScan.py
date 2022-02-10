#! /usr/bin/python3
import json
from json2html import *
from scapy.all import *

class UDPScan:

    def __init__(self, dst_ip, ports):
        self.dst_ip=dst_ip
        self.ports=ports
        self.src_port = RandShort()

    def do_scan(self):
        output=[]
        for dst_port in self.ports:
            udp_scan_resp, err = sr(IP(dst=self.dst_ip) / UDP(sport=self.src_port, dport=dst_port), timeout=0)
            print(" port: %s resp: %s , %s " % (str(dst_port), str(type(udp_scan_resp)), str(udp_scan_resp)))
            if err:
                #print(err)
                retrans = []
                for count in range(0, 3):
                    retrans.append(sr1(IP(dst=self.dst_ip) / UDP(sport=self.src_port, dport=dst_port), timeout=0))
                    for item in retrans:
                        if (str(type(item)) != "<class 'NoneType'>"):
                            val="Closed"
                            print(val)
                            udp_scan(dst_ip, dst_port, dst_timeout)
                        else:
                            val= "Open|Filtered"
                            print("Open|Filtered")
                            break
                output.append(str(dst_port) + ":" + val)
            elif (udp_scan_resp.haslayer(UDP)):
                #print("Open")
                output.append(str(dst_port) + ":" + "Open")
            elif (udp_scan_resp.haslayer(ICMP)):
                if (int(udp_scan_resp.getlayer(ICMP).type) == 3 and int(udp_scan_resp.getlayer(ICMP).code) == 3):
                    #print("Closed")
                    output.append(str(dst_port) + ":" + "Closed")
            elif (int(udp_scan_resp.getlayer(ICMP).type) == 3 and int(udp_scan_resp.getlayer(ICMP).code) in [1, 2, 9,
                                                                                                             10, 13]):
                #print("Filtered")
                output.append(str(dst_port) + ":" + "Filtered")
        return output

def main():
    # { "operation": "UDPScan", "target_ip":"192.168.1.40", "ports":[ 68, 5353, 42063, 2115, 2222 ], "type":"UDP" }
    ports = UDPScan("192.168.1.22", [1, 2, 22, 80])
    ans = ports.do_scan()
    print(ans)
    jsonString = json.dumps(ans)
    print(jsonString)
    print(json2html.convert(json=jsonString))


if __name__=="__main__":
    main()