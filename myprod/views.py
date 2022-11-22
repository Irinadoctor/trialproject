from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    return HttpResponse('This ia about page')


def home(request):
    return render(request, 'Home.html', {'greeting': 'Hello!'})


def reverse(request):
    user_text = request.GET['User']
    reversed_text = user_text[::-1]
    return render(request, 'reverse.html', {'User': user_text, 'reversedtext': reversed_text})
