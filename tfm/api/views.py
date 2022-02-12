from json2html import *
from .core.ARPping import ARPPing
from .serializers import *
from .models import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .core.core.portscanning import PortScanHandler
from .core.core.OSscanning.OSScanHandler import OSScanHandler
from .core.core.HTTPHeaderScanning.HTTPHeaderScanHandler import HTTPHeaderScanHandler
from .core.core.BannerGrabbingScanning.BannerGrabbingScanHandler import BannerGrabbinScanHandler
from .core.core.DNSScanning.DNSScanHandler import DNSScanHandler
from .core.core.FWDetectionScanning.FWDetectionHandler import FWDetectionHandler
from .core.core.IPV6Scanning.IPV6ScanHandler import IPV6ScanHandler
import json




class ModulesViewSet(viewsets.ModelViewSet):
    queryset = DefaultModule.objects.all().order_by('id')
    serializer_class = DefaultModule
class NetworkScanViewSet(viewsets.ModelViewSet):
    queryset = DefaultModule.objects.all().order_by('id')
    serializer_class = NetworkScanSerializer
class PortScanViewSet(viewsets.ModelViewSet):
    queryset = DefaultModule.objects.all().order_by('id')
    serializer_class = PortScanSerializer
class OsDetectionViewSet(viewsets.ModelViewSet):
    queryset = DefaultModule.objects.all().order_by('id')
    serializer_class = OsDetectionSerializer
class HttpHeaderViewSet(viewsets.ModelViewSet):
    queryset = DefaultModule.objects.all().order_by('id')
    serializer_class = HTTPHeaderSerializer
class BannerGrabbingViewSet(viewsets.ModelViewSet):
    queryset = DefaultModule.objects.all().order_by('id')
    serializer_class = BannerGrabbingSerializer
class FirewallDetectionViewSet(viewsets.ModelViewSet):
    queryset = DefaultModule.objects.all().order_by('id')
    serializer_class = FirewallDetectionSerializer
class DNSScanDetectionViewSet(viewsets.ModelViewSet):
    queryset = DefaultModule.objects.all().order_by('id')
    serializer_class = DNSScanSerializer
class IP6ScanViewSet(viewsets.ModelViewSet):
    queryset = DefaultModule.objects.all().order_by('id')
    serializer_class = IPV6ScanSerializer


@api_view(['GET', 'POST'])
def modules(request):
    if request.method == 'GET':
        snippets = DefaultModule.objects.all()
        serializer = ModulesSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ModulesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'POST'])
