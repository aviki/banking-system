from django.urls import path
from . import views

app_name = 'bank_app'

urlpatterns = [
        path('', views.index, name='index'),
        path('staff_dashboard/', views.staff_dashboard, name='staff_dashboard'),
        path('user_dashboard/', views.user_dashboard, name='user_dashboard'),
        path('create', views.create, name='create'),
        path('createaccount', views.createaccount, name='createaccount'),
        path('details/<int:pk>', views.details, name='details'),
        ]
