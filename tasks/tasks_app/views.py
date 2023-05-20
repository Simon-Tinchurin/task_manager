from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login
from .forms import TaskForm, CreateUserForm, LoginForm
from .models import Task


# view to register new user
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request,
                                username=username, password=password)
            login(request, user)
            return redirect('tasks')
    context = {'form': form}
    return render(request, 'register.html', context=context)


# view to log in existing user
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
    context = {'form': form}
    return render(request, 'login.html', context=context)


# main page with user's tasks
@login_required
def user_tasks(request):
    form = TaskForm()
    all_tasks = Task.objects.filter(user=request.user)
    context = {'form': form,
               'tasks': all_tasks}
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('tasks')
    return render(request, 'user_page.html', context=context)


def log_out(request):
    auth.logout(request)
    return redirect('')
