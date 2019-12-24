from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.register),
    url(r'^login$', views.login),
    url(r'^home$', views.success),
    url(r'^logout$', views.logout), 
    url(r'^jobs$', views.createJob),
    url(r'^jobs/new$', views.addJob),
    url(r'^jobs/(?P<job_id>\d+)$',views.jobDetails),
    url(r'^jobs/(?P<job_id>\d+)/remove$',views.deleteJob),
    url(r'^jobs/edit/(?P<job_id>\d+)$',views.editJob),
    url(r'^jobs/edit/back$', views.cancel),
    url(r'^back$', views.cancel),
    url(r'^jobs/main_page$', views.success),
    url(r'^jobs/logout$', views.logout),
    url(r'^jobs/new/logout$', views.logout),
    url(r'^jobs/edit/logout$', views.logout),

]