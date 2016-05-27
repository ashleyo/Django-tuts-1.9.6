from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

# Create your views here.
def post_create(request):
    return HttpResponse("<h1>Create</h1>")

def post_detail(request,postTitle=""):
    context = get_object_or_404(Post,title=postTitle)
    return render(request, 'blog/post_detail.html', {'post':context})
    
def post_list(request):
    context = Post.objects.all()
    return render(request, 'blog/index.html', {'posts':context})
    
def post_update(request):
    return HttpResponse("<h1>Update</h1>")

def post_delete(request):
    return HttpResponse("<h1>Delete</h1>")