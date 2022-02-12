from scapy.all import *
from ..portscanning.PortScanHandler import PortsScanHandler

class FWDetection():

    def __init__(self, target_ip, ports):
        self.target_ip = target_ip
        self.ports = ports

    def do_scan(self):
        output = []
        scan = PortsScanHandler("FilterPort",self.target_ip, self.ports, "TCP")
        output.append(scan.do_scan())
        print("output: ", output)
        for data in output:
            if "Filtered" in str(data):
                fw_detected = "FW detected : "
                break
            else:
                fw_detected = "FW not detected :"
        response = [fw_detected, output]
        print(response)
        return response


def main():
    #
    # {"operation": "FWDetection", "target_ip": "192.168.1.22", "ports": [22,80,443, 53] }
    #{
    #"operation": "UDPScan",
    #"target_ip": "192.168.1.22",
    #"ports_status": "[\"22:Open|Filtered\", \"33:Open|Filtered\", \"44:Open|Filtered\", \"55:Open|Filtered\", \"78:Open|Filtered\"]"
    #}
    target_ip = "192.168.1.22"
    ports = FWDetection("OSDetection", target_ip, [22,20,80,443])
    ans = ports.do_scan()
    print("Operative System: %s " % ans)


if __name__=="__main__":
    main()