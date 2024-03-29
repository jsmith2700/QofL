from django.shortcuts import render, redirect
from . forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, logout

def login(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user:
                auth.login(request, user)
                return redirect("home")
    
    context = {'loginform':form}
    return render(request, "login.html", context=context)

def registration(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("login")
    context = {'registerform':form}
    return render(request, "registration.html", context=context)

def base(request):
    return render(request, "base.html")


def user_logout(request):
    auth.logout(request)

    return redirect("login")