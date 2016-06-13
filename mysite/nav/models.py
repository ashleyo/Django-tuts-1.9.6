from django.db import models
from django.db.models import Q
from django.core.cache import cache

# Create your models here.
class NavItem(models.Model):
    display = models.CharField(max_length=20)
    redirect = models.CharField(max_length=63)
    redirectPage = models.CharField(max_length=63, blank=True, default="")
    priority = models.SmallIntegerField()
    tag = models.CharField(max_length=10)
    
    def __str__(self):
        return self.display

    '''Hold NavItem refreshes down to one every 15s - 
    these aren't going to change very often
    or hurt us if they are a bit stale
    '''
    @staticmethod
    def get_nav_by_app(app):
        if not cache.get(app):
            qs = NavItem.objects.order_by('priority').filter(
                Q(tag__contains=app) | 
                Q(tag='all')
                )
            cache.set(app,qs,15)
        return cache.get(app)

