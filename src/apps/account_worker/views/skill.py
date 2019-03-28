from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from src.apps.resume.models import Skill
from ..forms import SkillForm
from .mixins import (
    EduSkillJobSuccessUrlMixin, ResumeEduSkillJobContextMixin,
    EduSkillJobAjaxMixin, worker_access)


@method_decorator((login_required, worker_access), name='dispatch')
class SkillUpdateView(ResumeEduSkillJobContextMixin,
                      EduSkillJobSuccessUrlMixin, UpdateView):
    form_class = SkillForm
    model = Skill
    template_name = 'dashboard_worker/skill/update.html'


@method_decorator((login_required, worker_access), name='dispatch')
class SkillDeleteView(ResumeEduSkillJobContextMixin,
                      EduSkillJobSuccessUrlMixin, DeleteView):
    model = Skill
    template_name = 'dashboard_worker/skill/delete.html'


@method_decorator((login_required, worker_access), name='dispatch')
class SkillCreateView(
    EduSkillJobAjaxMixin, ResumeEduSkillJobContextMixin,
    EduSkillJobSuccessUrlMixin, CreateView
):
    form_class = SkillForm
    model = Skill
    template_name = 'dashboard_worker/skill/create.html'
