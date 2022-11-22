from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    return HttpResponse('This ia about page')


def home(request):
    return render(request, 'Home.html', {'greeting': 'Hello!'})
