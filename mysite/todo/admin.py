from django.contrib import admin
from .models import ToDoItem,ToDoFolder,Tag

admin.site.register(ToDoItem)
admin.site.register(Tag)
admin.site.register(ToDoFolder)
