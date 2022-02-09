#!/usr/bin/python3
from scapy.fields import FieldLenField, PacketLenField
from scapy.layers.dns import DNS, DNSQR
from scapy.packet import Packet
from scapy.supersocket import StreamSocket
import socket


class DNSTCP(Packet):
    name = "DNS over TCP"

    fields_desc = [FieldLenField("len", None, fmt="!H", length_of="dns"),
                   PacketLenField("dns", 0, DNS, length_from=lambda p: p.len)]

    # This method tells Scapy that the next packet must be decoded with DNSTCP
    def guess_payload_class(self, payload):
        return DNSTCP


sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create an TCP socket
sck.connect(("8.8.8.8", 53))  # connect to 8.8.8.8 on 53/TCP

# Create the StreamSocket and gives the class used to decode the answer
ssck = StreamSocket(sck)
ssck.basecls = DNSTCP

# Send the DNS query
ans = ssck.sr1(DNSTCP(dns=DNS(rd=1, qd=DNSQR(qname="www.google.com"))))
print(ans.summary())
print(ans.fields)