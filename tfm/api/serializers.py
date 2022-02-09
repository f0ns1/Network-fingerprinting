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

class OsDetectionSerializer():
    class Meta:
        model = DefaultModule
        fields = ('id', 'operation', 'input', 'output', 'time')
class HttpHeaderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DefaultModule
        fields = ('id', 'operation', 'input', 'output', 'time')
class BannerGrabbingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DefaultModule
        fields = ('id', 'operation', 'input', 'output', 'time')

class FirewallDetectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DefaultModule
        fields = ('id', 'operation', 'input', 'output', 'time')