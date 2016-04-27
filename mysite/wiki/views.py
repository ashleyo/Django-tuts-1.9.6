from django.shortcuts import render, redirect

from .models import Page

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
 