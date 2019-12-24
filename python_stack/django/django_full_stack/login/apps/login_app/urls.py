from django.conf.urls import url
from .import views 

urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r'^create/read$', views.read),
    url(r'^login$', views.login),
    url(r'^create/success$', views.success),
    url(r'^create/clear', views.clear),

]

