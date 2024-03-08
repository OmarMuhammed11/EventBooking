from django.shortcuts import render,redirect

def index(request):
   
   return render(request, 'eventmodule/home_page.html')

def event_detil(request):
   return render(request, 'eventmodule/eventd_page.html')