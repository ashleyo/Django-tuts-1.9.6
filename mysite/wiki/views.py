from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import SearchForm, UploadFileForm
from .models import Page, NavItem, Tag, UserFileUpload

nav = NavItem.objects.order_by('priority')[:]

import logging
logger = logging.getLogger('django')


StaticPages = { "Index":None, "Search": None, "Help": None, "Upload": None}
 
def SearchPageView(request):
    context = {'navitems':nav}
    if not request.method == 'POST':
        form = SearchForm()
    else:
        form = SearchForm(request.POST)
        if form.is_valid():
            if form.cleaned_data["search_content"]:
                pages = Page.objects.filter(content__contains = form.cleaned_data["text"]) 
            else:
                pages = Page.objects.filter(name__contains = form.cleaned_data["text"])
            context['pages'] = pages
    context['form'] = form
    return render(request, 'wiki/search_page.html', context)
StaticPages["Search"] = SearchPageView     

def HelpPageView(request):
    return render(request, 'wiki/help_page.html', {'navitems':nav,})
StaticPages["Help"] = HelpPageView
    
def IndexPageView(request):
    context = {'navitems':nav}
    context['pages'] = Page.objects.all().order_by('name')
    context['special_pages'] = StaticPages.keys()
    return render(request, 'wiki/index_page.html', context)
    
StaticPages["Index"] = IndexPageView

# Create your views here.
@login_required(login_url='wiki:login')
def edit_page(request, page_name):
    try:
        page = Page.objects.get(pk=page_name)
        content = page.content
        tags = " ".join([ tag.name for tag in page.tags.all() ])
    except Page.DoesNotExist:
        content=''
        tags=''
    return render(request,'wiki/edit_page.html', { 'page_name':page_name, 'content':content, "tags":tags})
    
@login_required(login_url='wiki:login')    
def save_page(request, page_name):
    content = request.POST["content"]
    tags_on_form = request.POST["tags"].title()
    taglist = [
            Tag.objects.get_or_create(name=tag)[0] for tag in tags_on_form.split()
            ] if "tags" in request.POST else []       
    try:
        page = Page.objects.get(pk=page_name)
        page.content = content
    except Page.DoesNotExist:
        page = Page(name=page_name, content=content)
    finally:
        for tag in taglist:
            page.tags.add(tag)
    page.save()
    return redirect('wiki:view_page', page_name=page_name)
        

def view_page(request, page_name):
    if page_name in StaticPages:
        return StaticPages[page_name](request)
    try:
        page = Page.objects.get(pk=page_name)
    except Page.DoesNotExist:
        return render(request,'wiki/create_page.html', { 'page_name':page_name})
    return render(request, 'wiki/view_page.html', {
        'page_name':page_name, 
        'content':page.content,
        'tags':page.tags.all(), 
        'navitems':nav,
        })
    
def register_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            ## create user 
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = User.objects.create_user(username=username, password=password)            
            user.save()
            return redirect('wiki:login')   
    else:
        form = UserCreationForm()
    return render(request, 'wiki/registration/create_user.html', {'form':form})
    
def view_tag(request, tag_name):
    context = {'navitems':nav, 'tag_name':tag_name}
    if tag_name.upper() == 'ALL':
        context['pages'] = Page.objects.all()
    else:
        tag = Tag.objects.get(pk=tag_name)
        context['pages'] = tag.page_set.all()
    return render(request,'wiki/view_tag.html', context)
    
def upload_file(request):
    context = {'navitems':nav}
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = UploadFileForm()
    context['form'] = form
    context['files'] = UserFileUpload.objects.all().order_by('upload')
    return render(request, 'wiki/upload.html', context)
StaticPages["Upload"] = upload_file    