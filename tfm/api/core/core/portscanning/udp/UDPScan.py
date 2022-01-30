#! /usr/bin/python3

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

dst_ip = "192.168.1.26"
src_port = RandShort()
dst_port=[]
dst_timeout=0

def udp_scan(dst_ip,dst_port,dst_timeout):
    udp_scan_resp = sr1(IP(dst=dst_ip)/UDP(dport=dst_port),timeout=dst_timeout)
    if (str(type(udp_scan_resp)) == "<class 'NoneType'>"):
        retrans = []
        for count in range(0,3):
            retrans.append(sr1(IP(dst=dst_ip)/UDP(dport=dst_port),timeout=dst_timeout))
            for item in retrans:
                if (str(type(item)) != "<class 'NoneType'>"):
                    udp_scan(dst_ip,dst_port,dst_timeout)
                return "Open|Filtered"
    elif (udp_scan_resp.haslayer(UDP)):
        return "Open"
    elif(udp_scan_resp.haslayer(ICMP)):
        if(int(udp_scan_resp.getlayer(ICMP).type)==3 and int(udp_scan_resp.getlayer(ICMP).code)==3):
            return "Closed"
    elif(int(udp_scan_resp.getlayer(ICMP).type)==3 and int(udp_scan_resp.getlayer(ICMP).code) in [1,2,9,10,13]):
        return "Filtered"

output=[]
for i in range(10):
    port_scan = udp_scan(dst_ip,i,dst_timeout)
    output.append(str(i)+":"+port_scan)
import json
from json2html import *

jsonString = json.dumps(output)
print(jsonString)
print(json2html.convert( json=jsonString ))