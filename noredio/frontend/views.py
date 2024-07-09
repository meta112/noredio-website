from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.

def index(Request):
    return render(Request, 'frontend/home.html')


def about(Request):
    return render(Request, 'frontend/about.html')

def contact(Request):
    return render(Request, 'frontend/contact.html')