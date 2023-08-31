from django.urls import path


urlpatterns = [
    path(' ', views.course_list, name = 'course_list'),
    path('assignment/<int:assignment_id>/', views.assignment_detail, name='assignment_detail')
]

AUTH_USER_MODEL = 'profiles.UserProfile'

