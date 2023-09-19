from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns =[
    path('<str:username>/', views.view_profile, name='view_profile'),
    path('register/', views.register, name = 'register'),
]