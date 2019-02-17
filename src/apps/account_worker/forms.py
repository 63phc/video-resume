from django import forms
from src.apps.resume.models import Resume


class ResumeUpdateForm(forms.ModelForm):

    class Meta:
        model = Resume
        fields = (
            'title',
            'other_skills',
            'hobbies',
            'about',
            'education',
            'skill',
            'job'
        )
        widgets = {
            'education': forms.CheckboxSelectMultiple,
            'skill': forms.CheckboxSelectMultiple,
            'job': forms.CheckboxSelectMultiple,
        }
