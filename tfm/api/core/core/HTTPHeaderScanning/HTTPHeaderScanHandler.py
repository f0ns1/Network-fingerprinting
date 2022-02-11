from .HTTPHeaderScan import HTTPHeaderScan


class HTTPHeaderScanHandler():

    def __init__(self, operation, target_ip):
        self.operation = operation
        self.target_ip = target_ip


    def do_scan(self):
        os = HTTPHeaderScan(self.target_ip)
        return os.do_scan()


def main():

    target_ip = "192.168.1.22"
    ports = HTTPHeaderScanHandler("OSDetection", target_ip)
    ans = ports.do_scan()
    print("Operative System: %s " % ans)


if __name__=="__main__":
    main()