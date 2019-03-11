from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from src.apps.resume.models import Education
from ..forms import EducationForm
from .mixins import (
    EduSkillJobSuccessUrlMixin, ResumeEduSkillJobContextMixin,
    EduSkillJobAjaxMixin, worker_access)


@method_decorator(worker_access, name='dispatch')
@method_decorator(login_required, name='dispatch')
class EducationUpdateView(ResumeEduSkillJobContextMixin,
                          EduSkillJobSuccessUrlMixin, UpdateView):
    form_class = EducationForm
    model = Education
    template_name = 'dashboard_worker/education/update.html'


@method_decorator(worker_access, name='dispatch')
@method_decorator(login_required, name='dispatch')
class EducationCreateView(
    EduSkillJobSuccessUrlMixin,  EduSkillJobAjaxMixin,
    ResumeEduSkillJobContextMixin, CreateView
):
    form_class = EducationForm
    model = Education
    template_name = 'dashboard_worker/education/create.html'


@method_decorator(worker_access, name='dispatch')
@method_decorator(login_required, name='dispatch')
class EducationDeleteView(ResumeEduSkillJobContextMixin,
                          EduSkillJobSuccessUrlMixin, DeleteView):
    model = Education
    template_name = 'dashboard_worker/education/delete.html'
