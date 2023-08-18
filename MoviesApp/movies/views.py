from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"movies/index.html",{});

def about(request):
    context = {
        'movies':['Skyrim','Lord Of Rings','KGF 2','RRR']
    }

    return render(request,'movies/about.html',context);