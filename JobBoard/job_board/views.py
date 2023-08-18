from django.shortcuts import render,HttpResponse

from .models import JobPosting
# Create your views here.

def index(request):
    return HttpResponse('<h1>Welcome</h1>')