from django.conf.urls import url
from .import views 

urlpatterns= [
    url(r"^$", views.index),
    url(r'wall$', views.create_msg),
    url(r'message$', views.create_cmt),
    url(r'delete$', views.delete_cmt),
]
