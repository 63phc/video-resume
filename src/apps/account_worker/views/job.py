from django.views.generic.edit import UpdateView, CreateView, DeleteView

from src.apps.resume.models import Job
from ..forms import JobForm
from .mixins import (
    EduSkillJobSuccessUrlMixin, ResumeEduSkillJobContextMixin,
    EduSkillJobAjaxMixin)


class JobCreateView(
    EduSkillJobAjaxMixin, ResumeEduSkillJobContextMixin,
    EduSkillJobSuccessUrlMixin, CreateView
):
    form_class = JobForm
    model = Job
    template_name = 'dashboard_worker/job/create.html'


class JobUpdateView(
    ResumeEduSkillJobContextMixin, EduSkillJobSuccessUrlMixin,
    UpdateView
):
    form_class = JobForm
    model = Job
    template_name = 'dashboard_worker/job/update.html'


class JobDeleteView(
    ResumeEduSkillJobContextMixin, EduSkillJobSuccessUrlMixin, DeleteView
):
    model = Job
    template_name = 'dashboard_worker/job/delete.html'
