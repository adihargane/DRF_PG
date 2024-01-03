from django.conf.urls import url
from apps.cbvusingquery import views

urlpatterns = [
    url(r'^employee/$', views.EmployeeCRUD.as_view(), name='CRUD APIs Employee table'),
    url(r'^filteremployeelist/$', views.FilterEmployeeList.as_view(), name='Filter Employee table data'),
]
