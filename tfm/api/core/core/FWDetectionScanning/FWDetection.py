from scapy.all import *

class FWDetection():

    def __init__(self, target_ip):
        self.target_ip = target_ip


    def do_scan(self):

        return "TO BE implemented"


def main():
    # { "operation": "test", "target_ip": "182.168.1.40", "response": "TO BE implemented" }
    target_ip = "192.168.1.22"
    ports = FWDetection("OSDetection", target_ip)
    ans = ports.do_scan()
    print("Operative System: %s " % ans)


if __name__=="__main__":
    main()