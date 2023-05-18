from django.shortcuts import render
from django.http import HttpResponse


def register(request):
    return HttpResponse('Registration page')


def login(request):
    return render(request, 'login.html')


def tasks_page(request):
    return HttpResponse('Tasks:')
