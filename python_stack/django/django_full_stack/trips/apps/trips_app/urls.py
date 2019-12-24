from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.register),
    url(r'^login$', views.login),
    url(r'^home$', views.success),
    url(r'^logout$', views.logout), 
    url(r'^trips$', views.createTrip), 
    url(r'^trips/new$', views.addTrip),
    url(r'^trips/(?P<trip_id>\d+)$',views.tripDetails),
    url(r'^trips/(?P<trip_id>\d+)/remove$',views.deleteTrip),
    url(r'^trips/edit/(?P<trip_id>\d+)$',views.editTrip),
    url(r'^trips/edit/cancel$', views.cancel),
    url(r'^trips/logout$', views.logout),
    url(r'^trips/new/logout$', views.logout),
    url(r'^trips/edit/logout$', views.logout),
    url(r'^trips/main_page$', views.success),
    url(r'^back$', views.cancel),
]
