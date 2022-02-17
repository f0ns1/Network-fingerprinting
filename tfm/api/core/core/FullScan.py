#!/usr/binpython3
import requests
import json
import time

import argparse
from json2html import *

class FullScan:

    def __init__(self, ports, target_ip):
        self.ports_init = ports
        self.target_ip = target_ip


    def do_post(self, url, data):
        print(url, " data ", data)
        return requests.post(url, json=data)


    def network_scan(self, ip):
        data = {'operation': 'network-scan', 'target_ip': ip}
        url = "http://127.0.0.1:8000/api/operations/networkscan"
        print("data %s " % data)
        return self.do_post(url, data)


    def get_ip(self, value):
        return value.split('/')[1].split('has ')[1].split(' says')[0]


    def get_host(self, target_ip):
        data = self.network_scan(target_ip)
        print(data.text)
        data = json.loads(data.text)
        print("data load : %s " % data['operation'])
        hosts = []
        for key, value in data.items():
            # print("response key : ", key, " value : ", value)
            if key != 'operation':
                ip = self.get_ip(value)
                # print(" ip ", ip)
                hosts.append(ip)
        return hosts


    def get_ports(self, host, ports):
        url = "http://127.0.0.1:8000/api/operations/portscan"
        json_out = []
        for i in ["TCPConnect", "TCPACKScan", "FinScan", "NullScan", "WindowScan", "Xmasport"]:
            data = {"operation": i, "target_ip": host, "ports": ports, "type": "TCP"}
            ports_r = self.do_post(url, data)
            json_out.append(ports_r.text)
        return json.dumps(json_out)


    def get_os(self, host):
        url = "http://127.0.0.1:8000/api/operations/osdetection"
        data = {"operation": "OSDetection", "target_ip": host}
        os_type = self.do_post(url, data)
        # print("os_type ", os_type.text)
        return json.loads(os_type.text)


    def generate_report(self, report_data):
        print("json_file : ", report_data)
        i = 1
        out = []
        json_file = {}
        for val in report_data:
            print(i, "val ", val)
            if i == 1:
                json_file['host'] = val
            elif i == 2:
                json_file['ports'] = val
            elif i == 3:
                json_file['os_type'] = val
            elif i == 4:
                json_file['http_header'] = val
            elif i == 5:
                json_file['banner_grabbing'] = val
            elif i == 6:
                json_file['fw_detection'] = val
            elif i == 7:
                json_file['dns_scan'] = val
            elif i == 8:
                json_file['ipv6_detection'] = val
                out.append(json_file)
                json_file = {}
                i = 0
            i = i + 1
        print("final value : ", out)
        return json.dumps(out)


    def report_2_file(self, report_data):
        report = self.generate_report(report_data)
        html = json2html.convert(json=report)
        print(html)
        name = './report_' + str(time.time()) + ".html"
        out = open(name, 'w')
        out.write(html)
        out.close()
        return name


    def get_http_header(self, host):
        url = "http://127.0.0.1:8000/api/operations/httpheader"
        data = {"operation": "HTTP_Headers", "target_ip": host, "path": "/"}
        http_header = self.do_post(url, data)
        return json.loads(http_header.text)


    def get_banner_grabbing(self, host, ports):
        url = "http://127.0.0.1:8000/api/operations/bannergrabbing"
        data = {
            "operation": "BannerGrabbing",
            "target_ip": host,
            "ports": ports
        }
        os_type = self.do_post(url, data)
        return json.loads(os_type.text)


    def get_fw_detection(self, host, ports):
        url = "http://127.0.0.1:8000/api/operations/fwdetection"
        data = {
            "operation": "",
            "target_ip": host,
            "ports": ports
        }
        fw_detection = self.do_post(url, data)
        return json.loads(fw_detection.text)


    def get_ipv6_detection(self, host, ports):
        url = "http://127.0.0.1:8000/api/operations/ipv6scan"
        data = {"operation": "ipv6scan", "target_ip": "multicast", 'timeout': 2}
        ipv6_type = self.do_post(url, data)
        # print("os_type ", os_type.text)
        return json.loads(ipv6_type.text)


    def get_dns_scan(self, host):
        url = "http://127.0.0.1:8000/api/operations/dnsdetection"
        data = {
            "operation": "DNSdetection",
            "target_ip": host,
            "dns_ip": "192.168.1.1"
        }
        dns_scan = self.do_post(url, data)
        # print("os_type ", os_type.text)
        return json.loads(dns_scan.text)

    def do_scan(self):
        target_ip = self.target_ip
        ports_init = self.ports_init
        hosts = self.get_host(target_ip)
        report_data = []
        for host in hosts:
            if host not in ["192.168.1.100", "192.168.1.1"]:
                print("host : ", host)
                report_data.append(host)
                ports = self.get_ports(host, ports_init)
                report_data.append(ports)
                print(" ports_status : ", ports)
                os_type = self.get_os(host)
                report_data.append(os_type)
                print(" os_type : ", os_type)
                http_header = self.get_http_header(host)
                report_data.append(http_header)
                print(" http_header : ", http_header)
                banner_grabbing = self.get_banner_grabbing(host, ports_init)
                report_data.append(banner_grabbing)
                print(" banner_grabbing : ", banner_grabbing)
                dns_scan = self.get_dns_scan(host)
                report_data.append(dns_scan)
                print(" dns_scan : ", dns_scan)
                fw_detection = self.get_fw_detection(host, ports_init)
                report_data.append(fw_detection)
                print(" fw_detection : ", fw_detection)
                ipv6_detection = self.get_ipv6_detection(host, ports_init)
                report_data.append(ipv6_detection)
                print(" ipv6_detection : ", ipv6_detection)
        return self.report_2_file(report_data)

def main():
    target_ip = "192.168.1.1/24"
    ports_init = [22, 80]
    scan = FullScan(ports_init, target_ip)
    print(scan.do_scan())





if __name__ == "__main__":
    main()
