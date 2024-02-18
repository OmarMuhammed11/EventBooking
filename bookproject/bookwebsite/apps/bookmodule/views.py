from django.shortcuts import render

def index(request):
    return render(request,'bookmodule/index.html')


def books(request):
    return render(request,'bookmodule/books.html')

def books1(requset):
    return render(requset,'templates/layouts/base.html')

# Create your views here.
