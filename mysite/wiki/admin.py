from django.contrib import admin

from .models import Page, NavItem, Tag

admin.site.register(Page)
admin.site.register(NavItem)
#stopgap, we really need to be able to associate Tags with Pages in the admin
admin.site.register(Tag)
