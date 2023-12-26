from django.conf.urls import url
from apps.fbv import views

urlpatterns = [
    url(r'^userlist/$', views.userList),
    url(r'^userlist/(?P<pk>[0-9]+)/$', views.userDetailsByPk),
    url(r'^usermaster/$', views.userMaster),
    url(r'^softusermaster/$', views.softUserMaster)
]
