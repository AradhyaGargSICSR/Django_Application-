# myapp/urls.py

from rest_framework import routers
from .views import InvoiceViewSet, InvoiceDetailViewSet
from django.http import HttpResponse
from django.urls import path, include

def empty_favicon(request):
    return HttpResponse(status=204)

router = routers.DefaultRouter()
router.register(r'invoices', InvoiceViewSet)
router.register(r'invoicedetails', InvoiceDetailViewSet)

urlpatterns = [
     path('', include(router.urls)),
]
urlpatterns = router.urls
