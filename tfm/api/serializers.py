from datetime import date

from rest_framework import serializers

from .models import DefaultModule

class ModulesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DefaultModule
        fields = ('id', 'operation', 'input', 'output', 'time')

class NetworkScanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DefaultModule
        fields = ('id', 'operation', 'target_ip')

class PortScanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DefaultModule
        fields = ('id', 'operation', 'input', 'output', 'time')

class OsDetectionSerializer(serializers.HyperlinkedModelSerializer):
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