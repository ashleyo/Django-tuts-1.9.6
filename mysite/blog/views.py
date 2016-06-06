from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post
from .forms import PostForm

# Create your views here.
def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
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
    queryset_list = Post.objects.all()
    
    paginator = Paginator(queryset_list, 6) # Show 6 posts per page
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
  
    return render(request, 'blog/index.html', {'posts':queryset, 'page_request_var':page_request_var})
    
def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
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
    
