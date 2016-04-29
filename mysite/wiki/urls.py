from django.conf.urls import url, include

from . import views

app_name = 'wiki'


urlpatterns = [
    url('^', include('django.contrib.auth.urls'))
]

# above includes ....
# Note that this means you cannot have wiki pages called login, logout, etc
# A TODO is probably to give these a prefix to remove that restriction
#^login/$ [name='login']
#^logout/$ [name='logout']
#^password_change/$ [name='password_change']
#^password_change/done/$ [name='password_change_done']
#^password_reset/$ [name='password_reset']
#^password_reset/done/$ [name='password_reset_done']
#^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$ [name='password_reset_confirm']
#^reset/done/$ [name='password_reset_complete']

urlpatterns += [
    #ex: /polls/
    url(r'^(?P<page_name>[^/]+)/edit/$', views.edit_page, name='edit_page'),
    url(r'^(?P<page_name>[^/]+)/save/$', views.save_page, name='save_page'),
    url(r'^(?P<page_name>[^/]+)/$', views.view_page, name='view_page'),

]