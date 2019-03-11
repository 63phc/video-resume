from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from src.apps.resume.models import Job
from ..forms import JobForm
from .mixins import (
    EduSkillJobSuccessUrlMixin, ResumeEduSkillJobContextMixin,
    EduSkillJobAjaxMixin, worker_access)


@method_decorator(worker_access, name='dispatch')
@method_decorator(login_required, name='dispatch')
class JobCreateView(
    EduSkillJobAjaxMixin, ResumeEduSkillJobContextMixin,
    EduSkillJobSuccessUrlMixin, CreateView
):
    form_class = JobForm
    model = Job
    template_name = 'dashboard_worker/job/create.html'


@method_decorator(worker_access, name='dispatch')
@method_decorator(login_required, name='dispatch')
class JobUpdateView(ResumeEduSkillJobContextMixin,
                    EduSkillJobSuccessUrlMixin, UpdateView):
    form_class = JobForm
    model = Job
    template_name = 'dashboard_worker/job/update.html'


@method_decorator(worker_access, name='dispatch')
@method_decorator(login_required, name='dispatch')
class JobDeleteView(ResumeEduSkillJobContextMixin,
                    EduSkillJobSuccessUrlMixin, DeleteView):
    model = Job
    template_name = 'dashboard_worker/job/delete.html'
