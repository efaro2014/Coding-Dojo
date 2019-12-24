from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.new),
    url(r'^create$', views.create),
    url(r'^(?P<my_val>\d+)$', views.method),
     url(r'^(?P<my_val>\d+)/destroy$', views.destroy)
]

