from django.db import models

# Create your models here.
class Tag(models.Model):
    ##TODO make tags save in consistent case regardless of how entered
    name = models.CharField(max_length=20, primary_key=True)
    
    def __str__(self):
        return self.name


class Page(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    content = models.TextField(blank=True)
    tags = models.ManyToManyField(Tag)
    
    def __str__(self):
        return self.name

class UserFileUpload(models.Model):
    upload = models.FileField(upload_to='uploads/')
    #file will be saved to MEDIA_ROOT/uploads
    
    def __str__(self):
        return self.upload.name
   
class HitsCounter(models.Model):
    _singleton_instance_id = 1
    counter = models.IntegerField()
    
    def reset_counter(self):
        self.counter = 0;

    def save(self, *args, **kwargs):
        self.pk = self._singleton_instance_id
        super(HitsCounter, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass
        
    