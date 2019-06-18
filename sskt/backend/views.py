from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login

# Create your views here.

def hello(request):
    user = authenticate(username='person', password='ILK123456')

    
    if user is not None:
    # A backend authenticated the credentials
        print(user.get_all_permissions())
        auth_login(request, user)
    else:
        pass
    return HttpResponse("zqq")

def login(request):
    user = authenticate(username='person', password='ILK123456')
    if user is not None:
    # A backend authenticated the credentials
        login(request.user)
    else:
        pass
    # No backend authenticated the credentials