from django.conf.urls import url

from . import views

app_name = 'wiki'

urlpatterns = [
    #ex: /polls/
        url(r'^(?P<page_name>[^/]+)/edit/$', views.edit_page, name='edit_page'),
        url(r'^(?P<page_name>[^/]+)/save/$', views.save_page, name='save_page'),
        url(r'^(?P<page_name>[^/]+)/$', views.view_page, name='view_page'),

]