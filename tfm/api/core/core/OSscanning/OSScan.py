#!/usr/bin/python3

from scapy.all import *

class OSScan:

    def __init__(self, target):
        self.target = target

    def get_OS(self):
        os = None
        print("get_OS ",self.ttl)
        if self.ttl == str(60):
            os="AIX"
        elif self.ttl == str(64):
            os="Linux|Android|MAC|Red Hat|Juniper|Foundry|FreeBSD|NetGear"
        elif self.ttl == str(128):
            os = "Windows"
        elif self.ttl == str(32):
            os = "Windows old version"
        elif self.ttl == str(255):
            os = "AIX|BSDI|HP-UX|Irix|Linux|NetBSD|Solaris|Stratus|SunOS|Ultrix"
        elif self.ttl == str(254):
            os = "Cisco"
        elif self.ttl == str(200):
            os = "MPE/IX (HP)"
        return os

    def do_scan(self):
        ans = sr1(IP(dst=self.target, proto=(0, 250)), timeout=1)
        if ans and ans.haslayer(IP):
            self.ttl = str(ans.getlayer(IP).ttl)
            print("ttl :", self.ttl)
            return self.get_OS()
        else:
            return "HOST: %s unrechable" % self.target


def main():
    target_ip = "192.168.1.22"
    ports = OSScan(target_ip)
    ans = ports.do_scan()
    print("Operative System: %s " % ans)


if __name__=="__main__":
    main()