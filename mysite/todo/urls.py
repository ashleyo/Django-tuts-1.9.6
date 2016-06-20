from django.conf.urls import url

from . import views

app_name = 'todo'

urlpatterns = [
    url(r'^list/$', views.ListView.as_view(), name='todo_list'),
    #url(r'^page/(?P<page_name>[^/]+)/save/$', views.save_page, name='save_page'),
]

