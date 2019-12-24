from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^read$', views.read),
    url(r'^read/(?P<shows_id>\d+)$',views.read_one),
    url(r'^read/(?P<shows_id>\d+)/delete$',views.delete_show),
    url(r'^read/(?P<shows_id>\d+)/edit$', views.edit_show),
]







