from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from .models import Post
from .forms import PostForm

from .apps import BlogConfig as thisApp
from nav.models import NavItem

@login_required(login_url='wiki:login')
def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            messages.success(request, "Post Created")
            return redirect(instance.get_absolute_url())
        else:
            messages.error(request, "Post could not be created")
    context = { 'form': form }
    return render(request, 'blog/post_form.html', context)

def post_detail(request,slug=None):
    context = get_object_or_404(Post,slug=slug)
    return render(request, 'blog/post_detail.html', {'post':context})
    
def post_list(request): 
    queryset_list = Post.objects.all()
    query_term = request.GET.get('q')
    if query_term:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query_term) |
            Q(content__icontains=query_term) |
            Q(author__first_name__icontains=query_term) |
            Q(author__last_name__icontains=query_term)
            ).distinct()
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
    context = {'posts': queryset, 
            'page_request_var': page_request_var, 
            'navitems' : NavItem.get_nav_by_app(thisApp.name) }
    return render(request, 'blog/index.html', context)

@login_required(login_url='wiki:login')    
def post_update(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)
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

@login_required(login_url='wiki:login')
def post_delete(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)
    m = "Deleted {} {}".format(instance.id,instance.title)
    instance.delete()
    messages.success(request, m)
    return redirect('blog:list')
    
