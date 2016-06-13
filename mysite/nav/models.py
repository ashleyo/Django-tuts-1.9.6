from django.db import models

# Create your models here.
class NavItem(models.Model):
    display = models.CharField(max_length=20)
    redirect = models.CharField(max_length=63)
    redirectPage = models.CharField(max_length=63, blank=True, default="")
    priority = models.SmallIntegerField()
    tag = models.CharField(max_length=10)
    
    def __str__(self):
        return self.display