from scapy.all import *

class BannerGrabbingScan():

    def __init__(self, target_ip):

        self.target_ip = target_ip


    def do_scan(self):

        return "TO BE implemented"


def main():

    target_ip = "192.168.1.22"
    ports = BannerGrabbingScan("OSDetection", target_ip)
    ans = ports.do_scan()
    print("Operative System: %s " % ans)


if __name__=="__main__":
    main()