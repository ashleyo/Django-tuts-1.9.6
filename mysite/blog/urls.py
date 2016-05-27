from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^create$', views.post_create, name='create'),
    url(r'^detail$', views.post_detail, name='detail'), 
    url(r'^update$', views.post_update, name='update'),
    url(r'^delete$', views.post_delete, name='delete'),
    url(r'^$', views.post_list, name='list'),
]