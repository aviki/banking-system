from django.urls import path
from . import views

app_name = 'bank_app'

urlpatterns = [
        path('dashboard', views.staff_dashboard, name='dashboard_dashboard'),
        path('', views.index, name='index'),
        path('create', views.create, name='create'),
        path('createaccount', views.createaccount, name='createaccount'),
        path('details/<int:pk>', views.details, name='details'),
        ]
