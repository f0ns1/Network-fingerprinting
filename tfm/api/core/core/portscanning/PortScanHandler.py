from .tcp.TCPconnect import TCPConnect
from .tcp.TCPAckScan import TCPAckScan
from .tcp.FinScan import FinScan
from .tcp.Filterport import FilterPort
from .tcp.NullScan import NullScan
from .tcp.WindowScan import WindowScan
from .tcp.Xmasport import Xmasport
from .udp.UDPScan import UDPScan

class PortsScanHandler():

    def do_scan(self):
        print(self.type)
        print(self.operation)
        if not self.ports:
            for i in range(65535):
                self.ports.append(i)
        print(self.ports)
        if self.type and self.type=="TCP":
            if self.operation == "TCPConnect":
                ports = TCPConnect(self.target_ip, self.ports)
                return ports.do_scan()
            elif self.operation == "TCPACKScan":
                ports = TCPAckScan(self.target_ip, self.ports)
                return ports.do_scan()
            elif self.operation == "FinScan":
                ports = FinScan(self.target_ip, self.ports)
                return ports.do_scan()
            elif self.operation == "NullScan":
                ports = NullScan(self.target_ip, self.ports)
                return ports.do_scan()
            elif self.operation == "FilterPort":
                ports = FilterPort(self.target_ip, self.ports)
                return ports.do_scan()
            elif self.operation == "WindowScan":
                ports = WindowScan(self.target_ip, self.ports)
                return ports.do_scan()
            elif self.operation == "Xmasport":
                ports = Xmasport(self.target_ip, self.ports)
                return ports.do_scan()
            else:
                return "TCP scan not supported: TCPConnect/FilterPortsScan/FinScan/NullScan/WindowScan/XmasScan"
        elif self.type and self.type == "UDP":
            udp = UDPScan(self.target_ip, self.ports)
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
    ports = [80,443]
    type = "TCP"
    ports = PortsScanHandler(operation, target_ip, ports, type)
    ans = ports.do_scan()
    print("Service answer: %s " % ans)


if __name__=="__main__":
    main()