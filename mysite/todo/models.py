from django.db import models

class ToDoFolder(models.Model):
    name=models.CharField(max_length=32)
    
    def save(self, *args, **kwargs):
        if (pk==1): 
            name='Unfiled'
        super().save(self, *args, **kwargs)

    def __str__(self):
        return self.name

NoUrgent = 1
MiUrgent = 2
HiUrgent = 3
NoImport = 1
MiImport = 2
HiImport = 3
URGENCY_CHOICES = ((NoUrgent,'Routine'),(MiUrgent,'Priority'),(HiUrgent,'Flash'))
IMPORT_CHOICES = ((NoImport,'Green'),(MiImport,'Amber'),(HiImport,'Critical'))

class ToDoItem(models.Model):
    complete = models.BooleanField(default=False)
    name = models.CharField(max_length=128)
    target_date = models.DateField()
    notes = models.TextField(blank=True)
    tags = models.ManyToManyField('Tag')
    urgency = models.SmallIntegerField(choices=URGENCY_CHOICES, default=NoUrgent)
    importance = models.SmallIntegerField(choices=IMPORT_CHOICES, default=NoImport)
    folder = models.ForeignKey(ToDoFolder,default = 1)
    
    def __str__(self):
        return self.name
    def get_priority(self):
        return self.urgency * self.importance

class Tag(models.Model):
    ##TODO make tags save in consistent case regardless of how entered
    name = models.CharField(max_length=20, primary_key=True)
    
    def __str__(self):
        return self.name


