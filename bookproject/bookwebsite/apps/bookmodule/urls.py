
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name='index'),
    path("books/",views.books,name = 'books'),
    path("book/<int:bnum>",views.book ,name = 'book_detail'),
    path("tags/",views.get_tags , name= 'tags'),
    path("create/",views.createBook,name='create'),
    path("update/<int:bnum>",views.update_book,name='update'),
    path("delate/<int:bnum>",views.delate_book,name='delate'),
    
]
