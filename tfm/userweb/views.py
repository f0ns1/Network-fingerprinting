from django.shortcuts import render

# Create your views here.

def index(request):
    context={}
    return render(request, 'index.html', context)

def scan(request):
    context={}
    return render(request, 'scan.html', context)

def reports(request):
    context={}
    return render(request, 'reports.html', context)
