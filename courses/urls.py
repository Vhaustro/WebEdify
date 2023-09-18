from django.urls import path
from . import views

urlpatterns = [
    path('', views.courses_list, name='course_list'),
    path('assignment/<int:assignment_id>/', views.assignment_detail, name='assignment_detail'),
]