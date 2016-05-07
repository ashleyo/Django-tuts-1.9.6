from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Page

import logging
logger = logging.getLogger('django')

# Create your views here.

def edit_page(request, page_name):
    try:
        page = Page.objects.get(pk=page_name)
        content = page.content
    except Page.DoesNotExist:
        content=''
    return render(request,'wiki/edit_page.html', { 'page_name':page_name, 'content':content})
    
    
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
    try:
        page = Page.objects.get(pk=page_name)
        content = page.content
    except Page.DoesNotExist:
        return render(request,'wiki/create_page.html', { 'page_name':page_name})
    return render(request, 'wiki/view_page.html', {'page_name':page_name, 'content':content})
    
def register_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            ## create user 
            logger.info('Valid form')
            #user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = User.objects.create_user(username=username, password=password)            
            user.save()
            return redirect('wiki:login')   
    else:
        logger.info('Invalid or empty form')
        form = UserCreationForm()
    logger.info('going to registration page')
    return render(request, 'registration/create_user.html', {'form':form})
 