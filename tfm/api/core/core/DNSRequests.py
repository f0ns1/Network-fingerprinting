#!/usr/bin/python3
from scapy.layers.dns import DNSQR, DNS
from scapy.layers.inet import IP, UDP
from scapy.sendrecv import sr1
from scapy.volatile import RandShort


class DNSRequest:

    def __init__(self, target, queryname, querytype):
        self.target= target
        self.queryname= queryname
        self.querytype = querytype

    def dnsRequest(self):
        return sr1(IP(dst=self.target)/UDP(sport=RandShort(), dport=53)/DNS(rd=1,qd=DNSQR(qname=self.queryname,qtype=self.querytype)))

    def response_data(self, ans):
        ans.summary()


def main():

    ###DNS Request
    dns = DNSRequest("8.8.8.8", "aula.campusciberseguridad.com", "A")
    ans= dns.dnsRequest()
    print(ans.summary())
    ###SOA Request
    dns = DNSRequest("8.8.8.8", "aula.campusciberseguridad.com", "SOA")
    ans = dns.dnsRequest()
    print(ans.summary())
    print(ans.ns.mname)
    ###MX Request
    dns = DNSRequest("8.8.8.8", "aula.campusciberseguridad.com", "MX")
    ans= dns.dnsRequest()
    print(ans.summary())
    results = [x.exchange for x in ans.an.iterpayloads()]
    print(results)


if __name__ == "__main__":
    main()
