from django.contrib import admin
from .models import Course, Assignment, Submission

class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'deadline')
    list_filter = ('courses')
    search_fields = ('title', 'course__title')
    date_hierarchy = ('deadline')
    ordering =('deadline')

class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('assignment', 'student', 'submitted_at')
    list_filter = ('assignment', 'student')
    search_fields = ('assignment__title', 'student__username')
    date_hierarchy = 'submitted_at'
    ordering = ('submitted_at')

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'enrollment_start_date', 'enrollment_end_date')
    list_filter = ('instructor',)
    search_fields = ('title', 'instructor__username')
    date_hierarchy = ('enrollment_start_date')
    ordering = ('-enrollment_start_date')


admin.site.register(Course, CourseAdmin)
admin.site.register(Assignment, AssignmentAdmin)
admin.site.register(Submission, SubmissionAdmin)

