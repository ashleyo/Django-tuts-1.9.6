from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns = [
    #url(r'^detail$', views.post_detail, name='detail'), #default maybe?
    url(r'^(?P<id>\d+)$', views.post_detail, name='detail'),
    url(r'^create$', views.post_create, name='create'),
    url(r'^(?P<id>\d+)/edit/$', views.post_update, name='update'),
    url(r'^(?P<id>\d+)/delete$', views.post_delete, name='delete'),
    url(r'^$', views.post_list, name='list'),
]