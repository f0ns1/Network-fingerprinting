from scapy.all import *

class HTTPHeaderScan():

    def __init__(self,  target_ip):
        self.target_ip = target_ip


    def do_scan(self):

        return "TO BE implemented"


def main():

    target_ip = "192.168.1.22"
    ports = HTTPHeaderScan( target_ip)
    ans = ports.do_scan()
    print("Operative System: %s " % ans)


if __name__=="__main__":
    main()