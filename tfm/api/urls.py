from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register(r'network-scan', views.NetworkScanViewSet)
router.register(r'modules', views.ModulesViewSet)
router.register(r'os-detection', views.OsDetectionViewSet)
router.register(r'http-header', views.HttpHeaderViewSet)
router.register(r'banner-grabbing', views.BannerGrabbingViewSet)
router.register(r'firewall-detection', views.FirewallDetectionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('operations/modules', views.modules, name='modules'),
    path('operations/networkscan', views.networkscan, name='networkscan'),
    path('operations/portscan', views.portscan, name='portscan'),
    path('operations/osdetection', views.osdetection, name='osdetection'),
    path('operations/dnsdetection', views.dnsdetection, name='dnsdetection'),
    path('operations/httpheader', views.httpheader, name='httpheader'),
    path('operations/bannergrabbing', views.bannergrabbing, name='bannergrabbing'),
    path('operations/fwdetection', views.firewalldetection, name='firewalldetection'),
    path('operations/ipv6scan', views.ipv6scan, name='ipv6scan'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]