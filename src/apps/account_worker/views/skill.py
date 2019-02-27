from django.views.generic.edit import UpdateView, CreateView, DeleteView

from src.apps.resume.models import Skill
from ..forms import SkillForm
from .mixins import (
    EduSkillJobSuccessUrlMixin, ResumeEduSkillJobContextMixin,
    EduSkillJobAjaxMixin)


class SkillUpdateView(
    ResumeEduSkillJobContextMixin, EduSkillJobSuccessUrlMixin, UpdateView
):
    form_class = SkillForm
    model = Skill
    template_name = 'dashboard_worker/skill/update.html'


class SkillDeleteView(
    ResumeEduSkillJobContextMixin, EduSkillJobSuccessUrlMixin, DeleteView
):
    model = Skill
    template_name = 'dashboard_worker/skill/delete.html'


class SkillCreateView(
    EduSkillJobAjaxMixin, ResumeEduSkillJobContextMixin,
    EduSkillJobSuccessUrlMixin, CreateView
):
    form_class = SkillForm
    model = Skill
    template_name = 'dashboard_worker/skill/create.html'
