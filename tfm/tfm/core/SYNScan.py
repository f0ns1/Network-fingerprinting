#!/usr/bin/python3
from scapy.all import *
from scapy.layers.inet import IP, TCP
from scapy.sendrecv import sr1
host="192.168.1.67"
localport=9999
destination=80
ports=[22,80,443,636]

for i in (ports):
    destination=i
    packet = IP(dst = host)/TCP( dport = destination, flags = "S")
    response = sr1(packet, timeout = 0.5)
    if("NoneType" in str(type(response))):
        pass
    elif(response.haslayer(TCP) and response.getlayer(TCP).flags == "RA"):
        p = IP(dst=host) / TCP( dport=destination, flags="R")
        ans,unans = sr(p, timeout=2)
        print("answer",ans.summary())
        #print("unanswer:",unans.summary())
        try:
            connection = socket.create_connection(host,destination, timeout=2)
            print(connection)
            servicio = socket.getservbyport(destination)
            print("[OPEN PORT]", destination, " ->", servicio)
        except Exception :
            print(Exception)
