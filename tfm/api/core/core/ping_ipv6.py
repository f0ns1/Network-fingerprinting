from scapy.all import *
import argparse

from scapy.layers.inet6 import IPv6, ICMPv6EchoRequest

class IPV6:
    def __init__(self):
        self._SLEEP=0
        self._MULTICAST_DEST="ff02::2"
        self.interface="wlo1"
        self._HOP_LIMIT=1
    def do_scan(self):
        output=[]
        for self._MULTICAST_DEST in ["ff02::1", "ff02::2", "ff02::5", "ff02::a"]:
            resp= sr1(IPv6(dst=self._MULTICAST_DEST, hlim=self._HOP_LIMIT) / IPv6ExtHdrHopByHop(options=RouterAlert()) / ICMPv6MLQuery(), iface=self.interface, timeout=20),time.sleep(self._SLEEP)
            if resp:
                print(resp)
                for r in resp:
                    if r:
                        print(r.show())
                        output.append(r.show())
                    else:
                        print(r)
        return output



ip = IPV6()
ip.do_scan()