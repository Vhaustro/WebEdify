from django.shortcuts import render
from .models import Courses, Assignments

def courses_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/courses_list.html', {'courses': courses})

def assignment_detail(request, assignment_id):
    assignment = Assignments.objects.get(pk=assignment_id)
    return render(request, 'course/assignment_detail.html', {'assignment', assignment})