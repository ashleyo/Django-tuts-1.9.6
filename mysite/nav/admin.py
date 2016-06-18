from django.contrib import admin
from .models import NavItem

class NavItemModelAdmin(admin.ModelAdmin):
    list_display = ['display', 'tag', 'priority']
    list_filter = ['tag']
    ordering = ['tag', 'priority']
    class Meta:
        model = NavItem


admin.site.register(NavItem, NavItemModelAdmin)
