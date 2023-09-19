from django import forms
from .models import Submission

class AssignmentSubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['file']