def ipv6scan(request):
    if request.method == 'GET':
        serializer = IPV6ScanSerializer(IPV6Seliazer(operation="", target_ip="", response=""))
        return Response(serializer.data)

    elif request.method == 'POST':
        dataJson = json.loads(request.body)
        print("operation: ", dataJson['operation'])
        print("target_ip: ", dataJson['target_ip'])
        operation = dataJson['operation']
        target_ip = dataJson['target_ip']
        timeout = dataJson['timeout']
        handler = IPV6ScanHandler(operation, target_ip, int(timeout))
        ans = handler.do_scan()
        print("Service answer: %s " % ans)
        serialized = json.dumps(ans)
        print(serialized)
        serializer = IPV6ScanSerializer(IPV6Seliazer(operation=operation, target_ip=target_ip, response=serialized))
        if serializer:
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def httpheader(request):
    if request.method == 'GET':
        serializer = HTTPHeaderSerializer(HTTPHeader(operation="", target_ip="", response=""))
        return Response(serializer.data)

    elif request.method == 'POST':
        dataJson = json.loads(request.body)
        print("operation: ", dataJson['operation'])
        print("target_ip: ", dataJson['target_ip'])
        operation = dataJson['operation']
        target_ip = dataJson['target_ip']
        handler = HTTPHeaderScanHandler(operation, target_ip)
        ans = handler.do_scan()
        print("Service answer: %s " % ans)
        serialized = json.dumps(ans)
        print(serialized)
        serializer = HTTPHeaderSerializer(HTTPHeader(operation=operation, target_ip=target_ip, response=serialized))
        if serializer:
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def bannergrabbing(request):
    if request.method == 'GET':
        serializer = BannerGrabbingSerializer(BannerGrabbing(operation="", target_ip="", response=""))
        return Response(serializer.data)

    elif request.method == 'POST':
        dataJson = json.loads(request.body)
        print("operation: ", dataJson['operation'])
        print("target_ip: ", dataJson['target_ip'])
        operation = dataJson['operation']
        target_ip = dataJson['target_ip']
        handler = BannerGrabbinScanHandler(operation, target_ip)
        ans = handler.do_scan()
        print("Service answer: %s " % ans)
        serialized = json.dumps(ans)
        print(serialized)
        serializer = BannerGrabbingSerializer(BannerGrabbing(operation=operation, target_ip=target_ip, response=serialized))
        if serializer:
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def firewalldetection(request):
    if request.method == 'GET':
        serializer = FirewallDetectionSerializer(FWDetection(operation="", target_ip="", response=""))
        return Response(serializer.data)

    elif request.method == 'POST':
        dataJson = json.loads(request.body)
        print("operation: ", dataJson['operation'])
        print("target_ip: ", dataJson['target_ip'])
        operation = dataJson['operation']
        target_ip = dataJson['target_ip']
        handler = FWDetectionHandler(operation, target_ip)
        ans = handler.do_scan()
        print("Service answer: %s " % ans)
        serialized = json.dumps(ans)
        print(serialized)
        serializer = FirewallDetectionSerializer(FWDetection(operation=operation, target_ip=target_ip, response=serialized))
        if serializer:
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def networkscan(request):
    if request.method == 'GET':
        snippets = DefaultModule.objects.all()
        serializer = NetworkScanSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        print("Network Scan post method ")
        dataJson = json.loads(request.body)
        print("operation: ", dataJson['operation'])
        print("target_ip: ", dataJson['target_ip'])
        arp= ARPPing(dataJson['target_ip'])
        ans, unans = arp.do_scan()
        output='{"operation":"'+dataJson['operation']+'"}'
        response = json.loads(output)
        count = 1
        for req, resp in ans:
            val = {'"'+str(count)+'"' : '"'+req.summary()+resp.summary()+'"'}
            print("val ", val)
            response.update(val)
            count += 1
        print("jsonresponse ", response)
        serializer = NetworkScanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def portscan(request):
    if request.method == 'GET':
        serializer = PortScanSerializer(PortScan(operation="", target_ip="", target_ports=[], ports_status=[]))
        return Response(serializer.data)

    elif request.method == 'POST':
        dataJson = json.loads(request.body)
        print("operation: ", dataJson['operation'])
        print("target_ip: ", dataJson['target_ip'])
        print("ports: ", dataJson['ports'])
        print("type: ", dataJson['type'])
        operation = dataJson['operation']
        target_ip = dataJson['target_ip']
        ports = dataJson['ports']
        type = dataJson['type']
        handler = PortScanHandler.PortsScanHandler(operation, target_ip, ports, type)
        ans = handler.do_scan()
        print("Service answer: %s " % ans)
        serialized = json.dumps(ans)
        print(serialized)
        serializer = PortScanSerializer(PortScan(operation=operation, target_ip=target_ip, target_ports=ports, ports_status=serialized))
        if serializer:
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def osdetection(request):
    if request.method == 'GET':
        serializer = OsDetectionSerializer(OSDetection(operation="", target_ip="", response=""))
        return Response(serializer.data)

    elif request.method == 'POST':
        dataJson = json.loads(request.body)
        print("operation: ", dataJson['operation'])
        print("target_ip: ", dataJson['target_ip'])
        operation = dataJson['operation']
        target_ip = dataJson['target_ip']
        os = OSScanHandler(operation, target_ip)
        resp = os.do_scan()
        print(resp)
        serialized = json.dumps(resp)
        print(serialized)
        serializer = OsDetectionSerializer(OSDetection(operation=operation, target_ip=target_ip, response=resp))
        if serializer:
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def dnsdetection(request):
    if request.method == 'GET':
        serializer = DNSScanSerializer(DNSSerializer(operation="", target_ip="", dns_ip="", response=""))
        return Response(serializer.data)

    elif request.method == 'POST':
        dataJson = json.loads(request.body)
        print("operation: ", dataJson['operation'])
        print("target_ip: ", dataJson['target_ip'])
        print("dns_ip: ", dataJson['dns_ip'])
        operation = dataJson['operation']
        target_ip = dataJson['target_ip']
        dns_ip = dataJson['dns_ip']
        os = DNSScanHandler(operation, target_ip, dns_ip)
        resp = os.do_scan()
        print(resp)
        serialized = json.dumps(resp)
        print(serialized)
        serializer = DNSScanSerializer(DNSSerializer(operation=operation, target_ip=target_ip, dns_ip=dns_ip,response=resp))
        if serializer:
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)