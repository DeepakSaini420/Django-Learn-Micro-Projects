from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1>Hello This is My App</h1>")

def about(request):
    return HttpResponse("<h1>About Page</h1>")

def hello(request,first_name):
    return HttpResponse(f"Hello {first_name}.How are you?")

def add(request,num1,num2):
    return HttpResponse(f"Your Answer {num1+num2}")

def subtract(request,num1,num2):
    return HttpResponse(f"Your Answer {num1-num2}")

def multiply(request,num1,num2):
    return HttpResponse(f"Your Answer {num1*num2}")