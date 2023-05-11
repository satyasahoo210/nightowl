from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpRequest
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as django_login, logout as django_logout

import logging

from .models import User, Establishment
from .forms import Register, Login, ChangePwd

from PIL import Image


# Create your views here.
def index(request):
    return render(request, 'index.html')


def register(request: HttpRequest):
    if request.method == 'GET':
        register_form = Register()
        context = {'form': register_form}
        return render(request, 'user/register.html', context)
    else:
        register_form = Register(request.POST)
        if register_form.is_valid():
            logging.debug('Register Form - valid')

            user:User = register_form.save(commit=False)
            user.set_password(register_form.cleaned_data.get('password'))
            user.save()
            messages.success(request, 'Registration Successful')
            return redirect('login')
        context = {'form': register_form}
        return render(request, 'user/register.html', context)


def login(request: HttpRequest):
    if request.method == 'GET':
        login_form = Login()
        context = {'form': login_form}
        return render(request, 'user/login.html', context)
    else:
        url = request.GET.get('next', '/home')
        login_form = Login(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)
            logging.debug(user)

            if user is not None:
                messages.info(request, 'Login Successful')
                django_login(request, user)
                return redirect(url)
            else:
                messages.error(request, 'Usernamer/Password might be wrong')
        
        context = {'form': login_form}
        return render(request, 'user/login.html', context)
                

def logout(request: HttpRequest):
    django_logout(request)
    return redirect('login')


def profile_picture(request: HttpRequest, username: str):
    path = get_object_or_404(User, username=username)._dp.path
    try:
        with open(path, "rb") as f:
            return HttpResponse(f.read(), content_type="image/jpeg")
    except Exception:
        red = Image.new('RGB', (50, 50), (255,0,0))
        response = HttpResponse(content_type="image/jpeg")
        red.save(response, "JPEG")
        return response

@login_required
def change_password(request: HttpRequest):
    if request.method == 'GET':
        change_pwd_form = ChangePwd()
        context = {'form': change_pwd_form}
    else:
        change_pwd_form = ChangePwd(request.POST)
        context = {'form': change_pwd_form}
        if change_pwd_form.is_valid():
            user = User.objects.get(id=request.user.id)
            user.set_password(change_pwd_form.cleaned_data.get('password'))
            user.save()
            messages.info(request, 'Password changed successfully')
            change_pwd_form = ChangePwd()

    return render(request, 'user/change_pwd.html', context)
    
@login_required
def home(request: HttpRequest):
    establishments = Establishment.objects.filter(active=True).order_by('type', '-rating')
    context = {
        'establishments': establishments
    }
    return render(request, 'secure/home.html', context=context)

@login_required
def profile(request: HttpRequest, username: str):
    user = get_object_or_404(User, username=username)

    context = {
        'user': user
    }
    return render(request, 'secure/profile.html', context=context)


# TODO: Profile Page, add profile picture
# TODO: stars rating, profile page