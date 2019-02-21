from django import forms
from src.apps.resume.models import Resume, Education, Skill, Job


class ResumeCreateUpdateForm(forms.ModelForm):

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

    def __init__(self, *args, **kwargs):
        super(ResumeCreateUpdateForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            resume = Resume.objects.get(pk=self.instance.pk)
            self.fields['education'].queryset = resume.education.all()
            self.fields['skill'].queryset = resume.skill.all()
            self.fields['job'].queryset = resume.job.all()
        else:
            self.fields['education'].queryset = Resume.objects.none()
            self.fields['skill'].queryset = Resume.objects.none()
            self.fields['job'].queryset = Resume.objects.none()


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
            'period_edu': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'name_institution': forms.Textarea(attrs={'class': 'form-control', 'rows': '5', 'required': 'required'}),
            'faculty': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'form_study': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
        }


class SkillCreateUpdateForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = (
            'name',
        )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'})
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
