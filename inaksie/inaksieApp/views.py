from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')


def contact(request):
    return render(request,'contact.html')


def intro(request):
    return render(request,'intro.html')


def portfolio(request):
    return render(request,'portfolio.html')


def werkwijze(request):
    return render(request,'werkwijze.html')