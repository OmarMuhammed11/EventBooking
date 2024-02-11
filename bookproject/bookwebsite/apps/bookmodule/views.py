from django.shortcuts import render

def index(request):
    return render(request,'bookmodule/index.html')


def books(request):
    return render(request,'bookmodule/books.html')

# Create your views here.
