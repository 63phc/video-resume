from django.views.generic.edit import UpdateView, CreateView, DeleteView

from src.apps.resume.models import Education
from ..forms import EducationForm
from .mixins import (
    EduSkillJobSuccessUrlMixin, ResumeEduSkillJobContextMixin,
    EduSkillJobAjaxMixin, CheckAccess)


class EducationUpdateView(
    CheckAccess, ResumeEduSkillJobContextMixin, EduSkillJobSuccessUrlMixin,
    UpdateView
):
    form_class = EducationForm
    model = Education
    template_name = 'dashboard_worker/education/update.html'


class EducationCreateView(
    EduSkillJobSuccessUrlMixin,  EduSkillJobAjaxMixin,
    ResumeEduSkillJobContextMixin, CreateView
):
    form_class = EducationForm
    model = Education
    template_name = 'dashboard_worker/education/create.html'


class EducationDeleteView(
    CheckAccess, ResumeEduSkillJobContextMixin, EduSkillJobSuccessUrlMixin,
    DeleteView
):
    model = Education
    template_name = 'dashboard_worker/education/delete.html'
