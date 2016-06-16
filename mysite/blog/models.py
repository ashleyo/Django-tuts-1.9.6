from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.text import slugify

def upload_location(instance, filename):
    return "{}/{}".format(instance.slug, filename)    

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,default=1)
    title = models.CharField(max_length=120)
    content = models.TextField()
    slug = models.SlugField(unique=True)
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
        return reverse('blog:detail', kwargs={"slug":self.slug})
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = create_slug(self)
        super().save(*args, **kwargs)
        
    class Meta:
        ordering=["-timestamp","-updated"]

def create_slug(instance, new_slug=None) :
    slug = slugify(instance.title)  
    if new_slug is not None:
        slug = new_slug
    qs =  Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:  
        new_slug = "{}-{}".format(slug,qs.first().id)
        return create_slug(instance, new_slug=new_slug) 
    return slug      

    
    