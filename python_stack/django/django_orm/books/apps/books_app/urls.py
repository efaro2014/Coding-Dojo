from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^books/(?P<books_id>\d+)$',views.view),
    url(r'^authors$', views.authors),
    url(r'^authors/(?P<authors_id>\d+)$', views.notes)
]

