from django.db import models
from django.core.urlresolvers import reverse


def upload_location(instance, filename):
    return "{}/{}".format(instance.id, filename)    

class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True,
            upload_to=upload_location, 
            width_field='width_field', 
            height_field='height_field')
    height_field = models.PositiveSmallIntegerField(null=True, default=0)
    width_field = models.PositiveSmallIntegerField(null=True, default=0)
    timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)
    updated = models.DateTimeField(auto_now=True,auto_now_add=False)
    
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={"id":self.id})
        
    class Meta:
        ordering=["-timestamp","-updated"]
        
    