from .DNSScan import DNSScan


class DNSScanHandler():

    def __init__(self, operation, target_ip):
        self.operation = operation
        self.target_ip = target_ip


    def do_scan(self):
        os = DNSScan(self.target_ip)
        return os.do_scan()


def main():

    target_ip = "192.168.1.22"
    ports = DNSScanHandler("OSDetection", target_ip)
    ans = ports.do_scan()
    print("Operative System: %s " % ans)


if __name__=="__main__":
    main()