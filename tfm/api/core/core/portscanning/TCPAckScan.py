#! /usr/bin/python3

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

dst_ip = "192.168.1.26"
src_port = RandShort()
dst_port=80

ack_flag_scan_resp = sr1(IP(dst=dst_ip)/TCP(dport=dst_port,flags="A"),timeout=2)
if (str(type(ack_flag_scan_resp)) == "<class 'NoneType'>"):
    print ("Stateful firewall presentn(Filtered)")
elif(ack_flag_scan_resp.haslayer(TCP)):
    if(ack_flag_scan_resp.getlayer(TCP).flags == 0x4):
        print ("No firewalln(Unfiltered)")
elif(ack_flag_scan_resp.haslayer(ICMP)):
    if(int(ack_flag_scan_resp.getlayer(ICMP).type)==3 and int(ack_flag_scan_resp.getlayer(ICMP).code) in [1,2,3,9,10,13]):
        print ("Stateful firewall presentn(Filtered)")