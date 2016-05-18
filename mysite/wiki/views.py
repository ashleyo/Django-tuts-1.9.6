from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import SearchForm
from .models import Page, NavItem

nav = NavItem.objects.order_by('priority')[:]

import logging
logger = logging.getLogger('django')


def SearchPageView(request):
    if not request.method == 'POST':
        form = SearchForm()
    else:
        form = SearchForm(request.POST)
        if form.is_valid():
            pages = Page.objects.filter(name__contains = form.cleaned_data["text"])  
            return render(request,'wiki/search_page.html', {"form":form, "pages":pages}) 
    return render(request, 'wiki/search_page.html', {"form":form})        

def HelpPageView(request):
    return render(request, 'wiki/help_page.html')

StaticPages = { "Search": SearchPageView, "Help": HelpPageView}



# Create your views here.
@login_required(login_url='wiki:login')
def edit_page(request, page_name):
    try:
        page = Page.objects.get(pk=page_name)
        content = page.content
    except Page.DoesNotExist:
        content=''
    return render(request,'wiki/edit_page.html', { 'page_name':page_name, 'content':content})
    
@login_required(login_url='wiki:login')    
def save_page(request, page_name):
    content = request.POST["content"]
    try:
        page = Page.objects.get(pk=page_name)
        page.content = content
    except Page.DoesNotExist:
        page = Page(name=page_name, content=content)
    page.save()
    return redirect('wiki:view_page', page_name=page_name)
        

def view_page(request, page_name):
    if page_name in StaticPages:
        return StaticPages[page_name](request)
    try:
        page = Page.objects.get(pk=page_name)
        content = page.content
    except Page.DoesNotExist:
        return render(request,'wiki/create_page.html', { 'page_name':page_name})
    return render(request, 'wiki/view_page.html', {'page_name':page_name, 'content':content, 'navitems':nav})
    
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
 