from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, './website/index.html')

def about(request):
    # return HttpResponse("Hello world. you are at about page")
    return render(request, 'about.html')

def contact(request):
    # return HttpResponse("Hello world. you are at contact page")
    return render(request, 'contact.html')