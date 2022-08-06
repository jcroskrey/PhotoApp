from email.policy import HTTP
from urllib.request import HTTPRedirectHandler
from django.shortcuts import render, HttpResponse


def home_view(request):
    return HttpResponse('hello world')
