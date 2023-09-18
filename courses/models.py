from django.db import models
from django.contrib.auth.models import User

class Courses(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    duration = models.PositiveIntegerField()
    cover_image = models.ImageField(upload_to='course_covers/')
    students = models.ManyToManyField(User, related_name='enrolled_courses')


class Assignments(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    file = models.FileField(upload_to='assignments/')

    def __str__(self):
        return self.title

class Submission(models.Model):
    assignment = models.ForeignKey(Assignments, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    submission_time = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='submissions/')

    def __str__ (self):
        return f"{self.student.username}'s submission for {self.assignment.title}"


