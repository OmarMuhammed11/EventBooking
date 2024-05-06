from django.shortcuts import render,redirect

#def index(request):
#   
 #  return render(request, 'eventmodule/home_page.html')

#def event_detil(request):
 #  return render(request, 'eventmodule/eventd_page.html')
#def event(request):
 #  pass
#def events(request):
 #  pass

# events/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import EventForm , RegistrationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def loginPage(request):
    template_name = ''
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request, username = username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')
    return render(request,'accounts\login.html')  # Specify your login template

def logoutUser(request):
    logout(request)
    return redirect('login')


#@login_required(login_url='/login')
def home(request):
    events = Event.objects.all()
    context = {'events': events}
    return render(request,'eventmodule/home_page.html',context)

@login_required(login_url='/login')
def event_list(request):
    events = Event.objects.all()
    return render(request, 'eventmodule/event_list.html', {'events': events})

@login_required(login_url='/login')
def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'eventmodule/event_detail.html', {'event': event})

@login_required(login_url='/login')
def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
           # event = form.save(commit=False)
           # event.organizer = request.user  # Set the current user as the organizer
           # event.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'eventmodule/event_form.html', {'form': form})

@login_required(login_url='/login')
def event_update(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm(instance=event)
    return render(request, 'eventmodule/event_form.html', {'form': form})

@login_required(login_url='/login')
def event_delete(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        event.delete()
        return redirect('event_list')
    return render(request, 'eventmodule/event_confirm_delete.html', {'event': event})

#@login_required
def registration_view(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account of '+user +' Created')
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

def about(request):
    
    return render(request,'eventmodule/about.html')


def contact_us(request):
    
    return render(request,'eventmodule/contact_us.html')

@login_required(login_url='/login')
def book_event(request):
    events = Event.objects.all()
    context = {'events': events}
    return render(request,'eventmodule/book_event.html',context)

@login_required(login_url='/login')
def account(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request,'eventmodule/account.html',context)