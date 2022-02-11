from datetime import date

from rest_framework import serializers

from .models import DefaultModule
from .models import PortsModule

class ModulesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DefaultModule
        fields = ('id', 'operation', 'input', 'output', 'time')

class NetworkScanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DefaultModule
        fields = ('id', 'operation', 'target_ip')


class PortScan:
    def __init__(self, operation, target_ip, target_ports, ports_status):
        self.operation= operation
        self.target_ip = target_ip
        self.target_ports = target_ports
        self.ports_status = ports_status

portscan = PortScan(operation="", target_ip="", target_ports=[], ports_status=[])


class PortScanSerializer(serializers.Serializer):
    operation = serializers.CharField(max_length=200)
    target_ip = serializers.CharField(max_length=200)
    target_ports = []
    ports_status = serializers.CharField(max_length=200)

class OSDetection:
    def __init__(self, operation, target_ip, response):
        self.operation= operation
        self.target_ip = target_ip
        self.response = response

osdetection = OSDetection(operation="", target_ip="", response="")


class OsDetectionSerializer(serializers.Serializer):
    operation = serializers.CharField(max_length=200)
    target_ip = serializers.CharField(max_length=200)
    response = serializers.CharField(max_length=2000)


class DNSSerializer:
    def __init__(self, operation, target_ip, dns_ip, response):
        self.operation= operation
        self.target_ip = target_ip
        self.dns_ip = dns_ip
        self.response = response

dns_scan = DNSSerializer(operation="", target_ip="", dns_ip = "", response="")


class DNSScanSerializer(serializers.Serializer):
    operation = serializers.CharField(max_length=200)
    target_ip = serializers.CharField(max_length=200)
    dns_ip = serializers.CharField(max_length=200)
    response = serializers.CharField(max_length=2000)

class BannerGrabbing:
    def __init__(self, operation, target_ip, response):
        self.operation= operation
        self.target_ip = target_ip
        self.response = response

banner_grabbing = BannerGrabbing(operation="", target_ip="", response="")


class BannerGrabbingSerializer(serializers.Serializer):
    operation = serializers.CharField(max_length=200)
    target_ip = serializers.CharField(max_length=200)
    response = serializers.CharField(max_length=2000)

class HTTPHeader:
    def __init__(self, operation, target_ip, response):
        self.operation= operation
        self.target_ip = target_ip
        self.response = response

http_header = HTTPHeader(operation="", target_ip="", response="")


class HTTPHeaderSerializer(serializers.Serializer):
    operation = serializers.CharField(max_length=200)
    target_ip = serializers.CharField(max_length=200)
    response = serializers.CharField(max_length=2000)

class FWDetection:
    def __init__(self, operation, target_ip, response):
        self.operation= operation
        self.target_ip = target_ip
        self.response = response

fw_detection = FWDetection(operation="", target_ip="", response="")


class FirewallDetectionSerializer(serializers.Serializer):
    operation = serializers.CharField(max_length=200)
    target_ip = serializers.CharField(max_length=200)
    response = serializers.CharField(max_length=2000)


class IPV6Seliazer:
    def __init__(self, operation, target_ip, response):
        self.operation= operation
        self.target_ip = target_ip
        self.response = response

fw_detection = FWDetection(operation="", target_ip="", response="")


class IPV6ScanSerializer(serializers.Serializer):
    operation = serializers.CharField(max_length=200)
    target_ip = serializers.CharField(max_length=200)
    response = serializers.CharField(max_length=2000)

