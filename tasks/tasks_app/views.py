from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login
from .forms import TaskForm, CreateUserForm, LoginForm


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('User registered!')
    context = {'form': form}
    return render(request, 'register.html', context=context)


def log_in(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request,
                                username=username,
                                password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('tasks')
    context = {'from': form}
    return render(request, 'login.html', context=context)


def user_tasks(request):
    return render(request, 'user_page.html')


def log_out(request):
    auth.logout(request)
    return redirect('')
