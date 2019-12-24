from django.conf.urls import url
from .import views 

urlpatterns = [
    url(r'^$', views.index),
    url(r'create$', views.register),
    url(r'dashboard$', views.login),
    url(r'read$', views.read),
    url(r'logout', views.logout),
    url(r'new$', views.trips),
]
