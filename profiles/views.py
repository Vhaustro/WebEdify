from django.contrib.auth import login 
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()

            login(request, user)
            return redirect ('profile')
        
        else:
            form = UserRegistrationForm()
        return render(request, 'registration/register.html', {'form': form})


def dashboard(request):
    user = request.user
    enrolled_courses = user.enrolled_courses.all()
    assignments = Assignment.objects.filter(course__in=enrolled_courses)
    # Get assignments, grades, and other relevant data
    return render(request, 'profiles/dashboard.html', {'enrolled_courses': enrolled_courses, 'assignments': assignments})

