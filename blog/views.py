from django.shortcuts import render, HttpResponse


def index(request):
    return HttpResponse("Hello, world. Here's going to be my blog.")