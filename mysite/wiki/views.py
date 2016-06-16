#from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse
# from django.db.models import F

from .forms import SearchForm, UploadFileForm
from .models import Page, Tag, UserFileUpload, HitsCounter #,NavItem

from .apps import WikiConfig as thisApp
from nav.models import NavItem
nav = NavItem.get_nav_by_app(thisApp.name)

import logging
logger = logging.getLogger('custom')
logger.info("Custom logger started")

class HitCounterManager:   
    @staticmethod
    def get_instance():
        try:
            hc = HitsCounter.objects.get(pk=1)
        except HitsCounter.DoesNotExist:
            hc = HitsCounter()
            hc.reset_counter()
            hc.save()
        return hc
    
    hc = get_instance.__func__()
    
    def process_response(self, request, response):
        # self.hc.counter = F('counter') + 1
        self.hc.counter += 1
        logger.info("Template rendered. Hit count {}".format(self.hc.counter))
        #self.hc.save(update_fields=['counter'])
        self.hc.save()
        return response

#convenience - allows a view to decide whether it wants NavItems
#or not without bothering about the implementation
def render_and_nav(request, template, context):
    context["navitems"] = NavItem.get_nav_by_app(thisApp.name)
    request.current_app = thisApp.name
    return TemplateResponse(request, template, context)

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
    agent = request.META["HTTP_USER_AGENT"]
    hits = HitCounterManager.hc.counter
    #return render(request, 'wiki/help_page.html', {'hits':hits, 'navitems':nav,'agent':agent})
    return render_and_nav(request, 'wiki/help_page.html', {'hits':hits, 'agent':agent})
StaticPages["Help"] = HelpPageView
    
def IndexPageView(request):
    context = {'navitems':nav}
    context['pages'] = Page.objects.all().order_by('name')
    context['special_pages'] = StaticPages.keys()
    return render(request, 'wiki/index_page.html', context)
    
StaticPages["Index"] = IndexPageView

@login_required(login_url='auth:login')
def edit_page(request, page_name):
    try:
        page = Page.objects.get(pk=page_name)
        content = page.content
        tags = " ".join([ tag.name for tag in page.tags.all() ])
    except Page.DoesNotExist:
        content=''
        tags=''
    return render(request,'wiki/edit_page.html', { 'page_name':page_name, 'content':content, "tags":tags})

#could do with a cancel button - only problem is where do we redirect to? 
@login_required(login_url='auth:login')    
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
    #return render(request, 'wiki/view_page.html', {
    return render_and_nav(request, 'wiki/view_page.html', {
        'page_name':page_name, 
        'content':page.content,
        'tags':page.tags.all(), 
        #'navitems':nav,
        })
    
def view_tag(request, tag_name):
    context = {'tag_name':tag_name}
    if tag_name.upper() == 'ALL':
        context['pages'] = Page.objects.all()
    else:
        tag = Tag.objects.get(pk=tag_name)
        context['pages'] = tag.page_set.all()
    return render_and_nav(request,'wiki/view_tag.html', context)
    
def upload_file(request):
    context = {}
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = UploadFileForm()
    context['form'] = form
    context['files'] = UserFileUpload.objects.all().order_by('upload')
    return render_and_nav(request, 'wiki/upload.html', context)
    
StaticPages["Upload"] = upload_file    