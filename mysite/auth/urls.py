from django.contrib.auth import views as auth_views
from django.conf.urls import url

from . import views

app_name = 'auth'

urlpatterns = [
    url(r'^login/$', auth_views.login, {'template_name': 'auth/registration/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'auth/registration/logged_out.html'}, name='logout'),
    url(r'^register/$', views.register_page, name='register'),
]




# urlpatterns = [
    # url('^', include('django.contrib.auth.urls'))
# ]

# above includes ....
#^login/$ [name='login']
#^logout/$ [name='logout']
#^password_change/$ [name='password_change']
#^password_change/done/$ [name='password_change_done']
#^password_reset/$ [name='password_reset']
#^password_reset/done/$ [name='password_reset_done']
#^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$ [name='password_reset_confirm']
#^reset/done/$ [name='password_reset_complete']