from django.views.generic import ListView as GenericListView
from .models import ToDoItem

class ListView(GenericListView):
    context_object_name = 'todos'
    queryset = ToDoItem.objects.order_by('target_date')
    template_name = 'todo/todo_list.html''
