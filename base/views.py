from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('home page')


def room(request):
    return HttpResponse('room page')

