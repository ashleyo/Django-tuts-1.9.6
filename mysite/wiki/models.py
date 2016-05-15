from django.db import models

# Create your models here.
class Page(models.Model):
    name = models.CharField(max_length=20,primary_key=True)
    content = models.TextField(blank=True)
    def __str__(self):
        return self.name

class NavItem(models.Model):
    display = models.CharField(max_length=20)
    redirect = models.CharField(max_length=63)
    priority = models.SmallIntegerField()
    tag = models.CharField(max_length=10)
    def __str__(self):
        return self.display
   
