from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('create_account/', views.create_account, name='create_account'),
    path('login/', views.login, name='login'),
    path('appointment_time_list/', views.appointment_time_list, name='appointment_time_list'),
    path('add_appointment/', views.add_appointment, name='add_appointment'),
    path('get_appointments/', views.get_appointments, name='get_appointments'),
    path('delete_appointment/', views.delete_appointment, name='delete_appointment'),
    path('update_appointment/', views.update_appointment, name='update_appointment'),


]
