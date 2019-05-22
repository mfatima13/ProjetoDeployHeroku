from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
# Create your views here.

def home(request):
    return render(request, 'home.html')
#
# def new(request):
#     return render(request, 'person_form.html')

def my_logout(request):
    logout(request)
    return redirect('home')

def my_view(request):

    username = request.POST['username']
    password = request.POSt['password']
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect('home')
    else:
        return redirect('login')