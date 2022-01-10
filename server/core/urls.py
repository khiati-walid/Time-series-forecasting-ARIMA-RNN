from django.urls import path, include, re_path
from rest_framework import routers
from .views import SalesView, FileUploadView,ClientView,EmployeeView

app_name = 'core'


router = routers.DefaultRouter()
router.register(r'sales', viewset=SalesView, basename='sales')
router.register(r'clients', viewset=ClientView, basename='clients')
router.register(r'employees', viewset=EmployeeView, basename='employees')

urlpatterns = [
    path('', include(router.urls)),
    re_path(r'^upload/(?P<filename>[^/]+)$', FileUploadView.as_view())
]