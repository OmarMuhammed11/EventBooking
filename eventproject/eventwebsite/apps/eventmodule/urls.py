from apps.eventmodule import views
from django.urls import path , include
from django.contrib.auth import views as auth_views
urlpatterns = [
  path('',views.home,name ='home'),
  path('login/', views.loginPage, name='login'),
  path('logout/', views.logoutUser, name='logout'),
  path('register/', views.registration_view, name='register'),
  path('event_list/', views.event_list, name='event_list'),
  path('create/',views.event_create, name='event_create'),
  path('<int:event_id>/', views.event_detail, name='event_detail'),
  path('<int:event_id>/update/', views.event_update, name='event_update'),
  path('<int:event_id>/delete/', views.event_delete, name='event_delete'),
  path('about/',views.about, name='about'),
  path('contactus/',views.contact_us, name='contact_us'),
  path('book_event/',views.book_event, name='book_event'),
  path('myaccount/',views.account, name='account'),
]
