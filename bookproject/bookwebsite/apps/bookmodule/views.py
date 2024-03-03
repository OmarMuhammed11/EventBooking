from django.shortcuts import render

def index(request):
    return render(request,'bookmodule/index.html')


def books(request):
    return render(request,'bookmodule/books.html')


def book(request,bnum):
    books={1:"Sen",2:"Aog"}
    
    return render(request,'bookmodule/book.html')
# Create your views here.

def get_tags(request):
    
    return render(request,'bookmodule/tags.html')