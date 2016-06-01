from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post
from .forms import PostForm

# Create your views here.
def post_create(request):
    form = PostForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, "Post Created")
            return redirect(instance.get_absolute_url())
        else:
            messages.error(request, "Post could not be created")
    context = { 'form': form }
    return render(request, 'blog/post_form.html', context)

def post_detail(request,id=1):
    context = get_object_or_404(Post,id=id)
    return render(request, 'blog/post_detail.html', {'post':context})
    
def post_list(request): 
    context = Post.objects.all()
    return render(request, 'blog/index.html', {'posts':context})
    
def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, "Post Edited")
            return redirect(instance.get_absolute_url())
        else:
            messages.error(request, "Post was not edited")
    context = { 
            'title' : instance.title, 
            'content' : instance.content,
            'form' : form,
            }
    return render(request, 'blog/post_form.html', context)

def post_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    m = "Deleted {} {}".format(instance.id,instance.title)
    instance.delete()
    messages.success(request, m)
    return redirect('blog:list')
