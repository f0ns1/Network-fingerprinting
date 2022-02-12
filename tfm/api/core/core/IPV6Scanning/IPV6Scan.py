from scapy.all import *


class IPV6Scan():

    def __init__(self, dest, timeout):
        self._SLEEP=0
        self._MULTICAST_DEST = dest
        self.interface="wlo1"
        self._HOP_LIMIT=1
        self.timeout=timeout

    def do_scan(self):
        output=[]
        if self._MULTICAST_DEST == "multicast":
            for self._MULTICAST_DEST in ["ff02::1"]:
                resp = sr1(IPv6(dst=self._MULTICAST_DEST, hlim=self._HOP_LIMIT) / IPv6ExtHdrHopByHop(
                    options=RouterAlert()) / ICMPv6MLQuery(), iface=self.interface, timeout=self.timeout), time.sleep(
                    self._SLEEP)
                if resp:
                    print(resp)
                    output.append(str(resp))
        else :
            resp = sr1(IPv6(dst=self._MULTICAST_DEST, hlim=self._HOP_LIMIT) / IPv6ExtHdrHopByHop(
                options=RouterAlert()) / ICMPv6MLQuery(), iface=self.interface, timeout=self.timeout), time.sleep(
                self._SLEEP)
            if resp:
                print(resp)
                output.append(str(resp))

        print("do_scan: output ", output)
        return output


def main():
    #
    # {
    #     "operation": "IPV6",
    #     "target_ip": "multicast",
    #     "timeout": 20
    # }
    target_ip = "192.168.1.22"
    ports = IPV6Scan("OSDetection", target_ip)
    ans = ports.do_scan()
    print("Operative System: %s " % ans)


if __name__=="__main__":
    main()