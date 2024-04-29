from apps.eventmodule import views
from django.urls import path , include

urlpatterns = [
 ## path('',views.index,name ='index'),
  path('', views.event_list, name='event_list'),
  path('create/',views.event_create, name='event_create'),
  path('<int:event_id>/', views.event_detail, name='event_detail'),
  path('<int:event_id>/update/', views.event_update, name='event_update'),
  path('<int:event_id>/delete/', views.event_delete, name='event_delete'),
]
