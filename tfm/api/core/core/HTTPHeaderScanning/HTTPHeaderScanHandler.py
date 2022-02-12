from .HTTPHeaderScan import HTTPHeaderScan


class HTTPHeaderScanHandler():

    def __init__(self, operation, target_ip, path, port=None):
        self.operation = operation
        self.target_ip = target_ip
        self.path = path
        self.port=80
        if port:
            self.port= port


    def do_scan(self):
        os = HTTPHeaderScan(self.target_ip, self.path)
        return os.do_scan()


def main():

    target_ip = "192.168.1.22"
    ports = HTTPHeaderScanHandler("OSDetection", target_ip, "/")
    ans = ports.do_scan()
    print("Operative System: %s " % ans)


if __name__=="__main__":
    main()