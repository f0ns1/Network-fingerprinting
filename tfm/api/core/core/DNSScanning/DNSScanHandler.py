from .DNSScan import DNSScan


class DNSScanHandler():

    def __init__(self, operation, target_ip, dns_ip):
        self.operation = operation
        self.target_ip = target_ip
        self.dns_ip = dns_ip


    def do_scan(self):
        os = DNSScan(self.dns_ip, self.target_ip)
        return os.do_scan()


def main():

    target_ip = "marca.com"
    ports = DNSScanHandler("OSDetection", target_ip, "8.8.8.8")
    ans = ports.do_scan()
    print("Operative System: %s " % ans)


if __name__=="__main__":
    main()