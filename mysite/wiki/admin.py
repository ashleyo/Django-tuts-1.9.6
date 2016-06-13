from django.contrib import admin

from .models import Page, Tag, UserFileUpload #,NavItem

admin.site.register(Page)
#admin.site.register(NavItem) # moved to its own app
#stopgap, we really need to be able to associate Tags with Pages in the admin
admin.site.register(Tag)
admin.site.register(UserFileUpload)