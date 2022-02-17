#!/usr/binpython3
import requests
import json
import time

import argparse
from json2html import *

def do_post(url,data):
    print(url, " data ", data)
    return requests.post(url, json = data)
    
def network_scan(ip):
    data = {'operation':'network-scan', 'target_ip': ip}
    url = "http://127.0.0.1:8000/api/operations/networkscan"
    print("data %s " % data)
    return do_post(url,data)

def get_ip(value):
    return value.split('/')[1].split('has ')[1].split(' says')[0]

def get_host(target_ip):
    data = network_scan(target_ip)
    print(data.text)
    data = json.loads(data.text)
    print("data load : %s " % data['operation'])
    hosts = []
    for key, value in data.items():
        #print("response key : ", key, " value : ", value)
        if key != 'operation':
            ip = get_ip(value)
            #print(" ip ", ip)
            hosts.append(ip)
    return hosts

def get_ports(host, ports):
    url = "http://127.0.0.1:8000/api/operations/portscan"
    json_out=[]
    for i in ["TCPConnect", "TCPACKScan", "FinScan", "NullScan", "WindowScan", "Xmasport"]:
        data = { "operation": i, "target_ip": host, "ports": ports, "type":"TCP" }
        ports_r = do_post(url, data)
        json_out.append(ports_r.text)
    return json.dumps(json_out)


def get_os(host):
    url = "http://127.0.0.1:8000/api/operations/osdetection"
    data = { "operation": "OSDetection", "target_ip": host }
    os_type = do_post(url, data)
    #print("os_type ", os_type.text)
    return json.loads(os_type.text)


def generate_report(report_data):
    print("json_file : ", report_data)
    i=1
    out =[]
    json_file = {}
    for val in report_data:
        print(i, "val ", val )
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
        i = i+1
    print("final value : ", out)
    return json.dumps(out)


def report_2_file(report_data):
    report = generate_report(report_data)
    html = json2html.convert(json=report)
    print(html)
    out = open('./report'+str(time.time())+".html", 'w')
    out.write(html)
    out.close()


def get_http_header(host):
    url = "http://127.0.0.1:8000/api/operations/httpheader"
    data = { "operation" : "HTTP_Headers", "target_ip": host , "path": "/" }
    http_header = do_post(url, data)
    return json.loads(http_header.text)


def get_banner_grabbing(host, ports):
    url = "http://127.0.0.1:8000/api/operations/bannergrabbing"
    data = {
    "operation": "BannerGrabbing",
    "target_ip": host,
    "ports": ports
    }
    os_type = do_post(url, data)
    return json.loads(os_type.text)


def get_fw_detection(host, ports):
    url = "http://127.0.0.1:8000/api/operations/fwdetection"
    data = {
    "operation": "",
    "target_ip": host,
    "ports": ports
    }
    fw_detection = do_post(url, data)
    return json.loads(fw_detection.text)


def get_ipv6_detection(host, ports):
    url = "http://127.0.0.1:8000/api/operations/ipv6scan"
    data = {"operation": "ipv6scan", "target_ip": "multicast", 'timeout':2}
    ipv6_type = do_post(url, data)
    # print("os_type ", os_type.text)
    return json.loads(ipv6_type.text)


def get_dns_scan(host):
    url = "http://127.0.0.1:8000/api/operations/dnsdetection"
    data = {
    "operation": "DNSdetection",
    "target_ip": host,
    "dns_ip": "192.168.1.1"
    }
    dns_scan = do_post(url, data)
    # print("os_type ", os_type.text)
    return json.loads(dns_scan.text)


def main():
    target_ip = ""
    ports_init = []
    parser = argparse.ArgumentParser()
    parser.add_argument('-ip-range', required=True, help="define IP or subnet range")
    parser.add_argument('-ports', type=list, default=[80, 22, 443], help="list of ports to scan")
    args = parser.parse_args()
    print("Init full process")
    target_ip = args.ip_range
    ports_init = args.ports
    ports_init2 = []
    for i in ports_init:
        ports_init2.append(int(i))
    print(ports_init2)
    hosts = get_host(target_ip)
    report_data = []
    for host in hosts:
        if host not in  ["192.168.1.100", "192.168.1.1"]:
            print("host : ", host)
            report_data.append(host)
            ports = get_ports(host, ports_init)
            report_data.append(ports)
            print(" ports_status : ", ports)
            os_type = get_os(host)
            report_data.append(os_type)
            print(" os_type : ", os_type)
            http_header = get_http_header(host)
            report_data.append(http_header)
            print(" http_header : ", http_header)
            banner_grabbing = get_banner_grabbing(host, ports_init)
            report_data.append(banner_grabbing)
            print(" banner_grabbing : ", banner_grabbing)
            dns_scan = get_dns_scan(host)
            report_data.append(dns_scan)
            print(" dns_scan : ", dns_scan)
            fw_detection = get_fw_detection(host, ports_init)
            report_data.append(fw_detection)
            print(" fw_detection : ", fw_detection)
            ipv6_detection = get_ipv6_detection(host, ports_init)
            report_data.append(ipv6_detection)
            print(" ipv6_detection : ", ipv6_detection)
    report_2_file(report_data)
    print("End full process")

if __name__=="__main__":
    main()
