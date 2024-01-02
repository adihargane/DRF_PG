from django.conf.urls import url
from apps.cbv import views

urlpatterns = [
    url(r'^vehicle/$', views.VehicleCRUD.as_view()),
    url(r'^vehicle/(?P<pk>[A-Za-z0-9]+)/$', views.VehicleCRUD.as_view()),
    url(r'^vehiclemaster/$', views.SoftVehicle.as_view()),
]
