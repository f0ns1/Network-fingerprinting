from json2html import *
from .core.ARPping import ARPPing
from .serializers import *
from .models import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
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
    serializer_class = HttpHeaderSerializer
class BannerGrabbingViewSet(viewsets.ModelViewSet):
    queryset = DefaultModule.objects.all().order_by('id')
    serializer_class = BannerGrabbingSerializer
class FirewallDetectionViewSet(viewsets.ModelViewSet):
    queryset = DefaultModule.objects.all().order_by('id')
    serializer_class = FirewallDetectionSerializer



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
def portscan(request):
    if request.method == 'GET':
        snippets = DefaultModule.objects.all()
        serializer = PortScanSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PortScanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def osdetection(request):
    if request.method == 'GET':
        snippets = DefaultModule.objects.all()
        serializer = PortScanSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PortScanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def httpheader(request):
    if request.method == 'GET':
        snippets = DefaultModule.objects.all()
        serializer = PortScanSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PortScanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def bannergrabbing(request):
    if request.method == 'GET':
        snippets = DefaultModule.objects.all()
        serializer = PortScanSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PortScanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def firewalldetection(request):
    if request.method == 'GET':
        snippets = DefaultModule.objects.all()
        serializer = PortScanSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PortScanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
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