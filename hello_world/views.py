from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    if request.method == 'POST':
        return HttpResponse("You must have POSTed siomething as there is a POST request received!")
    else:
        return HttpResponse(request.method)
