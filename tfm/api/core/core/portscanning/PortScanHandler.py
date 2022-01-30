from TCPconnect import TCPConnect
class PortsScanHandler():

    def do_scan(self):
        print(self.type)
        print(self.operation)
        if self.type and self.type=="TCP":
            if self.operation == "TCPConnect":
                ports= TCPConnect(self.target_ip, self.ports)
                return ports.do_scan()
            elif self.operation == "FilterPort":
                return
            elif self.operation == "FinScan":
                return
            elif self.operation == "NullScan":
                return
            elif self.operation == "TCPACKScan":
                return
            elif self.operation == "WindowScan":
                return
            elif self.operation == "XmasScan":
                return
            else:
                return "TCP scan not supported: TCPConnect/FilterPortsScan/FinScan/NullScan/WindowScan/XmasScan"
        elif self.type and self.type == "UDP":
            udp = UDPScann()
            return udp.do_scan()
        else:
            return "Operation Type not supported: TCP/UDP"

    def __init__(self, operation, target_ip, ports, type):
        print("operation: ", operation)
        print("target_ip: ", target_ip)
        print("ports: ", ports)
        print("type ", type)
        self.operation = operation
        self.target_ip = target_ip
        self.ports = ports
        self.type = type


def main():
    operation ="TCPConnect"
    target_ip = "192.168.1.26"
    ports = [1,2,3,4,5,22,23,80,443]
    type = "TCP"
    ports = PortsScanHandler(operation, target_ip, ports, type)
    ans = ports.do_scan()
    print("Service answer: %s " % ans)


if __name__=="__main__":
    main()