from django.shortcuts import render

def index(request):
    return render(request,'bookmodule/index.html')


def books(request):
    return render(request,'bookmodule/books.html')

def book(requset,bnum):
    
    return render(request,'bookmodule/book.html')
# Create your views here.
