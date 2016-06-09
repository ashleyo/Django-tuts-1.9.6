from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def register_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            ## create user 
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = User.objects.create_user(username=username, password=password)            
            user.save()
            return redirect('auth:login')   
    else:
        form = UserCreationForm()
    return render(request, 'auth/registration/create_user.html', {'form':form})