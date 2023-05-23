from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from accounts.models import *
import random

def home(request):
    return render(request , 'home.html')

def your_clubs(request):
    user=request.user
    clubs = JoinedClubs.objects.filter(user=user)
    if clubs == None:
        return render(request , 'your_clubs.html' , {'user_clubs': 0})
    user_clubs = clubs[0].clubs.all()
    print(clubs[0])
    print(user_clubs[0].club_events.all())
    return render(request , 'your_clubs.html' , {'user_clubs': user_clubs})

def all_clubs(request):
    clubs = Clubs.objects.filter()
    print(clubs)
    return render(request , 'all_clubs.html' , {'clubs': clubs})

def signup_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username = email)

        if user_obj.exists():
            messages.warning(request , 'Account with this Email already exists')
            return HttpResponseRedirect(request.path_info)
        user_obj = User.objects.create(first_name=first_name , last_name=last_name , email=email , username=email)
        user_obj.set_password(password)
        user_obj.save()
        print("success")
        messages.success(request , 'An Email has been sent to your mail')
        context = {'mail' : 'Resend Email'}
        return redirect('/login')
    return render(request , 'register.html')

def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username = email)
        
        if not user_obj.exists():
            messages.warning(request , 'Account not found')
            return HttpResponseRedirect(request.path_info)
        
        user_obj = authenticate(username = email , password = password)
        if user_obj:
            login(request , user_obj)
            return redirect('/your_clubs')

        else:
            messages.warning(request , 'Invalid Email Id or Password')
            return HttpResponseRedirect(request.path_info)
        
    return render(request , 'login.html')

def join_club(request , uid):
    club = Clubs.objects.filter(uid=uid)
    user = request.user
    
    join_clubb = JoinedClubs.objects.get_or_create(user=user)


    join_clubb[0].clubs.add(club[0])

    messages.success(request , 'Added Successfully')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))