from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return render(request,'about.html')
    # return HttpResponse("About")

def homepage(request):
    return render(request,'homepage.html')
    # return HttpResponse("Home Page")