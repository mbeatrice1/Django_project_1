from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.

def nav(request):
    return render(request,'navbar.html')
