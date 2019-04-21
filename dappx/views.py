
# Create your views here.
# dappx/views.py
from django.shortcuts import render
from dappx.forms import UserForm,UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
def index(request):
    return render(request,'dappx/index.html')
    
def head(request):
	return render(request,'dappx/h_page.html')
	
def about(request):
	return(render(request,"dappx/about.html"))	
	
def dest(request):
	return(render(request,"dappx/destination.html"))

def agra(request):
	return(render(request,"dappx/agra.html"))
	
def delhi(request):
	return(render(request,"dappx/delhi.html"))

def header(request):
	return(render(request,"dappx/header.html"))
	
def jaipur(request):
	return(render(request,"dappx/jaipur.html"))
	
def home(request):
	return(render(request,"dappx/home.html"))

def kerala(request):
	return(render(request,"dappx/kerala.html"))
	
def kolkata(request):
	return(render(request,"dappx/kolkata.html"))

def map(request):
	return(render(request,"dappx/map_page.html"))

def varanasi(request):
	return(render(request,"dappx/varanasi.html"))

@login_required
def special(request):
    return HttpResponse("You are logged in !")
@login_required
def user_logout(request):
    logout(request)
    #return HttpResponseRedirect(reverse('head'))
    return render(request, 'dappx/login.html', {})
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'dappx/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                #return HttpResponseRedirect('/dappx/'))
                return render(request,'dappx/h_page.html',{})
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'dappx/login.html', {})
        

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	