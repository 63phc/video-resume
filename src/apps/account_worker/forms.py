from django import forms
from src.apps.resume.models import Resume, Education, Skill, Job


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
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'other_skills': forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}),
            'hobbies': forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}),
            'about': forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}),
            'education': forms.CheckboxSelectMultiple,
            'skill': forms.CheckboxSelectMultiple,
            'job': forms.CheckboxSelectMultiple,
        }


class EducationCreateUpdateForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = (
            'period_edu',
            'name_institution',
            'faculty',
            'form_study'
        )
        widgets = {
            'period_edu': forms.TextInput(attrs={'class': 'form-control'}),
            'name_institution': forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}),
            'faculty': forms.TextInput(attrs={'class': 'form-control'}),
            'form_study': forms.TextInput(attrs={'class': 'form-control'}),
        }


class SkillCreateUpdateForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = (
            'name',
        )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }


class JobCreateUpdateForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = (
            'period_work',
            'position',
            'name_company'
        )
        widgets = {
            'period_work': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}),
            'name_company': forms.Textarea(attrs={'class': 'form-control', 'rows': '5'})
        }
