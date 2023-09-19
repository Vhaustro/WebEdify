from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import AssignmentSubmissionForm
from .models import Courses, Assignments

def course_detail(request, course_id):
    course = get_object_or_404(Courses, pk=course_id)
    assignments = Assignments.objects.filter(course=course)
    enrolled = course.students.filter(id=request.user.id).exists ()

    if request.method == 'POST':
        if 'enroll' in request.POST:
            course.students.add(request.user)
            messages.success(request, f'You have successfully enrolled in {course.title}')
            return redirect ('course_detail', course_id=course_id)
    
    return render(request, 'courses/course_detail.html', {'course':course, 'assignment':assignments, 'enrolled': enrolled})

def assignment_submission(request, assignment_id):
    assignment = get_object_or_404(Assignments, pk=assignment_id)

    if request.method == 'POST':
        form = AssignmentSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.assignment = assignment
            submission.student = request.user
            submission.save()
            messages.success(request, f'Your assignment for {assignment.title} has been submitted!')
            return redirect('course_detail', course_id=assignment.course.id)
    else:
        form = AssignmentSubmissionForm()

    return render(request, 'courses/assignment_submission.html', {'form': form, 'assignment': assignment})

def courses_list(request):
    courses = Courses.objects.all()
    return render(request, 'courses/courses_list.html', {'courses': courses})

def assignment_detail(request, assignment_id):
    assignment = Assignments.objects.get(pk=assignment_id)
    return render(request, 'course/assignment_detail.html', {'assignment', assignment})