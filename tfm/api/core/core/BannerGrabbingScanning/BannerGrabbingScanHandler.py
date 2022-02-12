from .BannerGrabbingScan import BannerGrabbingScan


class BannerGrabbinScanHandler():

    def __init__(self, operation, target_ip,ports):
        self.operation = operation
        self.target_ip = target_ip
        self.ports = ports


    def do_scan(self):
        os = BannerGrabbingScan(self.target_ip, self.ports)
        return os.do_scan()


def main():

    target_ip = "192.168.1.22"
    ports=[22, 443, 80]
    ports = BannerGrabbinScanHandler("OSDetection", target_ip, ports)
    ans = ports.do_scan()
    print("Operative System: %s " % ans)


if __name__=="__main__":
    main()