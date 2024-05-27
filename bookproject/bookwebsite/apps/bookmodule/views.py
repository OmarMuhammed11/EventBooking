from django.shortcuts import get_object_or_404, render,redirect
from .models import Book
from .forms import BookForm
from django.db.models import Q,Sum,Avg,Count,Max
def index(request):
    mybooks = Book.objects.all()
    if request.method == 'POST':
        keyword = request.POST.get('keyword')
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        if isTitle :
            item = Book.objects.filter(Q(title__iexact =keyword))
        if isAuthor :
            item = Book.objects.filter(Q(author__iexact =keyword))
        print(item) 
    return render(request,'bookmodule/index.html')

def createBook(request):
    my_form = BookForm()
    if request.method == 'POST':
        my_form = BookForm(request.POST)
        if my_form.is_valid():
            obj=my_form.save()
            return redirect('book_detail',bnum = obj.id)
    context = {'form': my_form}
    return render(request, "bookmodule/create_book.html", context)
    
    
def books(request):
     mybooks = Book.objects.all()
     avr=Book.objects.aggregate(Avg('price',defulte = 0.0))
     sum=Book.objects.aggregate(Sum('price',defulte = 0.0))
     
     context = {'books': mybooks,'avg':avr,'sum':sum}
     return render(request,'bookmodule/books.html',context)

def update_book(request,bnum):
    obj = Book.objects.get(id=bnum)
    if request.method == "POST":
        form = BookForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect("book_detail",bnum = obj.id)
    form = BookForm(instance= obj)
    context = {'form':form}
    return render(request,'bookmodule/update.html',context)

def delate_book(request,bnum):
     obj = Book.objects.get(id=bnum)
     ychoice = request.POST.get('yes')
     if request.method == "POST":
         if ychoice:
            obj.delete()
            return redirect("books")
     return render(request,'bookmodule/delate.html')
    
def book(request,bnum):
     b = get_object_or_404(Book, pk=bnum)
     context = {'book': b}
     
     return render(request,'bookmodule/book.html',context)
# Create your views here.

def get_tags(request):
     return render(request,'bookmodule/tags.html')